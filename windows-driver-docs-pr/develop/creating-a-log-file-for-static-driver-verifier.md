---
ms.assetid: EDA6357A-D18D-439D-A0DD-050BA51E1A79
title: Creating a log file for Static Driver Verifier
description: The Windows Server 2012 Hardware Certification Program requires a Driver Verification Log (DVL) for all applicable driver submissions.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a log file for Static Driver Verifier

The Windows Server 2012 [Hardware Certification Program](http://go.microsoft.com/fwlink/p/?linkid=227016) requires a Driver Verification Log (DVL) for all applicable driver submissions. You must run [Static Driver Verifier](https://msdn.microsoft.com/Library/Windows/Hardware/Ff552808) (SDV) prior to creating a DVL for your driver. The DVL contains a summary of the results from the Code Analysis and Static Driver Verifier log files. The log files do not contain source code information.

For best results, run the Code Analysis tool before you run Static Driver Verifier.

**To create a log file for Static Driver Verifier**

1.  In Microsoft Visual Studio Ultimate 2012, select the driver project file and then right-click to open the project properties. Select **Windows 8 Release** as the **Configuration** and **x64** as the **Platform**.
2.  If you have already run the Code Analysis tool, follow these instructions for [running Static Driver Verifier](https://msdn.microsoft.com/Library/Windows/Hardware/Hh454281#running_static_driver_verifier). For more information about using SDV, see Using Static Driver Verifier to Find Defects in Drivers
3.  If SDV finds defects in your driver, click the defect in the Results pane to view a trace of the code path that led to the rule violation. Fix any defects found in the driver and run SDV again.

Static Driver Verifier writes the results to the file SDV.DVL.xml in the SDV sub-directory of your project, for example, \\myDriverProject\\SDV.

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


For the most up-to-date information about Static Driver Verifier and the Driver Verification Log, refer to the WDK Release Notes. The Release Notes are available on the [Windows Driver Kit (WDK) download page](http://go.microsoft.com/fwlink/p/?linkid=254897).

**Important**   Timeouts, spaceouts, and other non-successful results in the DVL file are acceptable for certification submission. This will not cause the Static Tools test in HCK to fail. For HCK 2.0, the Static Tools Test only requires the presence of DVL file to show Code Analysis and SDV had been run, and does not require all rules to pass.

 

You can also run Static Driver Verifier from a Visual Studio Command Prompt window. Set up the environment by running one of the following batch files.

```cpp
"C:\Program Files\Microsoft Visual Studio 11.0\VC\vcvarsall.bat" x64
```

-Or-

```cpp
"C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC\vcvarsall.bat" x64
```

Run Static Driver Verifier.

```cpp
msbuild.exe <vcxprojectfile> /p:Configuration="Win8 Release" /p:Platform=x64 /target:sdv /p:inputs="/clean"
msbuild.exe <vcxprojectfile> /p:Configuration="Win8 Release" /p:Platform=x64 /target:sdv /p:inputs="/check:default.sdv"
```

## <span id="related_topics"></span>Related topics


* [Creating a driver verification log](creating-a-driver-verification-log.md)
* [Static Driver Verifier](https://msdn.microsoft.com/Library/Windows/Hardware/Ff552808)
* [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/Library/Windows/Hardware/Hh454281)
* [Hardware Certification Program](http://go.microsoft.com/fwlink/p/?linkid=227016)
 

 






