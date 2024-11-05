# Code from Amsterdam PVT November 2024

This repository is used to share code examples presented in the Amsterdam PVT in November 2024.

## Before you start
If you do not have programming experience before hand, there are couple of steps you will need to cover before you can start trying the examples out.

### Prepare your developer environment
- Install Python version 3 for Python related code
- Install Git
- Install a code editor, for example Visual Studio Code

### Clone the repository and install required libraries
When you have your developer environment up and running, make sure you install all libraries and modules required for your scripts. To keep your developer environment tidy, make sure to activate your virtual environment before installing the libraries.

Clone this repository to the environment in which your are working:
```bash
git clone https://github.com/juuliasantala/pvt_november_2024.git
```

Install the requirements to have all the necessary libraries for the code examples to work.

```bash
pip install -r requirements.txt 
```

### Set up environment variables in the subfolders

To execute the `cc_client_data` or `iosxe_livetools` code, create the file `.env` from `env.template` and update the values to match your environment.

1. Create a file `.env` from the `env.template`
    ```bash
    cp env.template .env
    ```

1. Fill in the data to the `.env`.


## Authors & Maintainers
* Juulia Santala jusantal@cisco.com

## License
This project is licensed to you under the terms of the [Cisco Sample Code License](LICENSE).

