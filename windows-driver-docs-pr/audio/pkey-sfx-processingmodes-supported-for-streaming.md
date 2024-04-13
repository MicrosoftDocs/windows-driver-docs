---
title: PKEY\_SFX\_ProcessingModes\_Supported\_For\_Streaming
description: In Windows 8.1 and later, the PKEY\_SFX\_ProcessingModes\_Supported\_For\_Streaming property key identifies the streaming processing modes supported by the driver.
ms.date: 03/06/2023
ms.topic: reference
---


# PKEY\_SFX\_ProcessingModes\_Supported\_For\_Streaming


In Windows 8.1 and later, the **PKEY\_SFX\_ProcessingModes\_Supported\_For\_Streaming** property key identifies the streaming processing modes supported by the driver. The driver developer should list the processing modes supported for streaming that their driver supports.

The INF file property key instructs the audio endpoint builder to set the CLSIDs for APOs into the effects property store. This information is used to build the audio graph that will be used to inform upper level apps what effects are in place.

## <span id="INF_File_Sample"></span><span id="inf_file_sample"></span><span id="INF_FILE_SAMPLE"></span>INF File Sample


An INF file specifies settings for an audio processing mode effect in the add-registry section for that device. The following INF example shows the strings and add-registry sections that loads the mode effect processing modes into the registry.

```inf
[Strings]
PKEY_SFX_ProcessingModes_Supported_For_Streaming = "{D3993A3F-99C2-4402-B5EC-A92A0367664B},5"
...
AUDIO_SIGNALPROCESSINGMODE_DEFAULT = "{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}"
AUDIO_SIGNALPROCESSINGMODE_MOVIE   = "{B26FEB0D-EC94-477C-9494-D1AB8E753F6E}"
AUDIO_SIGNALPROCESSINGMODE_COMMUNICATIONS = "{98951333-B9CD-48B1-A0A3-FF40682D73F7}"
...
[SWAPAPO.I.Association0.AddReg]
;To register an APO for streaming in multiple modes, use a REG_MULTI_SZ property and include all the desired modes:
HKR,"FX\\0",%PKEY_SFX_ProcessingModes_For_Streaming%,%REG_MULTI_SZ%,%AUDIO_SIGNALPROCESSINGMODE_DEFAULT%,%AUDIO_SIGNALPROCESSINGMODE_MOVIE%,%AUDIO_SIGNALPROCESSINGMODE_COMMUNICATIONS%
```

## Related topics


[Media-Class INF Extensions](media-class-inf-extensions.md)










