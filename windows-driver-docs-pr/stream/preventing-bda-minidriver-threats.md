---
title: Preventing BDA Minidriver Threats
description: Preventing BDA Minidriver Threats
ms.assetid: 090cd2fb-d35b-4c42-a90d-a0d567d4b93f
keywords:
- Broadcast Driver Architecture WDK AVStream , security
- BDA WDK AVStream , security
- security WDK BDA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Preventing BDA Minidriver Threats





The threats that can be [introduced into a BDA minidriver](introducing-threats-to-a-bda-minidriver.md) can be prevented in the following ways:

<a href="" id="threats-in-the-signal-transport-stream"></a>Threats in the signal transport stream  
BDA minidrivers should not interpret the contents of signal payloads because such contents could be destructive. BDA minidrivers should only assemble the payloads' buffers and pass them on to the next filter.

 

If BDA minidrivers interpret payloads, they should carefully verify the contents when parsing such contents from the payloads.

<a href="" id="threats-from-special-purpose-ioctls"></a>Threats from special-purpose IOCTLs  
BDA minidrivers should not expose interfaces to applications that allow those applications to have direct control of buses, memory, or any other hardware. Therefore, processing for all special-purpose IOCTLs should be removed from BDA minidrivers. Such IOCTLs include, for example, vendor-created debugging IOCTLs. To process such IOCTLs, BDA minidrivers would implement an [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) dispatch routine.

<a href="" id="threats-from-direct-wdm-dispatch-routines"></a>Threats from direct WDM dispatch routines  
BDA minidrivers should not provide WDM dispatch routines that bypass the Kernel Streaming (KS) class model. BDA minidrivers should use the AVStream module of the KS driver to provide [dispatch](creating-dispatch-tables.md) and [automation](defining-automation-tables.md) routines because it also provides security checks. To provide direct WDM dispatch routines, BDA minidrivers would implement any of the [IRP major function codes](https://msdn.microsoft.com/library/windows/hardware/ff550710).

 

 




