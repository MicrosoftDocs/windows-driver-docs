---
title: PKEY_AudioEndpoint_Min_VolumeInDb
description: The PKEY_AudioEndpoint_Min_VolumeInDb property key configures the minimum volume (in dB) for the software volume node.
ms.date: 12/19/2025
ms.topic: reference
---

# PKEY_AudioEndpoint_Min_VolumeInDb

In Windows 11 Version 24H2 and later, the **PKEY_AudioEndpoint_Min_VolumeInDb** property key configures the minimum volume (in dB) for the software volume node. Provide the minimum dB value that you would like to set.

If an audio driver doesn't implement a hardware volume node for an endpoint, Windows inserts a software volume node to control volume on that endpoint. There are situations, where the minimum volume value is too low. This settings information (INF) key provides the user a better experience when appropriate gain or attenuation is applied to the audio signal.

## Remarks

You can override the minimum software volume value for an endpoint by setting **PKEY_AudioEndpoint_Min_VolumeInDb** on a topology filter using the driver INF file. The value specified by the key is in dB units.

This key is used for both render and capture endpoints.

This key is ignored if the endpoint implements a hardware volume node.

Any value can be set, but Windows makes sure that the value it is within the minimum and maximum value settings. For example, if the specified value is greater than the max volume value, Windows sets the min value to the default volume value.

The data is stored as a 16.16 fixed point value. The upper 16 bits are used for the whole number of the value and the lower 16 bits are used for the fractional portion of the value.

## INF File Sample

```inf
; The following line overrides the minimum volume (in dB) for an endpoint.
; It is only applicable when hardware volume is not implemented.
; Decimal value expressed in fixed point 16.16 format and stored as a DWORD.

PKEY_AudioEndpoint_Min_VolumeInDb        = "{1DA5D803-D492-4EDD-8C23-E0C0FFEE7F0E},11"

; 10 dB
HKR,EP\0,%PKEY_AudioEndpoint_Min_VolumeInDb%,0x00010001,0xA0000

;-10 dB
;HKR,EP\0,%PKEY_AudioEndpoint_Min_VolumeInDb%,0x00010001,0xFFF60000
```

## Related articles

- [Media-Class INF Extensions](media-class-inf-extensions.md)
- [PKEY_AudioEndpoint_Default_VolumeInDb](pkey-audioendpoint-default-volumeindb.md)
- [PKEY_AudioEndpoint_Max_VolumeInDb](pkey-audioendpoint-max-volumeindb.md)
