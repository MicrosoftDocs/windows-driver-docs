---
title: Rotation element
description: The optional Rotation element specifies the amount to rotate each image of the scanned document.
MS-HAID:
- 'wsdss\_doc\_5e6727f8-8449-4fb2-871e-63991b7e5d97.xml'
- 'image.rotation'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: df12cd79-7c3e-4be5-9d7c-237ec014e9c1
keywords: ["Rotation element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn Rotation wscn MustHonor "" wscn Override "" wscn UsedDefault ""
api_type:
- Schema
---

# Rotation element


The optional **Rotation** element specifies the amount to rotate each image of the scanned document.

Usage
-----

``` syntax
<wscn:Rotation wscn:MustHonor=""               wscn:Override=""               wscn:UsedDefault=""
  MustHonor = "xs:string"
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:Rotation wscn:MustHonor=""               wscn:Override=""               wscn:UsedDefault="">
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

Required. One of 0, 90, 180, or 270.

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

The integer value of the **Rotation** element specifies the clockwise rotation to apply to each image of the scanned document. All WSD Scan Services must support the value 0 (that is, no rotation).

The client can specify the optional **MustHonor** attribute only when the **Rotation** element is contained within a **CreateScanJobRequest** hierarchy. For more information about **MustHonor** and its usage, see [**CreateScanJobRequest**](createscanjobrequest.md).

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **Rotation** element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

## <span id="see_also"></span>See also


[**CreateScanJobRequest**](createscanjobrequest.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**DocumentParameters**](documentparameters.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Rotation%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





