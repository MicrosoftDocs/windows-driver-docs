---
title: ScannerInfo element
description: The optional ScannerInfo element contains any administratively assigned descriptive information about the scanner.
ms.assetid: 41d31209-8269-42ef-99f2-83818eb06f6b
keywords: ["ScannerInfo element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScannerInfo xml lang "..."
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ScannerInfo element


The optional **ScannerInfo** element contains any administratively assigned descriptive information about the scanner.

Usage
-----

```xml
<wscn:ScannerInfo xml:lang="..."
  lang = "xs:string">
  text
</wscn:ScannerInfo xml:lang="...">
```

Attributes
----------

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong><strong>lang</strong></strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>(Optional) A character string that identifies the languages of the string that string specifies.<em>string</em></p></td>
</tr>
</tbody>
</table>

Text value
----------

A character string that provides descriptive information about the scanner.

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
<td><p><a href="scannerdescription.md" data-raw-source="[&lt;strong&gt;ScannerDescription&lt;/strong&gt;](scannerdescription.md)"><strong>ScannerDescription</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The configuration of the **ScannerInfo** element's value is implementation-specific; for example, you can configure this value through the scanner's local console or the device's web server. A scan device can return multiple versions of this element to enable support for multiple localized languages by using the **xml:lang** attribute.

Examples
--------

The following code example shows how you can use the ScannerInfo element.

```xml
<wscn:ScannerInfo xml:lang="en-AU, en-CA, en-GB, en-US">
  Out of courtesy to others, please scan only
  small (1-5 page) jobs at this scanner.
</wscn:ScannerInfo>
```

## See also

Description**](scannerdescription.md)
