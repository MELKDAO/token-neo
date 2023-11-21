# $Melk Token on NEO

To run the project, you need to have the following installed:
- [dotnet](https://dotnet.microsoft.com/en-us/download/dotnet)
- [neo test runner](https://github.com/ngdenterprise/neo-test#neo-test-runner)
- [neo express](https://github.com/neo-project/neo-express#installation)

## Running on CSharp

Install the N3 Extension on VScode.
Install dotnet SDK and neo express.

Reference tutorial: https://developers.neo.org/tutorials/2021/05/04/real-world-tokens and
https://github.com/neo-project/examples/blob/master/csharp/NEP17/NEP17.cs

Deploy the contract (after having the .nef and .manifest file) here: https://www.neonova.space/contract

## Running deploy on Java - passing parameters

Open `/deploy` -> `src/main/java/com/axlabs/neo/deployment`. You'll find a java file `Deployment.java`

If you're on vscode, just click the "Run" button that you should be seing inside of the file.

Don't forget to change the value of the WIF key (which is your private key) for the deployer and the Owner parameter for the deploy.

## Contract Addresses

### Sandbox (Testnet)

#### Token
`0x14646e09e3fd3a1a9a124069fdc1cb0dc0d17d6c`

https://dora.coz.io/contract/neo3/testnet/0x14646e09e3fd3a1a9a124069fdc1cb0dc0d17d6c

### Production (Testnet)

#### Token
`0xf40d025c99cf064fe11c4ba7ef4f93fe468c9a64`

https://dora.coz.io/contract/neo3/testnet/0xf40d025c99cf064fe11c4ba7ef4f93fe468c9a64

#### Transaction Hash

`0x096fc56463917afa9f9f579665612ddef5df8c866c8d927de88f375939072a38`

https://dora.coz.io/transaction/neo3/testnet/0x096fc56463917afa9f9f579665612ddef5df8c866c8d927de88f375939072a38