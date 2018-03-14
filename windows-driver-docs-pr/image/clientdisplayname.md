---
title: ClientDisplayName element
description: The required ClientDisplayName element specifies the string that the scanner should display in its user interface.
ms.assetid: e43e5c51-5f8e-47af-b5da-707b89401935
keywords: ["ClientDisplayName element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ClientDisplayName
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ClientDisplayName element


The required **ClientDisplayName** element specifies the string that the scanner should display in its user interface.

Usage
-----

``` syntax
<wscn:ClientDisplayName>
  text
</wscn:ClientDisplayName>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. Any valid character string.

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
<td><p>[<strong>ScanDestination</strong>](scandestination.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The displayed name enables a user to select the requesting client as a scan destination. When the user chooses this display name and presses the scan button, the WSD Scan Service will send a [**ScanAvailableEvent**](scanavailableevent.md) event to the scan destination that subscribed to receive it.

## <span id="see_also"></span>See also


[**ScanAvailableEvent**](scanavailableevent.md)

[**ScanDestination**](scandestination.md)

 

 






