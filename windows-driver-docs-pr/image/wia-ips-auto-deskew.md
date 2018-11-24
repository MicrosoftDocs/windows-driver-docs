---
title: WIA\_IPS\_AUTO\_DESKEW
description: The WIA\_IPS\_AUTO\_DESKEW property indicates if a device should use automatic skew correction. The WIA minidriver creates and maintains this property.
ms.assetid: e72d1af3-05ca-47b0-a2fe-0bb74a22b528
keywords: ["WIA_IPS_AUTO_DESKEW Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_AUTO_DESKEW
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_AUTO\_DESKEW


The WIA\_IPS\_AUTO\_DESKEW property indicates if a device should use automatic skew correction. The WIA minidriver creates and maintains this property.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

The following table describes the constants that are valid with the WIA\_IPS\_AUTO\_DESKEW property.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WIA_AUTO_DESKEW_ON</p></td>
<td><p>Use automatic skew correction.</p></td>
</tr>
<tr class="even">
<td><p>WIA_AUTO_DESKEW_OFF</p></td>
<td><p>Do not use automatic skew correction.</p></td>
</tr>
</tbody>
</table>

 

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
<td><p>Available in Windows Vista and later operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 





