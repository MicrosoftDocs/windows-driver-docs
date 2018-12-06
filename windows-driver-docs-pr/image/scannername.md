---
title: ScannerName element
description: The required ScannerName element specifies the administratively assigned user-friendly name of the scanner.
ms.assetid: 013a1cb8-4b59-4271-a7bd-eb8d741643e5
keywords: ["ScannerName element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScannerName xml lang "..."
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ScannerName element


The required **ScannerName** element specifies the administratively assigned user-friendly name of the scanner.

Usage
-----

```xml
<wscn:ScannerName xml:lang="..."
  lang = "xs:string">
  text
</wscn:ScannerName xml:lang="...">
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

A character string that specifies the scanner's user-friendly name.

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

The configuration of the **ScannerName** element's value is implementation-specific; for example, you can configure this value through the scanner's local console or the device's web server. If a device has only one hosted service, its friendly name and **ScannerName** element should have the same value. If the device contains several hosted services, **ScannerName** should identify the scanner.

A scan device can return multiple versions of this element to enable support for multiple localized languages by using the **xml:lang** attribute.

Examples
--------

The following code example shows how you can use the ScannerName element.

```xml
<wscn:ScannerName xml:lang="en-AU, en-CA, en-GB, en-US">
  Accounting Scanner in Copy Room 2
</wscn:ScannerName>
```

## See also

[**ScannerDescription**](scannerdescription.md)
