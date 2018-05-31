# Hl7 Validated Healthcare Directory (HcDir) Implementation Guide Repository 

Authors:  Brian Postlethwaite, Bob Dieterle, ONC Contributors

-----
FHIR STU3 Implementation Guide

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

In the build there is a batch file that performs the complete build `build.bat`.

Inside it has:
> "C:\ProgramData\Oracle\Java\javapath\java.exe" -Xmx1024m -jar "C:\git\org.hl7.fhir.igpublisher.jar" -ig ig.json

To keep the build running continually so that it only updates the files that you're changing, include the -watch option
this is done in the new batch file `build-watch.bat`

For more details on the IG Publisher refer to the documentation that can be found here:
http://wiki.hl7.org/index.php?title=IG_Publisher_Documentation
