---
title: Creating a Log File for the Code Analysis Tool
description: The Windows Server 2012 Hardware Certification Program requires a Driver Verification Log (DVL) for all applicable driver submissions.
ms.date: 03/19/2024
---

# Creating a log file for the code analysis tool

The [Windows Hardware Certification Program](/windows-hardware/design/compatibility/) requires a Driver Verification Log (DVL) for driver submissions. You may need to run the Code Analysis tool prior to creating a DVL for your driver. The DVL can contain a summary of the results from tools such as CodeQL, Code Analysis and Static Driver Verifier log files. The log files do not contain source code information. For additional details, see [Static Tools Logo Test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae) and [CodeQL and the Static Tools Logo Test](../devtest/static-tools-and-codeql.md)

## To run code analysis on the driver

1. In Microsoft Visual Studio, select the driver project file and then select and hold (or right-click) to open the project properties.
2. From the **Analyze** or **Build** menu, select **Run Code Analysis on Solution**.
3. If errors or warnings are found, use the **Code Analysis Report** window to investigate the cause of the errors. Use the warning messages to fix those problems. For more information about the Code Analysis tool, see [How to run Code Analysis for drivers](../devtest/how-to-run-code-analysis-for-drivers.md) and [Analyzing C/C++ Code Quality by Using Code Analysis](/previous-versions/visualstudio/visual-studio-2013/dd264897(v=vs.120)).

The Code Analysis tool for drivers writes the results to the file vc.nativecodeanalysis.all.xml in the build configuration and platform sub-directory of your project, for example, \\Windows 8Release\\x64.

## Remarks

Code Analysis for Drivers is a compile-time static verification tool that detects basic coding errors in C and C++ programs and includes a specialized module that is designed to detect errors in (primarily) kernel-mode driver code. In previous versions of the WDK, the driver-specific module for code analysis was part of a stand-alone tool called PREfast for Drivers (PFD).

### Visual Studio Command Prompt window

You can also run the Code Analysis tool from a Visual Studio Command Prompt window. Set up the environment by running one of the following batch files.

```cpp
"C:\Program Files\Microsoft Visual Studio 11.0\VC\vcvarsall.bat" x64
```

-Or-

```cpp
"C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC\vcvarsall.bat" x64
```

Run the Code Analysis tool. Use the appropriate Windows release for your submission.

```cpp
msbuild.exe <vcxprojectfile> /p:Configuration="Win8 Release" /P:Platform=x64 /target:clean
msbuild.exe <vcxprojectfile> /p:Configuration="Win8 Release" /P:Platform=x64 /P:RunCodeAnalysisOnce=True
```

For the most up-to-date information about the requirements for the Driver Verification Log, refer to the WDK Release Notes.

## Related topics

* [Creating a driver verification log](creating-a-driver-verification-log.md)
* [Creating a log file for Static Driver Verifier](creating-a-log-file-for-static-driver-verifier.md)
* [Code Analysis for Drivers](../devtest/code-analysis-for-drivers.md)
* [Hardware Certification Program](/previous-versions/windows/hardware/hck/jj124227(v=vs.85))
* [Analyzing C/C++ Code Quality by Using Code Analysis](/previous-versions/visualstudio/visual-studio-2013/dd264897(v=vs.120))
* [How to run Code Analysis for drivers](../devtest/how-to-run-code-analysis-for-drivers.md)
