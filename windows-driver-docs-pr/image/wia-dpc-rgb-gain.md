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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DPC_RGB_GAIN%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




