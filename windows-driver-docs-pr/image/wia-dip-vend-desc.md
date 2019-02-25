---
title: WIA\_DIP\_VEND\_DESC
description: The WIA\_DIP\_VEND\_DESC property contains a vendor description string for the WIA minidriver. The WIA service creates and maintains this property.
ms.assetid: 80bb6a4e-3391-4681-93d0-8b60774dfc3d
keywords: ["WIA_DIP_VEND_DESC Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DIP_VEND_DESC
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DIP\_VEND\_DESC


The WIA\_DIP\_VEND\_DESC property contains a vendor description string for the WIA minidriver. The WIA service creates and maintains this property.

## <span id="ddk_wia_dip_vend_desc_si"></span><span id="DDK_WIA_DIP_VEND_DESC_SI"></span>


Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The vendor description is obtained from the INF file. An application reads the WIA\_DIP\_VEND\_DESC property to get a description of the device vendor.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 





