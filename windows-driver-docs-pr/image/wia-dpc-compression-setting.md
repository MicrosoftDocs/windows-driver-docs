---
title: WIA\_DPC\_COMPRESSION\_SETTING
description: The WIA\_DPC\_COMPRESSION\_SETTING property contains either a range or a list of integers to represent perceived image quality.
ms.assetid: dfe22ff2-f613-49a5-8c55-38ba851e7ebd
keywords: ["WIA_DPC_COMPRESSION_SETTING Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_COMPRESSION_SETTING
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPC\_COMPRESSION\_SETTING


The WIA\_DPC\_COMPRESSION\_SETTING property contains either a range or a list of integers to represent perceived image quality.

## <span id="ddk_wia_dpc_compression_setting_si"></span><span id="DDK_WIA_DPC_COMPRESSION_SETTING_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST or WIA\_PROP\_RANGE

Access Rights: Read/write

Remarks
-------

The WIA\_DPC\_COMPRESSION\_SETTING property is intended to approximately linearly describe the perceived image quality over a broad range of scene content. Smaller integers represent lower quality (that is, maximum compression), and larger integers represent higher quality (that is, minimum compression). Any available settings on a device are relative only to that device and are therefore device-specific.

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

 

 





