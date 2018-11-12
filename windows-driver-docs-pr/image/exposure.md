---
title: Exposure element
description: The optional Exposure element specifies the exposure settings of the document.
ms.assetid: 70e02507-106f-45a9-92b1-29707cbbcbab
keywords: ["Exposure element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn Exposure wscn MustHonor ""
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Exposure element


The optional **Exposure** element specifies the exposure settings of the document.

Usage
-----

```xml
<wscn:Exposure wscn:MustHonor=""
  MustHonor = "xs:string">
  child elements
</wscn:Exposure wscn:MustHonor="">
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
</tbody>
</table>

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
<td><p><a href="autoexposure.md" data-raw-source="[&lt;strong&gt;AutoExposure&lt;/strong&gt;](autoexposure.md)"><strong>AutoExposure</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="exposuresettings.md" data-raw-source="[&lt;strong&gt;ExposureSettings&lt;/strong&gt;](exposuresettings.md)"><strong>ExposureSettings</strong></a></p></td>
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
<td><p><a href="documentfinalparameters.md" data-raw-source="[&lt;strong&gt;DocumentFinalParameters&lt;/strong&gt;](documentfinalparameters.md)"><strong>DocumentFinalParameters</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="documentparameters.md" data-raw-source="[&lt;strong&gt;DocumentParameters&lt;/strong&gt;](documentparameters.md)"><strong>DocumentParameters</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **Exposure** element can contain a [**AutoExposure**](autoexposure.md) or [**ExposureSettings**](exposuresettings.md) element, but not both. **AutoExposure** specifies that the device should automatically employ image processing techniques to reduce the background of the document to a white image. **ExposureSettings** specifies the specific **Exposure** adjustment values that the WSD Scan Service should apply to the image data after acquisition.

The client can specify the optional **MustHonor** attribute only when the **Exposure** element is contained within a **CreateScanJobRequest** hierarchy. For more information about **MustHonor** and its usage, see [**CreateScanJobRequest**](createscanjobrequest.md).

## See also


[**AutoExposure**](autoexposure.md)

[**CreateScanJobRequest**](createscanjobrequest.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**DocumentParameters**](documentparameters.md)

[**ExposureSettings**](exposuresettings.md)

 

 






