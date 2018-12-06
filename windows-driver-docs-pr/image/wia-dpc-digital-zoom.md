---
title: WIA\_DPC\_DIGITAL\_ZOOM
description: The WIA\_DPC\_DIGITAL\_ZOOM property contains the effective zoom ratio of a digital camera's acquired image, scaled by a factor of 10.
ms.assetid: 5f1ec791-fd51-4397-ac7d-5012c020ef0a
keywords: ["WIA_DPC_DIGITAL_ZOOM Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_DIGITAL_ZOOM
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPC\_DIGITAL\_ZOOM


The WIA\_DPC\_DIGITAL\_ZOOM property contains the effective zoom ratio of a digital camera's acquired image, scaled by a factor of 10.

## <span id="ddk_wia_dpc_digital_zoom_si"></span><span id="DDK_WIA_DPC_DIGITAL_ZOOM_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST or WIA\_PROP\_RANGE

Access Rights: Read/write

Remarks
-------

A WIA\_DPC\_DIGITAL\_ZOOM value of 10 corresponds to the absence of digital zoom (1X), which is the standard scene size that the camera captures. A value of 20 corresponds to a 2X zoom, where the camera captures one-fourth of the standard scene size.

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

 

 





