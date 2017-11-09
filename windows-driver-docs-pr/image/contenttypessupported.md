---
title: ContentTypesSupported element
description: The required ContentTypesSupported element contains a list of keywords that describe the different document content types that the scanner supports.
MS-HAID:
- 'wsdss\_configure\_6f895bb9-be86-419c-b651-587b958acf4a.xml'
- 'image.contenttypessupported'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f7ed2ba9-8cd9-486c-9bb0-3eb2c925450a
keywords: ["ContentTypesSupported element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ContentTypesSupported
api_type:
- Schema
---

# ContentTypesSupported element


The required **ContentTypesSupported** element contains a list of keywords that describe the different document content types that the scanner supports.

Usage
-----

``` syntax
<wscn:ContentTypesSupported>
  child elements
</wscn:ContentTypesSupported>
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
<td><p>[<strong>ContentTypeValue</strong>](contenttypevalue.md)</p></td>
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

Each [**ContentTypeValue**](contenttypevalue.md) element that is listed in a **ContentTypesSupported** element describes the main characteristics of the original document. The client will pick one content type for its [**ScanTicket**](scanticket.md) from this list when initiating a scan.

## <span id="see_also"></span>See also


[**ScanTicket**](scanticket.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ContentTypesSupported%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





