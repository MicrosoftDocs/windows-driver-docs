---
title: Supporting Property Sets
author: windows-driver-content
description: Supporting Property Sets
ms.assetid: 49a3e3e6-3a09-4202-a2cb-df65806d3336
keywords:
- Stream.sys class driver WDK Windows 2000 Kernel , property sets
- streaming minidrivers WDK Windows 2000 Kernel , property sets
- minidrivers WDK Windows 2000 Kernel Streaming , property sets
- property sets WDK streaming minidriver
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting Property Sets


## <a href="" id="ddk-supporting-property-sets-ksg"></a>


Both the minidriver as a whole and individual streams can receive property requests. The minidriver supplies the property sets it supports in the **DevicePropertiesArray** of [**HW\_STREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff559690). Each stream supplies the property sets it supports in the **StreamPropertiesArray** of the [**HW\_STREAM\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff559692) structure for that stream.

The minidriver defines a property set it handles through the [**KSPROPERTY\_SET**](https://msdn.microsoft.com/library/windows/hardware/ff565617) data structure, which in turn points to the array of [**KSPROPERTY\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff565176) structures, one for each property in the property set. If the **GetSupported** member of KSPROPERTY\_ITEM is **TRUE**, the minidriver supports getting the property data. If the **SetSupported** member of KSPROPERTY\_ITEM is **TRUE**, the minidriver supports setting the property data.

Most property support requests are handled automatically by the class driver, using information the minidriver provides in the KSPROPERTY\_ITEM structure for the property. For example, if the class driver receives a KSPROPERTY\_TYPE\_BASICSUPPORT request, it looks up the data type and value ranges in the **Values** member of KSPROPERTY\_ITEM. See [**KSPROPERTY\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff565176) for details. If the minidriver needs to perform custom processing of a support request (which is rare), it may set the **SupportHandler** member of KSPROPERTY\_ITEM to **TRUE**. The class driver then handles the support request as if it were a property get request. The minidriver can determine the actual type of the request from the **Flags** member of the property identifier.

The class driver gets or sets minidriver properties by passing a [**SRB\_GET\_DEVICE\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff568170) or [**SRB\_SET\_DEVICE\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff568204) request to the minidriver's [*StrMiniReceiveDevicePacket*](https://msdn.microsoft.com/library/windows/hardware/ff568463) routine. The class driver gets or sets stream properties by passing a SRB\_GET\_STREAM\_PROPERTY or SRB\_SET\_STREAM\_PROPERTY request to the stream's **StrMiniReceiveStreamControlPacket** routine.

The class driver handles many properties on behalf of the minidriver, with an occasional assist from the minidriver through one of the minidriver's callbacks. The minidriver does not define these properties in its property set arrays. For an explanation of how the class driver handles the [KSPROPSETID\_Pin](https://msdn.microsoft.com/library/windows/hardware/ff566584) and [KSPROPSETID\_Topology](https://msdn.microsoft.com/library/windows/hardware/ff566598) property sets, see [Supporting Multiple Streams](supporting-multiple-streams.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Supporting%20Property%20Sets%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


