# $Melk Token on NEO

To run the project, you need to have the following installed:
- [dotnet](https://dotnet.microsoft.com/en-us/download/dotnet)
- [neo3-boa](https://github.com/CityOfZion/neo3-boa/tree/master)
- [neo test runner](https://github.com/ngdenterprise/neo-test#neo-test-runner)
- [neo express](https://github.com/neo-project/neo-express#installation)

Refer to the installation and setup here: https://dojo.coz.io/neo3/boa/index.html

You also have to install dependencies on `requirements.txt

Run this command:

`pip install -r requirements.txt`

## Compile contract

Run `neo3-boa compile contracts/melk.py`

## Deploying contract

Be sure to set up your environment variables as shown in `.env.example`

Run `python3 scripts/deploy.py`


# Running on CSharp

Install the N3 Extension on VScode.
Install dotnet SDK and neo express.

Reference tutorial: https://developers.neo.org/tutorials/2021/05/04/real-world-tokens and
https://github.com/neo-project/examples/blob/master/csharp/NEP17/NEP17.cs

Deploy the contract (after having the .nef and .manifest file) here: https://www.neonova.space/contract

# Running deploy on Java - passing parameters

Open `/deploy` -> `src/main/java/com/axlabs/neo/deployment`. You'll find a java file `Deployment.java`

If you're on vscode, just click the "Run" button that you should be seing inside of the file.

Don't forget to change the value of the WIF key (which is your private key) for the deployer and the Owner parameter for the deploy.

## MELK TOKEN

- Address on testnet: `0x14646e09e3fd3a1a9a124069fdc1cb0dc0d17d6c`

