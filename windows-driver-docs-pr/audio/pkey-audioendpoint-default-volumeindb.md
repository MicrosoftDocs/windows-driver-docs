---
title: PKEY\_AudioEndpoint\_Default\_VolumeInDb
description: In Windows 10 Version 1605 and later, the PKEY\_AudioEndpoint\_Default\_VolumeInDb property key configures the default volume (in dB) for the software volume node.
ms.assetid: 9BC8E0D1-F4F3-4FB4-A50F-E4C79317EC30
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


```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20PKEY_AudioEndpoint_Default_VolumeInDb%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





