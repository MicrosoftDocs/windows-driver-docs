---
title: KSPROPSETID\_AudioDecoderOut
description: KSPROPSETID\_AudioDecoderOut
MS-HAID:
- 'dvdref\_48d192e5-9de4-494d-ac84-55aea2feef95.xml'
- 'stream.kspropsetid\_audiodecoderout'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 80292a43-305f-4c3c-aab1-e38f2eb749d1
---

# KSPROPSETID\_AudioDecoderOut


## <span id="ddk_kspropsetid_audiodecoderout_ks"></span><span id="DDK_KSPROPSETID_AUDIODECODEROUT_KS"></span>


The KSPROPSETID\_AudioDecoderOut property set defines properties to specify the forms of audio output that are available from the DVD decoder.

The KSPROPERTY\_AUDDECOUT enumeration in *Ksmedia.h* specifies the properties of this set.

DVD decoder minidrivers should implement support for the following audio stream properties:

[**KSPROPERTY\_AUDDECOUT\_MODES**](ksproperty-auddecout-modes.md)

[**KSPROPERTY\_AUDDECOUT\_CUR\_MODE**](ksproperty-auddecout-cur-mode.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPSETID_AudioDecoderOut%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




