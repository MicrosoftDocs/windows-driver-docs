---
title: WIA\_IPS\_PRINTER\_ENDORSER\_INK
description: The WIA\_IPS\_PRINTER\_ENDORSER\_INK property is used to report the current ink or toner status for the Imprinter/Endorser device.
ms.assetid: CCD7C10A-7739-4E75-B30C-2C2E7FE90B13
keywords: ["WIA_IPS_PRINTER_ENDORSER_INK Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_INK
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_PRINTER\_ENDORSER\_INK


The **WIA\_IPS\_PRINTER\_ENDORSER\_INK** property is used to report the current ink or toner status for the Imprinter/Endorser device. The property value indicates the remaining available ink, as a percentage of the total capacity. For example, a value of 50 indicates that there is half or 50% ink remaining. This property is initialized and maintained by the WIA mini-driver. This feature is available with Windows 8 and later versions of Windows.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read-Write

Remarks
-------

The **WIA\_IPS\_PRINTER\_ENDORSER\_INK** property is optional for the Imprinter/Endorser items. The valid values for this property are between 0 and 100, inclusive.

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

 

 





