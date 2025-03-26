---
title: Using SDV and the Sample Drivers
description: Using SDV and the Sample Drivers
ms.date: 07/02/2024
ms.topic: concept-article
---

# Using SDV and the Sample Drivers

To help you get started using Static Driver Verifier (SDV) you can run the tool on the SDV-FailDriver samples. The sample drivers contain intentional code errors that are designed to show the capabilities and features of SDV. These sample drivers are not functional and are not intended as examples for real driver development projects. There are SDV-FailDriver sample drivers available in the [Windows driver samples](https://github.com/Microsoft/Windows-driver-samples) repository on GitHub.

- [SDV-FailDriver-KMDF](https://github.com/Microsoft/Windows-driver-samples/tree/main/tools/sdv/samples/SDV-FailDriver-KMDF)
- [SDV-FailDriver-WDM](https://github.com/Microsoft/Windows-driver-samples/tree/main/tools/sdv/samples/SDV-FailDriver-WDM)
- [SDV-FailDriver-NDIS](https://github.com/Microsoft/Windows-driver-samples/tree/main/tools/sdv/samples/SDV-FailDriver-NDIS)
- [SDV-FailDriver-STORPORT](https://github.com/Microsoft/Windows-driver-samples/tree/main/tools/sdv/samples/SDV-FailDriver-STORPORT)

> [!IMPORTANT]
> SDV is no longer supported and SDV is not available in Windows 24H2 WDK or EWDK releases. It is not available in WDKs newer than build 26017, and is not included in the Windows 24H2 RTM WDK.
> SDV can still be used by downloading the Windows 11, version 22H2 EWDK (released October 24, 2023) with Visual Studio build tools 17.1.5 from [Download the Windows Driver Kit (WDK)](../download-the-wdk.md). Only the use of the Enterprise WDK to run SDV is recommended. Using older versions of the standard WDK in conjunction with recent releases of Visual Studio is not recommended, as this will likely result in analysis failures. <br>
> Going forward, CodeQL will be the primary static analysis tool for drivers. CodeQL provides a powerful query language that treats code as a database to be queried, making it simple to write queries for specific behaviors, patterns, and more.
> For more information about using CodeQL, see [CodeQL and the Static Tools Logo Test](static-tools-and-codeql.md).
