---
title: PKEY\_FX\_EndpointEffectClsid
description: In Windows 8.1 and later, the PKEY\_FX\_EndpointEffectClsid property key identifies the end point effect (EFX) in place. The driver developer should specify the list of supported processing modes that their driver supports.
ms.date: 03/06/2023
ms.topic: reference
---


# PKEY\_FX\_EndpointEffectClsid


In Windows 8.1 and later, the **PKEY\_FX\_EndpointEffectClsid** property key identifies the end point effect (EFX) in place. The driver developer should specify the list of supported processing modes that their driver supports.

The INF file property key instruct audio endpoint builder to set the CLSIDs for endpoint APOs into the effects property store. This information is used to build the audio graph that will be used to inform upper level apps what effects are in place.

## <span id="INF_File_Sample"></span><span id="inf_file_sample"></span><span id="INF_FILE_SAMPLE"></span>INF File Sample


An INF file specifies the default format for an audio endpoint device in the add-registry sections for that device. The following INF example shows the strings and add-registry section that loads the APO for an endpoint effect into the registry.

```inf
[Strings]
PKEY_FX_EndpointEffectClsid = "{D04E05A6-594B-4fb6-A80D-01AF5EED7D1D},7"
...
; Driver developers should replace this CLSIDs with that of their own APO
FX_ENDPOINT_CLSID               = "{00000000-0000-0000-0000-000000000000}"
...
[SWAPAPO.I.Association0.AddReg]
HKR,"FX\\0",%PKEY_FX_EndpointEffectClsid%,,%FX_ENDPOINT_CLSID%
```

## Related topics


[Media-Class INF Extensions](media-class-inf-extensions.md)

 

 






