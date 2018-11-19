---
title: KSPROPSETID\_AC3
description: KSPROPSETID\_AC3
ms.assetid: 172d8ed8-2dd3-438d-8dc6-f4f1bb128811
keywords: ["KSPROPSETID_AC3"]
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_AC3


## <span id="ddk_kspropsetid_ac3_ks"></span><span id="DDK_KSPROPSETID_AC3_KS"></span>


The `KSPROPSETID_AC3` property set exposes the AC-3 decoding and encoding capabilities of an audio device driver.

An audio driver that supports the AC-3 format can expose a wide range of properties for controlling the features of an AC-3 decoder/encoder. In addition, the properties of a stream can be queried to determine characteristics of the AC-3-encoded audio.

When the audio hardware does not support a particular capability, the driver for that hardware should fail the get- and set-property calls in order to inform the upper-layer driver that it must find another way to perform the specified function. For example, the driver for a decoder that does not support dynamic range compression should fail calls for that capability so that the upper layer will know that it needs to insert a compressor into the stream following the AC-3 decoder.

For information about AC-3 compression, see the AC-3 specification at the [Dolby Laboratories](https://go.microsoft.com/fwlink/p/?linkid=8730) website. The specification is titled *Digital Audio Compression Standard (AC-3)*.

The property items in this set are specified by KSPROPERTY\_AC3 enumeration values.

The KSPROPSETID\_AC3 property set contains the following properties:

[**KSPROPERTY\_AC3\_ALTERNATE\_AUDIO**](ksproperty-ac3-alternate-audio.md)

[**KSPROPERTY\_AC3\_BIT\_STREAM\_MODE**](ksproperty-ac3-bit-stream-mode.md)

[**KSPROPERTY\_AC3\_DIALOGUE\_LEVEL**](ksproperty-ac3-dialogue-level.md)

[**KSPROPERTY\_AC3\_DOWNMIX**](ksproperty-ac3-downmix.md)

[**KSPROPERTY\_AC3\_ERROR\_CONCEALMENT**](ksproperty-ac3-error-concealment.md)

[**KSPROPERTY\_AC3\_LANGUAGE\_CODE**](ksproperty-ac3-language-code.md)

[**KSPROPERTY\_AC3\_ROOM\_TYPE**](ksproperty-ac3-room-type.md)

 

 





