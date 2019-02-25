---
title: WIA\_DPC\_BATTERY\_STATUS
description: The WIA\_DPC\_BATTERY\_STATUS property defines the percentage of battery power that is left to operate a camera device.
ms.assetid: d6e50c77-9c30-4091-9d6e-7215907ba87b
keywords: ["WIA_DPC_BATTERY_STATUS Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_BATTERY_STATUS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPC\_BATTERY\_STATUS


The WIA\_DPC\_BATTERY\_STATUS property defines the percentage of battery power that is left to operate a camera device.

## <span id="ddk_wia_dpc_battery_status_si"></span><span id="DDK_WIA_DPC_BATTERY_STATUS_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The value of the WIA\_DPC\_BATTERY\_STATUS property should be an integer from 0 through 100. An application reads this property to determine the remaining battery life of the camera device.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Obsolete in Windows Vista and later operating systems and should no longer be used. However, this property is still defined in Windows Vista for compatibility with applications and devices designed for Windows Server 2003, Windows XP, and previous versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 





