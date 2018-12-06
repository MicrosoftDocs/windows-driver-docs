---
title: PKEY\_FX\_Offload\_StreamEffectClsid
description: In Windows 10, version 1511 and later, the PKEY\_FX\_Offload\_StreamEffectClsid property key identifies the stream effect (SFX) supported by the driver that will be loaded during offload playback.
ms.assetid: 2258E1F8-A96E-4991-B882-00197C2DB0B3
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PKEY\_FX\_Offload\_StreamEffectClsid


In Windows 10, version 1511 and later, the **PKEY\_FX\_Offload\_StreamEffectClsid** property key identifies the stream effect (SFX) supported by the driver that will be loaded during offload playback. The driver developer should specify the list of supported stream effects that their driver supports for the offload pin.

The INF file property key instructs the audio endpoint builder to set the CLSIDs for stream-effect APOs into the effects property store for offload. This information is used to build the audio graph that will be used to inform upper level apps what effects are in place.

## <span id="INF_File_Sample"></span><span id="inf_file_sample"></span><span id="INF_FILE_SAMPLE"></span>INF File Sample


An INF file specifies settings for an audio processing mode effect in the add-registry section for that device. The following INF example shows the strings and add-registry sections that loads the streaming processing modes supported into the registry.

```inf
[Strings]
PKEY_FX_Offload_StreamEffectClsid   = "{D04E05A6-594B-4fb6-A80D-01AF5EED7D1D},11"
...
; Driver developers should replace this CLSIDs with that of their own APO
FX_STREAM_CLSID      = "{00000000-0000-0000-0000-000000000000}"
...
[SWAPAPO.AddReg]
HKR,"FX\\0",% PKEY_FX_Offload_StreamEffectClsid %,,%FX_STREAM_CLSID%
```

## <span id="related_topics"></span>Related topics


[Media-Class INF Extensions](media-class-inf-extensions.md)










