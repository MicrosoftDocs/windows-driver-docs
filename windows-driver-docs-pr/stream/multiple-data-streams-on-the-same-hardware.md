---
title: Multiple Data Streams on the same Hardware
description: Multiple Data Streams on the same Hardware
ms.assetid: 23133022-6d00-44ad-8c0d-24715204cacc
keywords:
- multiple data streams WDK DVD decoder
- stream numbers supported WDK DVD decoder
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Multiple Data Streams on the same Hardware





Many decoders have several streams using the same piece of decoder hardware. For these devices, it is not necessary to perform key negotiation separately on each stream. To indicate this to the DVD decoder model, use the [**KS\_DVDCOPY\_SET\_COPY\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567639) property. When a get operation is issued on this property, a decoder may respond with either of the following:

KS\_DVDCOPYSTATE\_AUTHENTICATION\_NOT\_REQUIRED

KS\_DVDCOPYSTATE\_AUTHENTICATION\_REQUIRED

KS\_DVDCOPYSTATE\_AUTHENTICATION\_NOT\_REQUIRED indicates that the given stream does not require key negotiation because another stream on the same hardware has already performed it. For example, if the decoder receives the **Get** property on the audio stream first, it responds with **KS\_DVDCOPYSTATE\_AUTHENTICATION\_REQUIRED** on the audio stream and **KS\_DVDCOPYSTATE\_AUTHENTICATION\_NOT\_REQUIRED** on all other streams. After replying with AUTHENTICATION\_NOT\_REQUIRED, that stream does not receive any more key exchange properties until the next title key is negotiated. At that point, the decoder may again choose to reply with AUTHENTICATION\_NOT\_REQUIRED.

To allow for other applications besides DVD playback ones, in the case where a decoder needs to perform copyright protection on only one stream, the decoder performs negotiation on the first stream to receive a **Get** property call for **KS\_DVDCOPY\_SET\_COPY\_STATE** after stream opening. Do not hardcode the copyright protection properties to work with only one stream.

 

 




