---
title: WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MIN\_WIDTH
description: The WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MIN\_WIDTH property along with WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MAX\_WIDTH, WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MIN\_HEIGHT, and WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MAX\_HEIGHT are used to report the minimum and maximum dimensions, in pixels, of the images that can be uploaded to the Imprinter/Endorser to be rendered. The WIA minidriver creates and maintains this property.
ms.assetid: D79D21FA-494F-4EB2-A3C3-7804765998E4
keywords: ["WIA_IPS_PRINTER_ENDORSER_GRAPHICS_MIN_WIDTH Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_GRAPHICS_MIN_WIDTH
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MIN\_WIDTH


The **WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MIN\_WIDTH** property along with [**WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MAX\_WIDTH**](wia-ips-printer-endorser-graphics-max-width.md), [**WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MIN\_HEIGHT**](wia-ips-printer-endorser-graphics-min-height.md), and [**WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MAX\_HEIGHT**](wia-ips-printer-endorser-graphics-max-height.md) are used to report the minimum and maximum dimensions, in pixels, of the images that can be uploaded to the Imprinter/Endorser to be rendered. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipa_depth_si"></span><span id="DDK_WIA_IPA_DEPTH_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The value reported for**WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MIN\_WIDTH** must be less than or equal to the value reported for [**WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MAX\_WIDTH**](wia-ips-printer-endorser-graphics-max-width.md). The value reported for [**WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MIN\_HEIGHT**](wia-ips-printer-endorser-graphics-min-height.md) must be less than or equal to the value reported for [**WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS\_MAX\_HEIGHT**](wia-ips-printer-endorser-graphics-max-height.md). The WIA minidriver can report a 0 value for all these properties to indicate that images of any size are accepted.

If nonzero values are reported, the WIA application client should not attempt and must not expect success in uploading an image that is smaller than the minimum or larger than the maximum sizes reported by the WIA minidriver through these properties. The WIA minidriver must fail image upload requests when the image size doesn't match the supported range.

This property is required and valid for all Imprinter/Endorser items that report a nonzero value (True) for [**WIA\_IPS\_PRINTER\_ENDORSER\_GRAPHICS**](wia-ips-printer-endorser-graphics.md). These properties are invalid otherwise.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_PRINTER_ENDORSER_GRAPHICS_MIN_WIDTH%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




