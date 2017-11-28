---
title: PKEY\_MFX\_ProcessingModes\_Supported\_For\_Streaming
description: In Windows 8.1 and later, the PKEY\_MFX\_ProcessingModes\_Supported\_For\_Streaming property key identifies the mode effect processing modes supported for streaming supported by the driver.
ms.assetid: BE23FA51-FCA0-4391-B2AB-447C6096C75B
---

# PKEY\_MFX\_ProcessingModes\_Supported\_For\_Streaming


In Windows 8.1 and later, the **PKEY\_MFX\_ProcessingModes\_Supported\_For\_Streaming** property key identifies the mode effect processing modes supported for streaming supported by the driver. The driver developer should list the mode effect processing modes supported for streaming that their driver supports.

The INF file property key instructs the audio endpoint builder to set the CLSIDs for APOs into the effects property store. This information is used to build the audio graph that will be used to inform upper level apps what effects are in place.

## <span id="INF_File_Sample"></span><span id="inf_file_sample"></span><span id="INF_FILE_SAMPLE"></span>INF File Sample


An INF file specifies settings for an audio processing mode effect in the add-registry section for that device. The following INF example shows the strings and add-registry sections that loads the mode effect processing modes into the registry.

```
[Strings]
PKEY_MFX_ProcessingModes_Supported_For_Streaming = "{D3993A3F-99C2-4402-B5EC-A92A0367664B},6"
...
AUDIO_SIGNALPROCESSINGMODE_DEFAULT = "{C18E2F7E-933D-4965-B7D1-1EEF228D2AF3}"
AUDIO_SIGNALPROCESSINGMODE_MOVIE   = "{B26FEB0D-EC94-477C-9494-D1AB8E753F6E}"
AUDIO_SIGNALPROCESSINGMODE_COMMUNICATIONS = "{98951333-B9CD-48B1-A0A3-FF40682D73F7}"
...
[SWAPAPO.I.Association0.AddReg]
;To register an APO for streaming in multiple modes, use a REG_MULTI_SZ property and include all the desired modes:
HKR,"FX\\0",%PKEY_MFX_ProcessingModes_For_Streaming%,%REG_MULTI_SZ%,%AUDIO_SIGNALPROCESSINGMODE_DEFAULT%,%AUDIO_SIGNALPROCESSINGMODE_MOVIE%,%AUDIO_SIGNALPROCESSINGMODE_COMMUNICATIONS%
```

## <span id="related_topics"></span>Related topics


[Media-Class INF Extensions](media-class-inf-extensions.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20PKEY_MFX_ProcessingModes_Supported_For_Streaming%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





