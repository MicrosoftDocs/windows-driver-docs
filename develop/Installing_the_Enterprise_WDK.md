# Installing the Enterprise WDK 10
The current Windows Driver Kit (WDK) is optimized for individual developers using a state-based installation. Organizations with many developers using the WDK assume a high cost of individual installations of Visual Studio 2015 and the WDK.  To address this, the Enterprise Windows Driver Kit (Enterprise WDK) is a command-line build environment that is file-based, rather than machine based.  Once you create the environment file structure, you can have it consumed by version control software or you can zip the files and copy as needed. A .zip file created with the Enterprise WDK contains all the necessary compilers, linkers, build tools, headers and libs to build Visual Studio-based driver projects.

The Enterprise WDK contains the necessary elements to build drivers and basic Win32 test applications, and is based on Visual Studio 2015 Enterprise, WDK, and the standalone Windows Software Development Kit (SDK). Use your favorite code editor to modify source code and project files. Because it’s command-line, however, the Enterprise WDK does lack some of the features incorporated into Visual Studio, such as testing and driver deployment. 


##Enterprise WDK components
*	Visual Studio build tools, C/C++ compiler, linker and libs for Visual Studio build 14.00.24720.0 (VS 2015 Update 1)  
  *	Note that the Enterprise WDK does not include the IDE, devenv.exe.
*	Windows SDK build 10586.13
*	.NET Framework 4.6 SDK build 10586.13
*	Windows Driver Development Kit build 10586.0


##Known Issues
*	SDVand Code Analysis does not work in this release.
*	The Visual Studio IDE is not included in the Enterprise WDK and any functionality that requires the IDE will not work.

## Installation Instructions
1.	Download the [Enterprise WDK](https://msdn.microsoft.com/en-us/windows/hardware/mt612818.aspx).
2.	Expand the .zip file into an appropriately named directory, such as d:\ewdk.
3.	From an Administrator command prompt, navigate to the expanded folder in the previous step, and then run **LaunchBuildEnvcmd** to create the build environment. For example:
  **D:\EWDK\LaunchBuildEnv**

After you create the build environment, you can use it to work on the files or build Visual Studio projects. For example.  
*	Cd *directory_containing_project_files*
*	Msbuild *projectname*.vsproj

Basic MSBuild commands for projects and solutions:
* Msbuild project.vcxproj /p:configuration=[release | debug] /p:platform=[arm | Win32 | x64]

To create a desktop shortcut:

%comspec% /k pushd "<drive\dir>" && LaunchBuildEnv.cmd

Where drive\dir is the location that the files were extracted to, for example, d:\ewdk

%comspec% /k pushd "d:\ewdk" && LaunchBuildEnv.cmd


#See Also
<a href="https://msdn.microsoft.com/en-us/library/0k6kkbsd.aspx"> MSBuild Reference</a>





