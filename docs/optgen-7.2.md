---
title: "OptGen 7.2"
nav_order: 5
---

# OptGen 7.2.17

📅 Date: 2018-12-07<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.2.17-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.2.17-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * fixed an error related to the identification of the first demand segment being elastic for firm capacity/energy disconsideration

* IHM
  * fixed an error related to the visualization of firm capacity/energy values relative to plants that are using the system's default value in the min/max capacity constraint screen

# OptGen 7.2.17rc1

📅 Date: 2018-11-30<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.2.17rc1-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.2.17rc1-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * fixed an error related to the identification of firm capacity/energy constraints' infeasibility related to "all systems" 
  * fixed an error related to an incorrect consideration of projects being completely disbursed before the beginning of the study horizon in the total investment cost calculation

* IHM
  * fixed an error related to the identification of projects' names in the user-defined expansion plan (case-sensitive issue)

# OptGen 7.2.16

📅 Date: 2018-10-19<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.2.16-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.2.16-setup-linux.zip)

## New Features and Improvements

* OptGen 1
  * Now the model stops when a negative GAP convergence has been reached. This usually happens when the operative module does not converge
  * The writing of the hydro modification file has been updated to incorporate inflow x turbining and outflow vs elevation modification tables

* SDDP Importer
  * The importer has been updated to consider the new version of renewable and hydro modification files

## Fixed Bugs

* OptGen 1
  * fixed an error related to the identification of cases with elastic demand

# OptGen 7.2.15rc5

📅 Date: 2018-08-02<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.2.15rc5-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.2.15rc5-setup-linux.zip)

## New Features and Improvements

* SDDP Importer
  * Hydro inflow scenarios may be generated for all plants now regardless of which systems are selected for the execution

* OptGen 1
  * the writing of the renewable modification files has been updated to incorporate the O&M cost and the spilling penalty
  * added option to perform an execution restart recalculating the upper bound
  * new outpdec_<iter>.csv file with the investment decisions made in each iteration

## Fixed Bugs

* OptGen 1
  * fixed errors related to SDDP cases having weekly steps
  * fixed errors when reading the firm capacity/energy modification data

# OptGen 7.2.15rc4

📅 Date: 2018-04-06<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.2.15rc4-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.2.15rc4-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * fixed an error in the calculation of following outputs: "Long-run average cost (LRAC)" and "Long-run marginal cost (LRMC)"

* IHM
  * fixed an error on the "delete" button present in the firm capacity modification screens
  * fixed an error related to blocking the initial date for edition in the user-defined expansion plan screen when the decision date of the project is fixed 

# OptGen 7.2.15rc3

📅 Date: 2018-02-08<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.2.15rc3-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.2.15rc3-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * fixed an error when writing the firm capacity/energy outputs
  * fixed an error while considering default firm capacity/energy values for dummy plants having production coefficient less than or equal to zero

# OptGen 7.2.15rc2

📅 Date: 2018-01-31<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.2.15rc2-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.2.15rc2-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * fixed an error related to the firm capacity/energy of thermal plants presenting alternative fuels
  * fixed an error related to the installed capacity consideration of thermal plants presenting alternative fuels in the min/max constraints

# OptGen 7.2.14

📅 Date: 2017-12-07<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.2.14-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.2.14-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * fixed an error in the rolling horizon with projects presenting continuous decision variable

# OptGen 7.2.13

📅 Date: 2017-11-27<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.2.13-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.2.13-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * fixed an error when considering a total min/max constraint including fixed projects whose date of entrance into operation is set before the beginning of the study horizon

* IHM
  * fixed an error while opening the Optimal expansion plan in order to point to the OUTPDEC.CSV file

# OptGen 7.2.12

📅 Date: 2017-09-13<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.2.12-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.2.12-setup-linux.zip)

## New Features and Improvements

* OptGen 1
  * It is now possible to run OptGen using renewable stations
  * Increase of the maximum number os stages in weekly cases
  * New possible agents in minimum/maximum constraints: circuits
  * Increase in maximum number of scenarios to 99 (Scenario type of execution)

## Fixed Bugs

* OptGen 1
  * fixed a possible error when considering projects with construction time

* IHM
  * fixed an error when editing in "Value" field minimum/maximum constraints
  * fixed an error when editing payment schedules

# OptGen 7.2.11

📅 Date: 2017-01-18<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.2.11-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.2.11-setup-linux.zip)

## New Features and Improvements

* SDDP Importer
  * it is now possible to import weekly scenarios

## Fixed Bugs

* OptGen 1
  * fixed a possible error when reading an outdated parameter file
  * fixed a possible error when reading sddp's parameter file
  * fixed an error when running SDDP scenarios and reading hourly load data
  * fixed an error when running rolling horizon and using external initial storage or inflow in SDDP data
  * fixed a possible error when running rolling horizon and using continuous decision projects
  * fixed a possible error when running horizon year and using exclusively maximum capacity constraints

* IHM
  * fixed an error when reading an outdated user defined expansion plan file

* SDDP Importer
  * fixed a possible error when reading projects' typical data
  * fixed an error importing integer decision projects as continuous projects