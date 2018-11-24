---
title: ScanDestination element
description: The required ScanDestination element specifies a single scan destination on the client.
ms.assetid: 3cd685b2-36b2-4f28-a80f-a68204631e0c
keywords: ["ScanDestination element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScanDestination
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ScanDestination element


The required **ScanDestination** element specifies a single scan destination on the client.

Usage
-----

```xml
<wscn:ScanDestination>
  child elements
</wscn:ScanDestination>
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
<td><p><a href="clientcontext.md" data-raw-source="[&lt;strong&gt;ClientContext&lt;/strong&gt;](clientcontext.md)"><strong>ClientContext</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="clientdisplayname.md" data-raw-source="[&lt;strong&gt;ClientDisplayName&lt;/strong&gt;](clientdisplayname.md)"><strong>ClientDisplayName</strong></a></p></td>
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
<td><p><a href="scandestinations.md" data-raw-source="[&lt;strong&gt;ScanDestinations&lt;/strong&gt;](scandestinations.md)"><strong>ScanDestinations</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The client includes one or more **ScanDestination** elements within the **ScanDestinations** element that it sends when it creates a subscription. The WSD Scan Service uses the information that is provided within **ScanDestination** to create appropriate [**ScanAvailableEvent**](scanavailableevent.md) event elements.

## See also


[**ClientContext**](clientcontext.md)

[**ClientDisplayName**](clientdisplayname.md)

[**ScanAvailableEvent**](scanavailableevent.md)

[**ScanDestinations**](scandestinations.md)

 

 






