---
title: Error Injection
description: Error Injection
ms.assetid: d97d49bc-b216-40d6-afd1-aecff624624d
keywords:
- Windows Hardware Error Architecture WDK , error injection
- WHEA WDK , error injection
- hardware errors WDK WHEA , error injections
- errors WDK WHEA , error injection
- platform-specific hardware error driver plug-ins WDK WHEA , error injection
- PSHED plug-ins WDK WHEA , error injection
- error injection WDK WHEA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Error Injection


The PSHED exposes an interface to the operating system through which the Windows kernel can cause hardware error events to occur for testing and validation. If a PSHED plug-in is implemented that participates in error injection, it is then called by the PSHED to perform the error injection operations.

For more information about how to implement a PSHED plug-in that participates in error injection, see [Participating in Error Injection](participating-in-error-injection.md).

User-mode management applications can inject errors into the hardware platform by calling the [WHEA Management API](https://msdn.microsoft.com/library/windows/hardware/ff560556). For more information about how to implement WHEA management applications, see [WHEA Management Applications](whea-management-applications.md).

 

 




