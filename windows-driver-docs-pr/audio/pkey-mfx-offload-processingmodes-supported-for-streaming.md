---
title: PKEY\_MFX\_Offload\_ProcessingModes\_Supported\_For\_Streaming
description: In Windows 10, version 1511 and later, the PKEY\_MFX\_Offload\_ProcessingModes\_Supported\_For\_Streaming property key identifies the mode effect processing modes supported for offload streaming supported by the driver.
ms.assetid: 48E12E69-5159-4483-9891-2B689B7C3DCE
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PKEY\_MFX\_Offload\_ProcessingModes\_Supported\_For\_Streaming


In Windows 10, version 1511 and later, the **PKEY\_MFX\_Offload\_ProcessingModes\_Supported\_For\_Streaming** property key identifies the mode effect processing modes supported for offload streaming supported by the driver. The driver developer should list the mode effect processing modes supported for offloaded streaming that their driver supports.

The INF file property key instructs the audio endpoint builder to set the CLSIDs for APOs into the effects property store. This information is used to build the audio graph that will be used to inform upper level apps what effects are in place.

## <span id="INF_File_Sample"></span><span id="inf_file_sample"></span><span id="INF_FILE_SAMPLE"></span>INF File Sample


An INF file specifies settings for an audio processing mode effect in the add-registry section for that device. The following INF example shows the strings and add-registry sections that loads the offload streaming processing modes supported into the registry.

```inf
[Strings]
PKEY_MFX_Offload_ProcessingModes_Supported_For_Streaming = "{D3993A3F-99C2-4402-B5EC-A92A0367664B},12"
...
AUDIO_SIGNALPROCESSINGMODE_DEFAULT = "{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}"
AUDIO_SIGNALPROCESSINGMODE_MOVIE   = "{B26FEB0D-EC94-477C-9494-D1AB8E753F6E}"
AUDIO_SIGNALPROCESSINGMODE_MEDIA   = "{4780004E-7133-41D8-8C74-660DADD2C0EE}"

...
[SWAPAPO.I.Association0.AddReg]
;To register an APO for streaming in multiple modes, use a REG_MULTI_SZ property and include all the desired modes:
HKR,"FX\\0",%PKEY_MFX_Offload_ProcessingModes_For_Streaming%,%REG_MULTI_SZ%,%AUDIO_SIGNALPROCESSINGMODE_DEFAULT%,%AUDIO_SIGNALPROCESSINGMODE_MOVIE%,%AUDIO_SIGNALPROCESSINGMODE_MEDIA%
```

## <span id="related_topics"></span>Related topics


[Media-Class INF Extensions](media-class-inf-extensions.md)

 

 






