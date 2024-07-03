---
title: Using Static Driver Verifier
description: Using Static Driver Verifier
ms.date: 07/02/2024
---

# Using Static Driver Verifier

For information about what you need to do to get up and running quickly, see [Using Static Driver Verifier to Find Defects in Windows Drivers](using-static-driver-verifier-to-find-defects-in-drivers.md)

## In this section

- [Using Function Role Type Declarations](using-function-role-type-declarations.md)
- [Scanning the Driver](scanning-the-driver.md)
- [Interpreting Static Driver Verifier Results](interpreting-static-driver-verifier-results.md)
- [Using the Static Driver Verifier Report](using-the-static-driver-verifier-report.md)
- [Recommendations for Troubleshooting Static Driver Verifier](recommendations-for-troubleshooting-static-driver-verifier.md)
- [Using SDV and the Sample Drivers](using-sdv-and-the-sample-drivers.md)

> [!IMPORTANT]
> SDV is no longer supported and SDV is not available in Windows 24H2 WDK or EWDK releases. It is not available in WDKs newer than build 26017, and is not included in the Windows 24H2 RTM WDK.
> SDV can still be used by downloading the Windows 11, version 22H2 EWDK (released October 24, 2023) with Visual Studio build tools 17.1.5 from [Download the Windows Driver Kit (WDK)](../download-the-wdk.md). Only the use of the Enterprise WDK to run SDV is recommended. Using older versions of the standard WDK in conjunction with recent releases of Visual Studio is not recommended, as this will likely result in analysis failures. <br>
> Going forward, CodeQL will be the primary static analysis tool for drivers. CodeQL provides a powerful query language that treats code as a database to be queried, making it simple to write queries for specific behaviors, patterns, and more.
> For more information about using CodeQL, see [CodeQL and the Static Tools Logo Test](static-tools-and-codeql.md).
