---
title: PKEY\_CompositeFX\_EndpointEffectClsid
description: In Windows 10 Version 1803 and later, the PKEY\_CompositeFX\_EndpointEffectClsid property key identifies the end point effect (EFX) in place. 
ms.date: 11/15/2018
---

# PKEY\_CompositeFX\_EndpointEffectClsid

In Windows release 1803 and later, the **PKEY\_CompositeFX\_EndpointEffectClsid** property key identifies the end point effects (EFX) in place. The driver developer should specify the list of supported processing modes that their driver supports.

This property key is identical to the [PKEY\_FX\_EndpointEffectClsid](pkey-fx-endpointeffectclsid.md) property key, but it is a composite that is expressed as a reg multistring in the registry to allow multiple effects in a single position.

The INF file property key instruct audio endpoint builder to set the CLSIDs for endpoint APOs into the effects property store. This information is used to build the audio graph that will be used to inform upper level apps what effects are in place.

## <span id="INF_File_Sample"></span><span id="inf_file_sample"></span><span id="INF_FILE_SAMPLE"></span>INF File Sample

An INF file specifies the default format for an audio endpoint device in the add-registry sections for that device. The following INF example shows the strings and add-registry section that loads the APO for endpoint effects into the registry.

```inf
[Strings]
PKEY_CompositeFX_EndpointEffectClsid = "{D04E05A6-594B-4fb6-A80D-01AF5EED7D1D},15"
...

SWAP_FX_MODE_CLSID      = "{00000000-0000-0000-0000-000000000000}"
DELAY_FX_STREAM_CLSID   = "{00000000-0000-0000-0000-000000000000}"
...
 
[SWAPAPO.I.Association0.AddReg]
HKR,FX\0,%PKEY_CompositeFX_EndpointEffectClsid%,0x00010000,%SWAP_FX_MODE_CLSID%,%DELAY_FX_MODE_CLSID%

```


## <span id="related_topics"></span>Related topics

[Media-Class INF Extensions](media-class-inf-extensions.md)

 

 






