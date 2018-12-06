---
title: PKEY\_EFX\_KeywordDetector\_ProcessingModes\_Supported\_For\_Streaming
description: In Windows 10 and later, the PKEY\_EFX\_KeywordDetector\_ProcessingModes\_Supported\_For\_Streaming property key identifies the end point keyword detector processing modes supported for streaming supported by the driver.
ms.assetid: 517B7321-5726-4ADB-9FCD-82776B143FF9
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PKEY\_EFX\_KeywordDetector\_ProcessingModes\_Supported\_For\_Streaming


In Windows 10 and later, the **PKEY\_EFX\_KeywordDetector\_ProcessingModes\_Supported\_For\_Streaming** property key identifies the end point keyword detector processing modes supported for streaming supported by the driver. The driver developer should list the end point processing modes supported for streaming that their driver supports for the keyword detector pin.

This list only includes signal processing modes where the APO actually processes the audio signal during streaming. This list must not include any signal processing modes supported by the APO for discovery purposes only.

The INF file property key instructs the audio endpoint builder to set the CLSIDs for APOs into the effects property store. This information is used to build the audio graph that will be used to inform upper level apps what effects are in place.

Because end point effects (EFX) are after the sum or before the tee, there cannot be multiple modes associated with endpoint processing. For this reason, only a single mode, AUDIO\_SIGNALPROCESSINGMODE\_DEFAULT, can be specified.

## <span id="INF_File_Sample"></span><span id="inf_file_sample"></span><span id="INF_FILE_SAMPLE"></span>INF File Sample


An INF file specifies settings for an audio processing mode effect in the add-registry section for that device. The following INF example shows the strings and add-registry sections that loads the keyword detector streaming processing modes supported into the registry.

```inf
[Strings]
PKEY_EFX_KeywordDetector_ProcessingModes_Supported_For_Streaming = "{D3993A3F-99C2-4402-B5EC-A92A0367664B},10"
...
[SWAPAPO.I.Association0.AddReg]
; This line shows how to set the default processing mode for streaming.
HKR,FX\0,%PKEY_EFX_KeywordDetector_ProcessingModes_Supported_For_Streaming%,0x00010000,%AUDIO_SIGNALPROCESSINGMODE_DEFAULT%
```

## <span id="related_topics"></span>Related topics


[Media-Class INF Extensions](media-class-inf-extensions.md)

 

 






