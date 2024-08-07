# Hl7 Validated Healthcare Directory (VhDir) Implementation Guide Repository

A FHIR implementation guide enabling the exchange of validated healthcare directory information between a reference source (e.g. national directory) and 'local' workflow environments (e.g. local directories).

Authors:  Alex Kontur, Dan Chaput, Brian Postlethwaite, Bob Dieterle, Eric Haas, Nagesh Bashyam, ONC Contributors

-----
FHIR R4 Implementation Guide

GitHub will automatically trigger a new build whenever you commit changes.
> To manually trigger a build just `POST` to the Webhook URL yourself, for example via:
> `curl -X POST "https://2rxzc1u4ji.execute-api.us-east-1.amazonaws.com/prod/publish?HL7/ValidatedHealthcareDirectory"`

Note: a build takes 2-3 minutes to complete

### Find your rendered IG automatically available at

http://build.fhir.org/ig/HL7/VhDir/index.html

### For a build log see

http://build.fhir.org/ig/HL7/VhDir/build.log

http://build.fhir.org/ig/HL7/VhDir/qa.html

### Local continuous builds

These are network batch files that perform the complete build:

1. `build.bat`  (Windows)

  Inside it has:
  > "C:\ProgramData\Oracle\Java\javapath\java.exe" -Xmx1024m -jar "C:\git\org.hl7.fhir.igpublisher.jar" -ig ig.json

  To keep the build running continually so that it only updates the files that you're changing, include the -watch option
  this is done in the new batch file `build-watch.bat`

1.  `pub3.sh` (iOS)

  1. update the paths in the variables path1, path2, path3:

  1. run bash file `pub3.sh`  with optional arguments:
     1. `-s [directory name of source folder]` (omit if in root)
     1. `-t` run without terminology server
     1. `-o` run with version of the ig-publisher named in path2
     1. -d create the definitions files from the content in source  ( see https://github.com/Healthedata1/FHIR-IGPub-filebuilder
       )

  1.  updates to pages will trigger ig-publisher to rebuild


For more details on the IG Publisher refer to the documentation that can be
found here:
http://wiki.hl7.org/index.php?title=IG_Publisher_Documentation
