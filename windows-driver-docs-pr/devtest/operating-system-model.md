---
title: Operating System Model
description: Operating System Model
ms.assetid: a7200472-24e1-4ecf-86c7-a1b72c5661fc
keywords:
- Static Driver Verifier WDK , operating system model
- StaticDV WDK , operating system model
- SDV WDK , operating system model
- operating system model WDK Static Driver Verifier
- harness WDK Static Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Operating System Model


An SDV *operating system model* or *harness* consists of partial and abstracted segments of Windows code that act as the operating system during a verification. SDV includes a default operating system model and several specialized models that are used to verify particular [rules](static-driver-verifier-rule.md). SDV assembles the operating system model for a verification during the **Check** step of the [verification process](verification-process.md).

There is also a harness that executes parts of your driver in the same manner as the Windows Operating System by calling into entry points in the driver.

 

 





