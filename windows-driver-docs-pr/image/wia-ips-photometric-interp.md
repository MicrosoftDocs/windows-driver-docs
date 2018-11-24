---
title: WIA\_IPS\_PHOTOMETRIC\_INTERP
description: The WIA\_IPS\_PHOTOMETRIC\_INTERP property contains the current setting for white and black pixels. The WIA minidriver creates and maintains this property.
ms.assetid: 5d48ec37-68bb-446a-9236-c88d26f8a549
keywords: ["WIA_IPS_PHOTOMETRIC_INTERP Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PHOTOMETRIC_INTERP
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_PHOTOMETRIC\_INTERP


The WIA\_IPS\_PHOTOMETRIC\_INTERP property contains the current setting for white and black pixels. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ips_photometric_interp_si"></span><span id="DDK_WIA_IPS_PHOTOMETRIC_INTERP_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

An application reads the WIA\_IPS\_PHOTOMETRIC\_INTERP property to determine the value assigned to white or black pixels (depending on what the application is doing).

The following table describes the constants that are valid with WIA\_IPS\_PHOTOMETRIC\_INTERP.

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
<td><p>WIA_PHOTO_WHITE_0</p></td>
<td><p>White is 0, and black is 1.</p></td>
</tr>
<tr class="even">
<td><p>WIA_PHOTO_WHITE_1</p></td>
<td><p>White is 1, and black is 0.</p></td>
</tr>
</tbody>
</table>

 

If a device can be set to only a single value, create a WIA\_PROP\_LIST type, and place the valid value in it.

The WIA\_IPS\_PHOTOMETRIC\_INTERP property is required for all image acquisition items and stored images.

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

 

 





