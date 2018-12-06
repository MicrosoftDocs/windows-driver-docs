---
title: WIA\_DIP\_WIA\_VERSION
description: The WIA\_DIP\_WIA\_VERSION property contains the number (as a string) of the current WIA version that is installed on a computer. The WIA service creates and maintains this property.
ms.assetid: 6d849fc1-c22f-4839-a27d-7198f6e362fc
keywords: ["WIA_DIP_WIA_VERSION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DIP_WIA_VERSION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DIP\_WIA\_VERSION


The WIA\_DIP\_WIA\_VERSION property contains the number (as a string) of the current WIA version that is installed on a computer. The WIA service creates and maintains this property.

## <span id="ddk_wia_dip_wia_version_si"></span><span id="DDK_WIA_DIP_WIA_VERSION_SI"></span>


Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

An application reads WIA\_DIP\_WIA\_VERSION to determine the version of WIA that is installed on the computer.

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
<td><p>Available in Microsoft Windows XP and later operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 





