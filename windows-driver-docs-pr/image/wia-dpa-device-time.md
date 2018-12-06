---
title: WIA\_DPA\_DEVICE\_TIME
description: The WIA\_DPA\_DEVICE\_TIME property contains the current clock time that is stored on a device. The minidriver creates and maintains this property.
ms.assetid: 5f903eb8-6a9e-4f06-ba70-5c02d8b332e5
keywords: ["WIA_DPA_DEVICE_TIME Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPA_DEVICE_TIME
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPA\_DEVICE\_TIME


The WIA\_DPA\_DEVICE\_TIME property contains the current clock time that is stored on a device. The minidriver creates and maintains this property.

## <span id="ddk_wia_dpa_device_time_si"></span><span id="DDK_WIA_DPA_DEVICE_TIME_SI"></span>


Property Type: VT\_UI2 | VT\_VECTOR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read/write or read-only

Remarks
-------

When the WIA\_DPA\_DEVICE\_TIME property is read, the minidriver should check the device's current clock time and should always return the current time. This property is supported only by devices that have an internal clock. If the device clock can be set, this property is read/write; otherwise, it is read-only. WIA devices report time in a SYSTEMTIME structure (which is described in the Microsoft Windows SDK documentation).

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

 

 





