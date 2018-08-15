---
title: ScannerStateReasons element
description: The required ScannerStateReasons element is a list of ScannerStateReason elements that describes all of the reasons why the scanner is in its current state.
ms.assetid: 1b4e6537-4175-4bed-9af3-7887a2737784
keywords: ["ScannerStateReasons element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScannerStateReasons
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# ScannerStateReasons element


The required **ScannerStateReasons** element is a list of [**ScannerStateReason**](scannerstatereason.md) elements that describes all of the reasons why the scanner is in its current state.

Usage
-----

``` syntax
<wscn:ScannerStateReasons>
  child elements
</wscn:ScannerStateReasons>
```

Attributes
----------

There are no attributes.

Text value
----------

None

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
<td><p>[<strong>ScannerStateReason</strong>](scannerstatereason.md)</p></td>
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
<td><p>[<strong>ScannerStatus</strong>](scannerstatus.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>StatusSummary</strong>](statussummary.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **ScannerStateReasons** element is a list of **ScannerStateReason** elements, each of which describes a reason why the scanner is in its current state.

The WSD Scan Service informs a client about changes to the scanner's status by sending a [**ScannerStatusSummaryEvent**](scannerstatussummaryevent.md) event. A client can directly query the scanner's state by calling the [**GetScannerElementsRequest**](getscannerelementsrequest.md) operation.

## <span id="see_also"></span>See also


[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**ScannerStateReason**](scannerstatereason.md)

[**ScannerStatus**](scannerstatus.md)

[**ScannerStatusSummaryEvent**](scannerstatussummaryevent.md)

[**StatusSummary**](statussummary.md)

 

 






