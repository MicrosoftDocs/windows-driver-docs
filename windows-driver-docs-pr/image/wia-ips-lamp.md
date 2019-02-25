---
title: WIA\_IPS\_LAMP
description: The WIA\_IPS\_LAMP property contains the current configuration setting for a scanner's lamp. The WIA minidriver creates and maintains this property.
ms.assetid: a5eb83cf-824a-4c7c-a7e3-2f9af5a2eb3c
keywords: ["WIA_IPS_LAMP Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_LAMP
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_LAMP


The WIA\_IPS\_LAMP property contains the current configuration setting for a scanner's lamp. The WIA minidriver creates and maintains this property.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

The WIA\_IPS\_LAMP property enables the programmatic control of the scanner lamp; this lamp could be a dedicated lamp (for a transparency adapter) or the main scanner lamp (for dedicated film scanners).

The following table describes the constants that are valid with WIA\_IPS\_LAMP.

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
<td><p>WIA_LAMP_ON</p></td>
<td><p>The lamp is on.</p></td>
</tr>
<tr class="even">
<td><p>WIA_LAMP_OFF</p></td>
<td><p>The lamp is off.</p></td>
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

 

 





