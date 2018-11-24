---
title: WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_DOWNLOAD
description: The WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_DOWNLOAD property is used to report whether the Imprinter/Endorser item supports download image (graphic) data transfers. This property is initialized and maintained by the WIA minidriver.
ms.assetid: AE58548B-CB0A-45FE-A1C6-5C476061B89D
keywords: ["WIA_IPS_PRINTER_ENDORSER_GRAPHICS_DOWNLOAD Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_GRAPHICS_DOWNLOAD
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_DOWNLOAD


The **WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_DOWNLOAD** property is used to report whether the Imprinter/Endorser item supports download image (graphic) data transfers. This property is initialized and maintained by the WIA minidriver.




Property Type: VT\_I4 (Boolean)

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

If the current value of this property is set to a nonzero value (True), it means that the WIA minidriver supports transferring image data that is downloaded to it by the WIA application client. The transfer file format is described by the [**WIA\_IPA\_FORMAT**](wia-ipa-format.md) and [**WIA\_IPA\_TYMED**](wia-ipa-tymed.md) properties implemented on the same Imprinter/Endorser item.

This property is required and valid for all Imprinter/Endorser items that report a nonzero value (True) for [**WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS**](wia-ips-printer-endorser-graphics.md), but it can be implemented to always report a 0 value (False). The property is invalid otherwise.

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

 

 





