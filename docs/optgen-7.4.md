---
title: "OptGen 7.4"
nav_order: 3
---

# OptGen 7.4.49

ðŸ“… Date: 2022-03-22
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.49-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.49-setup-linux.zip)

## New Features and Improvements

* OptGen 1
  * Update the license identification to allow two different dongle USB keys connected to the computer
## Fixed Bugs

* OptGen 2
  * Fixed a bug with circuit sum constraints

# OptGen 7.4.48

ðŸ“… Date: 2022-02-14
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.48-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.48-setup-linux.zip)

## Fixed Bugs

* OptGen 2
  * Fixed the identification of incremental capacity constraints 
  * Fixed the sizing option with minimum incremental constraint (now the maximum and minimum year will be transfered to the year horizon)

# OptGen 7.4.47

ðŸ“… Date: 2022-02-01
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.47-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.47-setup-linux.zip)

## Fixed Bugs

* OptGen 2
  * Allow the names of interconnections to have a maximum of 12 characters instead of 10
  * Fixed an error related to elastic demand hourly prices

# OptGen 7.4.46

ðŸ“… Date: 2021-12-09
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.46-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.46-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed reading of SDDP configuration data to eliminate white spaces at the beginning of agent names

# OptGen 7.4.45

ðŸ“… Date: 2021-10-05
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.45-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.45-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error in the precedence constraint modeling with delay using the rolling horizon strategy

* OptGen 2
  * Fixed an error in the precedence constraint modeling with delay due to the rolling horizon strategy
  * Fixed an error related to the substitution of existing hydro plants

# OptGen 7.4.44

ðŸ“… Date: 2021-08-26
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.44-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.44-setup-linux.zip)

## Fixed Bugs

* IHM
  * Fixed an error related to the identification of interconnection projects in the interface

# OptGen 7.4.43

ðŸ“… Date: 2021-08-26
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.43-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.43-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error related to the expansion of "dummy" plants (multi-fuels or 3-winding transformer) when there is a timing strategy or a simulation of the OptGen 2 decision.
  * Fixed an error related to the expansion decision of hydro projects with dead storage fill-up
  * Add support to the version 2 of the datmcap.csv file

# OptGen 7.4.42

ðŸ“… Date: 2021-08-19
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.42-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.42-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed a numeric error while writing the optimal expansion plan file (outpdec.csv)

# OptGen 7.4.41

ðŸ“… Date: 2021-08-11
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.41-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.41-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed a bug in the importer of projects from a SDDP database when the dcirc file is in version 2

* OptGen 2
  * Fixed a bug, in the execution report, related to the comparison between OptGen 2 and SDDP operating cost

* IHM
  * Update the graph module to make it compatible with the new version of SDDP

# OptGen 7.4.40

ðŸ“… Date: 2021-06-28
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.40-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.40-setup-linux.zip)

## New Features and Improvements

* OptGen 1
  * The model now accepts continuous decision in the user-defined plan, even if the project is defined as binary

* OptGen 2
  * The execution of the OptGen 2 will now be skipped if there is a fixed user-defined plan

* IHM
  * Added functionality to execute a post-run script after the execution

## Fixed Bugs

* OptGen 1
  * Synchronized the inflows used in OptGen's SDDP final simulation with an execution of the SDDP "Stand-alone"

* OptGen 2
  * Fixed operational cost final report (file opt2_optgct)
  * Fixed an error with obligatory projects that are not in the user-defined plan, and have a fixed entrance date in the datprjc file

# OptGen 7.4.39

ðŸ“… Date: 2021-05-20
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.39-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.39-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error on the precision while printing the expansion plan solution
  * Fixed an error related to reading csv alphanumeric fields of input data files
  * Fixed an error related to battery projects being considered in the RHS of firm energy/capacity constraints

# OptGen 7.4.38

ðŸ“… Date: 2021-03-18
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.38-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.38-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed the integration between OptGen and SDDP 16.1 when the output files format is binary

# OptGen 7.4.37

ðŸ“… Date: 2021-02-12
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.37-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.37-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error related to a non-initialized variable

# OptGen 7.4.36

ðŸ“… Date: 2021-02-01
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.36-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.36-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error related to the new format of the sensib.dat file

# OptGen 7.4.35

ðŸ“… Date: 2020-11-30
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.35-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.35-setup-linux.zip)

## Fixed Bugs

* OptGen 2
  * Fixed an error when a thermal project substitutes an existing thermal plant with must-run constraint
  * Fixed an error with sum of interconnection constraint when the case is considering the network (the interconnections must be ignored)

# OptGen 7.4.34

ðŸ“… Date: 2020-10-16
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.34-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.34-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error in the timing strategy when using historical inflows in SDDP with an initial condition close to the end of the historical data

# OptGen 7.4.33

ðŸ“… Date: 2020-09-22
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.33-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.33-setup-linux.zip)

## New Features and Improvements

* IHM
  * Added a funcionality to check the input data before running the case (this functionality does not require the license dongle)

## Fixed Bugs

* OptGen 2
  * The model was considering pump hydro plants in the firm capacity/energy and installed capacity constraints. Now the model will disregard this technology in those constraints
  * Fixed an error related to installed capacity constraints when there are projects with modifications of type zero in SDDP (these modifications must be ignored by the model)

# OptGen 7.4.32

ðŸ“… Date: 2020-09-15
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.32-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.32-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error in the sizing strategy when there is a project not belonging to the study, but is selected in the user-defined expansion plan

* OptGen 2
  * Fixed an error related to the identification of circuits' expansion in the user-defined expansion plan

# OptGen 7.4.31

ðŸ“… Date: 2020-08-27
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.31-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.31-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error related to the sizing strategy when there is an user defined expansion plan being considered

# OptGen 7.4.30

ðŸ“… Date: 2020-07-22
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.30-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.30-setup-linux.zip)

## New Features and Improvements

* OptGen 1
  * New output file "outmcap.csv" with the RHS value of the additional minimum/maximum constraints

## Fixed Bugs

* OptGen 1
  * Fixed an error related to the firm capacity/energy of thermal and renewable plants that can be replaced by a project

# OptGen 7.4.29

ðŸ“… Date: 2020-07-07
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.29-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.29-setup-linux.zip)

## Fixed Bugs

* IHM
  * Assign the SDDP model as the default operating model when creating a new OptGen case or converting an old database

# OptGen 7.4.28

ðŸ“… Date: 2020-07-07
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.28-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.28-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error in the transmission network projects with SDDP 16

* IHM
  * Fixed an error related to the import functionality of hydro inflows from Time Series Lab
  * Fixed an error related to the identification of battery projects

# OptGen 7.4.27

ðŸ“… Date: 2020-06-24
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.27-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.27-setup-linux.zip)

## Fixed Bugs

* OptGen 2
  * Fixed an error related to a version of PSRClasses not compiled in linux
  * Fixed an error related to the typical days mapping, when there is the same amount of typical days per season, but a different number of typical days per stage

# OptGen 7.4.26

ðŸ“… Date: 2020-06-05
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.26-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.26-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error in the integration with SDDP 16.0

* OptGen 2
  * Fixed an error related to existing modifications of O&M costs for thermal projects
  * Fixed an error in the second kirchoff law for circuits not selected for monitoring
  * Fixed an error with the identification of circuit projects in the optimal expansion plan output file

# OptGen 7.4.25

ðŸ“… Date: 2020-05-17
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.25-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.25-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error related to obligated projects with minimum year equal maximum year of entrance, in rolling horizon strategy

# OptGen 7.4.24

ðŸ“… Date: 2020-05-06
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.24-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.24-setup-linux.zip)

## Fixed Bugs

* OptGen 2
  * Fixed an error related to projects in the user-defined expansion plan, entering in the middle of the horizon and participating in a precedence constraint

# OptGen 7.4.23

ðŸ“… Date: 2020-04-28
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.23-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.23-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error related to obligated projects with minimum year equal maximum year of entrance, in the middle of the horizon

# OptGen 7.4.22

ðŸ“… Date: 2020-04-27
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.22-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.22-setup-linux.zip)

## Fixed Bugs

* OptGen 2
  * Fixed an error related to the maximum capacity constraints that are defined for years after the current year of the rolling horizon

# OptGen 7.4.21

ðŸ“… Date: 2020-03-20
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.21-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.21-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error related to chronological investment cost of fixed projects before the initial year of the horizon
  * Fixed an error related to the execution of two instances of OptGen at the same time

# OptGen 7.4.20

ðŸ“… Date: 2020-03-05
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.20-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.20-setup-linux.zip)

## Fixed Bugs

* OptGen 2
  * Fixed an error related to negative values in sum of circuit flow constraints

# OptGen 7.4.19

ðŸ“… Date: 2020-02-27
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.19-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.19-setup-linux.zip)

## Fixed Bugs

* OptGen 2
  * Fixed an error in the battery net generation output file
  * Fixed thermal commitment by stage modelling
  * Changed the circuit reactance default values to 0.05% for reactance values lower than 0.05%

# OptGen 7.4.18

ðŸ“… Date: 2020-02-15
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.18-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.18-setup-linux.zip)

## Fixed Bugs

* OptGen 2
  * Fixed an error related to the maximum capacity of battery projects when there are SDDP modifications (that should be ignored) for them
  * Fixed an error in the battery balance modelling when OptGen 2 is executed by blocks

# OptGen 7.4.17

ðŸ“… Date: 2020-02-11
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.17-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.17-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error related to the year of entrance in operation in the Optimal Expansion CAPEX value report

* OptGen 2
  * Fixed an error related to the treatment of obligatory projects before the initial year of the study

# OptGen 7.4.16

ðŸ“… Date: 2020-02-07
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.16-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.16-setup-linux.zip)

## Fixed Bugs

* OptGen 2
  * Fixed an error in the calculation of the hydro firm capacity.
  * Fixed an error related to negative values of hydro O&M cost.
  * Fixed an error with reinforcement projects in the firm capacity/energy constraints

* IHM
  * Fixed an error in the firm capacity/energy screen.

# OptGen 7.4.15

ðŸ“… Date: 2019-12-04
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.15-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.15-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error related to the new version of the demand by blocks file (compatibility with SDDP 15.2Beta).

# OptGen 7.4.14

ðŸ“… Date: 2019-11-13
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.14-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.14-setup-linux.zip)

## Fixed Bugs

* OptGen 2
  * Fixed an error in precedence constraints when the maximum delay is zero.

# OptGen 7.4.13

ðŸ“… Date: 2019-11-05
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.13-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.13-setup-linux.zip)

## New Features and Improvements

* OptGen 2
  * Improved the computational time of reading and writing the problem by freeing the memory used in the previous year.

# OptGen 7.4.12

ðŸ“… Date: 2019-11-04
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.12-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.12-setup-linux.zip)

## New Features and Improvements

* OptGen 1
  * Added a new report (sddpwarnings.out) with the warnings from the sddp (in the sddpwarnings.csv file) per each iterations.

# OptGen 7.4.11

ðŸ“… Date: 2019-10-31
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.11-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.11-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error in the modification of the emergency flow limit of circuits.

* OptGen 2
  * Fixed an error in the output file of commitment decision, when the number of commitments blocks are less than 24.

* IHM
  * Fixed an error in the scenario selection screen when the total probability is close to 1.

# OptGen 7.4.10

ðŸ“… Date: 2019-10-04
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.10-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.10-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * The maximum number of batteries allowed has been increased to 5000.

# OptGen 7.4.9

ðŸ“… Date: 2019-10-04
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.9-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.9-setup-linux.zip)

## Fixed Bugs

* OptGen 2
  * Fixed an error in precedence constraints with projects not belonging to the study. Now the model will ignore them and build the constraints considering only the projects belonging to the study.
  * Fixed an error with the delay parameter in associative constraints.
  * Fixed an error related to a warning message of fuel contract.
* IHM
  * Fixed an error in the compact case tool.

# OptGen 7.4.8

ðŸ“… Date: 2019-09-26
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.8-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.8-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error related to modification of firm energy/capacity data that was ignored when modified value was equal to initial value.
  * Fixed an error related to the new version of load file

# OptGen 7.4.7

ðŸ“… Date: 2019-09-12
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.7-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.7-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error related to the new version of renewables file
* IHM
  * Fixed an error with the read expansion plan flag when there is no project in the user-defined expansion plan file

# OptGen 7.4.6

ðŸ“… Date: 2019-08-12
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.6-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.6-setup-linux.zip)

## New Features and Improvements

* OptGen 1
  * The interpretability of the precedence constraints has been improved, now the model considers the delay field as the minimum wait time for the next project to go into operation
* IHM
  * In the precedence constraint screen, now the minimum delay column come before the project name

# OptGen 7.4.5

ðŸ“… Date: 2019-08-12
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.5-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.5-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Updated the conditions to by-pass printing the output results during an intermediate run of a rolling horizon execution.
  * Fixed an error related to restart of cases with number of projects over 1500.
  * Maximum capacity constraints stopped being disabled during sizing phase of a horizon year execution, only when the constraints are TOTAL and maximum year is equal to horizon year.
* IHM
  * Fixed errors in data exhibition and sorting of precedence and minimum/maximum constraints

# OptGen 7.4.4

ðŸ“… Date: 2019-07-15
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.4-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.4-setup-linux.zip)

## Fixed Bugs

* OptGen 2
  * Fixed an error related to contract initial consumed amount

# OptGen 7.4.3

ðŸ“… Date: 2019-07-10
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.3-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.3-setup-linux.zip)

## Fixed Bugs

* OptGen 2
  * Fixed an error in the operative cost output in the screen in cases with elastic demand
  * Fixed an error related to the sizing heuristic
  * Fixed an error in the min/max constraints with percentage of the installed capacity of specific systems

# OptGen 7.4.2

ðŸ“… Date: 2019-07-02
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.2-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.2-setup-linux.zip)

## Fixed Bugs

* OptGen 2
  * Fixed an error related to the typical day calculator tool in weekly cases
  * Fixed an error related to the capacity of continuous projects in the user-defined expansion plan

* IHM
  * Fixed an error related to the number of stages of weekly cases

# OptGen 7.4.1

ðŸ“… Date: 2019-06-27
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.1-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.1-setup-linux.zip)

## Fixed Bugs

* IHM
  * Fixed an error related to the investment stage selection

# OptGen 7.4.0rc22

ðŸ“… Date: 2019-06-18
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc22-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc22-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error related to the identification of hourly elastic demand

# OptGen 7.4.0rc21

ðŸ“… Date: 2019-06-07
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc21-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc21-setup-linux.zip)

## New Features and Improvements

* OptGen 1
  * Now the model automatically writes the "lp" files when the investment problem is infeasible

# OptGen 7.4.0rc20

ðŸ“… Date: 2019-06-04
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc20-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc20-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error related to batteries project with integer variables in OptGen 2 solution strategy

# OptGen 7.4.0rc19

ðŸ“… Date: 2019-05-29
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc19-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc19-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error in the user-defined expansion plan with "exactly" and "at least" decisions for the same project
  * Fixed an error related to investment cost calculation of fixed projects out of the study horizon
  * Fixed an error related to the renewable modification file version

# OptGen 7.4.0rc18

ðŸ“… Date: 2019-05-24
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc18-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc18-setup-linux.zip)

## Fixed Bugs

* IHM
  * Fixed an error in the associated and exclusive projects' screens

# OptGen 7.4.0rc17

ðŸ“… Date: 2019-05-14
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc17-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc17-setup-linux.zip)

## New Features and Improvements

* OptGen 1
  * Added a header to the execution report, identifying the phase to which the report refers
  * Added the execution report for the "OptGen 2" Solution Strategy

## Fixed Bugs

* IHM
  * Fixed an error related to the default investment stage option when the user changes the solution strategy to be "OptGen 2"

# OptGen 7.4.0rc16

ðŸ“… Date: 2019-04-30
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc16-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc16-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error regarding planned decision option

* IHM
  * Fixed an error in the execution of optgen scenarios when no scenario is needed

# OptGen 7.4.0rc15

ðŸ“… Date: 2019-04-03
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc15-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc15-setup-linux.zip)

## New Features and Improvements

* OptGen 1
  * The system operating cost calculated by "OptGen 2" and the gap between it and the operating cost of the final simulation performed by SDDP are now presented in the optgen.out file
  * Now the model allows firm capacity modifications for committed  and candidate projects

# OptGen 7.4.0rc14

ðŸ“… Date: 2019-04-03
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc14-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc14-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error regarding the planned decision option

* IHM
  * Fixed an error in the "OptGen-Scenarios" execution when no scenario is needed

# OptGen 7.4.0rc13

ðŸ“… Date: 2019-03-28
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc13-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc13-setup-linux.zip)

## New Features and Improvements

* OptGen 1
  * The (unnecessary) final simulation in the last sub-horizon of the rolling horizon strategy has been removed

* IHM
  * Removed capacity column in the energy/firm capacity modification screens

# OptGen 7.4.0rc12

ðŸ“… Date: 2019-03-28
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc12-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc12-setup-linux.zip)

## New Features and Improvements

* OptGen 1
  * Added planned decision option for fixed projects
  * The "OptGen 2" configuration file name has been changed

* IHM
  * The option of keeping SDDP and OPTGEN input data files in different folders has been removed
  * The OptGen execution has been separated in two phases: (1) the expansion planning task and (2) the expansion plan simulation
  * Reorganization of the main screen
  * The order of the main screen icons has been changed

## Fixed Bugs

* OptGen 1
  * Fixed an error regarding the minimum entrance date due to the construction time
  * Fixed an error regarding obligatory projects entering into operation before the beginning of the study horizon in cases with rolling horizon

# OptGen 7.4.0rc11

ðŸ“… Date: 2019-02-12
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc11-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc11-setup-linux.zip)

## New Features and Improvements

* OptGen 1
  * Now the model considers integer variable decisions
  * Now the model executes TSLite automatically in PSRCloud/Linux enviroment

* IHM
  * Added the Dashboard option with the operation macro results
  * Now "OptGen 1" can be executed through the DOS console
  * Now OptGen warns the user when it is opening an empty case folder
  * The "compact case" option has been added
  * The "update license" option has been added

* HYDGEN
  * The "static scenarios" option has been added
  * The option to import external scenarios from TSL has been added
  * The option to automatically calculate probabilities for all scenarios has been added

## Fixed Bugs

* OptGen 1
  * Fixed an error related to executions using the "restart" option and considering the consecutive iteration strategy

* HYDGEN
  * Fixed an error that occurred when the last year of historical inflow files have only missing values

* SDDP Importer
  * Some errors have been changed to be warnings

* IHM
  * Fixed an error related to the hydro capacity being shown in energy/firm capacity constraints' screens

# OptGen 7.4.0rc10

ðŸ“… Date: 2018-10-26
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc10-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc10-setup-linux.zip)

## New Features and Improvements

* OptGen 1
  * Now, in the rolling horizon strategy, the model considers obligatory projects as optional in the first sub-horizons and obligatory in the last one

# OptGen 7.4.0rc9

ðŸ“… Date: 2018-10-04
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc9-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc9-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error related to hourly simulations with the new version of renewables file
  * "OptGen 2" output files are now being immediately written after the execution finishes

# OptGen 7.4.0rc8

ðŸ“… Date: 2018-09-28
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc8-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc8-setup-linux.zip)

## Fixed Bugs

* IHM
  * The interface is now writing the "OptGen 2" execution options

# OptGen 7.4.0rc7

ðŸ“… Date: 2018-07-26
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc7-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc7-setup-linux.zip)

## New Features and Improvements

* IHM
  * The "version 2" of the circuit configuration file has been added

# OptGen 7.4.0rc6

ðŸ“… Date: 2018-07-26
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc6-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc6-setup-linux.zip)

## New Features and Improvements

* OptGen 1
  * Now the model allows firm capacity modifications for future plants
  * Now the model executes a data check to verify optgen input data before running "OptGen 2"

## Fixed Bugs

* OptGen 1
  * Fixed an error related to batteries' modifications

* IHM
  * Fixed an error related to the generator capacity bein shown in the firm capacity/energy screens

# OptGen 7.4.0rc5

ðŸ“… Date: 2018-06-26
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc5-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc5-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error related to the usage of external (TSL) renewable scenarios input data

# OptGen 7.4.0rc4

ðŸ“… Date: 2018-05-29
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc4-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc4-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error in the firm capacity/energy input data

* HYDGEN
  * Fixed an error that occurred when a hydro plants is in a system not selected to be simulated

# OptGen 7.4.0rc3

ðŸ“… Date: 2018-05-21
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc3-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc3-setup-linux.zip)

## Fixed Bugs

* IHM
  * Fixed an error related to OptGen execution parameters' file
  * Fixed an error related to system identification in the firm capacity/energy screens

# OptGen 7.4.0rc2

ðŸ“… Date: 2018-05-16
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc2-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc2-setup-linux.zip)

## New Features and Improvements

* OptGen 1
  * A maximum execution time for "OptGen 2" strategy has been added

* IHM
  * The option to execute "OptGen 2" has been added

## Fixed Bugs

* IHM
  * Fixed an error related to the typical day calculator

# OptGen 7.4.0rc1

ðŸ“… Date: 2018-04-30
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc1-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0rc1-setup-linux.zip)

## New Features and Improvements

* OptGen 1
  * Batteries have been added as a new type of project
  * outpdec<iter>.csv files with the candidate plan of each OptGen iteration are now being written
  * Now the model considers chronological investment costs for the projects
  * The long run marginal cost (LRMC) output file is now being written
  * Sizing strategy option for "OptGen 2" has been added

* IHM
  * A chronological investment cost screen has been added
  * CSV import/export options for the hidro inflow data have been added

## Fixed Bugs

* OptGen 1
  * Fixed an error related to the convergence gap while using the consecutive iteration heuristic

# OptGen 7.4.0

ðŸ“… Date: 2018-04-01
ðŸ”— Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-7.4.0-setup-linux.zip)

Please refer to the "OptGen 7.4.0 Readme" file for the release notes (./Docs/OptGenReadmeEng.pdf)