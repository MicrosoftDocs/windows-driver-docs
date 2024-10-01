---
title: How to Create a Driver Verification Log
description: Learn why the Windows Server hardware certification program requires a driver verification log (DVL) for all applicable driver submissions.
ms.date: 09/26/2024
---

# How to create a driver verification log

The [Windows Hardware Certification Program](/windows-hardware/design/compatibility/) requires a driver verification log (DVL) for driver submissions. The DVL contains a summary of the results from static analysis tools, [CodeQL](../devtest/static-tools-and-codeql.md). The DVL doesn't contain any source code information. Before creating a DVL for your driver, run CodeQL, the code analysis tool, and static driver verifier. For more information, see [Static Tools Logo Test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae) and [CodeQL and the Static Tools Logo Test](../devtest/static-tools-and-codeql.md).

## Prepare the driver

1. Before running the code analysis tools, build and link your driver using the latest Windows Driver Kit (WDK).
1. Select **Release** for the solution configuration and **x64** for the solution platform.

## Determine and run the required tests

To determine which tests are required for the version of Windows you wish to certify for, see the [Static Tools Logo Test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae).

Run the following tests, as required.

- Run CodeQL. Address and fix defects that are found. Certification fails if defects that are deemed "Must-Fix" aren't corrected. For more information about CodeQL and the Static Tools Logo Test, see [CodeQL and the Static Tools Logo Test](../devtest/static-tools-and-codeql.md).

- Run [Static Driver Verifier](../devtest/static-driver-verifier.md). For information about creating the log file, see [Creating a log file for Static Driver Verifier](creating-a-log-file-for-static-driver-verifier.md) and [Using Static Driver Verifier to find defects in drivers](../devtest/using-static-driver-verifier-to-find-defects-in-drivers.md).

- Run Code Analysis tool for drivers. Address and fix any defects that are found. See [Creating a log file for the code analysis tool](creating-a-log-file-for-the-code-analysis-tool.md) and [How to run Code Analysis for drivers](../devtest/how-to-run-code-analysis-for-drivers.md). For more information about code analysis, see [Analyzing Application Quality by Using Code Analysis Tools](/previous-versions/visualstudio/visual-studio-2013/dd264897(v=vs.120)).

## Create the driver verification log

1. From the **Driver** menu, select **Create Driver Verification Log**.
1. Verify that the *Code Analysis Log*, *Static Driver Verifier Log*, and *CodeQL Log* files are detected.
1. Select **Create**.

The driver verification log has the file name extension .DVL.XML. The log is created in the project folder, for example, \\*myDriverProject*\\*myDriverName*.DVL.XML.

SDV performs a clean rebuild of the driver, which removes the Code Analysis log. As such, be sure to run SDV before running CA.

When you're ready to test your driver using the [Windows Hardware Lab Kit](/windows-hardware/test/hlk/), copy the driver verification log to the %systemdrive%\\DVL directory on the test computer. Delete the contents of the directory on the test computer before you copy the new driver verification log.

> [!IMPORTANT]
> Timeouts, spaceouts, and other non-successful results in the DVL file are acceptable for certification submission. Non-successful results won't cause the static tools test in HLK to fail.

## Use the Visual Studio command prompt window

You can also create the driver verification log from a Visual Studio command prompt window. Use either the Visual Studio native tools command prompt installed with Visual Studio, or the Enterprise Windows Driver Kit (EWDK).

```console
msbuild.exe <vcxprojectfile> /target:dvl /p:Configuration="Release" /P:Platform=x64
```

## Create a driver verification log outside of msbuild or Visual Studio

Microsoft ships as part of the [Windows Driver Kit (WDK)](../download-the-wdk.md) and [Enterprise WDK (eWDK)](../download-the-wdk.md#download-icon-for-ewdk-enterprise-wdk-ewdk) a component called *dvl.exe* which can be used to generate driver verification logs (DVLs) via command-line. Starting in WDK/eWDK preview versions 21342 and above, it's possible to generate a DVL from the command line outside of the context of msbuild or Visual Studio.

### Generate DVL from CodeQL sarif file

1. Locate dvl.exe from the WDK or a mounted eWDK. It's typically installed in *C:\Program Files (x86)\Windows Kits\10\Tools\dvl\dvl.exe*
1. Call dvl.exe by passing the `/manualCreate` flag, a driver name, a desired architecture, and `/sarifPath`. Where `/sarifPath` includes the path to the folder containing the sarif file.

```console
"C:\Program Files (x86)\Windows Kits\10\Tools\dvl\dvl.exe" /manualCreate <driverName> <driverArchitecture> /sarifPath <pathToSarifLocation>
```

### Generate a DVL from a CodeQL sarif file, or when using CA and SDV

1. Place the results that must be consumed to create the DVL in a single directory, along with any vcxproj file. For drivers to be certified for Windows Client, this file is the [CodeQL SARIF file](../devtest/static-tools-and-codeql.md#3-perform-analysis). Windows Server certification might also include the Code Analysis and Static Driver Verifier (SDV) results files. Check the [WHCP requirements](/windows-hardware/design/compatibility/whcp-specifications-policies) documents for specific details on which tools are required to be run for device driver certification.
1. Place the CodeQL SARIF files and Code Analysis XML files in the top level of the directory. Place the SDV DVL.xml file in a subfolder called *sdv*.
1. Navigate to the top-level directory which contains the CodeQL SARIF file from the command line.
1. Locate dvl.exe from the WDK or a mounted eWDK.
1. Call dvl.exe by passing the `/manualCreate` flag, a driver name, and a desired architecture. For example:

   Use one of the following strings for your *driverArchitecture*:

   - X86
   - X64
   - Arm
   - Arm64

   > [!NOTE]
   > Don't include ".sys" as part of your *driverName* string.

1. Inspect the DVL to ensure that it was generated correctly.

This usage is primarily intended for generating DVLs with CodeQL results, but can also be used for SDV and CA results.

## Release notes

The most current information about the Code Analysis tool, Static Driver Verifier, and the driver verification log, is in the WDK release notes on the [Windows Driver Kit (WDK) download page](https://go.microsoft.com/fwlink/p/?linkid=254897).

## Related topics

- [Creating a log file for Static Driver Verifier](creating-a-log-file-for-static-driver-verifier.md)
- [Creating a log file for the code analysis tool](creating-a-log-file-for-the-code-analysis-tool.md)
- [Hardware Certification Program](/previous-versions/windows/hardware/hck/jj124227(v=vs.85))
- [Analyzing Driver Quality by Using Code Analysis Tools](analyzing-driver-quality-by-using-code-analysis-tools.md)
- [How to run Code Analysis for drivers](../devtest/how-to-run-code-analysis-for-drivers.md)
- [Using Static Driver Verifier to find defects in drivers](../devtest/using-static-driver-verifier-to-find-defects-in-drivers.md)
- [CodeQL and the Static Tools Logo Test](../devtest/static-tools-and-codeql.md)
