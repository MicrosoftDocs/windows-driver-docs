---
title: ScanData element
description: The required ScanData element contains the binary data that represents the scanned image.
MS-HAID:
- 'wsdss\_ops\_fe260434-110b-444d-93ed-5862132f98f3.xml'
- 'image.scandata'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9b29224c-b1e1-4c64-8a4a-476f9d6eea45
keywords: ["ScanData element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScanData
api_type:
- Schema
---

# ScanData element


The required **ScanData** element contains the binary data that represents the scanned image.

Usage
-----

``` syntax
<wscn:ScanData/>
```

Attributes
----------

There are no attributes.

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
<td><p>[<strong>RetrieveImageResponse</strong>](retrieveimageresponse.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **ScanData** element contains an **xop:Include** element that specifies the location of the scan data relative to the SOAP Envelope/Body of a [**RetrieveImageResponse**](retrieveimageresponse.md) operation element. The actual scan data is appended to the SOAP Envelope/Body as a binary attachment.

## <span id="see_also"></span>See also


[**RetrieveImageResponse**](retrieveimageresponse.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ScanData%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





