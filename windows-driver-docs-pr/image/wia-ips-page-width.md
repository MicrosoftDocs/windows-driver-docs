---
title: WIA\_IPS\_PAGE\_WIDTH
description: The WIA\_IPS\_PAGE\_WIDTH property contains the width of the current page selected, in thousandths of an inch (.001). The WIA minidriver creates and maintains this property.
ms.assetid: b72d32bf-6f1b-4eb2-8f7c-f0de4e2caf26
keywords: ["WIA_IPS_PAGE_WIDTH Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PAGE_WIDTH
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_PAGE\_WIDTH


The WIA\_IPS\_PAGE\_WIDTH property contains the width of the current page selected, in thousandths of an inch (.001). The WIA minidriver creates and maintains this property.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

An application reads WIA\_IPS\_PAGE\_WIDTH to determine the physical dimensions of the page that is being scanned. If the extent settings are different from known page sizes, this property reports the width of the page whose [**WIA\_IPS\_PAGE\_SIZE**](wia-ips-page-size.md) property is set to WIA\_PAGE\_CUSTOM.

WIA\_IPS\_PAGE\_WIDTH must be in sync with the value of WIA\_IPS\_XEXTENT, which reports the width, in pixels, of the page to be scanned.

**Note**   The compatibility layer within the WIA service does not add support for the WIA\_IPS\_PAGE\_WIDTH property to the ADF item that is translated from a Windows XP WIA device if the property is not supported on the child item of the device. Applications should not expect an ADF item to always support WIA\_IPS\_PAGE\_WIDTH and should always check if it is supported at run time. (Typically, applications should check the support for any property to be negotiated.)

 

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
<td><p>Available in Windows Vista and later operating systems. For Windows XP, use the WIA_DPS_PAGE_WIDTH property instead.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## See also


[**WIA\_DPS\_PAGE\_WIDTH**](wia-dps-page-width.md)

[**WIA\_IPS\_PAGE\_HEIGHT**](wia-ips-page-height.md)

[**WIA\_IPS\_PAGE\_SIZE**](wia-ips-page-size.md)

 

 






