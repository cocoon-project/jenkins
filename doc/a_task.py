#!usr/binenv python
"""

	arborescence 

	/opt/tomcat/webapps/jenkins or /jenkins

 		/jobs
 			/OVC-WIN7-IE10
 			/OVC-WIN7-FF24
 				config.xml
 				lastStable -> builds/lastStable
 				lastSuccesful -> builds/lastSuccesful
 				nextBuildNumber
 				/builds
 					10 -> 2014-03-31_1313-15-34
 					lastStableBuild
 					lastFailedBuild
 					lastSuccesfulBuild
 					lastUnSuccesfulBuild
 					/2014-03-31_1313-15-34
 						build.xml
 						changelog.xml
 						robot_results.xml
 						/robot-plugin
 							log.html
 							output.xml
 							report.html
 				/workspace
 					build.xml
 					/OVC
 						.git
 						__init__.txt
 						Parameters_Global.txt
 						/Company
 							__init__.txt
 							CompanyTest.txt
 							Keyword_resource_CompanyTest.txt
 							Parameters_resources_companyTest.txt
 					/tmp
 						/arguments
 							argfile.txt
 						/log
 							log.html
 							output.xml
 							report.html
 							selenium-screenshot-20.png
 						/logs
 							log2014-05-12 13:42 CEST.zip





"""
from to_create import tstamp , echo , zip_ , delete ,mkdir , environ



basedir = environ['basedir']


ProjetDir = basedir + "/OVC"
ArgumentFile = basedir + "/tmp/arguments/argfile.txt"
OutPutDirectory = basedir + "/tmp/log/"
SaveLogDirectory = basedir + "/tmp/logs/"

pybot = "/usr/local/bin/pybot"

outputXML = basedir + "/tmp/log/output.xml"
POSToutputXML = basedir + "/tmp/log/POSToutput.xml"


#1 cleanup build artifacts
time_start = tstamp (  pattern="yyyy-MM-dd HH:mm z" )

zip_( destfile = SaveLogDirectory + "/log" + time_start + ".zip" ,basedir=OutPutDirectory )

delete ( OutPutDirectory )

#2 prepare
mkdir( OutPutDirectory )


#3 lancement pybot
echo( "Time:" + time_start + " - Starting tests...")

exec ( "pybot --argumentfile " + ArgumentFile + " --outputdir " + OutPutDirectory +" "+ ProjetDir )

time_end = tstamp(  pattern="yyyy-MM-dd HH:mm z" )

echo( "Time : " + time_end " - Ending tests.")