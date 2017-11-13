---
title: WIA\_IPS\_PHOTOMETRIC\_INTERP
description: The WIA\_IPS\_PHOTOMETRIC\_INTERP property contains the current setting for white and black pixels. The WIA minidriver creates and maintains this property.
MS-HAID:
- 'WIA\_PropTable\_1c5f7396-e770-4cde-8b84-9a2b6b8f1ca1.xml'
- 'image.wia\_ips\_photometric\_interp'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_PHOTOMETRIC_INTERP%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




