---
title: WIA\_IPS\_XRES
description: The WIA\_IPS\_XRES property contains the current horizontal resolution, in pixels per inch, for a device.
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
ms.date: 11/28/2017
ms.localizationpriority: medium
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

## See also


[**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md)

[**WIA\_IPS\_XPOS**](wia-ips-xpos.md)

[**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md)

[**WIA\_IPS\_YPOS**](wia-ips-ypos.md)

[**WIA\_IPS\_YRES**](wia-ips-yres.md)

 

 






