---
title: WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_UPLOAD
description: The WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_UPLOAD property is used to report whether the Imprinter/Endorser item supports upload image (graphic) data transfers. This property is initialized and maintained by the WIA minidriver.
ms.assetid: BCA1F340-5BF8-429A-90B9-9638E52E61DE
keywords: ["WIA_IPS_PRINTER_ENDORSER_GRAPHICS_UPLOAD Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_GRAPHICS_UPLOAD
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_UPLOAD


The **WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_UPLOAD** property is used to report whether the Imprinter/Endorser item supports upload image (graphic) data transfers. This property is initialized and maintained by the WIA minidriver.

## <span id="ddk_wia_ipa_depth_si"></span><span id="DDK_WIA_IPA_DEPTH_SI"></span>


Property Type: VT\_I4 (Boolean)

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

If the current value of this property is set to a nonzero value (True), it means that the WIA minidriver supports receiving image data that is uploaded to it by the WIA application client. The transfer file format is described by the [**WIA\_IPA\_FORMAT**](wia-ipa-format.md) and [**WIA\_IPA\_TYMED**](wia-ipa-tymed.md) properties implemented on the same Imprinter/Endorser item.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_PRINTER_ENDORSER_GRAPHICS_UPLOAD%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




