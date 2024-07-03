---
title: Static Driver Verifier Report
description: Static Driver Verifier Report
keywords:
- Static Driver Verifier WDK , Static Driver Verifier Report
- StaticDV WDK , Static Driver Verifier Report
- SDV WDK , Static Driver Verifier Report
- Static Driver Verifier WDK , locating errors
- StaticDV WDK , locating errors
- SDV WDK , locating errors
- locating errors WDK Static Driver Verifier
- errors WDK Static Driver Verifier
- panes WDK Static Driver Verifier
- Static Driver Verifier Report WDK
ms.date: 07/02/2024
---

# Static Driver Verifier Report

The Static Driver Verifier Report is an interactive display of the results of a verification. You can use the report to investigate the verification result and to identify paths in your driver that fail a SDV verification.

This section includes:

[Static Driver Verifier Report Panes](static-driver-verifier-report-panes.md)

> [!IMPORTANT]
> SDV is no longer supported and SDV is not available in Windows 24H2 WDK or EWDK releases. It is not available in WDKs newer than build 26017, and is not included in the Windows 24H2 RTM WDK.
> SDV can still be used by downloading the Windows 11, version 22H2 EWDK (released October 24, 2023) with Visual Studio build tools 17.1.5 from [Download the Windows Driver Kit (WDK)](../download-the-wdk.md). Only the use of the Enterprise WDK to run SDV is recommended. Using older versions of the standard WDK in conjunction with recent releases of Visual Studio is not recommended, as this will likely result in analysis failures. <br>
> Going forward, CodeQL will be the primary static analysis tool for drivers. CodeQL provides a powerful query language that treats code as a database to be queried, making it simple to write queries for specific behaviors, patterns, and more.
> For more information about using CodeQL, see [CodeQL and the Static Tools Logo Test](static-tools-and-codeql.md).
