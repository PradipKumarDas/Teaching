# ADVANCED MACHINE LEARNING

## Experiments

### Dimensionality Reduction

    1.1 Dimensionality Reduction Using Principal Component Analysis

_Remaining experiments are coming up._


## Laboratory Environment Setup on Windows [ONE-TIME SETUP]

Follow the below instructions to setup the environment on Windows to perform experimens.

1. Log into Windows as **_Student_** standard account. If you find that the current account is Administrator or BNMIT, make sure you log out and log back using Student account.

2. Open **Windows PowerShell** console and execute the following command to install a specific version of **_uv_** - the package and project management tool.
    ```
    PS> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.12.4/install.ps1 | iex"
    ```
    Close the PowerShell console.

3. Open **Command Prompt** and type `D:` and press Enter to change current drive from `C:` to `D:`.
    > [NOTE] Non-Windows installation drive such as `C:` is highly preferred. If `D:` or any other secondary drive is not available, continue installation on `C:` drive. In that case, replace letter `D` with 'C' wherever mentioned in this installation section.
  
4. Type `uv init lab_experiments` and press Enter to create workplace.

5. Type `cd lab_experiments` to change the directory to the workspace.

6. Keeping the Command Prompt console opened, open URL https://github.com/PradipKumarDas/Teaching/lab_experiments in a browser and download `pyproject.toml` and `uv.lock` file. 

7. Use **File Explorer** to move the downloaded files to directory `D:\lab_experiments` overwriting the existing ones.

8. Go back to already opened Command Prompt and check if it is already in any environment such as `base` the indication of which appear as a prefix to the prompt like `(base)D:\lab_experiments>". If so try executing command `deactivate` or `conda deactivate` to come out of that environment.

9. type `uv sync --extra cpu` for a CPU-only computer (or `uv sync --extra cu130` for GPU-enabled computer) and press Enter to synchronize the dependencies with the target environment. Note that this may take several minutes to complete depending upon Internet speed.

9. Keeping the Command Prompt open, open URL https://drive.google.com/drive/folders/10z5_cOia54qWcV541v7Vg-Hhy01xdpmJ?usp=sharing and download `data.zip`.

10. Extract the `.zip` file and move the extracted directory `data` to `D:\`. Make sure that contained files and subdirectories appear directly under `D:\data` and not under `D:\data\data`.

11. Go back to already opened Command Prompt and type `md advanced_machine_learning` to create course specific directory `advanced_machine_learning` under `D:\lab_experiments`.

12. Close the Command Prompt console.

Setup of the environment is now complete. 

## Activating Environment to Perform Experiments

Follow only the below instructions to perform experiments next time onwards.

1. Open **Command Prompt**, type `D:` and press Enter to change current drive from `C:` to `D:`.

2. Type `cd lab_experiments` and press Enter to change working directory from root to `lab_experiments`.

3. Type `.venv\Scripts\activate` and press Enter to activate development environment. Once activated, its prompt will appear before the command prompt like `(lab_experiments)D:\lab_experiments>`.

4. Type `cd advanced_machine_learning` and press Enter to change directory to course specific working directory.

5. Type `jupyter lab` and press Enter to open code editor. Note that the only Jupyter Lab is formally supported for now.

    > [**TROUBLESHOOTING**]
    > If error related to non-availability of Microsoft Visual C++ Redistributable is shown, perform the following steps.
    > - Open URL https://visualstudio.microsoft.com/downloads/ in a browser, 
    > - Expand section **Other Tools, Frameworks, and Redistributables**, 
    > - Select optin **Microsoft Visual C++ v14 Redistributable** with checkbox **x64** ticked and click **Download**.
    > - Execute the downloaded executable and follow the online instructions to install redistributables. Enter Administrator credential when asked.


