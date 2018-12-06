---
title: WIA\_DPC\_EXPOSURE\_INDEX
description: The WIA\_DPC\_EXPOSURE\_INDEX property enables you to emulate film speed settings on a digital camera.
ms.assetid: 805efbf0-b81f-49fd-82be-536d471d255e
keywords: ["WIA_DPC_EXPOSURE_INDEX Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_EXPOSURE_INDEX
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPC\_EXPOSURE\_INDEX


The WIA\_DPC\_EXPOSURE\_INDEX property enables you to emulate film speed settings on a digital camera.

## <span id="ddk_wia_dpc_exposure_index_si"></span><span id="DDK_WIA_DPC_EXPOSURE_INDEX_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST or WIA\_PROP\_RANGE

Access Rights: Read/write

Remarks
-------

Film speed settings correspond to the ISO designations (ASA/DIN). Typically, a device supports discrete enumerated values, but continuous control over a range of values is possible. A value of 0xFFFF for the WIA\_DPC\_EXPOSURE\_INDEX property corresponds to the Automatic ISO setting.

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

 

 





