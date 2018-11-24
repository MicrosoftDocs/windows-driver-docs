---
title: WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS
description: The WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS property is used to report whether the Imprinter/Endorser item supports graphics and image data along with text.
ms.assetid: F2550D8F-DF66-4184-909B-F0CCB68AD7C6
keywords: ["WIA_IPS_PRINTER_ENDORSER_GRAPHICS Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_GRAPHICS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS


The **WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS** property is used to report whether the Imprinter/Endorser item supports graphics and image data along with text. Graphics are typically used by the device to print/endorse near the text, or as a background image. The WIA minidriver creates and maintains this property.




Property Type: VT\_I4 (Boolean)

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

If **WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS** is supported and set to a value of nonzero (True), the Imprinter/Endorser supports graphic data.

This property is required for all Imprinter/Endorser items, but it can be implemented to always report a value of 0 (False).

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

 

 





