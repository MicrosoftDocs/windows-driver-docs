# Installing the Enterprise Windows Development Kit
The Windows Driver Kit is designed to meet the needs of an individual developer. Organizations that need to install and deploy the WDK at scale can use the Enterprise Windows Development kit. 

The Enterprise WDK is a command-line build environment that is file-based, rather than machine-based.  This means that once the environment file structure has been created, it can be consumed by version control software, or copied as needed.  The EWDK is available as a .zip file and contains all the necessary compilers, linkers, build tools, headers and libs to build Visual Studio–based driver projects.
The EWDK contains all necessary elements to build drivers and basic win32 test applications.  See the Appendix for some basic commands and the output of building a driver project.
The EWDK is based on Visual Studio 2015 Enterprise build 14.00.23026 and builds 10586 of the WDK and Standalone SDK.

Because the EWDK is command-line based, it does not contain some of the features incorporated into Visual Studio, including testing or driver deployment. These scenarios require the standard single-user installation. You can use your choice of code editors to modify source code and project files.

##This build of the enterprise WDK contains the following components
1.	Visual Studio build tools, C/C++ compiler, linker and libs for Visual Studio build 14.00.23026.0  
  a.	It does NOT include the IDE, devenv.exe.
2.	Windows Software Development Kit build 10586
3.	.NET Framework 4.6 Software Development Kit build 10586
4.	Windows Driver Development Kit build 10586
## Known Issues
------------------------------------
1.	SDVand Code Analysis does not work in this release.
2.	The IDE is not included in the EWDK, therefore functionality tied to the IDE is not present.

## Installation Instructions
------------------------------------
3.	From an Administrative command prompt in the expanded folder, run LaunchBuildEnvcmd to create the build environment
E.g. D:\EWDK\LaunchBuildEnv

4.	This environment can now be used to build VS projects, e.g.
a.	Cd directory containing project files
b.	Msbuild projectname.vsproj

## Appendix
Basic MSBuild command line:
Msbuild project.vcxproj /p:configuration=[release | debug] /p:platform=[arm | x86 | x64]

For MSBuild Reference, see
https://msdn.microsoft.com/en-us/library/0k6kkbsd.aspx

## Create a desktop shortcut
----------------------------------------------------------------------------------------------------------------------------
Create a desktop shortcut to the EWDK as follows by the following:
Create a desktop shortcut  with the following target:
%comspec% /k pushd "<drive\dir>" && LaunchBuildEnv.cmd
Where drive\dir is the location that the files where extracted to.  In our example, using d:\ewdk,
%comspec% /k pushd "d:\ewdk" && LaunchBuildEnv.cmd


