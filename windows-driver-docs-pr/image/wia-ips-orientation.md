---
title: WIA\_IPS\_ORIENTATION
description: The WIA\_IPS\_ORIENTATION property describes the current orientation of the document to scan. The WIA minidriver creates and maintains this property.
ms.assetid: e963d0d1-020c-4ec1-8b67-a89b1fd3e545
keywords: ["WIA_IPS_ORIENTATION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_ORIENTATION
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPS\_ORIENTATION


The WIA\_IPS\_ORIENTATION property describes the current orientation of the document to scan. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ips_orientation_si"></span><span id="DDK_WIA_IPS_ORIENTATION_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

An application sets the WIA\_IPS\_ORIENTATION property to define the original orientation of a page or image to be acquired. For more information about how to use WIA\_IPS\_ORIENTATION, see [**WIA\_DPS\_PAGE\_SIZE**](wia-dps-page-size.md).

The following table describes the constants that are valid with WIA\_IPS\_ORIENTATION.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>LANSCAPE</p></td>
<td><p>The orientation is a 90-degree counterclockwise rotation, relative to the PORTRAIT orientation.</p></td>
</tr>
<tr class="even">
<td><p>PORTRAIT</p></td>
<td><p>The orientation is at 0 degrees.</p></td>
</tr>
<tr class="odd">
<td><p>ROT180</p></td>
<td><p>The orientation is a 180-degree counterclockwise rotation, relative to the PORTRAIT orientation.</p></td>
</tr>
<tr class="even">
<td><p>ROT270</p></td>
<td><p>The orientation is a 270-degree counterclockwise rotation, relative to the PORTRAIT orientation.</p></td>
</tr>
</tbody>
</table>

 

The WIA\_IPS\_ORIENTATION property describes the orientation of the document to scan. This property affects the current scan frame and available page sizes.

WIA\_IPS\_ORIENTATIONis different from the [**WIA\_IPS\_ROTATION**](wia-ips-rotation.md) property, which refers to a rotation that is applied to an image *after* it is scanned. So, a ROT180 value for WIA\_IPS\_ORIENTATION is different from a ROT180 value for WIA\_IPS\_ROTATION. For WIA\_IPS\_ORIENTATION, ROT180 describes the orientation of the physical document to scan, relative to the scan direction, and for WIA\_IPS\_ROTATION, ROT180 describes the rotation to apply to an image after it is scanned.

The WIA\_IPS\_ORIENTATION property is required for ADF items and optional for all other image acquisition items.

**Note**   The compatibility layer within the WIA service does not add support for WIA\_IPS\_ORIENTATION to the ADF item that is translated from a Microsoft Windows XP WIA device if the property is not supported on the child item of the device. Applications should not expect that an ADF item will always support this property and should always check if WIA\_IPS\_ORIENTATION is supported at run time.

 

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


[**WIA\_DPS\_PAGE\_SIZE**](wia-dps-page-size.md)

[**WIA\_IPS\_ROTATION**](wia-ips-rotation.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_ORIENTATION%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





