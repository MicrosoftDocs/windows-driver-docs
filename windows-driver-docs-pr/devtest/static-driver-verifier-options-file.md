---
title: Static Driver Verifier Options File
description: Static Driver Verifier Options File
keywords:
- Static Driver Verifier WDK , input files
- StaticDV WDK , input files
- SDV WDK , input files
- input files WDK Static Driver Verifier
- files WDK Static Driver Verifier
- options files WDK Static Driver Verifier
ms.date: 07/02/2024
---

# Static Driver Verifier Options File

The Static Driver Verifier Options File, sdv-default.xml, stores the default option settings for Static Driver Verifier. This file is created in the \\tools\\sdv\\data\\wdm and \\tools\\sdv\\data\\wdf subdirectories of the WDK. You can edit the file to change the option settings and copy it to any driver's sources directory.

This section includes:

[Global and Local Options Files](global-and-local-options-files.md)

[Option File Fields](option-file-fields.md)

[Option File Examples](option-file-examples.md)

> [!IMPORTANT]
> SDV is no longer supported and SDV is not available in Windows 24H2 WDK or EWDK releases. It is not available in WDKs newer than build 26017, and is not included in the Windows 24H2 RTM WDK.
> SDV can still be used by downloading the Windows 11, version 22H2 EWDK (released October 24, 2023) with Visual Studio build tools 17.1.5 from [Download the Windows Driver Kit (WDK)](../download-the-wdk.md). Only the use of the Enterprise WDK to run SDV is recommended. Using older versions of the standard WDK in conjunction with recent releases of Visual Studio is not recommended, as this will likely result in analysis failures. <br>
> Going forward, CodeQL will be the primary static analysis tool for drivers. CodeQL provides a powerful query language that treats code as a database to be queried, making it simple to write queries for specific behaviors, patterns, and more.
> For more information about using CodeQL, see [CodeQL and the Static Tools Logo Test](static-tools-and-codeql.md).
