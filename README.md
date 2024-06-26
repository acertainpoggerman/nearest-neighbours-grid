# CodeAWeek #1

### Setting up the Project

The project will use a Python 3.12 virtual environment (venv) to run itself. To set up the virtual environment:

- First install the `virtualenv` package using `pip`:
```properties
pip install virtualenv
```

- Create a venv in the project using the command `python 3.12 -m venv <venv-name>` for example:
```cmd
C:\...\nearest-neighbours-grid> python3.12 -m venv myvenv
```

- To activate the virtual environment, run the command `<venv-name>\Scripts\Activate.ps1` (If you are using **Powershell**), or `<venv-name>\Scripts\activate.bat` (If you are using **Command Prompt**), for example:
```powershell
# powershell
PS C:\> myvenv\Scripts\Activate.ps1
```
```powershell
# cmd
C:\> myvenv\Scripts\activate.bat
```

> [!CAUTION]
> If You get an error in Powershell: `<venv-name>\Scripts\Activate.ps1 cannot be loaded because the execution of scripts is disabled on this system.` run the 

- Install the required libraries using 