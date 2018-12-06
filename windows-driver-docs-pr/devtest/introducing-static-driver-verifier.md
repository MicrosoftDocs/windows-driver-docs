---
title: Introducing Static Driver Verifier
description: Introducing Static Driver Verifier
ms.assetid: fa6e8b0f-0d0f-4293-87ec-e67decd6acb7
keywords:
- Static Driver Verifier WDK , about Static Driver Verifier
- StaticDV WDK , about Static Driver Verifier
- SDV WDK , about Static Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introducing Static Driver Verifier


Static Driver Verifier (SDV) is a static verification tool that runs at compile time. It explores paths in the driver code by symbolically executing the source code, making the fewest possible assumptions about the state of the operating system and the initial state of the driver. As a result, SDV can exercise code in paths that are missed in traditional testing.

SDV includes a set of rules that define proper interaction between a driver and the operating system kernel. During verification, SDV examines every applicable branch of the driver code and the library code that it uses, and tries to prove that the driver violates the rules. If SDV fails to prove a violation, it reports that the driver complies with the rules and passes the verification.

This section includes:

[Understanding Static Driver Verifier](understanding-static-driver-verifier.md)

[Static Driver Verifier Concepts](static-driver-verifier-concepts.md)

[Supported Drivers](supported-drivers.md)

[Static Driver Verifier Limitations](static-driver-verifier-limitations.md)

 

 





