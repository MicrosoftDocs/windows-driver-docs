---
title: Preventing BDA Minidriver Threats
author: windows-driver-content
description: Preventing BDA Minidriver Threats
MS-HAID:
- 'bdadg\_26003974-43c7-46ba-9e55-9afeaa0a4864.xml'
- 'stream.preventing\_bda\_minidriver\_threats'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 090cd2fb-d35b-4c42-a90d-a0d567d4b93f
keywords: ["Broadcast Driver Architecture WDK AVStream , security", "BDA WDK AVStream , security", "security WDK BDA"]
---

# Preventing BDA Minidriver Threats


## <a href="" id="ddk-preventing-bda-minidriver-threats-ksg"></a>


The threats that can be [introduced into a BDA minidriver](introducing-threats-to-a-bda-minidriver.md) can be prevented in the following ways:

<a href="" id="threats-in-the-signal-transport-stream"></a>Threats in the signal transport stream  
BDA minidrivers should not interpret the contents of signal payloads because such contents could be destructive. BDA minidrivers should only assemble the payloads' buffers and pass them on to the next filter.

 

If BDA minidrivers interpret payloads, they should carefully verify the contents when parsing such contents from the payloads.

<a href="" id="threats-from-special-purpose-ioctls"></a>Threats from special-purpose IOCTLs  
BDA minidrivers should not expose interfaces to applications that allow those applications to have direct control of buses, memory, or any other hardware. Therefore, processing for all special-purpose IOCTLs should be removed from BDA minidrivers. Such IOCTLs include, for example, vendor-created debugging IOCTLs. To process such IOCTLs, BDA minidrivers would implement an [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) dispatch routine.

<a href="" id="threats-from-direct-wdm-dispatch-routines"></a>Threats from direct WDM dispatch routines  
BDA minidrivers should not provide WDM dispatch routines that bypass the Kernel Streaming (KS) class model. BDA minidrivers should use the AVStream module of the KS driver to provide [dispatch](creating-dispatch-tables.md) and [automation](defining-automation-tables.md) routines because it also provides security checks. To provide direct WDM dispatch routines, BDA minidrivers would implement any of the [IRP major function codes](https://msdn.microsoft.com/library/windows/hardware/ff550710).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Preventing%20BDA%20Minidriver%20Threats%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


