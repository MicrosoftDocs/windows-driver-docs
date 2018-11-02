---
title: WIA\_DPC\_RGB\_GAIN
description: The WIA\_DPC\_RGB\_GAIN property contains a null-terminated Unicode string that represents the red, green, and blue gain, respectively, that is applied to image data.
ms.assetid: 26448818-0885-4084-a0f3-c9e25d15dbf2
keywords: ["WIA_DPC_RGB_GAIN Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_RGB_GAIN
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPC\_RGB\_GAIN


The WIA\_DPC\_RGB\_GAIN property contains a null-terminated Unicode string that represents the red, green, and blue gain, respectively, that is applied to image data. For example, "4:25:50" represents a red gain of 4, a green gain of 25, and a blue gain of 50.

## <span id="ddk_wia_dpc_rgb_gain_si"></span><span id="DDK_WIA_DPC_RGB_GAIN_SI"></span>


Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE or WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

The WIA\_DPC\_RGB\_GAIN property is parsed as follows: *R*:*G*:*B*. *R* represents the red gain, *G* represents the green gain, and *B* represents the blue gain. For example, for an RGB ratio of red=4, green=2, blue=3, the RGB string could be "4:2:3" or "2000:1000:1500". These values are relative to each other. You can use larger numbers for added granularity, but the color will be same if the ratio of red, green, and blue remains the same. The string parser for this property value should support UINT16 integers for *R*, *G*, and *B*.

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

 

 





