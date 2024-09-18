---
title: Creating a Driver Verification Log
description: Learn why the Windows Server Hardware Certification Program requires a Driver Verification Log (DVL) for all applicable driver submissions.
ms.date: 09/17/2024
---

# Creating a Driver Verification Log

The [Windows Hardware Certification Program](/windows-hardware/design/compatibility/) requires a Driver Verification Log (DVL) for driver submissions. The DVL can contain a summary of the results from Static Analysis Tools, [CodeQL](../devtest/static-tools-and-codeql.md). The DVL does not contain any source code information. You must run CodeQL, the Code Analysis tool and Static Driver Verifier as required, prior to creating a DVL for your driver. For additional details, see [Static Tools Logo Test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae) and [CodeQL and the Static Tools Logo Test](../devtest/static-tools-and-codeql.md).

## To create a driver verification log

### Prepare the driver

1. Before running the code analysis tools, be sure that you can build and link your driver using the latest Windows Driver Kit (WDK).
2. For the Driver Solution, make sure that you have selected a Release configuration as the Solution Configuration and x64 as the Solution Platform.

### Determine and run the required tests

1. Refer to the [Static Tools Logo Test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae) to determine what tests are required for the version of Windows you wish to certify for.

Run the following tests as required.

- Run CodeQL.  Address and fix defects that are found.  Certification will fail if defects that are deemed "Must-Fix" are not corrected.  For more information about CodeQL and the Static Tools Logo Test, see [CodeQL and the Static Tools Logo Test](../devtest/static-tools-and-codeql.md).
- Run [Static Driver Verifier](../devtest/static-driver-verifier.md). For information about creating the log file, see [Creating a log file for Static Driver Verifier](creating-a-log-file-for-static-driver-verifier.md) and [Using Static Driver Verifier to find defects in drivers](../devtest/using-static-driver-verifier-to-find-defects-in-drivers.md).
- Run Code Analysis tool for drivers. Address and fix any defects that are found. See [Creating a log file for the code analysis tool](creating-a-log-file-for-the-code-analysis-tool.md) and [How to run Code Analysis for Drivers](../devtest/how-to-run-code-analysis-for-drivers.md). For more information about code analysis, see [Analyzing C/C++ Code Quality by Using Code Analysis](/previous-versions/visualstudio/visual-studio-2013/dd264897(v=vs.120)).

### Create the driver verification log

1. Create the Driver Verification Log. From the **Driver** menu, select **Create Driver Verification Log...**.

2. Verify that the Code Analysis Log, Static Driver Verifier Log, and CodeQL Log files are detected. Select **Create**.

The driver verification log has the file name extension .DVL.XML. The log is created in the project folder, for example, \\*myDriverProject*\\*myDriverName*.DVL.XML.

**Note**  SDV performs a clean rebuild of the driver, which removes the Code Analysis log.  As such, please be sure to run SDV before running CA.

**Note**  When you are ready to test your driver using the [Windows Hardware Lab Kit](/windows-hardware/test/hlk/), you need to copy the driver verification log to the %systemdrive%\\DVL directory on the test computer. Be sure to delete the contents of the directory on the test computer before you copy the new driver verification log.

## Remarks

For the most up-to-date information about the Code Analysis tool, Static Driver Verifier, and the Driver Verification Log, refer to the WDK Release Notes. The Release Notes are available on the [Windows Driver Kit (WDK) download page](https://go.microsoft.com/fwlink/p/?linkid=254897).

>[!IMPORTANT]
> Timeouts, spaceouts, and other non-successful results in the DVL file are acceptable for certification submission. This will not cause the Static Tools test in HLK to fail.

### Visual Studio Command Prompt window

You can also create the driver verification log from a Visual Studio Command Prompt window, either by the Visual Studio Native Tools Command Prompt installed with Visual Studio or via the Enterprise Windows Driver Kit (EWDK). 

```cpp
msbuild.exe <vcxprojectfile> /target:dvl /p:Configuration="Release" /P:Platform=x64
```

## Creating a Driver Verification Log Outside of msbuild or Visual Studio

Microsoft ships as part of the [Windows Driver Kit (WDK)](../download-the-wdk.md) and [Enterprise WDK (eWDK)](../download-the-wdk.md#download-icon-for-ewdk-enterprise-wdk-ewdk) a component called *dvl.exe* which can be used to generate Driver Verification Logs (DVLs) via command-line.  Starting in WDK/eWDK preview versions 21342 and above, it is possible to generate a DVL from the command line outside of the context of msbuild or Visual Studio. 

### Follow these steps to generate DVL from CodeQL sarif file:

1. Locate dvl.exe from the WDK or a mounted eWDK. This is typically installed in the path "C:\Program Files (x86)\Windows Kits\10\Tools\dvl\dvl.exe"
2. Call dvl.exe by passing the /manualCreate flag, a driver name, a desired architecture and /sarifPath. Where /sarifPath is the path to the folder containing the sarif file.

```cmd
"C:\Program Files (x86)\Windows Kits\10\Tools\dvl\dvl.exe" /manualCreate <driverName> <driverArchitecture> /<sarifPath>
```

### When using CA and SDV follow these steps to generate the DVL:

1. Place the results that must be consumed to create the DVL in a single directory, along with any vcxproj file.  Typically for drivers intended to be certified for Windows Client, this is the [CodeQL SARIF file](../devtest/static-tools-and-codeql.md#3-perform-analysis).  For Windows Server certification, this may also include the Code Analysis and Static Driver Verifier (SDV) results files.  Check the [WHCP requirements](/windows-hardware/design/compatibility/whcp-specifications-policies) documents for specific details on which tools are required to be run for device driver certification.
2. CodeQL SARIF files and Code Analysis XML files should be placed in the top level of the directory.  The SDV DVL.xml file should be placed in a “sdv” subfolder.
3. From the command line, navigate to the top-level directory which contains the CodeQL SARIF file.
4. Locate dvl.exe from the WDK or a mounted eWDK.
5. Call dvl.exe by passing the /manualCreate flag, a driver name, and a desired architecture. For example:

One of the following strings should be used for your driverArchitecture string:

- X86
- X64
- Arm
- Arm64

**Do not include ".sys" as part of your driverName string**

6. Inspect the generated DVL to ensure that it was generated correctly

This usage is primarily intended for generating DVLs with CodeQL results, but can also be used for SDV and CA results.  

## Related topics

* [Creating a log file for Static Driver Verifier](creating-a-log-file-for-static-driver-verifier.md)
* [Creating a log file for the code analysis tool](creating-a-log-file-for-the-code-analysis-tool.md)
* [Hardware Certification Program](/previous-versions/windows/hardware/hck/jj124227(v=vs.85))
* [Analyzing Driver Quality by Using Code Analysis Tools](analyzing-driver-quality-by-using-code-analysis-tools.md)
* [How to run Code Analysis for drivers](../devtest/how-to-run-code-analysis-for-drivers.md)
* [Using Static Driver Verifier to find defects in drivers](../devtest/using-static-driver-verifier-to-find-defects-in-drivers.md)
* [CodeQL and the Static Tools Logo Test](../devtest/static-tools-and-codeql.md)
