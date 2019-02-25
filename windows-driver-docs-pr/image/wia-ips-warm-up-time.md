---
title: WIA\_IPS\_WARM\_UP\_TIME
description: The WIA\_IPS\_WARM\_UP\_TIME property contains the maximum warm-up time, in milliseconds, that a device needs before starting the scanning operation. The WIA minidriver creates and maintains this property.
ms.assetid: 081cdb91-d5d8-4458-9a78-72fcbb13c7da
keywords: ["WIA_IPS_WARM_UP_TIME Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_WARM_UP_TIME
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_WARM\_UP\_TIME


The WIA\_IPS\_WARM\_UP\_TIME property contains the maximum warm-up time, in milliseconds, that a device needs before starting the scanning operation. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ips_warm_up_time_si"></span><span id="DDK_WIA_IPS_WARM_UP_TIME_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

An application can read the WIA\_IPS\_WARM\_UP\_TIME property to determine the maximum warm-up time for a device. The application can then present a "waiting for the device to warm up" dialog box to let users know that a wait or pause might occur before anything happens.

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

 

 





