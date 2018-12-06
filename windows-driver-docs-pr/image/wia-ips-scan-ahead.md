---
title: WIA\_IPS\_SCAN\_AHEAD
description: The WIA\_IPS\_SCAN\_AHEAD property is used to enable scan ahead in the hardware device (scan at highest possible speed, buffering scanned images in the scanner's internal memory, transferring buffered images in parallel to the client application at an equal or lower speed). The WIA minidriver creates and maintains this property.
ms.assetid: 706BA423-399F-4859-BF41-10D3A88B61DD
keywords: ["WIA_IPS_SCAN_AHEAD Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_SCAN_AHEAD
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_SCAN\_AHEAD


The **WIA\_IPS\_SCAN\_AHEAD** property is used to enable scan ahead in the hardware device (scan at highest possible speed, buffering scanned images in the scanner's internal memory, transferring buffered images in parallel to the client application at an equal or lower speed). The WIA minidriver creates and maintains this property.




**Note**  This property replaces [**WIA\_DPS\_SCAN\_AHEAD\_PAGES**](wia-dps-scan-ahead-pages.md), which is now obsolete.

 

Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/Write

Remarks
-------

The following table describes the valid values for the **WIA\_IPS\_SCAN\_AHEAD** property.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WIA_SCAN_AHEAD_DISABLED</p></td>
<td><p>Scan ahead is disabled. This is the required default value if the property is supported.</p></td>
</tr>
<tr class="even">
<td><p>WIA_SCAN_AHEAD_ENABLED</p></td>
<td><p>Scan ahead is enabled. The WIA client application must download images as fast as it can. If the scan job is canceled before it is finished, some scanned documents may be lost (not yet transferred to the application).</p></td>
</tr>
</tbody>
</table>

 

This property is valid only for the Feeder item (WIA\_CATEGORY\_FEEDER) and is optional.

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


[**WIA\_DPS\_SCAN\_AHEAD\_PAGES**](wia-dps-scan-ahead-pages.md)

 

 






