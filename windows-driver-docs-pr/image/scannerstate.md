---
title: ScannerState element
description: The required ScannerState element identifies the current state of the scanning portion of the scan device.
ms.assetid: 64cd5319-a52d-4ff3-976c-060886381d11
keywords: ["ScannerState element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScannerState
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# ScannerState element


The required **ScannerState** element identifies the current state of the scanning portion of the scan device.

Usage
-----

``` syntax
<wscn:ScannerState>
  text
</wscn:ScannerState>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. One of the following string values.

| Value      | Description                                                  |
|------------|--------------------------------------------------------------|
| Idle       | The scanner is available and can start processing a new job. |
| Processing | The scanner is currently processing jobs.                    |
| Stopped    | No jobs can be processed and intervention is needed.         |

 

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
<td><p>[<strong>ScannerStatus</strong>](scannerstatus.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>StatusSummary</strong>](statussummary.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

The WSD Scan Service informs a client about changes to the scanner's status by sending a [**ScannerStatusSummaryEvent**](scannerstatussummaryevent.md) event. A client can directly query the scanner's state by calling the [**GetScannerElementsRequest**](getscannerelementsrequest.md) operation.

You can both extend and subset the allowed values for this element.

## <span id="see_also"></span>See also


[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**ScannerStatus**](scannerstatus.md)

[**ScannerStatusSummaryEvent**](scannerstatussummaryevent.md)

[**StatusSummary**](statussummary.md)

 

 






