---
title: CompressionQualityFactor element
description: The optional CompressionQualityFactor element specifies an idealized integer amount of image quality, on a scale from 0 through 100.
MS-HAID:
- 'wsdss\_doc\_62131dcd-ee84-40ac-be6b-7dcd4377ee33.xml'
- 'image.compressionqualityfactor'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e66ab41d-3f77-4c60-b0bf-d050f467c6b4
keywords: ["CompressionQualityFactor element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn CompressionQualityFactor wscn MustHonor "" wscn Override "" wscn UsedDefault ""
api_type:
- Schema
---

# CompressionQualityFactor element


The optional **CompressionQualityFactor** element specifies an idealized integer amount of image quality, on a scale from 0 through 100.

Usage
-----

``` syntax
<wscn:CompressionQualityFactor wscn:MustHonor=""                               wscn:Override=""                               wscn:UsedDefault=""
  MustHonor = "xs:string"
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:CompressionQualityFactor wscn:MustHonor=""                               wscn:Override=""                               wscn:UsedDefault="">
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

Required. An integer in the range from 0 through 100.

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

Any lossy compression type uses the integer value to determine the amount of acceptable image loss, where a higher value indicates a higher image quality and a correspondingly larger file size. A value of 100 indicates that the device should use the least amount of compression that it supports to produce the highest image quality possible. Currently, JPEG compression is the only supported lossy compression type.

If the requested image compression type is lossless and **MustHonor** is not present or is **false**, the WSD Scan Service should ignore the **CompressionQualityFactor** element and instead use a value of 100. If the compression type is lossless and **MustHonor** is **true**, the WSD Scan Service should reject the [**ScanTicket**](scanticket.md) element if a value other than 100 is specified.

The client can specify the optional **MustHonor** attribute only when the **CompressionQualityFactor** element is contained within a **CreateScanJobRequest** hierarchy. For more information about **MustHonor** and its usage, see [**CreateScanJobRequest**](createscanjobrequest.md).

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **CompressionQualityFactor** element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

You can subset the allowed values for this element.

## <span id="see_also"></span>See also


[**CreateScanJobRequest**](createscanjobrequest.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**DocumentParameters**](documentparameters.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20CompressionQualityFactor%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





