---
title: ContentType element
description: The optional ContentType element specifies the main characteristics of the original document.
ms.assetid: 0e91e4ec-5569-452f-b929-9d2923f3147d
keywords: ["ContentType element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ContentType wscn MustHonor "" wscn Override "" wscn UsedDefault ""
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ContentType element


The optional **ContentType** element specifies the main characteristics of the original document.

Usage
-----

``` syntax
<wscn:ContentType wscn:MustHonor=""                  wscn:Override=""                  wscn:UsedDefault=""
  MustHonor = "xs:string"
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:ContentType wscn:MustHonor=""                  wscn:Override=""                  wscn:UsedDefault="">
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
<p>Optional. A Boolean value that must be 0, false, 1, or true.</p></td>
</tr>
<tr class="even">
<td><p><strong><strong>Override</strong></strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>Optional. A Boolean value that must be 0, false, 1, or true.</p></td>
</tr>
<tr class="odd">
<td><p><strong><strong>UsedDefault</strong></strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>Optional. A Boolean value that must be 0, false, 1, or true.</p></td>
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
<td><p><span id="Auto"></span><span id="auto"></span><span id="AUTO"></span>Auto</p></td>
<td><p>The scan device will automatically detect the original type.</p></td>
</tr>
<tr class="even">
<td><p><span id="Text"></span><span id="text"></span><span id="TEXT"></span>Text</p></td>
<td><p>The document is mainly composed of distinct text that contrasts strongly with the background.</p></td>
</tr>
<tr class="odd">
<td><p><span id="Photo"></span><span id="photo"></span><span id="PHOTO"></span>Photo</p></td>
<td><p>The original is mainly composed of photographic images, where shades change gradually and edges are not distinct.</p></td>
</tr>
<tr class="even">
<td><p><span id="Halftone"></span><span id="halftone"></span><span id="HALFTONE"></span>Halftone</p></td>
<td><p>The original is mainly composed of halftoned images.</p></td>
</tr>
<tr class="odd">
<td><p><span id="Mixed"></span><span id="mixed"></span><span id="MIXED"></span>Mixed</p></td>
<td><p>A multipage document with characteristics of more than one specific DocumentType.</p></td>
</tr>
</tbody>
</table>

 

You can both extend and subset values for this element.

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
<td><p>[<strong>DocumentFinalParameters</strong>](documentfinalparameters.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>DocumentParameters</strong>](documentparameters.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The client can specify the optional **MustHonor** attribute only when the **ContentType** element is contained within a **CreateScanJobRequest** hierarchy. For more information about **MustHonor** and its usage, see [**CreateScanJobRequest**](createscanjobrequest.md).

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **ContentType** element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

## <span id="see_also"></span>See also


[**CreateScanJobRequest**](createscanjobrequest.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**DocumentParameters**](documentparameters.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ContentType%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





