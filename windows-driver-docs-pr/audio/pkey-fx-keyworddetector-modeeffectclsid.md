---
title: PKEY\_FX\_KeywordDetector\_ModeEffectClsid
description: In Windows 10 and later, the PKEY\_FX\_KeywordDetector\_ModeEffectClsid property key identifies the mode effect (MFX) supported by the driver for the keyword detector pin.
ms.assetid: 67030999-0658-4880-9CC8-A25496DE584E
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PKEY\_FX\_KeywordDetector\_ModeEffectClsid


In Windows 10 and later, the **PKEY\_FX\_KeywordDetector\_ModeEffectClsid** property key identifies the mode effect (MFX) supported by the driver for the keyword detector pin. The driver developer should specify the single supported processing mode that their driver supports for the keyword detector pin.

The INF file property key instructs the audio endpoint builder to set the CLSIDs for endpoint APOs into the effects property store. This information is used to build the audio graph that will be used to inform upper level apps what effects are in place.

## <span id="INF_File_Sample"></span><span id="inf_file_sample"></span><span id="INF_FILE_SAMPLE"></span>INF File Sample


An INF file specifies settings for an audio mode effect in the add-registry section for that device. The following INF example shows the strings and add-registry section that loads the APO for a keyword detector mode effect into the registry.

```inf
[Strings]
PKEY_FX_KeywordDetector_ModeEffectClsid     = "{D04E05A6-594B-4fb6-A80D-01AF5EED7D1D},9"
...
; Driver developers should replace this CLSIDs with that of their own APO
FX_KEYWORD_MODE_CLSID      = "{00000000-0000-0000-0000-000000000000}"
...
[SWAPAPO.I.Association0.AddReg]
HKR,"FX\\0",%PKEY_FX_KeywordDetector_ModeEffectClsid%,,%FX_KEYWORD_MODE_CLSID%
```

## <span id="related_topics"></span>Related topics


[Media-Class INF Extensions](media-class-inf-extensions.md)

 

 






