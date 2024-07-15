---
title: "OptGen 8.1"
nav_order: 2
---
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

