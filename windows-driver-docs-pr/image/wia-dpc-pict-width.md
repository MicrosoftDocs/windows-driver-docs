---
title: WIA\_DPC\_PICT\_WIDTH
description: The WIA\_DPC\_PICT\_WIDTH property describes the width, in pixels, to use for newly captured images.
ms.assetid: 08ff2ef6-1c65-4a46-bf17-f7c5126279d4
keywords: ["WIA_DPC_PICT_WIDTH Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_PICT_WIDTH
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPC\_PICT\_WIDTH


The WIA\_DPC\_PICT\_WIDTH property describes the width, in pixels, to use for newly captured images.

## <span id="ddk_wia_dpc_pict_width_si"></span><span id="DDK_WIA_DPC_PICT_WIDTH_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST or WIA\_PROP\_RANGE

Access Rights: Read/write

Remarks
-------

The list of valid values for the WIA\_DPC\_PICT\_WIDTH property has a one-to-one correspondence to the list of valid values for the [**WIA\_DPC\_PICT\_HEIGHT**](wia-dpc-pict-height.md) property. If the individual width and height are linearly settable and orthogonal to each other, you can express them as a range.

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


[**WIA\_DPC\_PICT\_HEIGHT**](wia-dpc-pict-height.md)

 

 






