---
title: "OptGen 8.0"
nav_order: 2
---
# OptGen 8.0.12

📅 Date: 2023-02-08<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.12-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.12-setup-linux.zip)

## Fixed bugs

* OptGen 1
  * Fixed an error where the model freezes at the end of the execution in Linux OS

# OptGen 8.0.11

📅 Date: 2023-01-23
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.11-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.11-setup-linux.zip)

## New Features and Improvements

* OptGen 1
  * Write decommissioning decisions on optgen.out, optsol01.csv and outidec.csv files

## Fixed Bugs

* OptGen 1
  * Fixed an error related to the invesment date of fixed decisions in the project screen (minimum date = maximum date)
  * Fixed an error with the modifications file when running with the integration with NetPlan
  * Fixed an error when running the model with fixed policy on SDDP (the case crashes when the file vinsim.sav exists due to a previous execution)

* OptGen 2
  * Fixed an error in the general constraints modeling when there are elastic demand variables selected
  * Fixed an error with USCN option when the case has power injection data (the USCN option won't impact the injection data anymore)

* IHM
  * Fixed numerical errors related to the user-defined expansion plan

# OptGen 8.0.10

📅 Date: 2023-01-11
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.10-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.10-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error related to the restart option with a fixed user-defined plan
  * Fixed an error in the rolling horizon when there is no hydro plant in the case and the model tries to copy the inflow.csv file
  * Fixed how the model handles capacity constraints when the maximum date is outside the study horizon. Now it's always ignored independently on its type (total or incremental)

* OptGen 2
  * Fixed an error when there are fixed projects in the user-defined plan with 0 MW of capacity (hydro reservoirs for example)

* IHM
  * Fixed errors related to the integration with NetPlan

# OptGen 8.0.9

📅 Date: 2022-11-30
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.9-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.9-setup-linux.zip)

## New Features and Improvements

* OptGen 2
  * The second kirchoff law for circuit projects is now activated by default

* IHM
  * Now the interface allows adding multiple projects at the same time

## Fixed Bugs

* OptGen 1
  * Fixed an error related to the lower-bound when the consecutive iteration heuristics is being used

* OptGen 2
  * Improved the performance of the optimization problem when the case has generic constraints in SDDP
  * Fixed an error related to renewables and batteries in SDDP generic constraints

# OptGen 8.0.8

📅 Date: 2022-11-16
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.8-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.8-setup-linux.zip)

## Fixed Bugs

* OptGen 2
  * Fixed an error with NetPlan integration when the SDDP network files are also in the case
  * Fixed an error with an output file of the CSP operation

# OptGen 8.0.7

📅 Date: 2022-11-01
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.7-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.7-setup-linux.zip)

## New Features and Improvements

* OptGen 1
  * Fixed an error related to the generation of dashboard files

# OptGen 8.0.6

📅 Date: 2022-10-28
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.6-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.6-setup-linux.zip)

## New Features and Improvements

* OptGen 1
  * Added the possibility to restart the execution after an unexpected interrumption

* OptGen 2
  * Added the possibility to run OptGen 2 with a fixed user-defined plant ("FOPT,2" in the "datoption.csv" file)
  * Added the output files "opt2_firmcaprhs" and "opt2_firmenerhs" with the firm energy and capacity annual requirement

## Fixed Bugs

* OptGen 1
  * Fixed an error related to 3-winding transformer memory allocation
  * Fixed an error related to unidentified projects in the chronological investment cost file

# OptGen 8.0.5

📅 Date: 2022-10-03
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.5-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.5-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error related to hotstart execution (restart after an unexpected error)

# OptGen 8.0.4

📅 Date: 2022-09-26
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.4-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.4-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error when the case doesn't have a defined demand for every system
  * Now, when the final simulation of SDDP crashes, OptGen will always recover the operation policy if it's available
  * Fixed an error related to the TSL scenarios when the sizing strategy is activated
  * Fixed the format of the explog file when the case has more than 500 projects
* OptGen 2
  * Fixed an error related to batteries on firm energy constraints

# OptGen 8.0.3

📅 Date: 2022-09-08
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.3-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.3-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed the 3 Winding Transformers "Big-M" calculation
* OptGen 2
  * Allow overwriting any solver control defined internally by the model thourgh the optgxpress.dat file
  * Fixed an error related to the consideration of hourly demand scenarios

# OptGen 8.0.2

📅 Date: 2022-07-25
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.2-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.2-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error related to investment in 3 winding transformers projects
* OptGen 2
  * Fixed an error related to curtailment and O&M costs of renewable plants

# OptGen 8.0.1

📅 Date: 2022-07-11
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.1-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.1-setup-linux.zip)

## Fixed Bugs

* OptGen 1
  * Fixed an error related to the identification of repeated solutions during the consecutive iterations heuristics
  * Fixed an error in a execution with restart when the previous optimal expansion plan is infeasible (the model must continue the optimization disregarding the previous plan)

# OptGen 8.0.0

📅 Date: 2022-06-24
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.0-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-8.0.0-setup-linux.zip)

Please refer to the "OptgenReleaseNotes-8.0" file for the release notes (./Docs/OptgenReleaseNotes-8.0-ENG.pdf)

