---
title: ScannerCurrentTime element
description: The required ScannerCurrentTime element indicates the current date and time according to the scanner's internal clock.
ms.assetid: 7103fdb4-dfa4-40b0-b20e-022e2a42bf5c
keywords: ["ScannerCurrentTime element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScannerCurrentTime
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ScannerCurrentTime element


The required **ScannerCurrentTime** element indicates the current date and time according to the scanner's internal clock.

Usage
-----

```xml
<wscn:ScannerCurrentTime>
  text
</wscn:ScannerCurrentTime>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. Any valid value for the dateTime type. For more information about dateTime, see XML Schema Part 2: Datatypes Second Edition.**dateTimedateTime**

## Child elements


There are no child elements.

## Parent elements


<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="scannerstatus.md" data-raw-source="[&lt;strong&gt;ScannerStatus&lt;/strong&gt;](scannerstatus.md)"><strong>ScannerStatus</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The scanner's internal clock does not have to be a real-time clock. The clock can start at zero (0001-01-01T00:00:00Z) and start counting up when the device is turned on.

All times are based on the time at startup, so the client can calculate duration and relative time by reading the **ScannerCurrentTime** element and comparing it to the previous time value.

## See also


[**ScannerStatus**](scannerstatus.md)

 

 






