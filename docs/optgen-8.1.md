---
title: "OptGen 8.1"
nav_order: 2
---

# OptGen 8.1.13

📅 Date: 2025-01-31<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.13-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.13-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an issue related to min/max constraints with a maximum date beyond the planning horizon that include projects wih operational lifetime, preventing infeasibility problems.

* OptGen 2
  * Fixed the calculation of generic constraint penalties in the objective function and implements the option for hard generic constraints, avoiding unnecessary creation of slack variables.

## New Features

* OptGen
  * Adds validation for rolling horizon runs when the horizon configuration is invalid and there is a discontinuity between them.

# OptGen 8.1.12

📅 Date: 2024-12-19<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.12-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.12-setup-linux.zip)

## Fixed Bugs

* IHM
  * Fixed an error related to PSRIO scripts considering battery generation and load marginal cost

## New Features

* OptGen 2
  * Added reduced cost output for investment decision variables

# OptGen 8.1.11

📅 Date: 2024-11-26<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.11-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.11-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error in the convergence report file when the model restarts in a PSRCloud execution

* OptGen 2
  * Fixed an error in SDDP's generic constraints penalty

* IHM
  * Fixed an error defining firm capacity/energy constraints (the interface was corrupting the file and the model was considering the values in MWavg instead of p.u)
  * NID projects now can only have investment cost in M$  
  * Improve the "Compact case data" functionality to include execution reports and important model's output to analyze a simulation

# OptGen 8.1.10

📅 Date: 2024-10-16<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.10-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.10-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error related to associativity constraints without a maximum delay when the case has multiple rolling horizons

* OptGen 2
  * Fixed battery project operative lifetime when it has a substitution constraint defined (for example, a project A replaces battery B that have operative lifetime). The model was ignoring the operative lifetime.

# OptGen 8.1.9

📅 Date: 2024-10-08<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.9-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.9-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error when reading initial conditions of state variables in the operation problem
  * Fixed an error when printing investment and reimbursement costs in the execution report, for the project expansion schedule when there is reinforcement
  * Implementation of logic to obtain values of dual variables for Minimum and Maximum capacity constraints
  * Logic implemented for running the case with typical day representation

* OptGen 2
  * Fixed outputs of fuel consumption when there are fuel contract renewals
  * Fixed outputs of absolute quantities by stages
  * Fixed output of flow in DC links

# OptGen 8.1.8

📅 Date: 2024-09-09<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.8-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.8-setup-linux.zip)

## Fixed Bugs

* OptGen 2
  * Fixed an error related to the firm capacity of renewable plants on executions with restart (from PSRCloud or directly from the interface)
  * Fixed an error related to the aggregation of input data that varies per block to typical day (sum constraints for example)
  * Fixed an error related to the expansion plan the execution of the model is restarted from PSRCloud an a sub-optimal feasible solution is found

# OptGen 8.1.7

📅 Date: 2024-08-30<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.7-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.7-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error related to substitution of multi-fuel thermal plants
  * Fixed an error related to the expansion of transmission lines (improved the Big-M value considering the monitoring status)
  * Fixed an error related to projects defined in the user-defined expansion plan in dates out of the horizon when the project is not selected to belong to the study
  * Fixed an error related to the resilience module when the case has dynamic probabilistic reserve
  * Improved the convergence report in the model's dashboard

* OptGen 2
  * Fixed an error when there are free contracts defined

* IHM
  * Fixed the 3-winding transformer capacity in the project's list
  * Fixed an error loading precedence constraints

# OptGen 8.1.6

📅 Date: 2024-07-15<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.6-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.6-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Increased the maximum number of circuits modification allowed
  * Improved integration with PSRCloud

# OptGen 8.1.5

📅 Date: 2024-06-25<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.5-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.5-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Increased the maximum number of circuits modification allowed

* OptGen 2
  * Fixed an error related to fuel contracts constraints
  
## New Features

* OptGen 2
  * Added an option to identify excess generation during the expansion planning phase (RXGM,1 in the datoption.csv file)

# OptGen 8.1.4

📅 Date: 2024-06-06<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.4-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.4-setup-linux.zip)

## Fixed Bugs

* OptGen 2
  * Fixed an error related to SDDP generic constraint
  * Fixed an error related to the delay on precedence constraint
  * Fixed an error related to the outputs after a PSRCloud restart happens
  * Fixed an error related to SDDP's contract
  * Fixed an error related to the logic of number of scenarios when there's no renewable station in the database
  * Fixed interconnection capacity for future agents that are not projects

* IHM
  * Fixed an error related to the importation of SDDP modification into user-defined expansion plan
  * Fixed an error on the header of the datmcap.csv file
  * Fixed an error related to the default firm energy/capacity unit
  * Fixed an error related to the system and type of the agents being replaced by projects

# OptGen 8.1.3

📅 Date: 2024-05-15<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.3-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.3-setup-linux.zip)

## New Features

* IHM
  * Improved the model's dashboard
  * Improved loading time of minimum/maximum constraints

## Fixed Bugs

* OptGen 1
  * Fixed an error updating NetPlan expansion files after the optimal expansion plan is found
  * Fixed an error related to the hotstart on linux machines (or PSRCloud)
  * Fixed an error related to the inflows when SDDP's policy is fixed along OptGen's iterations

* OptGen 2
  * Fixed an error related to the hotstart on linux machines (or PSRCloud)
  * Fixed an error related to joint reserve of DPR + Absolute when the Absolute requirement is 0
  * Fixed an error related to infeasibility calculation of minimum/maximum constraints
  * Fixed an error related to the compatibilization with SDDP's general constraints
  * Fixed an error in cases with NetPlan and phase-shifter
  * Fixed an error related to the automatic generation of typical days mapping when it's not found
  * Fixed an error related to hydro plants with maintenance and individual reserve defined

* IHM
  * Fixed an error on the selection of critical scenarios (resilience planning)

# OptGen 8.1.2

📅 Date: 2024-04-09<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.2-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.2-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error related to the storage of electrification elements. Now the modelling will be similar to the batteries
  * Fixed an error related to the firm energy/capacity constraints when the case has flexible demand

* OptGen 2
  * Fixed an error in the circuit capacity output file

* IHM
  * Fixed an error in the project's importer
  * Added a validation procedure in the min/max additional constraints data

# OptGen 8.1.1

📅 Date: 2024-04-01<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.1-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.1-setup-linux.zip)

## New Features

* OptGen 1
  * Now the model will automatically detect when the execution is done with fixed policy (simulation on SDDP) and there's no need to add the UPOL parameter in datoption.csv file

## Fixed Bugs

* OptGen 1
  * Fixed an error related to the resilience planning modelling

* IHM
  * Fixed an error related to the hydro inflows scenarios defined on OptGen's interface

# OptGen 8.1.0

📅 Date: 2024-03-18<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.0-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.1.0-setup-linux.zip)

Please refer to the following link for the release notes: https://psr-energy.com/software/optgen-8.1.html

