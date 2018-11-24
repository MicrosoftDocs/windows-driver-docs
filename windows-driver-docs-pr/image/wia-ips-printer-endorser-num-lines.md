---
title: WIA\_IPS\_PRINTER\_ENDORSER\_NUM\_LINES
description: The WIA\_IPS\_PRINTER\_ENDORSER\_NUM\_LINES property specifies the maximum number of lines of text that can be printed or endorsed on each side of a document by the Imprinter/Endorser unit.
ms.assetid: 64C9C0B7-78C9-4EDF-B91D-2E9AD45A4D1E
keywords: ["WIA_IPS_PRINTER_ENDORSER_NUM_LINES Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_NUM_LINES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/22/2018
ms.localizationpriority: medium
---

# WIA\_IPS\_PRINTER\_ENDORSER\_NUM\_LINES


The **WIA\_IPS\_PRINTER\_ENDORSER\_NUM\_LINES** property specifies the maximum number of lines of text that can be printed or endorsed on each side of a document by the Imprinter/Endorser unit. This property is initialized and maintained by the WIA mini-driver, and it is available with Windows 8 and later versions of Windows.

Property Type: VT\_UI4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The **WIA\_IPS\_PRINTER\_ENDORSER\_NUM\_LINES** property is optional for the Imprinter/Endorser items. When this property is not supported, only a single line of text is allowed on each side of a document.

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

 

 





