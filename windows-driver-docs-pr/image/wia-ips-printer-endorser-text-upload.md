---
title: WIA\_IPS\_PRINTER\_ENDORSER\_TEXT\_UPLOAD
description: The WIA\_IPS\_PRINTER\_ENDORSER\_TEXT\_UPLOAD property is used to report whether the Imprinter/Endorser item supports upload text data transfers. The WIA minidriver creates and maintains this property.
ms.assetid: FE239B61-6656-462B-A962-2101A1F0C683
keywords: ["WIA_IPS_PRINTER_ENDORSER_TEXT_UPLOAD Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_TEXT_UPLOAD
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_PRINTER\_ENDORSER\_TEXT\_UPLOAD


The **WIA\_IPS\_PRINTER\_ENDORSER\_TEXT\_UPLOAD** property is used to report whether the Imprinter/Endorser item supports upload text data transfers. The WIA minidriver creates and maintains this property.




Property Type: VT\_I4 (Boolean)

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

If the current value of this property is set to a value of True (nonzero), the WIA minidriver supports receiving text data that is uploaded by the application client. The transfer file format is described by the [**WIA\_IPA\_FORMAT**](wia-ipa-format.md) and [**WIA\_IPA\_TYMED**](wia-ipa-tymed.md) properties implemented on the same Imprinter/Endorser item.

This property is required for all Imprinter/Endorser items, but it can be implemented to always report a value of 0 (False). Also, if the Imprinter/Endorser item reports WiaItemTypeFile and WiaItemTypeTransfer, this property is required and must report a nonzero value (True).

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

 

 





