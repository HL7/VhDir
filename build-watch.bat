@echo off 

"C:\ProgramData\Oracle\Java\javapath\java.exe" -Xmx@2048m -jar "C:\git\org.hl7.fhir.igpublisher.jar" -ig ig.json -watch

pause
