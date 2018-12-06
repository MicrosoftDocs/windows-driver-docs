---
title: WIA\_DPS\_MAX\_SCAN\_TIME
description: The WIA\_DPS\_MAX\_SCAN\_TIME property contains the maximum time to scan a single page with the current property settings, in milliseconds.
ms.assetid: 28c24b1b-9318-46d2-86eb-f948247de8ab
keywords: ["WIA_DPS_MAX_SCAN_TIME Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_MAX_SCAN_TIME
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPS\_MAX\_SCAN\_TIME


The WIA\_DPS\_MAX\_SCAN\_TIME property contains the maximum time to scan a single page with the current property settings, in milliseconds.

## <span id="ddk_wia_dps_max_scan_time_si"></span><span id="DDK_WIA_DPS_MAX_SCAN_TIME_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

An application reads the WIA\_DPS\_MAX\_SCAN\_TIME property to estimate how much the time it will take to scan a page. This estimate is helpful when you are determining the conditions of a device that has stopped responding. The WIA minidriver creates and maintains this property.

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

 

 





