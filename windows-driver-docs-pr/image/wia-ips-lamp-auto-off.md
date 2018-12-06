---
title: WIA\_IPS\_LAMP\_AUTO\_OFF
description: The WIA\_IPS\_LAMP\_AUTO\_OFF property contains the current configuration setting for automatically shutting off a scanner's lamp. The WIA minidriver creates and maintains this property.
ms.assetid: 82a3b5dc-0a70-4e2a-a863-6019b04cbbaf
keywords: ["WIA_IPS_LAMP_AUTO_OFF Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_LAMP_AUTO_OFF
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_LAMP\_AUTO\_OFF


The WIA\_IPS\_LAMP\_AUTO\_OFF property contains the current configuration setting for automatically shutting off a scanner's lamp. The WIA minidriver creates and maintains this property.

Property Type: VT\_UI4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/write

Remarks
-------

The WIA\_IPS\_LAMP\_AUTO\_OFF property enables the programmatic control of how long a lamp will be kept on when a scanner is not in use; this lamp could be a dedicated lamp (for a transparency adapter) or the main scanner lamp (for dedicated film scanners).

You should implement WIA\_IPS\_LAMP\_AUTO\_OFF only if the device supports an automatic lamp-off feature.

The valid values for WIA\_IPS\_LAMP\_AUTO\_OFF range from 0 through 4095 seconds.

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

 

 





