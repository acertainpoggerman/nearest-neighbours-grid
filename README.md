# CodeAWeek #1

## Setting up the Project

### Cloning this Repository
TODO: Add Text Here

### Final Touches
The project will use a Python 3.12 virtual environment (venv) to run itself. To set up the virtual environment:

- First install the `virtualenv` package using `pip`:
```properties
pip install virtualenv
```

- Create a venv in the project (`C:\...\nearest-neighbours-grid>`) using the following command:
```cmd
python3.12 -m venv myvenv
```

- To activate the virtual environment, run the command `<venv-name>\Scripts\Activate.ps1` (If you are using **Powershell**), or `<venv-name>\Scripts\activate.bat` (If you are using **Command Prompt**), for example:
```powershell
# powershell
PS C:\...\nearest-neighbours-grid> myvenv\Scripts\Activate.ps1
```
```powershell
# cmd
C:\...\nearest-neighbours-grid> myvenv\Scripts\activate.bat
```
You should have something that looks like this:
```powershell
(venv) PS C:\...\nearest-neighbours-grid> 
```

<br>

> [!TIP] 
> If You get an error in Powershell: `<venv-name>\Scripts\Activate.ps1 cannot be loaded because the execution of scripts is disabled on this system.` run the following command:
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force
> ```
> and try to activate the virtual environment again.

<br>

- Install the required libraries from the `requirements.txt` file using the command with the venv activated (i.e. in `(venv) PS C:\...\nearest-neighbours-grid>`):
```powershell
pip install -r requirements.text
```
