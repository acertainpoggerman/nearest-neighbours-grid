# CodeAWeek #1

## The Challenge

## Setting up the Project

### Cloning this Repository
To start this project, Fork the repository, and clone it to your local machine. If you have trouble doing this, see [Forking Repositories](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo).

<!-- TODO: Add Text Here -->

### Setting up the venv
The project will use a Python 3.12 virtual environment (venv) to run itself. Simplified, a virtual environment is an isolated running space of the programming language (in this case Python). This means all libraries and scripts in this environment are isolated from other environments (even the system version of Python).

> [!TIP]
> To learn more about python's virtual environment, you can check the official documentation [here](https://docs.python.org/3/library/venv.html).

To set up the virtual environment:

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

> [!TIP] 
> If You get an error in Powershell: `<venv-name>\Scripts\Activate.ps1 cannot be loaded because the execution of scripts is disabled on this system.` run the following command:
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force
> ```
> and try to activate the virtual environment again.

<br>

- Install the required libraries from the `requirements.txt` file using the command with the venv activated (i.e. in `(venv) PS C:\...\nearest-neighbours-grid>`):
```powershell
pip install -r requirements.txt
```

> [!IMPORTANT]  
> Make sure to select the **venv Python Executable** as the Interpreter if you are using VS Code. If you are using **PyCharm** to load the project, the venv Interpreter should be automatically detected in the project.

### Creating your Solution
Your directory tree should look similar to this:

```
nearest-neighbours-grid/
├─ src/
│  ├─ misc/
│  │  ├─ constants.py
│  │  ├─ utils.py
│  ├─ main.py
│  ├─ grid.py
│  ├─ button.py
├─ venv/
├─ assets/
```

You will ideally only need to write code in `grid.py`, but if you want to add any helper functions or constants, you can place them in `utils.py` or `constants.py` under `misc/`.
