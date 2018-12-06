---
title: WIA\_IPS\_ROTATION
description: The WIA\_IPS\_ROTATION property contains the current rotation setting for image rotation, if it is implemented. The WIA minidriver creates and maintains this property.
ms.assetid: 5d117d55-b7e4-46eb-aeb5-54636749081f
keywords: ["WIA_IPS_ROTATION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_ROTATION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_ROTATION


The WIA\_IPS\_ROTATION property contains the current rotation setting for image rotation, if it is implemented. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ips_rotation_si"></span><span id="DDK_WIA_IPS_ROTATION_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

An application sets the WIA\_IPS\_ROTATION property to inform a driver how much (if at all) to rotate an image before the driver returns it to the application.

The following table describes the rotation constants that are defined for WIA\_IPS\_ROTATION.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Constant</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PORTRAIT</p></td>
<td><p>The driver will not rotate the image.</p></td>
</tr>
<tr class="even">
<td><p>LANSCAPE</p></td>
<td><p>The driver rotates the image 90 degrees counterclockwise.</p></td>
</tr>
<tr class="odd">
<td><p>ROT180</p></td>
<td><p>The driver rotates the image 180 degrees counterclockwise.</p></td>
</tr>
<tr class="even">
<td><p>ROT270</p></td>
<td><p>The driver rotates the image 270 degrees counterclockwise.</p></td>
</tr>
</tbody>
</table>

 

The WIA minidriver is responsible for rotating image data before sending it back to the application. The application is responsible for checking the image headers to see the newly rotated values.

It can be difficult to understand the effect of rotation on the current image's selection area (which is defined by the [**WIA\_IPS\_XPOS**](wia-ips-xpos.md), [**WIA\_IPS\_YPOS**](wia-ips-ypos.md), [**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md), and [**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md) properties).

*Selection area* refers to the selected area on the physical scanner bed that an image is be acquired from. The WIA\_IPS\_ROTATION property does *not* modify the selection area. The driver applies a counterclockwise rotation according to WIA\_IPS\_ROTATION only after the driver has acquired the appropriate selection area. WIA\_IPS\_ROTATION *does* affect the dimensions of the output image, so these dimensions must be reflected in the resulting image's data header.

[**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md) is not related to [**WIA\_IPS\_ORIENTATION**](wia-ips-orientation.md). WIA\_IPS\_ORIENTATION describes the orientation of the document to be scanned relative to the direction of the scan; in contrast, WIA\_IPS\_ROTATION describes the rotation that is to be applied to an image after it is scanned.

WIA\_IPS\_ORIENTATION can impact the area to be scanned. Not all page sizes are available in both landscape and portrait, and the extents of the image from an change in WIA\_IPS\_ORIENTATION could crop the image. WIA\_IPS\_ROTATION does not impact the image extents and is not related to the orientation of the document that is to be scanned.

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


[**WIA\_IPS\_ORIENTATION**](wia-ips-orientation.md)

[**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md)

[**WIA\_IPS\_XPOS**](wia-ips-xpos.md)

[**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md)

[**WIA\_IPS\_YPOS**](wia-ips-ypos.md)

 

 






