---
title: ADFBack element
description: The optional ADFBack element describes the capabilities of the back side of a duplex automatic document feeder (ADF) that is attached to the scanner.
MS-HAID:
- 'wsdss\_adffilm\_4b6bb6c3-9708-48ae-85fc-102b499fca27.xml'
- 'image.adfback'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f364c001-ec1a-4f8c-b25a-eaa5368ba05f
keywords: ["ADFBack element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ADFBack
api_type:
- Schema
---

# ADFBack element


The optional **ADFBack** element describes the capabilities of the back side of a duplex automatic document feeder (ADF) that is attached to the scanner.

Usage
-----

``` syntax
<wscn:ADFBack>
  child elements
</wscn:ADFBack>
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
<td><p>[<strong>ADFColor</strong>](adfcolor.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ADFMaximumSize</strong>](adfmaximumsize.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ADFMinimumSize</strong>](adfminimumsize.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ADFOpticalResolution</strong>](adfopticalresolution.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ADFResolutions</strong>](adfresolutions.md)</p></td>
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
<td><p>[<strong>ADF</strong>](adf.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The WSD Scan Service should specify the **ADFBack** elements and its children only if the scanner's ADF supports duplexing.

## <span id="see_also"></span>See also


[**ADF**](adf.md)

[**ADFColor**](adfcolor.md)

[**ADFMaximumSize**](adfmaximumsize.md)

[**ADFMinimumSize**](adfminimumsize.md)

[**ADFOpticalResolution**](adfopticalresolution.md)

[**ADFResolutions**](adfresolutions.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ADFBack%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





