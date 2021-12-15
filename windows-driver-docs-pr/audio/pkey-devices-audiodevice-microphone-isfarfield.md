---
title: PKEY\_Devices\_AudioDevice\_Microphone\_IsFarField
description: In Windows 10 Version 19H1 and later, **PKEY\_Devices\_AudioDevice\_Microphone\_IsFarField** property key identifies indicates if the microphone will capture far field audio.
ms.date: 02/13/2019
---

# PKEY\_Devices\_AudioDevice\_Microphone\_IsFarField

In Windows 10 19H1 and later, the **PKEY\_Devices\_AudioDevice\_Microphone\_IsFarField** property key indicates if the microphone will capture far field audio.

Starting in Windows 10 19H1, using the PKEY\_Devices\_AudioDevice\_Microphone\_IsFarField property is a requirement for systems that support far field audio, typically for use by a  voice assistant.

A value of 1 indicates that the microphone will capture far field audio, which will make the microphone a preferred endpoint for a voice assistant.

A value of 0 or no property key indicates that the microphone does not support far field or support is unknown, so the endpoint will not be prioritized for use by a voice assistant.

The property should be set via INF, and preferably an extension INF provided by the OEM as opposed to the base INF for the audio device. For more information about extension INF files, see [Creating a componentized audio driver installation](./audio-universal-drivers.md#creating-a-componentized-audio-driver-installation) and [Using an Extension INF File](../install/using-an-extension-inf-file.md).

## INF File Sample

The sysvad sample ComponentizedAudioSampleExtension.inf file includes this property. The sample shows the value set to 0x1 indicating the microphone does capture far field audio.

```inf
;HKR,EP\1,%PKEY_Devices_AudioDevice_Microphone_IsFarField%,0x00010001,0x1
```

## Requirements

|Requirement|Value |
|--- |--- |
|Minimum supported client|Windows 10 Version 19H1|
|Header|Ksmedia.h|

## Related topics

[Media-Class INF Extensions](media-class-inf-extensions.md)
