---
title: WIA\_DPS\_SCAN\_AHEAD\_PAGES
description: The WIA\_DPS\_SCAN\_AHEAD\_PAGES property contains a value that indicates whether a scanner will cache pages in a scanner buffer before sending them to an application.
ms.assetid: 8c00b029-dc9f-43e1-af4a-088e143351ca
keywords: ["WIA_DPS_SCAN_AHEAD_PAGES Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_SCAN_AHEAD_PAGES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPS\_SCAN\_AHEAD\_PAGES


The WIA\_DPS\_SCAN\_AHEAD\_PAGES property contains a value that indicates whether a scanner will cache pages in a scanner buffer before sending them to an application.

## <span id="ddk_wia_dps_scan_ahead_pages_si"></span><span id="DDK_WIA_DPS_SCAN_AHEAD_PAGES_SI"></span>


**Note**  This property is now obsolete. Use [**WIA\_IPS\_SCAN\_AHEAD**](wia-ips-scan-ahead.md) instead.

 

Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE (from zero through the maximum number of pages that the document feeder can hold)

Access Rights: Read/write

Remarks
-------

If the WIA\_DPS\_SCAN\_AHEAD\_PAGES property is zero, scan ahead is disabled, and the scanner will not scan ahead any pages.

If the scanner performs data transfers on the buffered scan-ahead item, the scanner will retrieve the buffered pages. WIA properties cannot be changed during a scan-ahead operation. WIA\_DPS\_SCAN\_AHEAD\_PAGES is optional.

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

## See also


[**WIA\_IPS\_SCAN\_AHEAD**](wia-ips-scan-ahead.md)

 

 






