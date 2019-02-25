---
title: PROPSETID\_VIDCAP\_TVAUDIO
description: PROPSETID\_VIDCAP\_TVAUDIO
ms.assetid: 33c76f30-2e4b-48b7-a463-f6363419dca3
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





