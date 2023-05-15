---
title: WIA_IPS_ALARM
description: The WIA_IPS_ ALARM property is used to configure the audible alarm.
keywords: ["WIA_IPS_ALARM Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPS_ALARM
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/04/2023
---

# WIA_IPS_ALARM

The **WIA_IPS_ ALARM** property is used to configure the audible alarm (beep) that is produced by the WIA mini-driver at the device, in one of the following conditions:

- When this property is implemented on a Feeder item (WIA_CATEGORY_FEEDER), and multi-feed detection is enabled, the audible alarm (beep) sound should be played by the device when a multiple feed condition is detected. (When the WIA_IPS_MULTI_FEED property is supported and set to a value that is not WIA_MULTI_FEED_DETECT_DISABLED, it means that multi-feed detection is enabled.)

- When this property is implemented on a Barcode Reader item (WIA_CATEGORY_BARCODE_READER), and barcode detection is enabled, the audible alarm (beep) sound should be played by the device when a barcode is successfully detected.

- When this property is implemented on a Patch Code Reader item (WIA_CATEGORY_PATCH_CODE_READER), and patch code detection is enabled, the audible alarm (beep) sound should be played by the device when a patch code is successfully detected.

This property is initialized and maintained by the WIA mini-driver, and is available with Windows 8 and later versions of Windows.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read-Write

## Remarks

The valid values for this property are shown in the following table.

| Value | Description |
|--|--|
| WIA_ALARM_NONE | No audible alarm (beep) is played at the device. |
| WIA_ALARM_BEEP1 | An audible alarm (beep) is played at the device. |
| WIA_ALARM_BEEP2 | Another audible alarm (beep) is played at the device. |
| WIA_ALARM_BEEP3 | Another audible alarm (beep) is played at the device. |
| WIA_ALARM_BEEP4 | Another audible alarm (beep) is played at the device. |
| WIA_ALARM_BEEP5 | Another audible alarm (beep) is played at the device. |
| WIA_ALARM_BEEP6 | Another audible alarm (beep) is played at the device. |
| WIA_ALARM_BEEP7 | Another audible alarm (beep) is played at the device. |
| WIA_ALARM_BEEP8 | Another audible alarm (beep) is played at the device. |
| WIA_ALARM_BEEP9 | Another audible alarm (beep) is played at the device. |
| WIA_ALARM_BEEP10 | Another audible alarm (beep) is played at the device. |

The WIA mini-driver can implement one or more WIA_ALARM_BEEP values, each one for a different beep sound or signal supported by the device. If the device can only produce one beep sound, the WIA mini-driver must only implement the WIA_ALARM_NONE and WIA_ALARM_BEEP1 values.

This property is valid and optional for the Feeder item (WIA_CATEGORY_FEEDER) when the WIA_IPS_MULTI_FEED property is supported. This property is also valid and optional for the Barcode Reader (WIA_CATEGORY_BARCODE_READER) and the Patch Code Reader (WIA_CATEGORY_PATCH_CODE_READER) items. When this property is implemented, the WIA_ALARM_NONE value is required and must be set by the mini-driver as the default value.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
