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


## MELK TOKEN

- Address on testnet: `0xa22dfdd6c47bf0b8c343d3e588a8ad635ee01e83`

