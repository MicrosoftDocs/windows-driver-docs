---
title: PROPSETID\_VIDCAP\_VIDEOCONTROL
description: PROPSETID\_VIDCAP\_VIDEOCONTROL
ms.assetid: 892663c1-a807-4d03-9af0-f065149e7d42
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PROPSETID\_VIDCAP\_VIDEOCONTROL


## <span id="ddk_propsetid_vidcap_videocontrol_ks"></span><span id="DDK_PROPSETID_VIDCAP_VIDEOCONTROL_KS"></span>


The PROPOSETID\_VIDCAP\_VIDEOCONTROL property set controls supplemental aspects of video capture operations such as enumerating available frame rates and image orientation. Generally, analog digitizers can support any frame rate request that USB and 1394 conferencing cameras support, but with a limited set of frame rates.

The KSPROPERTY\_VIDCAP\_VIDEOCONTROL enumeration in *ksmedia.h* specifies the properties of this set.

Support for this property set is optional and should be implemented only by minidrivers of devices that cannot capture video at arbitrary frame rates.

Video capture minidrivers are required to implement the following properties:

[**KSPROPERTY\_VIDEOCONTROL\_CAPS**](ksproperty-videocontrol-caps.md)

Video capture minidrivers may optionally implement the following properties:

[**KSPROPERTY\_VIDEOCONTROL\_ACTUAL\_FRAME\_RATE**](ksproperty-videocontrol-actual-frame-rate.md)

[**KSPROPERTY\_VIDEOCONTROL\_FRAME\_RATES**](ksproperty-videocontrol-frame-rates.md)

[**KSPROPERTY\_VIDEOCONTROL\_MODE**](ksproperty-videocontrol-mode.md)

### <span id="directshow_interface"></span><span id="DIRECTSHOW_INTERFACE"></span>DirectShow Interface

There is no DirectShow interface that provides access to this property set.

 

 





