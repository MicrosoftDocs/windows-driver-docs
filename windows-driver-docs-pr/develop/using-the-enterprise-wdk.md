---
title: Using the Enterprise WDK 10
description: Describes how to set up a command-line based environment for organization use of the WDK.
ms.date: 08/25/2017
ms.localizationpriority: medium
---

# Using the Enterprise WDK 10

The Enterprise Windows Driver Kit (Enterprise WDK) is a command-line build environment that does not require any installation prior to use.  Once you have downloaded the EWDK, you can manage it with version control software or you can zip the files and copy as needed.  A .zip file created with the Enterprise WDK contains all the necessary compilers, linkers, build tools, headers and libs to build Visual Studio-based driver projects.

The Enterprise WDK contains the necessary elements to build drivers and basic Win32 driver test applications.  Use your favorite code editor to modify source code and project files.  Because it is command-line based, the Enterprise WDK does lack some of the features incorporated into Visual Studio, such as an IDE, driver deployment and driver testing. 



## Getting Started

> [!NOTE] 
> Starting in Windows 10 version 1709, the Enterprise WDK is ISO-based.  To get started, download and mount the ISO, then run `LaunchBuildEnv`.

1.	Download the EWDK from:
[WDK & EWDK download](../download-the-wdk.md)
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

[MSBuild Reference](/visualstudio/msbuild/msbuild-reference)