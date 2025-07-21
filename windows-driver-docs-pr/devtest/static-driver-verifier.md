---
title: Static Driver Verifier
description: Static Driver Verifier
keywords:
- verifying drivers WDK , Static Driver Verifier
- driver verification WDK , Static Driver Verifier
- Static Driver Verifier WDK
- StaticDV WDK
- SDV WDK
- paths WDK SDV
- compile-time static verification tool WDK
ms.date: 07/02/2024
ms.topic: concept-article
---

# Static Driver Verifier

Static Driver Verifier (also known as "StaticDV" or "SDV") is a static verification tool that systematically analyzes the source code of Windows kernel-mode drivers. SDV is a compile time tool that is capable of discovering defects and design issues in a driver. Based on a set of interface rules and a model of the operating system, SDV determines whether the driver correctly interacts with the Windows operating system kernel.

> [!IMPORTANT]
> SDV is no longer supported and SDV is not available in Windows 24H2 WDK or EWDK releases. It is not available in WDKs newer than build 26017, and is not included in the Windows 24H2 RTM WDK.
> SDV can still be used by downloading the Windows 11, version 22H2 EWDK (released October 24, 2023) with Visual Studio build tools 17.1.5 from [Download the Windows Driver Kit (WDK)](../download-the-wdk.md). Only the use of the Enterprise WDK to run SDV is recommended. Using older versions of the standard WDK in conjunction with recent releases of Visual Studio is not recommended, as this will likely result in analysis failures. <br>
> Going forward, CodeQL will be the primary static analysis tool for drivers. CodeQL provides a powerful query language that treats code as a database to be queried, making it simple to write queries for specific behaviors, patterns, and more.
> For more information about using CodeQL, see [CodeQL and the Static Tools Logo Test](static-tools-and-codeql.md).

## Installing Static Driver Verifier

Static Driver Verifier is available as part of the Windows Driver Kit (WDK) in both the full WDK experience and in the standalone Enterprise WDK.  In addition, the Visual C++ Redistributable Packages for Visual Studio are required for SDV to run. See the following:

* [Microsoft Visual C++ Redistributable latest supported downloads](/cpp/windows/latest-supported-vc-redist)

## Visual Studio Integration

Static Driver Verifier is integrated into Visual Studio. You can run static analysis on your Visual Studio driver project. You can launch, configure, and control Static Driver Verifier from the **Driver** menu in Visual Studio.

## Static Driver Verifier Documentation

* [Static Driver Verifier Known Issues](../develop/static-driver-verifier-known-issues.md): Lists latest known issues for Static Driver Verifier
* [Using Static Driver Verifier to Find Defects in Drivers](using-static-driver-verifier-to-find-defects-in-drivers.md): Tells you what you need to get started analyzing your driver code in the Visual Studio environment.
* [Static Driver Verifier commands (MSBuild)](-static-driver-verifier-commands--msbuild-.md): Lists the MSBuild commands to use to run SDV in a Visual Studio Command Prompt window.
* [Introducing Static Driver Verifier](introducing-static-driver-verifier.md): Provides an overview of the static analysis tool.
* [Using Static Driver Verifier](using-static-driver-verifier.md): Provides the details about using and configuring the static analysis tool.
* [Static Driver Verifier Report](static-driver-verifier-report.md): Describes the viewer that displays the detailed trace of the static code analysis.
* [Static Driver Verifier Rules](static-driver-verifier-rules.md): The rules define the requirements for proper interaction between a driver model and the kernel interface of the operating system.
* [Static Driver Verifier Reference](static-driver-verifier-reference.md): Provides reference information about the function role types, SDV configuration files, error, and warning messages.

## Finding Bugs in Windows Driver Code

Microsoft uses SDV to test the kernel-mode drivers that are included with the Microsoft Windows operating system and to test the sample drivers in the WDK. By using the DDI compliance rules for specific driver models, SDV can verify correct driver behavior. For example, SDV can verify that the driver:

* Calls functions at the correct IRQL
* Acquires and releases locks in the correct sequence
* Correctly uses functions that handle I/O request packets (IRP)

SDV examines all possible paths through the driver code. It is designed to find serious errors in obscure paths that are unlikely to be encountered even in thorough testing.

## Additional resources

For specific information about the drivers that SDV can verify, see [Supported Drivers](supported-drivers.md)

For more information and tips about using Static Driver Verifier, see the following:

* [Windows Hardware Certification blog](https://techcommunity.microsoft.com/t5/Windows-Hardware-Certification/bg-p/WindowsHardwareCertification)
* [Windows Kernel community site](https://techcommunity.microsoft.com/t5/Windows-Kernel/ct-p/WindowsKernel)
* [Windows Hardware Testing and Certification forum](https://social.msdn.microsoft.com/Forums/home?forum=whck)
