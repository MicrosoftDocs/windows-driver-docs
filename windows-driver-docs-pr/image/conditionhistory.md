---
title: ConditionHistory element
description: The optional ConditionHistory element is a collection of ConditionHistoryEntry elements that provide details about recent conditions and errors on the scanner.
ms.assetid: 3725a635-6571-4a34-b8f9-9fe6881bd6da
keywords: ["ConditionHistory element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ConditionHistory
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ConditionHistory element


The optional **ConditionHistory** element is a collection of [**ConditionHistoryEntry**](conditionhistoryentry.md) elements that provide details about recent conditions and errors on the scanner.

Usage
-----

``` syntax
<wscn:ConditionHistory>
  child elements
</wscn:ConditionHistory>
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
<td><p>[<strong>ConditionHistoryEntry</strong>](conditionhistoryentry.md)</p></td>
</tr>
</tbody>
</table>

## Parent elements


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>ScannerStatus</strong>](scannerstatus.md)</p></td>
<td><p></p>
<p>ScannerStatus</p></td>
</tr>
</tbody>
</table>

Remarks
-------

A client can query the scanner's **ConditionHistory** element by calling the [**GetScannerElementsRequest**](getscannerelementsrequest.md) operation.

The conditions vary in severity from informational to critical.

## <span id="see_also"></span>See also


[**ConditionHistoryEntry**](conditionhistoryentry.md)

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**ScannerStatus**](scannerstatus.md)

 

 






