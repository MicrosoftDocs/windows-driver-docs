---
title: Error Injection
author: windows-driver-content
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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Error Injection


The PSHED exposes an interface to the operating system through which the Windows kernel can cause hardware error events to occur for testing and validation. If a PSHED plug-in is implemented that participates in error injection, it is then called by the PSHED to perform the error injection operations.

For more information about how to implement a PSHED plug-in that participates in error injection, see [Participating in Error Injection](participating-in-error-injection.md).

User-mode management applications can inject errors into the hardware platform by calling the [WHEA Management API](https://msdn.microsoft.com/library/windows/hardware/ff560556). For more information about how to implement WHEA management applications, see [WHEA Management Applications](whea-management-applications.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Error%20Injection%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


