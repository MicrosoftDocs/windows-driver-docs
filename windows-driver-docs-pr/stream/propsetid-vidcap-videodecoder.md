---
title: PROPSETID\_VIDCAP\_VIDEODECODER
description: PROPSETID\_VIDCAP\_VIDEODECODER
ms.assetid: 86b581b7-51fd-4662-8291-4c5baf9d3b16
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20PROPSETID_VIDCAP_VIDEODECODER%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




