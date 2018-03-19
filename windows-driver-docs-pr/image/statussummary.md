---
title: StatusSummary element
description: The required StatusSummary element contains a summary of the scan device's current status.
ms.assetid: cb361b3b-bd73-449d-9f31-0c1aea882330
keywords: ["StatusSummary element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn StatusSummary
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# StatusSummary element


The required **StatusSummary** element contains a summary of the scan device's current status.

Usage
-----

``` syntax
<wscn:StatusSummary>
  child elements
</wscn:StatusSummary>
```

Attributes
----------

There are no attributes.

## Child elements


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
<td><p>[<strong>ScannerState</strong>](scannerstate.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ScannerStateReasons</strong>](scannerstatereasons.md)</p></td>
</tr>
</tbody>
</table>

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
<td><p>[<strong>ScannerStatusSummaryEvent</strong>](scannerstatussummaryevent.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The WSD Scan Service must include the **StatusSummary** element when it sends a [**ScannerStatusSummaryEvent**](scannerstatussummaryevent.md) event element to the client. The scanner's current state and reasons for why it is in this state are specified in the [**ScannerState**](scannerstate.md) and [**ScannerStateReasons**](scannerstatereasons.md) elements, respectively.

## <span id="see_also"></span>See also


[**ScannerStateReasons**](scannerstatereasons.md)

[**ScannerState**](scannerstate.md)

**ScannerStateReasons**
[**ScannerStatusSummaryEvent**](scannerstatussummaryevent.md)

 

 






