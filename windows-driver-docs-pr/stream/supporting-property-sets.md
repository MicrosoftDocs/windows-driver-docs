---
title: Supporting Property Sets
description: Supporting Property Sets
keywords:
- Stream.sys class driver WDK Windows 2000 Kernel , property sets
- streaming minidrivers WDK Windows 2000 Kernel , property sets
- minidrivers WDK Windows 2000 Kernel Streaming , property sets
- property sets WDK streaming minidriver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Property Sets





Both the minidriver as a whole and individual streams can receive property requests. The minidriver supplies the property sets it supports in the **DevicePropertiesArray** of [**HW\_STREAM\_HEADER**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_stream_header). Each stream supplies the property sets it supports in the **StreamPropertiesArray** of the [**HW\_STREAM\_INFORMATION**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_stream_information) structure for that stream.

The minidriver defines a property set it handles through the [**KSPROPERTY\_SET**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_set) data structure, which in turn points to the array of [**KSPROPERTY\_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_item) structures, one for each property in the property set. If the **GetSupported** member of KSPROPERTY\_ITEM is **TRUE**, the minidriver supports getting the property data. If the **SetSupported** member of KSPROPERTY\_ITEM is **TRUE**, the minidriver supports setting the property data.

Most property support requests are handled automatically by the class driver, using information the minidriver provides in the KSPROPERTY\_ITEM structure for the property. For example, if the class driver receives a KSPROPERTY\_TYPE\_BASICSUPPORT request, it looks up the data type and value ranges in the **Values** member of KSPROPERTY\_ITEM. See [**KSPROPERTY\_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_item) for details. If the minidriver needs to perform custom processing of a support request (which is rare), it may set the **SupportHandler** member of KSPROPERTY\_ITEM to **TRUE**. The class driver then handles the support request as if it were a property get request. The minidriver can determine the actual type of the request from the **Flags** member of the property identifier.

The class driver gets or sets minidriver properties by passing a [**SRB\_GET\_DEVICE\_PROPERTY**](./srb-get-device-property.md) or [**SRB\_SET\_DEVICE\_PROPERTY**](./srb-set-device-property.md) request to the minidriver's [*StrMiniReceiveDevicePacket*](/windows-hardware/drivers/ddi/strmini/nc-strmini-phw_receive_device_srb) routine. The class driver gets or sets stream properties by passing a SRB\_GET\_STREAM\_PROPERTY or SRB\_SET\_STREAM\_PROPERTY request to the stream's **StrMiniReceiveStreamControlPacket** routine.

The class driver handles many properties on behalf of the minidriver, with an occasional assist from the minidriver through one of the minidriver's callbacks. The minidriver does not define these properties in its property set arrays. For an explanation of how the class driver handles the [KSPROPSETID\_Pin](./kspropsetid-pin.md) and [KSPROPSETID\_Topology](./kspropsetid-topology.md) property sets, see [Supporting Multiple Streams](supporting-multiple-streams.md).

 

