---
title: PROPSETID\_VIDCAP\_VIDEODECODER
description: PROPSETID\_VIDCAP\_VIDEODECODER
ms.assetid: 86b581b7-51fd-4662-8291-4c5baf9d3b16
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PROPSETID\_VIDCAP\_VIDEODECODER


## <span id="ddk_propsetid_vidcap_videodecoder_ks"></span><span id="DDK_PROPSETID_VIDCAP_VIDEODECODER_KS"></span>


The PROPSETID\_VIDCAP\_VIDEODECODER property set controls analog video decoder devices. An analog video decoder converts baseband analog video signals into a digital format such as RGB or YUV.

The KSPROPERTY\_VIDCAP\_VIDEODECODER enumeration in *ksmedia.h* specifies the properties of this set.

Support for this property set is optional and should be implemented only by analog video capture devices.

Video capture minidrivers are required to implement the following properties:

[**KSPROPERTY\_VIDEODECODER\_CAPS**](ksproperty-videodecoder-caps.md)

[**KSPROPERTY\_VIDEODECODER\_STANDARD**](ksproperty-videodecoder-standard.md)

[**KSPROPERTY\_VIDEODECODER\_STATUS**](ksproperty-videodecoder-status.md)

Video capture minidrivers may optionally implement the following properties:

[**KSPROPERTY\_VIDEODECODER\_OUTPUT\_ENABLE**](ksproperty-videodecoder-output-enable.md)

[**KSPROPERTY\_VIDEODECODER\_VCR\_TIMING**](ksproperty-videodecoder-vcr-timing.md)

### <span id="directshow_interface"></span><span id="DIRECTSHOW_INTERFACE"></span>DirectShow Interface

The DirectShow **IAMAnalogVideoDecoder** interface (see the DirectShow documentation in the Microsoft Windows SDK) provides access to the properties of this set.

 

 





