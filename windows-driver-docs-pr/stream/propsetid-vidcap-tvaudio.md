---
title: PROPSETID\_VIDCAP\_TVAUDIO
description: PROPSETID\_VIDCAP\_TVAUDIO
MS-HAID:
- 'vidcapprop\_0e85e696-b0d5-4ba9-a6a2-a8c8759f725e.xml'
- 'stream.propsetid\_vidcap\_tvaudio'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 33c76f30-2e4b-48b7-a463-f6363419dca3
---

# PROPSETID\_VIDCAP\_TVAUDIO


## <span id="ddk_propsetid_vidcap_tvaudio_ks"></span><span id="DDK_PROPSETID_VIDCAP_TVAUDIO_KS"></span>


The PROPSETID\_VIDCAP\_TVAUDIO property set controls settings that are unique to the audio that is associated with television sources. This includes secondary audio program (SAP), and stereo or mono selection. These controls are generally found on devices external to the system audio mixer.

The KSPROPERTY\_VIDCAP\_TVAUDIO enumeration in *ksmedia.h* specifies the properties of this set.

Support for this property set is optional and should be implemented only by minidrivers of devices that support TV audio.

TV audio capture minidrivers are required to implement the following properties:

[**KSPROPERTY\_TVAUDIO\_CAPS**](ksproperty-tvaudio-caps.md)

[**KSPROPERTY\_TVAUDIO\_CURRENTLY\_AVAILABLE\_MODES**](ksproperty-tvaudio-currently-available-modes.md)

[**KSPROPERTY\_TVAUDIO\_MODE**](ksproperty-tvaudio-mode.md)

### <span id="directshow_interface"></span><span id="DIRECTSHOW_INTERFACE"></span>DirectShow Interface

The DirectShow **IAMTVAudio** interface (see the DirectShow documentation in the Microsoft Windows SDK) provides access to the properties of this set.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20PROPSETID_VIDCAP_TVAUDIO%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




