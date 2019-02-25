---
title: WIA\_DPS\_PLATEN\_COLOR
description: The WIA\_DPS\_PLATEN\_COLOR property contains the current platen color.
ms.assetid: d1bc9bc8-ad23-48b8-8456-21aa3556ab69
keywords: ["WIA_DPS_PLATEN_COLOR Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_PLATEN_COLOR
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPS\_PLATEN\_COLOR


The WIA\_DPS\_PLATEN\_COLOR property contains the current platen color.

## <span id="ddk_wia_dps_platen_color_si"></span><span id="DDK_WIA_DPS_PLATEN_COLOR_SI"></span>


Property Type: VT\_UI1 | VT\_VECTOR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

A minidriver should report the WIA\_DPS\_PLATEN\_COLOR as a vector of four BYTE values in the form of an RGBQUAD structure (which is described in the Microsoft Windows SDK documentation). The WIA minidriver creates and maintains this property.

An application reads WIA\_DPS\_PLATEN\_COLOR to get the scanner's platen color. This color can help the application post-process the final image.

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

 

 





