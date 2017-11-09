---
title: InputSize element
description: The optional InputSize element specifies the size of the original scan media.
MS-HAID:
- 'wsdss\_doc\_497a57f4-53af-4018-b59d-5159225956f3.xml'
- 'image.inputsize'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 406cfff9-7357-467f-a07a-340e32d9220f
keywords: ["InputSize element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn InputSize wscn MustHonor ""
api_type:
- Schema
---

# InputSize element


The optional **InputSize** element specifies the size of the original scan media.

Usage
-----

``` syntax
<wscn:InputSize wscn:MustHonor=""
  MustHonor = "xs:string">
  child elements
</wscn:InputSize wscn:MustHonor="">
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
<td><p>[<strong>DocumentSizeAutoDetect</strong>](documentsizeautodetect.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>InputMediaSize</strong>](inputmediasize.md)</p></td>
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
<td><p>[<strong>DocumentFinalParameters</strong>](documentfinalparameters.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>DocumentParameters</strong>](documentparameters.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **InputSize** element can contain the [**DocumentSizeAutoDetect**](documentsizeautodetect.md) or [**InputMediaSize**](inputmediasize.md) element, but not both. **DocumentSizeAutoDetect** specifies that the device utomatically detects the size of the original page. **InputMediaSize** specifies the size of the media to be scanned for the current job.

The client can specify the optional **MustHonor** attribute only when the **InputSize** element is contained within a **CreateScanJobRequest** hierarchy. For more information about **MustHonor** and its usage, see [**CreateScanJobRequest**](createscanjobrequest.md).

## <span id="see_also"></span>See also


[**CreateScanJobRequest**](createscanjobrequest.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**DocumentParameters**](documentparameters.md)

[**DocumentSizeAutoDetect**](documentsizeautodetect.md)

[**InputMediaSize**](inputmediasize.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20InputSize%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





