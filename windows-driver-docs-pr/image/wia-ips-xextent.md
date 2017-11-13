---
title: WIA\_IPS\_XEXTENT
description: The WIA\_IPS\_XEXTENT property contains the current width, in pixels, of a selected image to acquire.
MS-HAID:
- 'WIA\_PropTable\_93f85633-ec7c-4b97-bf31-3e4b6f9116f6.xml'
- 'image.wia\_ips\_xextent'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 00e8f705-5c2a-40ac-8635-b21a5d3315a3
keywords: ["WIA_IPS_XEXTENT Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_XEXTENT
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPS\_XEXTENT


The WIA\_IPS\_XEXTENT property contains the current width, in pixels, of a selected image to acquire.

## <span id="ddk_wia_ips_xextent_si"></span><span id="DDK_WIA_IPS_XEXTENT_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/write

Remarks
-------

An application sets the WIA\_IPS\_XEXTENT property to mark the upper-left corner (that is, the width) of the selection area to acquire. The minidriver creates and maintains this property.

WIA\_IPS\_XEXTENT is required for all image acquisition enabled items and child items of these items; this property is not available for storage items or stored image items.

When a fixed page size is set, the driver has to set the WIA\_IPS\_XEXTENT, [**WIA\_IPS\_XPOS**](wia-ips-xpos.md), [**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md), and [**WIA\_IPS\_YPOS**](wia-ips-ypos.md) properties to match the page size dimensions and a "0" origin. For center document alignment, the driver has to set WIA\_IPS\_XPOS to ((scan area width - document width) / 2) \* resolution \[DPI\]) and WIA\_IPS\_YPOS to ((scan area height - document height) / 2) \* resolution \[DPI\]).

When the origin or one extent is changed, the driver has to update the [**WIA\_IPS\_PAGE\_SIZE**](wia-ips-page-size.md) property to CUSTOM\_SIZE and the [**WIA\_IPS\_PAGE\_WIDTH**](wia-ips-page-width.md) and [**WIA\_IPS\_PAGE\_HEIGHT**](wia-ips-page-height.md) properties to match the scan area extents. Orientation and rotation should not affect these properties, unless an orientation change (not a rotation change) renders the origin or one extent outside of the available document scan area.

A driver must also to update the WIA\_IPS\_XEXTENT, WIA\_IPS\_XPOS, WIA\_IPS\_YEXTENT, and WIA\_IPS\_YPOS properties when [**WIA\_IPS\_XRES**](wia-ips-xres.md) and [**WIA\_IPS\_YRES**](wia-ips-yres.md) are changed.

**Note**   Flatbed and Film child items must support only the WIA\_IPS\_XEXTENT, WIA\_IPS\_XPOS, WIA\_IPS\_XRES, WIA\_IPS\_YEXTENT, WIA\_IPS\_YPOS, and WIA\_IPS\_YRES properties. All other properties, required or optional for their parent (the base Flatbed or Film items), are only optional for these items. The only exceptions are the WIA\_IPA\_ITEM\_*Xxx* properties, which are required for all items.

 

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

## <span id="see_also"></span>See also


[**WIA\_IPA\_PIXELS\_PER\_LINE**](wia-ipa-pixels-per-line.md)

[**WIA\_IPS\_PAGE\_HEIGHT**](wia-ips-page-height.md)

[**WIA\_IPS\_PAGE\_SIZE**](wia-ips-page-size.md)

[**WIA\_IPS\_PAGE\_WIDTH**](wia-ips-page-width.md)

[**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md)

[**WIA\_IPS\_XPOS**](wia-ips-xpos.md)

[**WIA\_IPS\_XRES**](wia-ips-xres.md)

[**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md)

[**WIA\_IPS\_YPOS**](wia-ips-ypos.md)

[**WIA\_IPS\_YRES**](wia-ips-yres.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_XEXTENT%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





