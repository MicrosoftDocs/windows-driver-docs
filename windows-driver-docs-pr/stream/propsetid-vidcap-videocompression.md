---
title: PROPSETID\_VIDCAP\_VIDEOCOMPRESSION
description: PROPSETID\_VIDCAP\_VIDEOCOMPRESSION
MS-HAID:
- 'vidcapprop\_ffe19cd7-ef63-4b73-b474-9b40dbdf60f1.xml'
- 'stream.propsetid\_vidcap\_videocompression'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 7af6f7f0-d446-4b44-9423-efd37f731e0b
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20PROPSETID_VIDCAP_VIDEOCOMPRESSION%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




