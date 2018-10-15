---
title: FormatsSupported element
description: The required FormatsSupported element is a collection of elements that list the document file formats that the scanner supports.
ms.assetid: bb4b6630-f865-4ec7-b7d1-8be424eea345
keywords: ["FormatsSupported element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn FormatsSupported
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# FormatsSupported element


The required **FormatsSupported** element is a collection of elements that list the document file formats that the scanner supports.

Usage
-----

```xml
<wscn:FormatsSupported>
  child elements
</wscn:FormatsSupported>
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
<td><p>[<strong>FormatValue</strong>](formatvalue.md)</p></td>
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
<td><p>[<strong>DeviceSettings</strong>](devicesettings.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

Each [**FormatValue**](formatvalue.md) element specifies a file format that describes both the file type and compression type.

## See also


[**DeviceSettings**](devicesettings.md)

[**FormatValue**](formatvalue.md)

 

 






