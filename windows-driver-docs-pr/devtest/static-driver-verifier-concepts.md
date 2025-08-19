---
title: Static Driver Verifier Concepts
description: Static Driver Verifier Concepts
ms.date: 07/02/2024
ms.topic: concept-article
---

# Static Driver Verifier Concepts

This section describes concepts that are specific to SDV and includes:

[Static Driver Verifier Rule](static-driver-verifier-rule.md)

[Operating System Model](operating-system-model.md)

[Verification Engine](verification-engine.md)

[Verification Process](verification-process.md)

[Passing and Failing a Verification](passing-and-failing-a-verification.md)

[Library Processing in Static Driver Verifier](library-processing-in-static-driver-verifier.md)

> [!IMPORTANT]
> SDV is no longer supported and SDV is not available in Windows 24H2 WDK or EWDK releases. It is not available in WDKs newer than build 26017, and is not included in the Windows 24H2 RTM WDK.
> SDV can still be used by downloading the Windows 11, version 22H2 EWDK (released October 24, 2023) with Visual Studio build tools 17.1.5 from [Download the Windows Driver Kit (WDK)](../download-the-wdk.md). Only the use of the Enterprise WDK to run SDV is recommended. Using older versions of the standard WDK in conjunction with recent releases of Visual Studio is not recommended, as this will likely result in analysis failures. <br>
> Going forward, CodeQL will be the primary static analysis tool for drivers. CodeQL provides a powerful query language that treats code as a database to be queried, making it simple to write queries for specific behaviors, patterns, and more.
> For more information about using CodeQL, see [CodeQL and the Static Tools Logo Test](static-tools-and-codeql.md).
