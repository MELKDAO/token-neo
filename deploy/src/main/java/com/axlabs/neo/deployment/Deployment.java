package com.axlabs.neo.deployment;

import io.neow3j.contract.ContractManagement;
import io.neow3j.contract.NefFile;
import io.neow3j.contract.SmartContract;
import io.neow3j.crypto.WIF;
import io.neow3j.protocol.Neow3j;
import io.neow3j.protocol.core.response.ContractManifest;
import io.neow3j.protocol.core.response.NeoApplicationLog;
import io.neow3j.protocol.http.HttpService;
import io.neow3j.transaction.AccountSigner;
import io.neow3j.transaction.TransactionBuilder;
import io.neow3j.types.ContractParameter;
import io.neow3j.types.Hash160;
import io.neow3j.types.Hash256;
import io.neow3j.types.NeoVMStateType;
import io.neow3j.utils.Await;
import io.neow3j.utils.Numeric;
import io.neow3j.wallet.Account;

import java.io.File;

public class Deployment {

    public static void main(String[] args) throws Throwable {
        Neow3j neow3j = Neow3j.build(new HttpService("node_url")); // testnet, for ex is http://seed2t5.neo.org:20332

        // This is the account that will pay for the deployment transaction but does not have any special rights in the contract. If you don't have your WIF, but have your hexstring private key, use the line below.
        // String wif = WIF.getWIFFromPrivateKey(Numeric.hexStringToByteArray("YOUR_HEXADECIMAL_PRIVATE_KEY"));

        String wif = "YOUR_WIF";
        Account signingAccount = Account.fromWIF(wif);
        System.out.println(signingAccount.getAddress());
        AccountSigner signer = AccountSigner.none(signingAccount);
        System.out.println(signer.getScriptHash());

        // Put the NEF file and the manifest file in the resources folder.
        File nefFile = new File(Deployment.class.getClassLoader().getResource("contract.nef").toURI());
        System.out.println(nefFile);
        NefFile nef = NefFile.readFromFile(nefFile);
        File manifestFile = new File(Deployment.class.getClassLoader().getResource("contract.manifest.json").toURI());
        ContractManifest manifest = io.neow3j.protocol.ObjectMapperFactory.getObjectMapper()
                .readValue(manifestFile, ContractManifest.class);

        // This is where you can set the parameters for the contract's "constructor".
        // Currently, there is one Hash160 parameter that holds the address of the contract owner account.
        // It will be passed to the
        ContractParameter owner = ContractParameter.hash160(Hash160.fromAddress("OWNER_ADDRESS"));
        System.out.println(owner);


        TransactionBuilder builder = new ContractManagement(neow3j).deploy(nef, manifest, owner).signers(signer);

        Hash256 txHash = builder.sign().send().getSendRawTransaction().getHash();
        System.out.println("Deploy Transaction Hash: " + txHash.toString());
        Await.waitUntilTransactionIsExecuted(txHash, neow3j);

        NeoApplicationLog log = neow3j.getApplicationLog(txHash).send().getApplicationLog();
        if (log.getExecutions().get(0).getState().equals(NeoVMStateType.FAULT)) {
            throw new Exception("Failed to deploy smart contract. NeoVM error message: "
                    + log.getExecutions().get(0).getException());
        }
        Hash160 contractHash = SmartContract.calcContractHash(signer.getScriptHash(), nef.getCheckSumAsInteger(),
                manifest.getName());
        System.out.println("Contract Hash: " + contractHash);
    }
}
