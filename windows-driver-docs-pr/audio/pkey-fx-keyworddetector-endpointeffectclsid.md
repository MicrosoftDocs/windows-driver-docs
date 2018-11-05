---
title: PKEY\_FX\_KeywordDetector\_EndpointEffectClsid
description: In Windows 10 and later, the PKEY\_FX\_KeywordDetector\_EndpointEffectClsid property key identifies the keyword detector end point effect (EFX) in place.
ms.assetid: 2D776DB4-A317-4097-B188-65CA495D0F89
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PKEY\_FX\_KeywordDetector\_EndpointEffectClsid


In Windows 10 and later, the **PKEY\_FX\_KeywordDetector\_EndpointEffectClsid** property key identifies the keyword detector end point effect (EFX) in place. The driver developer should specify the single supported processing mode that their driver supports for the keyword detector pin.

The INF file property key instruct audio endpoint builder to set the CLSIDs for endpoint APOs into the effects property store. This information is used to build the audio graph that will be used to inform upper level apps what effects are in place.

## <span id="INF_File_Sample"></span><span id="inf_file_sample"></span><span id="INF_FILE_SAMPLE"></span>INF File Sample


An INF file specifies the default format for an audio endpoint device in the add-registry sections for that device. The following INF example shows the strings and add-registry section that loads the APO for an endpoint keyword detector effect into the registry.

```inf
[Strings]
PKEY_FX_KeywordDetector_EndpointEffectClsid = "{D04E05A6-594B-4fb6-A80D-01AF5EED7D1D},10"
...
; Driver developers should replace this CLSIDs with that of their own APO
FX_KEYWORD_ENDPOINT_CLSID               = "{00000000-0000-0000-0000-000000000000}"
...
[SWAPAPO.I.Association0.AddReg]
HKR,"FX\\0",%PKEY_FX_KeywordDetector_EndpointEffectClsid%,,%FX_KEYWORD_ENDPOINT_CLSID%
```

## <span id="related_topics"></span>Related topics


[Media-Class INF Extensions](media-class-inf-extensions.md)

 

 






