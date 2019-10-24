---
title: Supporting Multiple Streams
description: Supporting Multiple Streams
ms.assetid: 89f79078-129a-44cc-8b7e-5f5c1c33a473
keywords:
- Stream.sys class driver WDK Windows 2000 Kernel , multiple streams
- streaming minidrivers WDK Windows 2000 Kernel , multiple streams
- minidrivers WDK Windows 2000 Kernel Streaming , multiple streams
- multiple streams WDK streaming minidriver
- stream numbers supported WDK streaming minidriver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Multiple Streams





The minidriver describes the streams it supports in its [*StrMiniReceiveDevicePacket*](https://docs.microsoft.com/windows-hardware/drivers/ddi/strmini/nc-strmini-phw_receive_device_srb) routine, in response to a SRB\_GET\_STREAM\_INFO request. The **CommandData.StreamBuffer** points to the [**HW\_STREAM\_DESCRIPTOR**](https://docs.microsoft.com/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_stream_descriptor) structure the minidriver should fill in with a description of the streams it supports.

The HW\_STREAM\_DESCRIPTOR structure begins with a [**HW\_STREAM\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_stream_header) structure, which describes the number of streams the minidriver supports. It is followed by an array of [**HW\_STREAM\_INFORMATION**](https://docs.microsoft.com/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_stream_information) structures, each of which describes an individual stream. The class driver uses each HW\_STREAM\_INFORMATION to handle the [KSPROPSETID\_Pin](https://docs.microsoft.com/windows-hardware/drivers/stream/kspropsetid-pin) property set − the index within the array serves as the pin type ID.

For most minidrivers, the data in the HW\_STREAM\_DESCRIPTOR is fixed at compile-time. In that case, the minidriver can allocate the data structure statically.

The minidriver describes the topology of connections between its streams through the Topology member of HW\_STREAM\_HEADER. The class drivers uses this structure to handle the [KSPROPSETID\_Topology](https://docs.microsoft.com/windows-hardware/drivers/stream/kspropsetid-topology) property set for the minidriver.

 

 




