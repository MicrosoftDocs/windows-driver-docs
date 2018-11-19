---
title: PROPSETID\_VIDCAP\_VIDEOCOMPRESSION
description: PROPSETID\_VIDCAP\_VIDEOCOMPRESSION
ms.assetid: 7af6f7f0-d446-4b44-9423-efd37f731e0b
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PROPSETID\_VIDCAP\_VIDEOCOMPRESSION


## <span id="ddk_propsetid_vidcap_videocompression_ks"></span><span id="DDK_PROPSETID_VIDCAP_VIDEOCOMPRESSION_KS"></span>


The PROPSETID\_VIDCAP\_VIDEOCOMPRESSION property set controls the video compression settings of a device.

The KSPROPERTY\_VIDCAP\_VIDEOCOMPRESSION enumeration in *ksmedia.h* specifies the properties of this set.

Support for this property set is optional and should be implemented only by devices that implement a video compression codec.

Video capture minidrivers are required to implement the following properties:

[**KSPROPERTY\_VIDEOCOMPRESSION\_GETINFO**](ksproperty-videocompression-getinfo.md)

[**KSPROPERTY\_VIDEOCOMPRESSION\_KEYFRAME\_RATE**](ksproperty-videocompression-keyframe-rate.md)

[**KSPROPERTY\_VIDEOCOMPRESSION\_OVERRIDE\_FRAME\_SIZE**](ksproperty-videocompression-override-frame-size.md)

[**KSPROPERTY\_VIDEOCOMPRESSION\_OVERRIDE\_KEYFRAME**](ksproperty-videocompression-override-keyframe.md)

[**KSPROPERTY\_VIDEOCOMPRESSION\_PFRAMES\_PER\_KEYFRAME**](ksproperty-videocompression-pframes-per-keyframe.md)

[**KSPROPERTY\_VIDEOCOMPRESSION\_QUALITY**](ksproperty-videocompression-quality.md)

[**KSPROPERTY\_VIDEOCOMPRESSION\_WINDOWSIZE**](ksproperty-videocompression-windowsize.md)

### <span id="directshow_interface"></span><span id="DIRECTSHOW_INTERFACE"></span>DirectShow Interface

The DirectShow **IAMVideoCompression** interface (see the DirectShow documentation in the Microsoft Windows SDK) provides access to the properties of this set.

 

 





