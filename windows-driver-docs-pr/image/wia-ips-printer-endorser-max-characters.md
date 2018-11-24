---
title: WIA\_IPS\_PRINTER\_ENDORSER\_MAX\_CHARACTERS
description: The WIA\_IPS\_PRINTER\_ENDORSER\_MAX\_CHARACTERS property describes the maximum number of characters (excluding the NULL terminator) that the Imprinter/Endorser item can print or endorse on each page.
ms.assetid: B78BC67D-2B49-4A0E-A275-2A9A8F97F84E
keywords: ["WIA_IPS_PRINTER_ENDORSER_MAX_CHARACTERS Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_MAX_CHARACTERS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_PRINTER\_ENDORSER\_MAX\_CHARACTERS


The **WIA\_IPS\_PRINTER\_ENDORSER\_MAX\_CHARACTERS** property describes the maximum number of characters (excluding the NULL terminator) that the Imprinter/Endorser item can print or endorse on each page. This property is initialized and maintained by the WIA mini-driver, and is available with Windows 8 and later versions of Windows.

Property Type: VT\_UI4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The **WIA\_IPS\_PRINTER\_ENDORSER\_MAX\_CHARACTERS** property must be supported by all Imprinter/Endorser items. When implemented, the property value **must be** greater than zero (0).

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

 

 





