---
title: PKEY\_AudioEndpoint\_Default\_VolumeInDb
description: In Windows 10 Version 1605 and later, the PKEY\_AudioEndpoint\_Default\_VolumeInDb property key configures the default volume (in dB) for the software volume node.
ms.assetid: 9BC8E0D1-F4F3-4FB4-A50F-E4C79317EC30
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PKEY\_AudioEndpoint\_Default\_VolumeInDb


In Windows 10 Version 1605 and later, the **PKEY\_AudioEndpoint\_Default\_VolumeInDb** property key configures the default volume (in dB) for the software volume node. The driver developer should provide the default dB value that they would like to set.

If an audio driver is not implementing hardware volume node for an endpoint, the OS inserts a software volume node to control volume on that endpoint. There are situations, where the default volume value is too low. This INF key provides the user a better experience when appropriate gain or attenuation is applied to audio signal.

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


IHVs and OEMs can override the default software volume value for an endpoint by setting PKEY\_AudioEndpoint\_Default\_VolumeInDb on a topology filter using the driver INF file. The value specified by the key is in dB units.

This key will be used for both render and capture endpoints.

This key is ignored if the endpoint has implemented a hardware volume node.

Any value can be set, but the OS will make sure that the value it is within the min and max value settings. For example, if the specified value is greater than max volume value, OS will set the default value to the max volume value.

The data is stored as a 16.16 fixed point value. The upper 16 bits are used for the whole number of the value and the lower 16 bits are used for the fractional portion of the value.

## <span id="INF_File_Sample"></span><span id="inf_file_sample"></span><span id="INF_FILE_SAMPLE"></span>INF File Sample


```inf
; The following line overrides the default volume (in dB) for an endpoint. 
; It is only applicable when hardware volume is not implemented. 
; Decimal value expressed in fixed point 16.16 format and stored as a DWORD. 

PKEY_AudioEndpoint_Default_VolumeInDb        = "{1DA5D803-D492-4EDD-8C23-E0C0FFEE7F0E},9" 

; 10 dB 
HKR,EP\0,%PKEY_AudioEndpoint_Default_VolumeInDb%,0x00010001,0xA0000 

;-10 dB 
;HKR,EP\0,%PKEY_AudioEndpoint_Default_VolumeInDb%,0x00010001,0xFFF60000
```

## <span id="related_topics"></span>Related topics


[Media-Class INF Extensions](media-class-inf-extensions.md)

 

 






