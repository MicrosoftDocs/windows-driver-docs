---
title: Master Clocks
author: windows-driver-content
description: Master Clocks
ms.assetid: bdd228c1-a15f-4c08-8991-299a3f2e1ee8
keywords:
- master clocks WDK kernel streaming
- synchronization WDK kernel streaming
- KSPROPERTY_STREAM_MASTERCLOCK
- physical time WDK kernel streaming
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Master Clocks


## <a href="" id="ddk-master-clocks-ksg"></a>


Minidrivers can synchronize streams to clocks created by other minidrivers; multiple streams can be synchronized to one clock. If the pin uses or produces such a *master clock*, the minidriver should support [**KSPROPERTY\_STREAM\_MASTERCLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff565713). Clients also can use this property to set the master clock for the pin. Pins that perform rendering and capturing operations frequently use a master clock. The minidriver is responsible for releasing clock references upon termination.

The interface to a master clock is a file object that supports methods, properties and events.

All queries against the file object are available only at PASSIVE\_LEVEL. However, the clock position query also is supported through a direct function call pointer available at DISPATCH\_LEVEL, which is valid as long as the file object is valid. This direct call must be passed to the clock's file object as a context parameter.

The file handle is acquired through a create request on a filter pin instance, much as the pin creation is done by IRP\_MJ\_CREATE. The request causes a file handle to be created, just as a file handle to a pin is created, with its own context information. This file handle is then passed back to the caller and can be used to set the master clock for kernel-mode filters. At the time the filter is being assigned the graph's master clock, a pin instance can query the parent file object to determine if it owns the master clock.

When a filter is given the file handle to this master clock, it can then be used to query properties. If a master clock is based on a kernel-mode filter, it must support an interface to query the file handle to the kernel-mode portion of the master clock. If the interface is not supported, then it is assumed that the clock is user mode-based, and kernel-mode filters cannot synchronize to it.

The DirectShow proxy filter requesting the master clock handle then passes it to its underlying kernel-mode filter file handle. The kernel-mode filter references the underlying file object. If the filter already had a master clock, it dereferences the file object and uses the new handle. To do this, the filter must be in *Stop state*.

The physical time on the master clock object is frequently hardware-based. If a filter that presents the master clock has no physical clock, then the stream time progresses according to the time stamps of the data presented. In such a situation, time stamps may stop due to a lack of data.

The physical time behind the master clock may be remote, in which case it is the responsibility of the local proxy to provide accurate readings. For example, the proxy has responsibility for compensating for the delay across a 1394 connection, or averaging the delay across a network. Additionally, if some other kernel filter is a proxy for a second device on the same 1394 bus, the two devices may negotiate a private method of interfacing with the master clock. In such a case, the devices must use private interfaces to determine clock type in order to verify compatibility.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Master%20Clocks%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


