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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DPS_PLATEN_COLOR%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




