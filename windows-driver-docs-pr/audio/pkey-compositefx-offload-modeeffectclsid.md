---
title: PKEY\_CompositeFX\_Offload\_ModeEffectClsid
description: In Windows 10, version 1803 and later, the PKEY\_CompositeFX\_Offload\_ModeEffectClsid key identifies the mode effect (MFX) supported by the driver that will be loaded during offload playback.
ms.date: 03/06/2023
ms.topic: reference
---

# PKEY\_CompositeFX\_Offload\_ModeEffectClsid


In Windows 10, version 1803 and later, the **PKEY\_CompositeFX\_Offload\_ModeEffectClsid** key identifies the mode effect (MFX) supported by the driver that will be loaded during offload playback. The driver developer should specify the list of supported processing modes that their driver supports.

This property key is identical to the [PKEY\_FX\_Offload\_ModeEffectClsid](pkey-fx-offload-modeeffectclsid.md) property key, but it is a composite that is expressed as a reg multistring in the registry to allow multiple effects in a single position.

The INF file property key instructs the audio endpoint builder to set the CLSIDs for mode APOs into the effects property store. This information is used to build the audio graph that will be used to inform upper level apps what effects are in place.

## <span id="INF_File_Sample"></span><span id="inf_file_sample"></span><span id="INF_FILE_SAMPLE"></span>INF File Sample


An INF file specifies settings for an audio processing mode effect in the add-registry section for that device. The following INF example shows the strings and add-registry sections that loads the loads the APO for a mode effect to be used during offload playback into the registry.

```inf
[Strings]
PKEY_CompositeFX_Offload_ModeEffectClsid     = "{D04E05A6-594B-4fb6-A80D-01AF5EED7D1D},20"
...
; Driver developers should replace this CLSIDs with that of their own APO
SWAP_FX_MODE_CLSID      = "{00000000-0000-0000-0000-000000000000}"
DELAY_FX_STREAM_CLSID   = "{00000000-0000-0000-0000-000000000000}"
...
 
[SWAPAPO.I.Association0.AddReg]
HKR,FX\0,%PKEY_CompositeFX_Offload_ModeEffectClsid%,0x00010000,%SWAP_FX_MODE_CLSID%,%DELAY_FX_MODE_CLSID%

```

## Related topics


[Media-Class INF Extensions](media-class-inf-extensions.md)

 

 






