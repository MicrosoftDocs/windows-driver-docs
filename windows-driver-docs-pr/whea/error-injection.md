---
title: Error Injection
description: Error Injection
keywords:
- Windows Hardware Error Architecture WDK , error injection
- WHEA WDK , error injection
- hardware errors WDK WHEA , error injections
- errors WDK WHEA , error injection
- platform-specific hardware error driver plug-ins WDK WHEA , error injection
- PSHED plug-ins WDK WHEA , error injection
- error injection WDK WHEA
ms.date: 04/20/2017
---

# Error Injection


The PSHED exposes an interface to the operating system through which the Windows kernel can cause hardware error events to occur for testing and validation. If a PSHED plug-in is implemented that participates in error injection, it is then called by the PSHED to perform the error injection operations.

For more information about how to implement a PSHED plug-in that participates in error injection, see [Participating in Error Injection](participating-in-error-injection.md).

User-mode management applications can inject errors into the hardware platform by calling the [WHEA Management API](/windows-hardware/drivers/ddi/_whea/). For more information about how to implement WHEA management applications, see [WHEA Management Applications](whea-management-applications.md).

 

