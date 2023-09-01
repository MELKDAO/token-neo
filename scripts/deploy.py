from pathlib import Path
from neo3.core import types
import asyncio
from neo3.api.wrappers import (
    GenericContract,
    ChainFacade,
    NeoToken,
    GasToken,
    NEP17Contract,
    ContractMethodResult,
)
from neo3.api.helpers.signing import sign_insecure_with_account
from neo3.api.helpers import unwrap
from neo3.contracts import nef, manifest
from neo3.network.payloads.verification import Signer
from neo3.wallet.account import Account
from neo3.api.noderpc import NeoRpcClient
from dotenv import load_dotenv
import os

load_dotenv()

private_key = os.getenv(
    "PRIVATE_KEY"
)  # private key of the account that will deploy the contract
password = os.getenv(
    "PASSWORD"
)  # password of the account that will deploy the contract

account = Account.from_wif(private_key, password)


async def deploy(facade: ChainFacade):
    root = Path(__file__).parent.parent
    nef_file = root / "contracts" / "melk.nef"
    nef_contract = nef.NEF.from_file(nef_file)

    manifest_file = root / "contracts" / "melk.manifest.json"
    manifest_contract = manifest.ContractManifest.from_file(manifest_file)

    print("Deploying contract ...")
    receipt = await facade.invoke(
        GenericContract.deploy(nef_contract, manifest_contract)
    )
    print("done")
    return receipt


async def main():
    return
    facade = ChainFacade.node_provider_testnet()
    facade.rpc_host = "http://seed1t5.neo.org:20332"  # fixing wrong RPC TESTNET

    facade.add_signer(
        sign_insecure_with_account(account, password=password),
        Signer(account.script_hash),
    )

    # Uncomment this if you want to deploy a new contract. Then, replace the contract hash below in the string

    # receipt = await deploy(facade=facade)
    # print(receipt)

    contract_hash = types.UInt160.from_string(
        "0x1b817f8f7f76dae84d3343908b0c2a7df770c3e5"
    )

    token = NEP17Contract(contract_hash)

    balance = await facade.test_invoke(token.balance_of(account.address))
    print(f"Current MELK token balance: {balance}")

    total_supply = await facade.test_invoke(token.total_supply())
    print(f"Total supply: {total_supply}")

    is_paused = await facade.test_invoke(token.call_function("is_paused"))
    print(f"Is paused: {is_paused.stack[0].value}")

    destination = "NaQSq2VexRSoWgKHmbM8qVbLPpZqefD5SL"  # replace this with the destination address
    print("Transfering MELK tokens")
    res = await facade.invoke(token.transfer(account.address, destination, 10))
    print(res)

    print("Checking if balance changed")
    balance = await facade.test_invoke(token.balance_of(destination))
    print(balance)


if __name__ == "__main__":
    asyncio.run(main())
