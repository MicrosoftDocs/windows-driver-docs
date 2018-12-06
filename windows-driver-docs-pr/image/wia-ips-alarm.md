---
title: WIA\_IPS\_ALARM
description: The WIA\_IPS\_ ALARM property is used to configure the audible alarm (beep) that is produced by the WIA mini-driver at the device, in one of the following conditions When this property is implemented on a Feeder item (WIA\_CATEGORY\_FEEDER), and multi-feed detection is enabled, the audible alarm (beep) sound should be played by the device when a multiple feed condition is detected. (When the WIA\_IPS\_MULTI\_FEED property is supported and set to a value that is not WIA\_MULTI\_FEED\_DETECT\_DISABLED, it means that multi-feed detection is enabled.)When this property is implemented on a Barcode Reader item (WIA\_CATEGORY\_BARCODE\_READER), and barcode detection is enabled, the audible alarm (beep) sound should be played by the device when a barcode is successfully detected. When this property is implemented on a Patch Code Reader item (WIA\_CATEGORY\_PATCH\_CODE\_READER), and patch code detection is enabled, the audible alarm (beep) sound should be played by the device when a patch code is successfully detected.
ms.assetid: A029F7CD-C057-43FA-83AF-4B47B5A76B3F
keywords: ["WIA_IPS_ALARM Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_ALARM
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_ALARM


The **WIA\_IPS\_ ALARM** property is used to configure the audible alarm (beep) that is produced by the WIA mini-driver at the device, in one of the following conditions:

-   When this property is implemented on a Feeder item (WIA\_CATEGORY\_FEEDER), and multi-feed detection is enabled, the audible alarm (beep) sound should be played by the device when a multiple feed condition is detected. (When the WIA\_IPS\_MULTI\_FEED property is supported and set to a value that is not WIA\_MULTI\_FEED\_DETECT\_DISABLED, it means that multi-feed detection is enabled.)
-   When this property is implemented on a Barcode Reader item (WIA\_CATEGORY\_BARCODE\_READER), and barcode detection is enabled, the audible alarm (beep) sound should be played by the device when a barcode is successfully detected.
-   When this property is implemented on a Patch Code Reader item (WIA\_CATEGORY\_PATCH\_CODE\_READER), and patch code detection is enabled, the audible alarm (beep) sound should be played by the device when a patch code is successfully detected.

This property is initialized and maintained by the WIA mini-driver, and is available with Windows 8 and later versions of Windows.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read-Write

Remarks
-------

The valid values for this property are shown in the following table.

| Value              | Description                                           |
|--------------------|-------------------------------------------------------|
| WIA\_ALARM\_NONE   | No audible alarm (beep) is played at the device.      |
| WIA\_ALARM\_BEEP1  | An audible alarm (beep) is played at the device.      |
| WIA\_ALARM\_BEEP2  | Another audible alarm (beep) is played at the device. |
| WIA\_ALARM\_BEEP3  | Another audible alarm (beep) is played at the device. |
| WIA\_ALARM\_BEEP4  | Another audible alarm (beep) is played at the device. |
| WIA\_ALARM\_BEEP5  | Another audible alarm (beep) is played at the device. |
| WIA\_ALARM\_BEEP6  | Another audible alarm (beep) is played at the device. |
| WIA\_ALARM\_BEEP7  | Another audible alarm (beep) is played at the device. |
| WIA\_ALARM\_BEEP8  | Another audible alarm (beep) is played at the device. |
| WIA\_ALARM\_BEEP9  | Another audible alarm (beep) is played at the device. |
| WIA\_ALARM\_BEEP10 | Another audible alarm (beep) is played at the device. |

 

The WIA mini-driver can implement one or more WIA\_ALARM\_BEEP values, each one for a different beep sound or signal supported by the device. If the device can only produce one beep sound, the WIA mini-driver must only implement the WIA\_ALARM\_NONE and WIA\_ALARM\_BEEP1 values.

This property is valid and optional for the Feeder item (WIA\_CATEGORY\_FEEDER) when the WIA\_IPS\_MULTI\_FEED property is supported. This property is also valid and optional for the Barcode Reader (WIA\_CATEGORY\_BARCODE\_READER) and the Patch Code Reader (WIA\_CATEGORY\_PATCH\_CODE\_READER) items. When this property is implemented, the WIA\_ALARM\_NONE value is required and must be set by the mini-driver as the default value.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 





