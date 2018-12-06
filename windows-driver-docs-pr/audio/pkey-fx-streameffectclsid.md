---
title: PKEY\_FX\_StreamEffectClsid
description: In Windows 8.1 and later, the PKEY\_FX\_StreamEffectClsid property key identifies the stream effect (SFX) supported by the driver. The driver developer should specify the list of supported stream effects that their driver supports.
ms.assetid: 8557AE39-56DF-4184-A74A-186AF30F2A63
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PKEY\_FX\_StreamEffectClsid


In Windows 8.1 and later, the **PKEY\_FX\_StreamEffectClsid** property key identifies the stream effect (SFX) supported by the driver. The driver developer should specify the list of supported stream effects that their driver supports.

The INF file property key instructs the audio endpoint builder to set the CLSIDs for endpoint APOs into the effects property store. This information is used to build the audio graph that will be used to inform upper level apps what effects are in place.

## <span id="INF_File_Sample"></span><span id="inf_file_sample"></span><span id="INF_FILE_SAMPLE"></span>INF File Sample


An INF file specifies settings for an audio endpoint device in the add-registry section for that device. The following INF example shows the strings and add-registry sections that loads the APO for a stream effect into the registry.

```inf
[Strings]
PKEY_FX_StreamEffectClsid   = "{D04E05A6-594B-4fb6-A80D-01AF5EED7D1D},5"
...
; Driver developers should replace this CLSIDs with that of their own APO
FX_STREAM_CLSID      = "{00000000-0000-0000-0000-000000000000}"
...
[SWAPAPO.AddReg]
HKR,"FX\\0",%PKEY_FX_StreamEffectClsid%,,%FX_STREAM_CLSID%
```

## <span id="related_topics"></span>Related topics


[Media-Class INF Extensions](media-class-inf-extensions.md)

 

 






