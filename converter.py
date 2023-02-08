import os
import sys
import fnmatch
import subprocess

base_path = os.path.abspath(os.path.split(sys.argv[0])[0])

f = open(os.path.join(base_path,"..","changelog.txt"), 'r')
content = f.readlines()
f.close()

finalChangelog = []

k = 0
while k < len(content):
    line = content[k]
    if line[0:6] == "OptGen":
        Version = line[6:].partition("(")[0]
        Date = line[0:].partition("(")[2].partition(")")[0]
        finalChangelog.append("# OptGen " + Version.strip() + "\n\n")
        finalChangelog.append("📅 Date: " + Date.strip() + "\n")
        finalChangelog.append("🔗 Download:\n[Windows](https://www.psr-inc.com/app/link/?t=d&f=optgen-" + Version.strip() + "-setup.zip)\n\|\n[Linux](https://www.psr-inc.com/app/link/?t=d&f=optgen-" + Version.strip() + "-setup-linux.zip)\n")
    elif line[0:29] == "New Features and Improvements":
        finalChangelog.append("## New Features and Improvements\n")
    elif line[0:10] == "Fixed Bugs":
        finalChangelog.append("## Fixed Bugs\n")
    elif line[0:10] == "- OptGen 1":
        finalChangelog.append("* OptGen 1\n")
    elif line[0:7] == "- Model":
        finalChangelog.append("* OptGen 1\n")
    elif line[0:10] == "- OptGen 2":
        finalChangelog.append("* OptGen 2\n")
    elif line[0:5] == "- IHM":
        finalChangelog.append("* IHM\n")
    elif line[0:5] == "- GUI":
        finalChangelog.append("* IHM\n")
    elif line[0:8] == "- HYDGEN":
        finalChangelog.append("* HYDGEN\n")
    elif line[0:8] == "- Hydgen":
        finalChangelog.append("* HYDGEN\n")
    elif line[0:15] == "- SDDP Importer":
        finalChangelog.append("* SDDP Importer\n")
    elif line[0:20] == "- SDDP data importer":
        finalChangelog.append("* SDDP Importer\n")
    elif line[0:33] == "- SDDP historical inflow importer":
        finalChangelog.append("* SDDP Importer\n")
    elif line[0:6] == "Please":
        finalChangelog.append(line)
    elif line[0:3] == "  -":
        finalChangelog.append("  *" + line[3:])
    else:
        print("DEU RUIM NA LINHA " + str(k))
        print(line)
        finalChangelog.append("\n")
    k += 1

f = open(os.path.join(base_path,"changelog2.txt"), 'w')
f.writelines(finalChangelog)
f.close()