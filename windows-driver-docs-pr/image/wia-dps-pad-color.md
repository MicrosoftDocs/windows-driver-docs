---
title: WIA\_DPS\_PAD\_COLOR
description: The WIA\_DPS\_PAD\_COLOR property contains the current pad color that is used when the WIA minidriver pads unaligned data. The WIA minidriver creates and maintains this property.
ms.assetid: db78fc1b-72e4-4edc-8f4f-9209e6b36aa6
keywords: ["WIA_DPS_PAD_COLOR Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_PAD_COLOR
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPS\_PAD\_COLOR


The WIA\_DPS\_PAD\_COLOR property contains the current pad color that is used when the WIA minidriver pads unaligned data. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_dps_pad_color_si"></span><span id="DDK_WIA_DPS_PAD_COLOR_SI"></span>


Property Type: VT\_UI1 | VT\_VECTOR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read/write

Remarks
-------

The WIA\_DPS\_PAD\_COLOR property should be reported as a vector of four BYTE values in the form of an RGBQUAD structure (which is described in the Microsoft Windows SDK documentation).

An application reads WIA\_DPS\_PAD\_COLOR to get the padding color that is used.

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

 

 





