---
title: WIA\_IPS\_DESKEW\_X
description: The WIA\_IPS\_DESKEW\_X property, together with the WIA\_IPS\_DESKEW\_Y property, describes the upper two corners of a skewed image. The WIA minidriver creates and maintains this property.
ms.assetid: 0392d392-d814-4691-abb5-a8167bc101bb
keywords: ["WIA_IPS_DESKEW_X Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_DESKEW_X
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_DESKEW\_X


The WIA\_IPS\_DESKEW\_X property, together with the [**WIA\_IPS\_DESKEW\_Y**](wia-ips-deskew-y.md) property, describes the upper two corners of a skewed image. The WIA minidriver creates and maintains this property.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/write

Remarks
-------

The WIA\_IPS\_DESKEW\_X and WIA\_IPS\_DESKEW\_Y properties describe where the two upper corners of a skewed image are located within the bounding rectangle that [**WIA\_IPS\_XPOS**](wia-ips-xpos.md), [**WIA\_IPS\_YPOS**](wia-ips-ypos.md), [**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md), and [**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md) properties define.

The valid values for WIA\_IPS\_DESKEW\_X must be between 0 and (WIA\_IPS\_XEXTENT - 1). A value of 0 means that no skew correction should be performed.

WIA\_IPS\_DESKEW\_X contains the number of pixels in the x-direction from WIA\_IPS\_XPOS to the x-coordinate of the uppermost corner of the image to be corrected.

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
<td><p>Available in Windows Vista and later operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## See also


[**WIA\_IPS\_DESKEW\_Y**](wia-ips-deskew-y.md)

[**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md)

[**WIA\_IPS\_XPOS**](wia-ips-xpos.md)

[**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md)

[**WIA\_IPS\_YPOS**](wia-ips-ypos.md)

 

 






