---
title: Describing Extended Sample Information in AVStream Codecs
author: windows-driver-content
description: Describing Extended Sample Information in AVStream Codecs
ms.assetid: 04447525-78f5-4c77-9a41-4e6e4729f729
keywords:
- AVStream hardware codec support WDK , extended sample information
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Describing Extended Sample Information in AVStream Codecs


Decoder filters can find extended sample information in the extended [**KSSTREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567138) structure [**KS\_FRAME\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567645), which follows KSSTREAM\_HEADER in memory.

The driver must propagate information specified in KSSTREAM\_HEADER.OptionsFlags from input (source) to output (destination) KS pins.

Encoders should include extended sample information in the extended KSSTREAM\_HEADER structure, KS\_FRAME\_INFO. Specifically, an encoder should update the member **dwFrameFlags** to indicate KS\_VIDEO\_FLAG\_I\_FRAME and KS\_VIDEO\_FLAG\_P\_FRAME, as applicable.

Surface stride is specified in KS\_FRAME\_INFO's lSurfacePitch member (union with **Reserved1** member). For more information about surface stride, see [Handling Stride in AVStream Codecs](handling-stride-in-avstream-codecs.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Describing%20Extended%20Sample%20Information%20in%20AVStream%20Codecs%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


