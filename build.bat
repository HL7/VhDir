@echo off 

for /f "usebackq" %%x in (`dir /od /b "%ProgramFiles%\java\jdk*"`) do set newestJDK=%ProgramFiles%\java\%%x
set JAVA_HOME=%newestJDK%
echo Using %JAVA_HOME%

"%JAVA_HOME%\bin\java.exe" -Xmx2048m -jar "C:\git\org.hl7.fhir.igpublisher.jar" -ig ig.json

pause
