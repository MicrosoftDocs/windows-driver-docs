---
title: Static Driver Verifier Reference
description: Static Driver Verifier Reference
keywords:
- Static Driver Verifier WDK , reference
- StaticDV WDK , reference
- SDV WDK , reference
ms.date: 07/02/2024
---

# Static Driver Verifier Reference

This section includes:

[Static Driver Verifier KMDF Function Declarations](static-driver-verifier-kmdf-function-declarations.md)

[Static Driver Verifier NDIS Function Declarations](static-driver-verifier-ndis-function-declarations.md)

[Static Driver Verifier Input Files](static-driver-verifier-input-files.md)

[Static Driver Verifier Output Files](static-driver-verifier-output-files.md)

[Static Driver Verifier Error Messages](static-driver-verifier-error-messages.md)

> [!IMPORTANT]
> SDV is no longer supported and SDV is not available in Windows 24H2 WDK or EWDK releases. It is not available in WDKs newer than build 26017, and is not included in the Windows 24H2 RTM WDK.
> SDV can still be used by downloading the Windows 11, version 22H2 EWDK (released October 24, 2023) with Visual Studio build tools 17.1.5 from [Download the Windows Driver Kit (WDK)](../download-the-wdk.md). Only the use of the Enterprise WDK to run SDV is recommended. Using older versions of the standard WDK in conjunction with recent releases of Visual Studio is not recommended, as this will likely result in analysis failures. <br>
> Going forward, CodeQL will be the primary static analysis tool for drivers. CodeQL provides a powerful query language that treats code as a database to be queried, making it simple to write queries for specific behaviors, patterns, and more.
> For more information about using CodeQL, see [CodeQL and the Static Tools Logo Test](static-tools-and-codeql.md).

## Related topics

[DDI Compliance Rules](./static-driver-verifier-rules.md)
