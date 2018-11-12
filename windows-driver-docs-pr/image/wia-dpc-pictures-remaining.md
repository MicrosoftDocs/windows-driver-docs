---
title: WIA\_DPC\_PICTURES\_REMAINING
description: The WIA\_DPC\_PICTURES\_REMAINING property contains the number of pictures that a user can take by using a camera device, given the current property settings. The WIA minidriver creates and maintains this property.
ms.assetid: ac6cd3e0-c6fe-4783-8094-67083e308308
keywords: ["WIA_DPC_PICTURES_REMAINING Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_PICTURES_REMAINING
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPC\_PICTURES\_REMAINING


The WIA\_DPC\_PICTURES\_REMAINING property contains the number of pictures that a user can take by using a camera device, given the current property settings. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_dpc_pictures_remaining_si"></span><span id="DDK_WIA_DPC_PICTURES_REMAINING_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

If the WIA\_DPC\_PICTURES\_REMAINING property settings change and the changes affect the size of the images that the camera device produces, the WIA minidriver should update the number of remaining pictures.

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

 

 





