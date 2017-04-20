---
title: Multiple Data Streams on the same Hardware
author: windows-driver-content
description: Multiple Data Streams on the same Hardware
ms.assetid: 23133022-6d00-44ad-8c0d-24715204cacc
keywords:
- multiple data streams WDK DVD decoder
- stream numbers supported WDK DVD decoder
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Multiple Data Streams on the same Hardware


## <a href="" id="ddk-multiple-data-streams-on-the-same-hardware-ksg"></a>


Many decoders have several streams using the same piece of decoder hardware. For these devices, it is not necessary to perform key negotiation separately on each stream. To indicate this to the DVD decoder model, use the [**KS\_DVDCOPY\_SET\_COPY\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567639) property. When a get operation is issued on this property, a decoder may respond with either of the following:

KS\_DVDCOPYSTATE\_AUTHENTICATION\_NOT\_REQUIRED

KS\_DVDCOPYSTATE\_AUTHENTICATION\_REQUIRED

KS\_DVDCOPYSTATE\_AUTHENTICATION\_NOT\_REQUIRED indicates that the given stream does not require key negotiation because another stream on the same hardware has already performed it. For example, if the decoder receives the **Get** property on the audio stream first, it responds with **KS\_DVDCOPYSTATE\_AUTHENTICATION\_REQUIRED** on the audio stream and **KS\_DVDCOPYSTATE\_AUTHENTICATION\_NOT\_REQUIRED** on all other streams. After replying with AUTHENTICATION\_NOT\_REQUIRED, that stream does not receive any more key exchange properties until the next title key is negotiated. At that point, the decoder may again choose to reply with AUTHENTICATION\_NOT\_REQUIRED.

To allow for other applications besides DVD playback ones, in the case where a decoder needs to perform copyright protection on only one stream, the decoder performs negotiation on the first stream to receive a **Get** property call for **KS\_DVDCOPY\_SET\_COPY\_STATE** after stream opening. Do not hardcode the copyright protection properties to work with only one stream.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Multiple%20Data%20Streams%20on%20the%20same%20Hardware%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


