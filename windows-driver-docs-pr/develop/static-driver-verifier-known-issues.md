---
title: Static Driver Verifier Known Issues
description: 
author: selerner
ms.author: selerner
ms.date: 11/07/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Static Driver Verifier Known Issues

This page describes common issues you may encounter when using the Static Driver Verifier tool in the WDK. The information below pertains specifically to the version of the tool that ships with Windows 10 October 2018 Update (Version 1809).

## InterceptedBuild failures

Primary symptom: SDV fails with `FATAL ERROR: Unrecoverable error in InterceptedBuild stage`.  

When examining the DVL file, you will see an `AssessmentScore` value with `ScoreName="[driverName].[architecture].SDV.NA.Reason"` and `ScoreUnit="Unrecoverable error in InterceptedBuild stage."`

For InterceptedBuild failures, perform the following steps to diagnose the issue.

1. Rerun SDV from the Visual Studio 2017 Native Tools Command Line with the /debug flag.  For details on command options, see [Static Driver Verifier commands](https://docs.microsoft.com/windows-hardware/drivers/devtest/-static-driver-verifier-commands--msbuild-).

    a. First, run SDV's library function on any dependent library projects.  For example: `msbuild /p:Configuration=Release /p:Platform=x64 /t:sdv /p:inputs="/lib /debug"`.

    b. Then run SDV on the driver project itself.  For example: `msbuild /p:Configuration=Release /p:Platform=x64 /t:sdv /p:inputs="/check /debug"`

2. Confirm that the failure again occurs in the InterceptedBuild stage.

3. Navigate to the `sdv` folder that is generated in the driver folder when you run SDV.

4. Open `smvcl.log` and search for the phrase "internal compiler error".

    a. If an error message containing **internal compiler error** and a phrase similar to **fatal error C1001: An internal error has occurred in the compiler.  (compiler file 'msc1.cpp', line 1511)** is present, this is a known issue which requires errata (errata ID 40705). If you need further assistance, please email <stlogohelp@microsoft.com>.

    b. If an error message containing **internal compiler error** is present but does not look like the above, this will likely require an errata but may not be an existing known issue.  Email <stlogohelp@microsoft.com>.

    c. If you do not see any lines containing **internal compiler error**, search for any lines beginning with **error**.  These may or may not be issues requiring errata.  Email <stlogohelp@microsoft.com>.

5. Open smvlink1.log and search for the phrase **internal compiler error**.

    a. If an error message containing **internal compiler error** and **slamcl: error: at phase 2: out of memory** is present, this is a known issue which requires errata.

    b. If you do not see any lines containing **internal compiler error**, search for any lines beginning with **error**.  These may or may not be issues requiring errata.  Email <stlogohelp@microsoft.com>.

    c. If you do not see any of the above, reach out to MSFT for support.

To reach out to MSFT for support, please ensure source code is not shared by running the following:

1. Run SDV with the /debug flag enabled, and pipe the output to a text file.

2. Navigate to the `sdv` folder in the driver directory and run the following commands to clear build results that might expose sources:

    ```cmd
    del /s *.obj
    del /s *.rawcfg*
    del /s *.li
    del /s *.pdb
    del /s *.sys
    ```

3. Send the following files to <stlogohelp@microsoft.com>:

    a. The text file with the output of running SDV

    b. The **smexecute-NormalBuild.log** file

    c. The **smvexecute-InterceptedBuild.log** file

    d. The "sdv" subfolder

## Visual Studio C++ 2013 runtimes not present

Primary symptom: When running SDV on a system that does not have the Visual Studio C++ 2012 and 2013 runtimes, the user may see errors in pop-up boxes such as The code execution cannot proceed because \[MSVCR110.dll or VCOMP110.dll\] was not found.  Reinstalling the program may fix this problem.

In this case, the solution is to install both the x86 and x64 Visual C++ Redistributable for Visual Studio 2012 and 2013.

## Best practice: use Visual Studio 2017 Version 15.8 

By default, code analysis does not automatically build the driver in Visual Studio 15.7.  If the driver depends on binaries being generated, this can lead to a failure in the **Output** pane.  Instead, we recommend using version 15.8 instead.

## DVL generation failure after removing configuration from a project

Primary symptom: After removing a configuration from a project via the Configuration Manager window, the user sees the following message when selecting **Create Driver Verification Log**: `Please select a driver project. Driver Verification Log cannot be created for the selected platform tool set: 'v100'"`

Workaround: 

1. Back up your project file, and then open the project file in a text editor.

2. Under the `\<PropertyGroup Label="Globals"\>` section, find two XML tags: one with the format `\<Configuration\>\[Configuration type\]\</Configuration\>` and one with the format `\<Platform Condition="'$(Platform)' == ''"\>\[Architecture\]\</Platform\>`, where `\[Configuration type\]` and `\[Architecture\]` are the default configuration and release for this type of project.

3. Update `\[Configuration type\]` and `\[Architecture\]` to values appropriate for your project.  For example, if you removed the Win32 platform, you might update `\[Architecture\]` to x64 instead.

Alternative workaround:

1. Open a Visual Studio 2017 Native Tools Command Prompt.

2. Navigate to the driver folder.

3. Run `msbuild [Your Project] /p:Configuration=[Configuration type]  /p:Platform=[Architecture] /t:dvl`, where `\[Your Project\]` is the vcxproj file, `\[Configuration type\]` is a valid configuration such as Release, and `\[Architecture\]` is a valid architecture such as x64.

## DVL generation does not work on ServerCore, use Server GUI

The Static Tools Logo test fails when run.  Reviewing the test logs shows a failure similar to
`Failed to load 'C:\hlk\JobsWorkingDir\Tasks\WTTJobRun4749E809-0166-E811-8368-F4521454FFE1\Devfund_DvlTest.dll'. (Could not load managed test module because RoMetadata.dll could not be found)`

Make sure the TAEF package is deployed or RoMetadata.dll is deployed to a location in your PATH environment variable.  

The key symptom is the failure to load RoMetadata.dll.

If you have a Server GUI installation with the same architecture and Windows version as your ServerCore installation, copy the RoMetadata.dll file from Server GUI to ServerCore.  The DLL can be found in the System32 folder (for example, `C:\Windows\System32`) and should be placed in the same folder on the ServerCore machine.  This should enable the test to run on ServerCore.  If you are still experiencing issues, please refer to the next workaround.

The second workaround is to run on Server GUI and then merge the package with the package containing the results from Server Core. For info on merging packets, see [Merge packages](https://docs.microsoft.com/windows-hardware/test/hlk/user/merge-packages).

## Static Driver Verifier fails with exiting lib.exe/iwrap.exe with 0xc0000142 error

The smvbuild.log file contains a message similar to this error:

```
c:\Program Files\Microsoft Visual Studio\2017\BuildTools\Common7\IDE\VC\VCTargets\Microsoft.CppCommon.targets(1144,5): error MSB6006: "Lib.exe" exited with code -1073741502.

Done executing task "LIB" -- FAILED.
```

Please use errata 41600 for this issue.
