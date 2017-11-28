---
title: WIA\_DPC\_WHITE\_BALANCE
description: The WIA\_DPC\_WHITE\_BALANCE property specifies how a digital camera blends color channels.
ms.assetid: f0f9dd8e-940a-4a42-b6d7-1d1e86c0a530
keywords: ["WIA_DPC_WHITE_BALANCE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_WHITE_BALANCE
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_DPC\_WHITE\_BALANCE


The WIA\_DPC\_WHITE\_BALANCE property specifies how a digital camera blends color channels.

## <span id="ddk_wia_dpc_white_balance_si"></span><span id="DDK_WIA_DPC_WHITE_BALANCE_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

The following table describes possible values for the WIA\_DPC\_WHITE\_BALANCE property:

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
<td><p>WHITEBALANCE_AUTO</p></td>
<td><p>The camera uses an automatic mechanism to set the white balance.</p></td>
</tr>
<tr class="even">
<td><p>WHITEBALANCE_DAYLIGHT</p></td>
<td><p>The camera sets the white balance to a value that is appropriate for use in daylight conditions.</p></td>
</tr>
<tr class="odd">
<td><p>WHITEBALANCE_FLASH</p></td>
<td><p>The camera sets the white balance to a value that is appropriate for use with an electronic flash.</p></td>
</tr>
<tr class="even">
<td><p>WHITEBALANCE_FLORESCENT</p></td>
<td><p>The camera sets the white balance to a value that is appropriate for use with a fluorescent light source.</p></td>
</tr>
<tr class="odd">
<td><p>WHITEBALANCE_MANUAL</p></td>
<td><p>Your driver can set the white balance directly by using the [<strong>WIA_DPC_RGB_GAIN</strong>](wia-dpc-rgb-gain.md) property.</p></td>
</tr>
<tr class="even">
<td><p>WHITEBALANCE_ONEPUSH_AUTO</p></td>
<td><p>The camera determines the white balance setting when a user presses the capture button while pointing the camera at a white surface.</p></td>
</tr>
<tr class="odd">
<td><p>WHITEBALANCE_TUNGSTEN</p></td>
<td><p>The camera sets the white balance to a value that is appropriate for use with a tungsten light source.</p></td>
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
<td><p>Obsolete in Windows Vista and later operating systems and should no longer be used. However, this property is still defined in Windows Vista for compatibility with applications and devices designed for Windows Server 2003, Windows XP, and previous versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**WIA\_DPC\_RGB\_GAIN**](wia-dpc-rgb-gain.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DPC_WHITE_BALANCE%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





