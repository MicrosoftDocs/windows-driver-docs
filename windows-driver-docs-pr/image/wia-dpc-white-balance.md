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
ms.date: 11/28/2017
ms.localizationpriority: medium
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
<td><p>Your driver can set the white balance directly by using the <a href="wia-dpc-rgb-gain.md" data-raw-source="[&lt;strong&gt;WIA_DPC_RGB_GAIN&lt;/strong&gt;](wia-dpc-rgb-gain.md)"><strong>WIA_DPC_RGB_GAIN</strong></a> property.</p></td>
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

## See also


[**WIA\_DPC\_RGB\_GAIN**](wia-dpc-rgb-gain.md)

 

 






