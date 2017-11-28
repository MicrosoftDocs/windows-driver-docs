---
title: WIA\_IPS\_PATCH\_CODE\_SEARCH\_DIRECTION
description: The WIA\_IPS\_PATCH\_CODE\_SEARCH\_DIRECTION property is used to configure the direction (relative to the scan direction) in which the device searches for patch codes on each scan document page.
ms.assetid: 24541B0D-4B9B-439F-8454-AFDD3D16A448
keywords: ["WIA_IPS_PATCH_CODE_SEARCH_DIRECTION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PATCH_CODE_SEARCH_DIRECTION
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPS\_PATCH\_CODE\_SEARCH\_DIRECTION


The **WIA\_IPS\_PATCH\_CODE\_SEARCH\_DIRECTION** property is used to configure the direction (relative to the scan direction) in which the device searches for patch codes on each scan document page.

## <span id="ddk_wia_ipa_depth_si"></span><span id="DDK_WIA_IPA_DEPTH_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/Write

Remarks
-------

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
<td><p>WIA_PATCH_CODE_HORIZONTAL_SEARCH</p></td>
<td><p>Device searches for patch codes horizontally.</p></td>
</tr>
<tr class="even">
<td><p>WIA_PATCH_CODE_VERTICAL_SEARCH</p></td>
<td><p>Device searches for patch codes vertically.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_PATCH_CODE_HORIZONTAL_VERTICAL_SEARCH</p></td>
<td><p>Device searches for patch codes first horizontally then vertically.</p></td>
</tr>
<tr class="even">
<td><p>WIA_PATCH_CODE_VERTICAL_HORIZONTAL_SEARCH</p></td>
<td><p>Device searches for patch codes first vertically then horizontally.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_PATCH_CODE_AUTO_SEARCH</p></td>
<td><p>Device searches for patch codes in its own direction that is automatically detected at run-time or predefined.</p></td>
</tr>
</tbody>
</table>

 

This property is required for all Patch Code Reader items but it can be implemented to support only the WIA\_PATCH\_CODE\_AUTO\_SEARCH value.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_PATCH_CODE_SEARCH_DIRECTION%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




