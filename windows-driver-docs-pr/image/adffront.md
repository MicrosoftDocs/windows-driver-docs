---
title: ADFFront element
description: The required ADFFront element describes the capabilities of the front side of the automatic document feeder (ADF) that is attached to the scanner.
MS-HAID:
- 'wsdss\_adffilm\_0c06ec4f-7f1d-4c40-b75c-0845f17ab6d0.xml'
- 'image.adffront'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 6b49f5da-6866-4ec6-8973-7c582bd3a1a1
keywords: ["ADFFront element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ADFFront
api_type:
- Schema
---

# ADFFront element


The required **ADFFront** element describes the capabilities of the front side of the automatic document feeder (ADF) that is attached to the scanner.

Usage
-----

``` syntax
<wscn:ADFFront>
  child elements
</wscn:ADFFront>
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

If the scanner has an ADF the WSD Scan Service must provide details for it in the **ADFFront** element, regardless of the ADF's duplexing capabilities.

## <span id="see_also"></span>See also


[**ADF**](adf.md)

[**ADFColor**](adfcolor.md)

[**ADFMaximumSize**](adfmaximumsize.md)

[**ADFMinimumSize**](adfminimumsize.md)

[**ADFOpticalResolution**](adfopticalresolution.md)

[**ADFResolutions**](adfresolutions.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ADFFront%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





