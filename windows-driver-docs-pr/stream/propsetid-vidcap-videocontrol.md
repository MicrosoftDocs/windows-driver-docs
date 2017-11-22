---
title: PROPSETID\_VIDCAP\_VIDEOCONTROL
description: PROPSETID\_VIDCAP\_VIDEOCONTROL
MS-HAID:
- 'vidcapprop\_f7bdca37-592e-4826-a67e-f02222524a17.xml'
- 'stream.propsetid\_vidcap\_videocontrol'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 892663c1-a807-4d03-9af0-f065149e7d42
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20PROPSETID_VIDCAP_VIDEOCONTROL%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




