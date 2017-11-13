---
title: WIA\_DPS\_PAGE\_WIDTH
description: The WIA\_DPS\_PAGE\_WIDTH property contains the width of the currently selected page, in thousandths of an inch (.001).
MS-HAID:
- 'WIA\_PropTable\_45b860a6-5bf8-4c82-badb-ee9b8b64158a.xml'
- 'image.wia\_dps\_page\_width'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 02787660-3fb3-4e5d-ade8-b11ad29412c1
keywords: ["WIA_DPS_PAGE_WIDTH Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_PAGE_WIDTH
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_DPS\_PAGE\_WIDTH


The WIA\_DPS\_PAGE\_WIDTH property contains the width of the currently selected page, in thousandths of an inch (.001).

## <span id="ddk_wia_dps_page_width_si"></span><span id="DDK_WIA_DPS_PAGE_WIDTH_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

An application reads the WIA\_DPS\_PAGE\_WIDTH property to determine the physical dimensions of the page that is being scanned. If the extent settings are different from known page sizes, this property reports the width of the page whose [**WIA\_DPS\_PAGE\_SIZE**](wia-dps-page-size.md) property is set to WIA\_PAGE\_CUSTOM. The WIA minidriver creates and maintains WIA\_DPS\_PAGE\_WIDTH.

WIA\_DPS\_PAGE\_WIDTH must provide a measurement equivalent to the value of the [**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md) property, which reports the width, in pixels, of the page to scan.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available for Microsoft Windows XP. For Windows Vista and later, use the identical WIA_IPS_PAGE_WIDTH property.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**WIA\_DPS\_PAGE\_HEIGHT**](wia-dps-page-height.md)

[**WIA\_DPS\_PAGE\_SIZE**](wia-dps-page-size.md)

[**WIA\_IPS\_PAGE\_WIDTH**](wia-ips-page-width.md)

[**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DPS_PAGE_WIDTH%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





