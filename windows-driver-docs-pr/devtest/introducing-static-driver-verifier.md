---
title: Introducing Static Driver Verifier
description: Introducing Static Driver Verifier
keywords:
- Static Driver Verifier WDK , about Static Driver Verifier
- StaticDV WDK , about Static Driver Verifier
- SDV WDK , about Static Driver Verifier
ms.date: 04/20/2017
---

# Introducing Static Driver Verifier

Static Driver Verifier (SDV) is a static verification tool that runs at compile time. It explores paths in the driver code by symbolically executing the source code, making the fewest possible assumptions about the state of the operating system and the initial state of the driver. As a result, SDV can exercise code in paths that are missed in traditional testing.

SDV includes a set of rules that define proper interaction between a driver and the operating system kernel. During verification, SDV examines every applicable branch of the driver code and the library code that it uses, and tries to prove that the driver violates the rules. If SDV fails to prove a violation, it reports that the driver complies with the rules and passes the verification.

This section includes:

[Understanding Static Driver Verifier](understanding-static-driver-verifier.md)

[Static Driver Verifier Concepts](static-driver-verifier-concepts.md)

[Supported Drivers](supported-drivers.md)

[Static Driver Verifier Limitations](static-driver-verifier-limitations.md)

> [!IMPORTANT]
> SDV is no longer supported and SDV is not available in Windows 24H2 WDK or EWDK releases. It is not available in WDKs newer than build 26017, and is not included in the Windows 24H2 RTM WDK.
> SDV can still be used by downloading the Windows 11, version 22H2 EWDK (released October 24, 2023) with Visual Studio build tools 17.1.5 from [Download the Windows Driver Kit (WDK)](../download-the-wdk.md). Only the use of the Enterprise WDK to run SDV is recommended. Using older versions of the standard WDK in conjunction with recent releases of Visual Studio is not recommended, as this will likely result in analysis failures. <br>
> Going forward, CodeQL will be the primary static analysis tool for drivers. CodeQL provides a powerful query language that treats code as a database to be queried, making it simple to write queries for specific behaviors, patterns, and more.
> For more information about using CodeQL, see [CodeQL and the Static Tools Logo Test](static-tools-and-codeql.md).
