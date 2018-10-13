---
title: ScannerStatus element
description: The required ScannerStatus element contains the current status of the scanner-related information that automata (such as time and changing conditions in the scanner) control.
ms.assetid: 39a1bbc1-acee-4ac8-8b14-35a3be5076ae
keywords: ["ScannerStatus element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScannerStatus
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# ScannerStatus element


The required **ScannerStatus** element contains the current status of the scanner-related information that automata (such as time and changing conditions in the scanner) control.

Usage
-----

```xml
<wscn:ScannerStatus>
  child elements
</wscn:ScannerStatus>
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
<td><p>[<strong>ActiveConditions</strong>](activeconditions.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ConditionHistory</strong>](conditionhistory.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ScannerCurrentTime</strong>](scannercurrenttime.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ScannerState</strong>](scannerstate.md)</p></td>
</tr>
<tr class="odd">
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
<td><p>[<strong>ElementData Element for ScannerElements</strong>](elementdata-for-scannerelements-element.md)</p></td>
</tr>
</tbody>
</table>

## See also


[**ActiveConditions**](activeconditions.md)

[**ConditionHistory**](conditionhistory.md)

[**ElementData Element for ScannerElements**](elementdata-for-scannerelements-element.md)

[**ScannerCurrentTime**](scannercurrenttime.md)

[**ScannerState**](scannerstate.md)

[**ScannerStateReasons**](scannerstatereasons.md)

 

 






