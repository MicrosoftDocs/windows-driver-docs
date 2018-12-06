---
title: WIA\_DPS\_PAGE\_WIDTH
description: The WIA\_DPS\_PAGE\_WIDTH property contains the width of the currently selected page, in thousandths of an inch (.001).
ms.assetid: 02787660-3fb3-4e5d-ade8-b11ad29412c1
keywords: ["WIA_DPS_PAGE_WIDTH Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_PAGE_WIDTH
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPS\_PAGE\_WIDTH


The WIA\_DPS\_PAGE\_WIDTH property contains the width of the currently selected page, in thousandths of an inch (.001).

## <span id="ddk_wia_dps_page_width_si"></span><span id="DDK_WIA_DPS_PAGE_WIDTH_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

An application reads the WIA\_DPS\_PAGE\_WIDTH property to determine the physical dimensions of the page that is being scanned. If the extent settings are different from known page sizes, this property reports the width of the page whose [**WIA\_DPS\_PAGE\_SIZE**](wia-dps-page-size.md) property is set to WIA\_PAGE\_CUSTOM. The WIA minidriver creates and maintains WIA\_DPS\_PAGE\_WIDTH.

WIA\_DPS\_PAGE\_WIDTH must provide a measurement equivalent to the value of the [**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md) property, which reports the width, in pixels, of the page to scan.

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
<td><p>Available for Microsoft Windows XP. For Windows Vista and later, use the identical WIA_IPS_PAGE_WIDTH property.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## See also


[**WIA\_DPS\_PAGE\_HEIGHT**](wia-dps-page-height.md)

[**WIA\_DPS\_PAGE\_SIZE**](wia-dps-page-size.md)

[**WIA\_IPS\_PAGE\_WIDTH**](wia-ips-page-width.md)

[**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md)

 

 






