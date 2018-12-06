---
title: WIA\_DPC\_COPYRIGHT\_INFO
description: The WIA\_DPC\_COPYRIGHT\_INFO property contains the copyright notification.
ms.assetid: 6945f121-46db-4287-a31a-80c26bd852da
keywords: ["WIA_DPC_COPYRIGHT_INFO Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_COPYRIGHT_INFO
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPC\_COPYRIGHT\_INFO


The WIA\_DPC\_COPYRIGHT\_INFO property contains the copyright notification.

## <span id="ddk_wia_dpc_copyright_info_si"></span><span id="DDK_WIA_DPC_COPYRIGHT_INFO_SI"></span>


Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read/write

Remarks
-------

A device uses the WIA\_DPC\_COPYRIGHT\_INFO property to populate the Copyright field in every EXIF image that it captures.

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

 

 





