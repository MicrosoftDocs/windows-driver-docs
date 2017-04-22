---
title: DVD Regionalization
author: windows-driver-content
description: DVD Regionalization
ms.assetid: 931441c8-9521-43c9-86f1-dbf75d36e190
keywords:
- DVD decoder minidrivers WDK
- regionalization WDK DVD decoder
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DVD Regionalization


## <a href="" id="ddk-dvd-regionalization-ksg"></a>


The DVD decoder minidriver should not be involved in any part of the regionalization process. Other parts of the streaming architecture enforce regionalization. Under most circumstances, the decoder minidriver does not implement the [**KS\_DVDCOPY\_REGION**](https://msdn.microsoft.com/library/windows/hardware/ff567638) property.

If the decoder is limited to a certain region (by hardware or other considerations), then it may respond to the **KS\_DVDCOPY\_REGION** property to override all other system regions. The DVD decoder minidriver should set exactly one bit corresponding to the region that the decoder is designated for. Note that the logic is *inverted* from the region coding on the media. For example, a decoder designed to work only in Region 1 (USA) returns 0x01 to the **KS\_DVDCOPY\_REGION** property.

If the decoder provides a region, the system region change application still functions. It changes the system region in case there are other decoders in the system. Note that Windows DVD playback only functions if the system region and the decoder region match.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20DVD%20Regionalization%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


