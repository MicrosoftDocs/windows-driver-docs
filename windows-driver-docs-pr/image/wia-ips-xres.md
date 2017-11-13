---
title: WIA\_IPS\_XRES
description: The WIA\_IPS\_XRES property contains the current horizontal resolution, in pixels per inch, for a device.
MS-HAID:
- 'WIA\_PropTable\_4e3539d2-1541-4622-b41d-0d8a65793123.xml'
- 'image.wia\_ips\_xres'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: cde64e80-b4b0-4360-a14e-b6918b97aabc
keywords: ["WIA_IPS_XRES Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_XRES
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPS\_XRES


The WIA\_IPS\_XRES property contains the current horizontal resolution, in pixels per inch, for a device.

## <span id="ddk_wia_ips_xres_si"></span><span id="DDK_WIA_IPS_XRES_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE or WIA\_PROP\_LIST

Access Rights: Read/write or read-only

Remarks
-------

An application sets the WIA\_IPS\_XRES property to set the horizontal resolution. The WIA minidriver creates and maintains this property.

If a device can be set to only a single value, create a WIA\_PROP\_LIST type and place the valid value in it. This situation also applies when one resolution setting depends on another resolution. (For example, the vertical resolution can depend on the horizontal resolution.)

WIA\_IPS\_XRES is required for all image acquisition-enabled items and stored image items; it is not available for storage items.

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


[**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md)

[**WIA\_IPS\_XPOS**](wia-ips-xpos.md)

[**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md)

[**WIA\_IPS\_YPOS**](wia-ips-ypos.md)

[**WIA\_IPS\_YRES**](wia-ips-yres.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_XRES%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





