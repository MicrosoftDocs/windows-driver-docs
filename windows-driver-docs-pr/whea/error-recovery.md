---
title: Error Recovery
author: windows-driver-content
description: Error Recovery
ms.assetid: 5710625f-bb65-41d4-a5c9-d61a48178859
keywords:
- Windows Hardware Error Architecture WDK , error recovery
- WHEA WDK , error recovery
- hardware errors WDK WHEA , error recovery
- errors WDK WHEA , error recovery
- platform-specific hardware error driver plug-ins WDK WHEA , error recovery
- PSHED plug-ins WDK WHEA , error recovery
- error recovery WDK WHEA
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Error Recovery


During the handling of a recoverable hardware error, the operating system attempts to recover from the error condition. First the operating system attempts to recover from the error condition on its own. Then the Windows kernel calls into the PSHED to give it an opportunity to perform any hardware operations that are required to recover from the error condition. If a PSHED plug-in is implemented that participates in error recovery, it is then called by the PSHED so that it can perform any additional platform-specific hardware operations that are required to fully recover from the error condition. Regardless of whether the operating system successfully recovers from the error condition on its own, the Windows kernel always calls the PSHED to ensure that the PSHED and any registered PSHED plug-in have the opportunity to update or modify the hardware state as necessary.

For more information about how to implement a PSHED plug-in that participates in error recovery, see [Participating in Error Recovery](participating-in-error-recovery.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Error%20Recovery%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


