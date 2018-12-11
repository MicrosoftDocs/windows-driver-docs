---
title: PKEY\_Devices\_AudioDevice\_Microphone\_IsFarField
description: In Windows 10 Version 19H1 and later, **PKEY\_Devices\_AudioDevice\_Microphone\_IsFarField** property key identifies indicates if the microphone will capture far field audio.
ms.date: 12/10/2018
ms.localizationpriority: medium
---

# PKEY\_Devices\_AudioDevice\_Microphone\_IsFarField

In Windows 10 19H1 and later, the **PKEY\_Devices\_AudioDevice\_Microphone\_IsFarField** property key identifies indicates if the microphone will capture far field audio.

A value of 1 indicates that the microphone will capture far field audio, which will make the microphone a preferred endpoint for a voice assistant. A value of 0 or no property key indicates that the microphone does not support far field or support is unknown, so the endpoint will not be prioritized for use by a voice assistant.

The property is meant to be set by the audio driver, most likely via INF. This is similar to other properties, like the neversetasdefault property.


## <span id="INF_File_Sample"></span><span id="inf_file_sample"></span><span id="INF_FILE_SAMPLE"></span>INF File Sample

The sysvad sample componentizedAudioSampleExtension.inf file includes this property. The sample shows the value set to 0x1 indicating the microphone does capture far field audio.

```inf
;HKR,EP\1,%PKEY_Devices_AudioDevice_Microphone_IsFarField%,0x00010001,0x1
```

## <span id="related_topics"></span>Related topics

[Media-Class INF Extensions](media-class-inf-extensions.md)

 

 






