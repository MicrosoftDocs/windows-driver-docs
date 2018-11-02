---
title: InputSource element
description: The optional InputSource element specifies the source of the original document on the scanning device.
ms.assetid: a49ed5d8-6d49-4997-9704-de1cd6c7d0c7
keywords: ["InputSource element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn InputSource wscn MustHonor "" wscn Override "" wscn UsedDefault ""
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# InputSource element


The optional **InputSource** element specifies the source of the original document on the scanning device.

Usage
-----

```xml
<wscn:InputSource wscn:MustHonor=""                  wscn:Override=""                  wscn:UsedDefault=""
  MustHonor = "xs:string"
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:InputSource wscn:MustHonor=""                  wscn:Override=""                  wscn:UsedDefault="">
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
<td><p><strong><strong>MustHonor</strong></strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>Optional. A Boolean value that must be 0, false, 1, or true.<strong>falsetrue</strong></p></td>
</tr>
<tr class="even">
<td><p><strong><strong>Override</strong></strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>Optional. A Boolean value that must be 0, false, 1, or true.<strong>falsetrue</strong></p></td>
</tr>
<tr class="odd">
<td><p><strong><strong>UsedDefault</strong></strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>Optional. A Boolean value that must be 0, false, 1, or true.<strong>falsetrue</strong></p></td>
</tr>
</tbody>
</table>

Text value
----------

Required. One of the following values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><span id="ADF"></span><span id="adf"></span>ADF</p></td>
<td><p>The document should be delivered by a document feeding device, scanning only the front side of each page.</p></td>
</tr>
<tr class="even">
<td><p><span id="ADFDuplex"></span><span id="adfduplex"></span><span id="ADFDUPLEX"></span>ADFDuplex</p></td>
<td><p>The document should be delivered by a document feeding device, scanning both sides of each page.</p></td>
</tr>
<tr class="odd">
<td><p><span id="Film"></span><span id="film"></span><span id="FILM"></span>Film</p></td>
<td><p>The document should be scanned by using the film scanning option.</p></td>
</tr>
<tr class="even">
<td><p><span id="Platen"></span><span id="platen"></span><span id="PLATEN"></span>Platen</p></td>
<td><p>The document should be scanned from the scanner platen.</p></td>
</tr>
</tbody>
</table>

 

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
<td><p><a href="documentfinalparameters.md" data-raw-source="[&lt;strong&gt;DocumentFinalParameters&lt;/strong&gt;](documentfinalparameters.md)"><strong>DocumentFinalParameters</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="documentparameters.md" data-raw-source="[&lt;strong&gt;DocumentParameters&lt;/strong&gt;](documentparameters.md)"><strong>DocumentParameters</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The client can specify the optional **MustHonor** attribute only when the **InputSource** element is contained within a **CreateScanJobRequest** hierarchy. For more information about **MustHonor** and its usage, see [**CreateScanJobRequest**](createscanjobrequest.md).

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **InputSource** element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

You can both extend and subset the allowed values for this element.

## See also


[**CreateScanJobRequest**](createscanjobrequest.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**DocumentParameters**](documentparameters.md)

 

 






