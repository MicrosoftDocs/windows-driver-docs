---
title: WIA\_IPS\_FILM\_SCAN\_MODE
description: The WIA\_IPS\_FILM\_SCAN\_MODE property contains the current film scan configuration settings. The WIA minidriver creates and maintains this property.
ms.assetid: 3bbe362e-1868-4327-a862-8711f09969f7
keywords: ["WIA_IPS_FILM_SCAN_MODE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_FILM_SCAN_MODE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_FILM\_SCAN\_MODE


The WIA\_IPS\_FILM\_SCAN\_MODE property contains the current film scan configuration settings. The WIA minidriver creates and maintains this property.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

The following table describes the constants that are valid with the WIA\_IPS\_FILM\_SCAN\_MODE property

| Scan type                  | Definition                                         |
|----------------------------|----------------------------------------------------|
| WIA\_FILM\_COLOR\_SLIDE    | The scan will be a color scan.                     |
| WIA\_FILM\_COLOR\_NEGATIVE | The scan will be a color scan of a negative.       |
| WIA\_FILM\_BW\_NEGATIVE    | The scan will be black and white (grayscale) scan. |

 

This property is required for the root item in the WIA item tree of film scanners and transparency adapters.

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

 

 





