#! /usr/bin/env python
#

from subprocess import call
import os

sitePath = os.path.normpath(os.path.dirname((os.path.join(os.getcwd(),os.path.dirname(__file__) ) ) ) )
siteDir = os.path.join(sitePath,"www")


print "Building {:s}".format(siteDir)

call("cd {:s} && mkdocs build --theme united --clean --verbose".format(sitePath), shell=True)

## Need to put the content in place too.


# uwDocDir = "/underworld/underworld2/docs" # This assumes the unix build
# uwDeployDir = os.path.join(siteDir, "Introduction")
#
# call("cp -r {:s} {:s}".format(os.path.join(uwDocDir,"examples"), uwDeployDir), shell=True)
# call("cp -r {:s} {:s}".format(os.path.join(uwDocDir,"user_guide"), uwDeployDir), shell=True)
# call("cp -r {:s} {:s}".format(os.path.join(uwDocDir,"publications"), uwDeployDir), shell=True)

# uwDeployDir = os.path.join(siteDir, "Underworld")
# call("cp -r {:s} {:s}".format(os.path.join(uwDocDir,"api_doc"), uwDeployDir), shell=True)
