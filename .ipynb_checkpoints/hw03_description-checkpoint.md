# Homework 3 - _From Notebooks to Research Packages, Part II_

* **Statistics 159/259, Fall 2025**
* **Due Friday 11/06/2025, 11:59PM PT**
* Prof. F. Pérez and GSIs J. Butler and S. Andrade, Department of Statistics, UC Berkeley.
* This assignment is worth a maximum of **40 points**.
* Assignment type: **individual**.

For this assignment, we will start from the conclusion of HW 2, using again the code from the [LIGO Gravitational Wave Detection Tutorial](https://github.com/losc-tutorial/LOSC_Event_tutorial).

In this assignment we are effectively giving you the solution to HW 2 as a starting point; you will now add a bit more structure, tests, documentation, etc, to complete the picture.

## Deliverables

### [5 points] Repository structure

The repository starts with all the code and data with the same layout as LIGO created it. First, let's organize the input and output files from the main notebook (`LOSC_Event_tutorial.ipynb`). Create three new directories: `data`, `figures`, and `audio`. Move the `.hdf5` files and the `.json` file into the `data` folder. Now, run through the notebook, correcting any cells where the data is loaded to now look in the `data` directory for each file to be loaded. Also, whenever a figure/plot or audio file is saved in the notebook, edit the file path so that the file is saved directly in the `figures` or `audio` directories, respectively.

*Hint: For editing the data loading paths, consider modifying the paths contained in the variables `fnjson`, `fn_L1`, `fn_H1`, and `fn_template` so that they look in the `data` folder. Remember to also write the csv created in the very last cell directly to the `data` folder as well.*


### [ 5 points] Installable package

In HW 2 you made `ligotools` usable as a local package that could be imported from the current directory. Now you will make it an *installable* package as discussed in [lecture](https://stat159.berkeley.edu/fall-2025/lectures/packaging/packaging/), with an appropriate `pyproject.toml` file. Use the [mytoy](https://github.com/fperez/mytoy) repository as guiding example for this and next part, being sure to include the same dependencies as specified in the `environment.yml` file (you can specify `python >= 3.9`).

*Hint: You may see an error indicating that `numpy` could not be found when building the package. You may have to include `numpy` in the list of required packages under the `build-system` section of `pyproject.toml`.*


Note: for the authorship, you should list as authors "Ligo Scientific Collaboration (LSC) and `<your name>`".

### [ 5 points ] Add tests for `readligo.py`

You should create at least two small tests that test the output of the functions in `readligo.py`, adding them to the `ligotools` package.  Make a subfolder within the `ligotools` folder called `tests` and put in there a file called `test_readligo.py` with your tests given as functions. 

The command `pytest ligotools`, run from the home folder of your homework repo, should run all those tests.

### [ 5 points ] Create `utils.py` and add some utilities

In the `ligotools` package, make a new module called `utils.py` and move the following functions from the notebook into `utils`: `whiten`, `write_wavfile`, `reqshift`. You will then need to update the notebook to use these functions imported from `ligotools.utils` instead, ensuring that the notebook now runs with no errors.

Also find the notebook cell that begins with

```
# -- To calculate the PSD of the data, choose an overlap and a window (common to all detectors)
#   that minimizes "spectral leakage" https://en.wikipedia.org/wiki/Spectral_leakage
```

and move its plotting code into a separate utility function in your `utils.py` file. Call this function from the notebook in a similar way to the other utility functions.

*Hint: in your utils.py file, make sure you import all the packages those functions need..*

### [ 5 points ] Add tests to `utils.py`

You should add two separate small tests that test the output of functions in `utils.py`. Add those tests into the `tests` directory you created earlier, into a separate `python` script called `test_utils.py`. These should the functions you moved from the notebook (`whiten`, `write_wavfile`, `reqshift`).

The command `pytest ligotools`, called from the home directory of your repo, should run all those tests.

### [ 5 points ] MyST: Local Builds and Deploying to GitHub Pages

Set up the repository to be a proper MyST one that builds a page for the main notebook and includes a visible Binder link in the build. Be sure can you can view a local copy of your website on the Jupyterhub, as detailed in [Lab 7](https://stat159.berkeley.edu/fall-2025/lab/lab07/lab07/). *Please only include the landing page with the binder link and the notebook as tabs on your website; you can control which pages get displayed by editing the `myst.yml` file and including a table of contents, as specified in Lab 8 and the MyST documentation.*

Further, deploy your website to GitHub Pages, ensuring a GitHub Action has been properly setup and configured so that, each time you push to the repo, the website automatically updates. Details on how to complete this are also provided in [Lab 7](https://stat159.berkeley.edu/fall-2025/lab/lab07/lab07/).

### [ 5 points ] Makefile

There should be a `Makefile` with the following targets.

- `env`: creates and configures the environment (but does not activate it). If you have already created an environment of the same name, have the command instead update the environment with a provided `environment.yml` file
- `html`: build the `html` rendering of your MyST site (i.e. what's produced when you call `myst build --html` on the command line). Note this build can only be viewed locally.
- `clean`: clean up the `figures`, `audio`  and `_build` folders.

### [5 points] GitHub repository

In this homework we are going to evaluate your overall workflow using git and GitHub. Be sure that you repository includes:

- Clear commit messages as you make progress on the homework.
- You should have a `README.md` with a basic description of the project with the Binder badge on it so you can directly launch Binder from there.
- Not include any other file or folder that those needed for the project. For archiving this you can include a `.gitignore` file with the files you want git to ignore.
- Add the link to your MyST site to the repo (preferably in the 'About' section of your repo on GitHub).
- Complete the `ai_documentation.txt` file with descriptions of how you used AI tools for this assignment, and any prompts and output.
