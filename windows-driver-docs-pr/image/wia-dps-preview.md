---
title: WIA\_DPS\_PREVIEW
description: The WIA\_DPS\_PREVIEW property indicates the preview mode for a device. An application sets this property to place the device into a preview mode.
MS-HAID:
- 'WIA\_PropTable\_af853d91-abb3-4f0a-a026-137aecbf63fa.xml'
- 'image.wia\_dps\_preview'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 410f58c0-479c-44ab-8126-a5dec79b713b
keywords: ["WIA_DPS_PREVIEW Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_PREVIEW
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_DPS\_PREVIEW


The WIA\_DPS\_PREVIEW property indicates the preview mode for a device. An application sets this property to place the device into a preview mode.

## <span id="ddk_wia_dps_preview_si"></span><span id="DDK_WIA_DPS_PREVIEW_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

The following table describes the constants that are valid with the WIA\_DPS\_PREVIEW property.

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
<td><p>WIA_FINAL_SCAN</p></td>
<td><p>The application will perform a final scan.</p></td>
</tr>
<tr class="even">
<td><p>WIA_PREVIEW_SCAN</p></td>
<td><p>The application will perform a preview scan.</p></td>
</tr>
</tbody>
</table>

 

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
<td><p>Available for Microsoft Windows XP. For Windows Vista and later, use the identical WIA_IPS_PREVIEW property.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**WIA\_IPS\_PREVIEW**](wia-ips-preview.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DPS_PREVIEW%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





