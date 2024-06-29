# Code a Week #1


| **Difficulty** | 🟨🟨🟨⬛⬛⬛ `Medium`      |
| :---------- | -------------------------------- |
| **Language(s)**   | `Python`                   |
| **Themes**   | `GUI` `Algorithms` `Conceptual` |

## Challenge
<p align="center">
  <img src="https://github.com/acertainpoggerman/nearest-neighbours-grid/assets/127584171/74d9e204-2917-434f-a97c-47fc28779953" alt="UI Picture" width="640">
</p>

<br>

You have a grid, text above it indicating the number of points on the grid, as well as 3 buttons below the grid:

- (_leftmost_) The link button, which when clicked should connect the 2 closest points on the grid with a line.
- (_middle_) The refresh button, which clears the grid (if the grid is in click mode), or should randomly put `n` number of points on the grid (If it not in click mode).
- (_rightmost_) The button that toggles click mode on/off. Will highlight blue if in click mode.

The challenge is to implement 3 things:
- The method that randomizes the points on the grid.
- The method for adding / removing of points in **click mode**.
- The method that finds the 2 **nearest points** in the grid (in _O(nlogn)_ time).

See more information about the challenge [here](#creating-your-solution).

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

<br>

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

You will ideally only need to write code in `grid.py`, but if you want to add any helper functions or constants, you can place them in `utils.py` or `constants.py` under `misc/`. Before we go to the challenges, it is important to understand how the points on the grid work:

> [!IMPORTANT]
> Points on the grid are stored in the attribute `self.points` in the Grid object, each point being represented as a tuple `(x, y)`, where x and y are **integers**. The point coordinates are in **grid-space** as opposed to **screen-space** for example:
> 
> <img src="https://github.com/acertainpoggerman/nearest-neighbours-grid/assets/127584171/38787877-e735-4818-b69c-014a52b25b8e" alt="UI Picture" width="300">
>
> To add a point to the grid, you simply append it to `self.points`, and to remove a point from the grid, use `self.points.remove((x, y))`. As an additional rule, points cannot be placed on or outside the boundary (i.e. the thick line):
>
> <img src="https://github.com/acertainpoggerman/nearest-neighbours-grid/assets/127584171/2ae076e4-56ae-459c-8c35-b3e634a7fda8" alt="UI Picture" width="300">
> 




There are only 3 functions required to be implemented:

1. `Grid.randomize_points(n)` (~ Line 202 in `grid.py`): A method with takes a number of points `n` & should return a list of `n` randomly placed non-overlapping points (i.e. points that do not share the same coordinates) on the grid.

Example: `randomize_points(5)`
| `self.points = [(2, 4), (1, 3), (5, 1), (4, 2), (1, 1)]` | `self.points = [(6, 6), (4, 6), (6, 2), (7, 5), (3, 3)]` | `self.points = [(1, 1), (2, 2), (4, 4), (6, 6), (7, 7)]` |
| -- | -- | -- |
| ![image](https://github.com/acertainpoggerman/nearest-neighbours-grid/assets/127584171/ea58d51e-afd0-48b9-a9f0-fee774c118bf) | ![image](https://github.com/acertainpoggerman/nearest-neighbours-grid/assets/127584171/c77e8868-c5ff-491f-b338-58eca316b1bd) | ![image](https://github.com/acertainpoggerman/nearest-neighbours-grid/assets/127584171/cbe3358a-3b42-40c5-a927-31ea3d1eb3ee) |


2. `Grid.toggle_point(pos)` (~ Line 227 in `grid.py`): A method which takes the position of the cursor relative to the grid and should add or remove a point from an intersection on the grid nearest to that cursor position (Essentially snap the points to the grid intersection). Since the points are in grid space.

Example:
| Adding Points to the Grid | Removing Existing Points from the Grid |
| -- | -- |
| ![grid-clicking](https://github.com/acertainpoggerman/nearest-neighbours-grid/assets/127584171/75137cf9-d3eb-4217-9edc-e27ab7b4c066) | ![grid-clicking-removing](https://github.com/acertainpoggerman/nearest-neighbours-grid/assets/127584171/e3088bd6-4072-4641-9300-07a44f9f38ae) |

3. `Grid.find_nearest_points()` (~ Line 254 in `grid.py`): A method which should return a tuple containing the coordinates of the two closest points. If it works as intended, clicking the link button in the GUI should draw a line connecting the 2 closest points. In the case the closest 2 points share the same distance, only one of the pairs should be picked.

Example:
| `self.points = [(6, 6), (4, 6), (6, 2), (7, 5), (3, 3), (1, 2), (3, 1), (1, 7)]` | `self.points = [(1, 1), (3, 3), (1, 2), (7, 7), (4, 4), (6, 3), (7, 3), (3, 1), (1, 7)]` |
| --- | --- |
| ![Screenshot 2024-06-29 154915](https://github.com/acertainpoggerman/nearest-neighbours-grid/assets/127584171/ba332319-6231-42aa-ad91-fdbf7b87a2e8) | ![image](https://github.com/acertainpoggerman/nearest-neighbours-grid/assets/127584171/beea5c90-ad46-4919-a965-8b4f5bedddee) |


> [!IMPORTANT]
> The program is made to crash intentionally on any of the following conditions 😃:
> - There are duplicate points (i.e. points with the same coordinates) in `self.points`.
> - There are points placed on or outside the grid boundary in `randomize_points()` or `toggle_point()`.
> - `find_nearest_points()` returns coordinates of points that do not currently exist on the grid.

## Extra
This challenge was inspired from **Divide & Conquer** algorithms, specifically *finding nearest neighbours* algorithm. Other algorithms you can check out that follow this principle are:
- Sorting Algorithms (mergesort & quicksort)
- The Counting Inversions Algorithm (Used in earlier page ranking & recommendation systems)

Good Luck, Have Fun 💀.


