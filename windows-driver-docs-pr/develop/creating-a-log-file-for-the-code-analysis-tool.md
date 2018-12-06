---
ms.assetid: 4985B206-9E7F-45FE-9067-7CFD15A7AAAD
title: Creating a log file for the code analysis tool
description: The Windows Server 2012 Hardware Certification Program requires a Driver Verification Log (DVL) for all applicable driver submissions.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a log file for the code analysis tool

The Windows Server 2012 [Hardware Certification Program](http://go.microsoft.com/fwlink/p/?linkid=227016) requires a Driver Verification Log (DVL) for all applicable driver submissions. You must run the Code Analysis tool prior to creating a DVL for your driver. The DVL contains a summary of the results from the Code Analysis and Static Driver Verifier log files. The log files do not contain source code information.

**To run code analysis on the driver**

1.  In Microsoft Visual Studio Ultimate 2012, select the driver project file and then right-click to open the project properties. Select **Windows 8 Release** as the **Configuration** and **x64** as the **Platform**.
2.  From the **Analyze** or **Build** menu, click **Run Code Analysis on Solution**.
3.  If errors or warnings are found, use the **Code Analysis Report** window to investigate the cause of the errors. Use the warning messages to fix those problems. For more information about the Code Analysis tool, see [How to run Code Analysis for drivers](https://msdn.microsoft.com/Library/Windows/Hardware/Hh454219) and [Analyzing C/C++ Code Quality by Using Code Analysis](http://go.microsoft.com/fwlink/p/?linkid=226836).

The Code Analysis tool for drivers writes the results to the file vc.nativecodeanalysis.all.xml in the build configuration and platform sub-directory of your project, for example, \\Windows 8Release\\x64.

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


Code Analysis for Drivers is a compile-time static verification tool that detects basic coding errors in C and C++ programs and includes a specialized module that is designed to detect errors in (primarily) kernel-mode driver code. In previous versions of the WDK, the driver-specific module for code analysis was part of a stand-alone tool called PREfast for Drivers (PFD).

You can also run the Code Analysis tool from a Visual Studio Command Prompt window. Set up the environment by running one of the following batch files.

```cpp
"C:\Program Files\Microsoft Visual Studio 11.0\VC\vcvarsall.bat" x64
```

-Or-

```cpp
"C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC\vcvarsall.bat" x64
```

Run the Code Analysis tool.

```cpp
msbuild.exe <vcxprojectfile> /p:Configuration="Win8 Release" /P:Platform=x64 /target:clean
msbuild.exe <vcxprojectfile> /p:Configuration="Win8 Release" /P:Platform=x64 /P:RunCodeAnalysisOnce=True
```

For the most up-to-date information about the requirements for the Driver Verification Log, refer to the WDK Release Notes.

## <span id="related_topics"></span>Related topics


* [Creating a driver verification log](creating-a-driver-verification-log.md)
* [Creating a log file for Static Driver Verifier](creating-a-log-file-for-static-driver-verifier.md)
* [Code Analysis for Drivers](https://msdn.microsoft.com/Library/Windows/Hardware/Hh454182)
* [Hardware Certification Program](http://go.microsoft.com/fwlink/p/?linkid=227016)
* [Analyzing C/C++ Code Quality by Using Code Analysis](http://go.microsoft.com/fwlink/p/?linkid=226836)
* [How to run Code Analysis for drivers](https://msdn.microsoft.com/Library/Windows/Hardware/Hh454219)
 

 






