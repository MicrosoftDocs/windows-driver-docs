---
title: Supporting Multiple Streams
author: windows-driver-content
description: Supporting Multiple Streams
ms.assetid: 89f79078-129a-44cc-8b7e-5f5c1c33a473
keywords:
- Stream.sys class driver WDK Windows 2000 Kernel , multiple streams
- streaming minidrivers WDK Windows 2000 Kernel , multiple streams
- minidrivers WDK Windows 2000 Kernel Streaming , multiple streams
- multiple streams WDK streaming minidriver
- stream numbers supported WDK streaming minidriver
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting Multiple Streams


## <a href="" id="ddk-supporting-multiple-streams-ksg"></a>


The minidriver describes the streams it supports in its [*StrMiniReceiveDevicePacket*](https://msdn.microsoft.com/library/windows/hardware/ff568463) routine, in response to a SRB\_GET\_STREAM\_INFO request. The **CommandData.StreamBuffer** points to the [**HW\_STREAM\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff559686) structure the minidriver should fill in with a description of the streams it supports.

The HW\_STREAM\_DESCRIPTOR structure begins with a [**HW\_STREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff559690) structure, which describes the number of streams the minidriver supports. It is followed by an array of [**HW\_STREAM\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff559692) structures, each of which describes an individual stream. The class driver uses each HW\_STREAM\_INFORMATION to handle the [KSPROPSETID\_Pin](https://msdn.microsoft.com/library/windows/hardware/ff566584) property set − the index within the array serves as the pin type ID.

For most minidrivers, the data in the HW\_STREAM\_DESCRIPTOR is fixed at compile-time. In that case, the minidriver can allocate the data structure statically.

The minidriver describes the topology of connections between its streams through the Topology member of HW\_STREAM\_HEADER. The class drivers uses this structure to handle the [KSPROPSETID\_Topology](https://msdn.microsoft.com/library/windows/hardware/ff566598) property set for the minidriver.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Supporting%20Multiple%20Streams%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


