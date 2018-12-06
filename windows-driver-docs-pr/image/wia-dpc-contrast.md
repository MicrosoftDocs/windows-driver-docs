---
title: WIA\_DPC\_CONTRAST
description: The WIA\_DPC\_CONTRAST property indicates the perceived contrast of a captured image.
ms.assetid: 78477714-0cf3-464c-9d32-7aba0b7def16
keywords: ["WIA_DPC_CONTRAST Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_CONTRAST
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPC\_CONTRAST


The WIA\_DPC\_CONTRAST property indicates the perceived contrast of a captured image.

## <span id="ddk_wia_dpc_contrast_si"></span><span id="DDK_WIA_DPC_CONTRAST_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST or WIA\_PROP\_RANGE

Access Rights: Read/write

Remarks
-------

The WIA\_DPC\_CONTRAST property can contain either a list of values or a range of values.

The minimum supported value for WIA\_DPC\_CONTRAST represents the least amount of contrast, and the maximum value represents the most contrast. Typically, a value in the middle of the range represents normal, or default, contrast.

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

 

 





