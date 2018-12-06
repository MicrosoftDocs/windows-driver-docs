---
title: WIA\_IPS\_PRINTER\_ENDORSER\_PADDING
description: The WIA\_IPS\_PRINTER\_ENDORSER\_PADDING property configures the valid special padding characters that are printed or endorsed to fill blank spaces in counters, data and time sequences.
ms.assetid: 44C8A517-43E5-4986-9B8A-46167B5884E5
keywords: ["WIA_IPS_PRINTER_ENDORSER_PADDING Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_PADDING
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_PRINTER\_ENDORSER\_PADDING


The **WIA\_IPS\_PRINTER\_ENDORSER\_PADDING** property configures the valid special padding characters that are printed or endorsed to fill blank spaces in counters, data and time sequences. This property is initialized and maintained by the WIA mini-driver, and is available with Windows 8 and later versions of Windows.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read-Write

Remarks
-------

The valid values for this property are shown in the following table.

| Value                      | Description                                        |
|----------------------------|----------------------------------------------------|
| WIA\_PRINT\_PADDING\_NONE  | No padding.                                        |
| WIA\_PRINT\_PADDING\_ZERO  | The zero (0) digit is used as a padding character. |
| WIA\_PRINT\_PADDING\_BLANK | The space (blank) character is used for padding.   |

 

The **WIA\_IPS\_PRINTER\_ENDORSER\_PADDING** property is optional for the Imprinter/Endorser items. When this property is not supported, the printer/endorser device does not support padding.

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

 

 





