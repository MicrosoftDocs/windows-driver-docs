---
title: Creating a Log File for Static Driver Verifier
description: Learn how to run a Static Driver Verifier (SDV) before creating a Driver Verification Log (DVL) for your driver.
ms.date: 03/19/2024
---

# Creating a log file for Static Driver Verifier

The [Windows Hardware Certification Program](/windows-hardware/design/compatibility/) requires a Driver Verification Log (DVL) for driver submissions. You may need to run Static Driver Verifier prior to creating a DVL for your driver.   The DVL can contain a summary of the results from tools such as CodeQL, Code Analysis and Static Driver Verifier. The log files do not contain source code information. For additional details, see [Static Tools Logo Test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae) and [CodeQL and the Static Tools Logo Test](../devtest/static-tools-and-codeql.md).

## Create the log file for SDV

1. In Microsoft Visual Studio, select the driver project file and then select and hold (or right-click) to open the project properties.
2. If you have already run the Code Analysis tool, follow these instructions for [running Static Driver Verifier](../devtest/using-static-driver-verifier-to-find-defects-in-drivers.md#running-static-driver-verifier). For more information about using SDV, see Using Static Driver Verifier to Find Defects in Drivers
3. If SDV finds defects in your driver, select the defect in the Results pane to view a trace of the code path that led to the rule violation. Fix any defects found in the driver and run SDV again.

Static Driver Verifier writes the results to the file SDV.DVL.xml in the SDV sub-directory of your project, for example, \\myDriverProject\\SDV.

## Remarks

For the most up-to-date information about Static Driver Verifier and the Driver Verification Log, refer to the WDK Release Notes. The Release Notes are available on the [Windows Driver Kit (WDK) download page](https://go.microsoft.com/fwlink/p/?linkid=254897).

>[!IMPORTANT]
>Timeouts, spaceouts, and other non-successful results in the DVL file are acceptable for certification submission. This will not cause the Static Tools test in HCK to fail. For HCK 2.0, the Static Tools Test only requires the presence of DVL file to show Code Analysis and SDV had been run, and does not require all rules to pass.

### Visual Studio Command Prompt window

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

## Related topics

* [Creating a driver verification log](creating-a-driver-verification-log.md)
* [Static Driver Verifier](../devtest/static-driver-verifier.md)
* [Using Static Driver Verifier to Find Defects in Drivers](../devtest/using-static-driver-verifier-to-find-defects-in-drivers.md)
* [Hardware Certification Program](/previous-versions/windows/hardware/hck/jj124227(v=vs.85))
