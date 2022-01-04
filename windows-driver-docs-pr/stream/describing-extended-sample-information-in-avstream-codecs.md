---
title: Describing Extended Sample Information in AVStream Codecs
description: Describing Extended Sample Information in AVStream Codecs
keywords:
- AVStream hardware codec support WDK , extended sample information
ms.date: 04/20/2017
---

# Describing Extended Sample Information in AVStream Codecs


Decoder filters can find extended sample information in the extended [**KSSTREAM\_HEADER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksstream_header) structure [**KS\_FRAME\_INFO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_frame_info), which follows KSSTREAM\_HEADER in memory.

The driver must propagate information specified in KSSTREAM\_HEADER.OptionsFlags from input (source) to output (destination) KS pins.

Encoders should include extended sample information in the extended KSSTREAM\_HEADER structure, KS\_FRAME\_INFO. Specifically, an encoder should update the member **dwFrameFlags** to indicate KS\_VIDEO\_FLAG\_I\_FRAME and KS\_VIDEO\_FLAG\_P\_FRAME, as applicable.

Surface stride is specified in KS\_FRAME\_INFO's lSurfacePitch member (union with **Reserved1** member). For more information about surface stride, see [Handling Stride in AVStream Codecs](handling-stride-in-avstream-codecs.md).

 

