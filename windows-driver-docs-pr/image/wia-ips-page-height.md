---
title: WIA\_IPS\_PAGE\_HEIGHT
description: The WIA\_IPS\_PAGE\_HEIGHT property contains the height, in thousandths of an inch (.001), of the currently selected page. The WIA minidriver creates and maintains this property.
ms.assetid: f8721f87-641c-4da8-ad3a-a38bf18d3111
keywords: ["WIA_IPS_PAGE_HEIGHT Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PAGE_HEIGHT
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_PAGE\_HEIGHT


The WIA\_IPS\_PAGE\_HEIGHT property contains the height, in thousandths of an inch (.001), of the currently selected page. The WIA minidriver creates and maintains this property.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

An application reads WIA\_IPS\_PAGE\_HEIGHT to determine the physical dimensions of the page that is being scanned. If the extent settings are different from the known page sizes, this property reports the height of the page whose [**WIA\_IPS\_PAGE\_SIZE**](wia-ips-page-size.md) property is set to WIA\_PAGE\_CUSTOM.

WIA\_IPS\_PAGE\_HEIGHT must provide a measurement in thousandths of an inch that is equivalent to the pixel value that is reported by [**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md), which reports the height, in pixels, of the page to be scanned.

**Note**  The compatibility layer within the WIA service does not add support for the WIA\_IPS\_PAGE\_HEIGHT property to the ADF item that is translated from a Windows XP WIA device if the property is not supported on the child item of the device. Applications should not expect that an ADF item will always support WIA\_IPS\_PAGE\_HEIGHT and should always check if it is supported at run time. (Applications should typically check for this support for any property that is be negotiated.)

 

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
<td><p>Available in Windows Vista and later operating systems. For Windows XP, use the WIA_DPS_PAGE_HEIGHT property instead.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## See also


[**WIA\_DPS\_PAGE\_HEIGHT**](wia-dps-page-height.md)

[**WIA\_IPS\_PAGE\_SIZE**](wia-ips-page-size.md)

[**WIA\_IPS\_PAGE\_WIDTH**](wia-ips-page-width.md)

[**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md)

 

 






