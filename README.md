<h2 align="center">Implementation of Applied Elasticity Problem in Juypter Notebook with SymPy</h2>


This is a repository of Jupyter Notebook files that I have used to solve the problems related to the course "Applied Elasticity" in the Autumn Semester. Since the derivation of the biharmonic equation in polar coordinates is rather long, I thought of using Jupyter Notebook and SymPy to programmatically derive the expressions. 

### 2D Elasticity in Polar Coordinates:

We follow the development of the ideas as presented in the classic "Theory of Elasticity" by Timoshenko and Goodier.

* The file ["PolarCoordinates_Definitions.ipynb"](https://github.com/anuragap98/Applied-Elasticity-Notebook/blob/main/2D%20Elasticity%201-%20Polar%20Coordinates%20using%20SymPy.ipynb) is where all the transformations from the rectangular Cartesian coordinate system to the polar coordinate system required to obtain the biharmonic equation are set up. The stresses are also transformed from the rectangular Cartesian coordinate system to the polar coordinate system. <br>


* The functions defined in the file ["PolarCoordinates_Definitions.ipynb"](https://github.com/anuragap98/Applied-Elasticity-Notebook/blob/main/2D%20Elasticity%201-%20Polar%20Coordinates%20using%20SymPy.ipynb) are collected in [polarUtilities.py](https://github.com/anuragap98/Applied-Elasticity-Notebook/blob/main/polarUtilities.py). These definitions will be invoked in the subsequent files by importing `polarUtilities`. <br>


* The file ["Axisymmetric_PressureVessel.ipynb"](https://github.com/anuragap98/Applied-Elasticity-Notebook/blob/main/2D%20Elasticity%201-%20Axisymmetric%20Problems%20%E2%80%93%20Thick-Walled%20Pressure%20Vessel.ipynb) addresses the set-up of axisymmetric problems with particular focus on the solution of the thick-walled pressure vessel problem. This file uses the [polarUtilities.py](https://github.com/anuragap98/Applied-Elasticity-Notebook/blob/main/polarUtilities.py) file. <br>


* The file ["CurvedBar_PureBending_onlystress.ipynb"](https://github.com/anuragap98/Applied-Elasticity-Notebook/blob/main/2D%20Elasticity%201-%20Pure%20Bending%20of%20a%20Curved%20Bar.ipynb) addresses the problem of pure bending of a curved bar. This file uses the [polarUtilities.py](https://github.com/anuragap98/Applied-Elasticity-Notebook/blob/main/polarUtilities.py) file. <br>


* The other file ["Flamant.ipynb"](https://github.com/anuragap98/Applied-Elasticity-Notebook/blob/main/Elasticity%202%20-Flament%20problem.ipynb) addresses another classic problem of a vertical point loading on an infinite half space. This file uses the [polarUtilities.py](https://github.com/anuragap98/Applied-Elasticity-Notebook/blob/main/polarUtilities.py) file. <br>
   

<p align="center">Contribution -> (https://github.com/jeevanjyoti4/elasticity)</p>

