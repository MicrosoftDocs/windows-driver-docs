---
title: Installing the Enterprise WDK 10
description: Describes how to set up a command-line based environment for organization use of the WDK.
author: Dansimp
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installing the Enterprise WDK 10
The current Windows Driver Kit (WDK) is optimized for individual developers using a state-based installation. Organizations with many developers using the WDK assume a high cost of individual installations of Visual Studio 2015 and the WDK.  To address this, the Enterprise Windows Driver Kit (Enterprise WDK) is a command-line build environment that is file-based, rather than machine based.  Once you create the environment file structure, you can have it consumed by version control software or you can zip the files and copy as needed. A .zip file created with the Enterprise WDK contains all the necessary compilers, linkers, build tools, headers and libs to build Visual Studio-based driver projects.

The Enterprise WDK contains the necessary elements to build drivers and basic Win32 test applications. Use your favorite code editor to modify source code and project files. Because it's a command-line, the Enterprise WDK does lack some of the features incorporated into Visual Studio, such as testing and driver deployment. 

## Enterprise WDK 1703 Prerequisites
*	.NET Framework 4.6 SDK build 4.6.01586

## Enterprise WDK 1607 Prerequisites
*	.NET Framework 4.6 SDK build 10586.13

## Installation Instructions
1.	Download one of the following: 
 * [Enterprise WDK 1703](https://developer.microsoft.com/windows/hardware/license-terms-enterprise-wdk-1703) 
 * [Enterprise WDK 1607](https://developer.microsoft.com/en-us/windows/hardware/license-terms-enterprise-wdk)
2.	Expand the .zip file into an appropriately named directory, such as d:\ewdk.
3.	From an Administrator command prompt, navigate to the expanded folder in the previous step, and then run **LaunchBuildEnvcmd** to create the build environment. For example:
  **D:\EWDK\LaunchBuildEnv**

After you create the build environment, you can use it to work on the files or build Visual Studio projects. For example.  
*	Cd *directory_containing_project_files*
*	Msbuild *projectname*.vsproj

Basic MSBuild commands for projects and solutions:
* Msbuild project.vcxproj /p:configuration=[release | debug] /p:platform=[arm | Win32 | x64]

To create a desktop shortcut:

%comspec% /k pushd `<drive\dir>` && LaunchBuildEnv.cmd

Where `<drive\dir>` is the location that the files were extracted to, for example, d:\ewdk

%comspec% /k pushd "d:\ewdk" && LaunchBuildEnv.cmd


## See Also
[ MSBuild Reference](https://msdn.microsoft.com/en-us/library/0k6kkbsd.aspx)








