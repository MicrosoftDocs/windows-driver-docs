---
title: WIA\_IPS\_PRINTER\_ENDORSER\_TEXT\_DOWNLOAD
description: The WIA\_IPS\_PRINTER\_ENDORSER\_TEXT\_DOWNLOAD property is used to report whether the Imprinter/Endorser item supports download text data transfers. The WIA minidriver creates and maintains this property.
ms.assetid: AEFF6C6F-8DA9-4AFF-8614-A1134C7C499C
keywords: ["WIA_IPS_PRINTER_ENDORSER_TEXT_DOWNLOAD Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_TEXT_DOWNLOAD
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_PRINTER\_ENDORSER\_TEXT\_DOWNLOAD


The WIA\_IPS\_PRINTER\_ENDORSER\_TEXT\_DOWNLOAD property is used to report whether the Imprinter/Endorser item supports download text data transfers. The WIA minidriver creates and maintains this property.




Property Type: VT\_I4 (Boolean)

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

If the current value of this property is set to a value of True (nonzero), the WIA minidriver supports receiving text data that is uploaded by the application client. The transfer file format is described by the [**WIA\_IPA\_FORMAT**](wia-ipa-format.md) and [**WIA\_IPA\_TYMED**](wia-ipa-tymed.md) properties implemented on the same Imprinter/Endorser item.

This property is required for all Imprinter/Endorser items but it can be implemented to always report a value of 0 (False).

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

 

 





