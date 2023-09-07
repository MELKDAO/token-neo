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
    nef_file = (
        root
        / "contracts"
        / "melkToken"
        / "src"
        / "bin"
        / "sc"
        / "melkTokenContract.nef"
    )
    nef_contract = nef.NEF.from_file(nef_file)

    # manifest_file = root / "contracts" / "melk.manifest.json"
    # manifest_contract = manifest.ContractManifest.from_file(manifest_file)

    print("Deploying contract ...")
    receipt = await facade.invoke(GenericContract.deploy(nef_contract, manifest=None))
    print("done")
    return receipt


async def main():
    # if you want to deploy on testnet, just change to node_provider_mainnet
    facade = ChainFacade.node_provider_testnet()
    facade.rpc_host = "http://seed1t5.neo.org:20332"  # fixing wrong RPC TESTNET

    facade.add_signer(
        sign_insecure_with_account(account, password=password),
        Signer(account.script_hash),
    )

    receipt = await deploy(facade=facade)
    print(receipt)
    return


if __name__ == "__main__":
    asyncio.run(main())
