---
title: WIA\_IPS\_PRINTER\_ENDORSER\_MAX\_GRAPHICS
description: The WIA\_IPS\_PRINTER\_ENDORSER\_MAX\_GRAPHICS property describes the maximum number of images that the Imprinter/Endorser item can print or endorse on each page.
ms.assetid: A8FB39D2-659C-45E9-BE5E-627E594B9D3A
keywords: ["WIA_IPS_PRINTER_ENDORSER_MAX_GRAPHICS Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_MAX_GRAPHICS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_PRINTER\_ENDORSER\_MAX\_GRAPHICS


The **WIA\_IPS\_PRINTER\_ENDORSER\_MAX\_GRAPHICS** property describes the maximum number of images that the Imprinter/Endorser item can print or endorse on each page. This property is useful when the Imprinter/Endorser item supports graphics upload via multi-page (TYMED\_MULTIPAGE\_FILE) file format transfers. This property is initialized and maintained by the WIA mini-driver, and is available with Windows 8 and later versions of Windows.

Property Type: VT\_UI4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The **WIA\_IPS\_PRINTER\_ENDORSER\_MAX\_GRAPHICS** property is optional for the Imprinter/Endorser items that support graphics upload. When implemented, the property value **must be** greater than zero (0).

For more information about the TYMED\_MULTIPAGE\_FILE constant, see [**WIA\_IPA\_TYMED**](wia-ipa-tymed.md).

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

## See also


[**WIA\_IPA\_TYMED**](wia-ipa-tymed.md)

 

 






