---
title: AutoExposure element
description: The required AutoExposure element specifies that the WSD Scan Service should automatically determine the exposure settings for the document.
MS-HAID:
- 'wsdss\_doc\_32f33f0a-cebc-45ec-95b2-aee70b9122e0.xml'
- 'image.autoexposure'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ccc2b246-cfa1-4d79-b968-7b4bbaad17ee
keywords: ["AutoExposure element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn AutoExposure
api_type:
- Schema
---

# AutoExposure element


The required **AutoExposure** element specifies that the WSD Scan Service should automatically determine the exposure settings for the document.

Usage
-----

``` syntax
<wscn:AutoExposure>
  text
</wscn:AutoExposure>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. A Boolean value that must be 0, false, 1, or true.**falsetrue**

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
<td><p>[<strong>Exposure</strong>](exposure.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

When the Boolean value of the **AutoExposure** element is 1 or **true**, the scan device will employ image processing techniques to reduce the background of the document to white.

When the value is 0 or **false**, the device should use the default settings for each of the exposure settings.

## <span id="see_also"></span>See also


[**Exposure**](exposure.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20AutoExposure%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





