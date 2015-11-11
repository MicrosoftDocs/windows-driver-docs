# Installing the Enterprise Windows Development Kit
The current WDK is optimized for individual developers using a state-based installation. Organizations with more than just a few developers using the WDK assume a high cost of individual installations of Visual Studio 2015 and the WDK.  To address this, the Enterprise WDK is a command-line build environment that is file-based, rather than machine based.  Once you create the environment file structure, you can have it consumed by version control software or zip the files and xcopy as needed. A .zip file created with the EWDK contains all the necessary compilers, linkers, build tools, headers and libs to build Visual Studio-based driver projects.

The EWDK contains the necessary elements to build drivers and basic win32 test applications and is based on Visual Studio 2015 Enterprise build 14.00.23026 and builds 10586 of the WDK and Standalone SDK. Use your favorite code editor to modify source code and project files. Because it is command-line, however, the EWDK does lack some of the features incorporated into Visual Studio, such as testing or driver deployment. 


##Enterprise WDK components
*	Visual Studio build tools, C/C++ compiler, linker and libs for Visual Studio build 14.00.23026.0  
  *	Note that the EWDK does not include the IDE, devenv.exe.
*	Windows Software Development Kit build 10586
*	.NET Framework 4.6 Software Development Kit build 10586
*	Windows Driver Development Kit build 10586


##Known Issues
*	SDVand Code Analysis does not work in this release.
*	The Visual Studio IDE is not included in the EWDK and any functionality that requires the IDE will not work.

## Installation Instructions
1.	Download the file EnterpriseWDK_full_10586.zip from MSDN
2.	Expand the .zip file into an appropriately named directory, such as d:\ewdk.
3.	From an Administrator command prompt, navigate to the expanded folder in the previous step, and then run **LaunchBuildEnvcmd** to create the build environment. For example:
  **D:\EWDK\LaunchBuildEnv**

Once you create the build environment, you can use it to work on the files or build Visual Studio projects, for example.  
*	Cd *directory_containing_project_files*
*	Msbuild *projectname*.vsproj

Basic MSBuild commands for projects and solutions:
* Msbuild project.vcxproj /p:configuration=[release | debug] /p:platform=[arm | Win32 | x64]

To create a desktop shortcut:

%comspec% /k pushd "<drive\dir>" && LaunchBuildEnv.cmd

Where drive\dir is the location that the files were extracted to, for example, d:\ewdk

%comspec% /k pushd "d:\ewdk" && LaunchBuildEnv.cmd


See Also
<a href="https://msdn.microsoft.com/en-us/library/0k6kkbsd.aspx"> https://msdn.microsoft.com/en-us/library/0k6kkbsd.aspx</a>





