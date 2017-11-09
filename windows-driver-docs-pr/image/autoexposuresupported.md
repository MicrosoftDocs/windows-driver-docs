---
title: AutoExposureSupported element
description: The required AutoExposureSupported element specifies whether the scan device supports automatic adjustment of the various exposure settings.
MS-HAID:
- 'wsdss\_configure\_31ba967f-5a4f-4b28-9993-dba02e70c013.xml'
- 'image.autoexposuresupported'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 36ef003f-b049-4eb2-8fe3-53aa77db3065
keywords: ["AutoExposureSupported element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn AutoExposureSupported
api_type:
- Schema
---

# AutoExposureSupported element


The required **AutoExposureSupported** element specifies whether the scan device supports automatic adjustment of the various exposure settings.

Usage
-----

``` syntax
<wscn:AutoExposureSupported>
  text
</wscn:AutoExposureSupported>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. A Boolean value that must be 0, 1, false, or true.**falsetrue**

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
<td><p>[<strong>DeviceSettings</strong>](devicesettings.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

[**Exposure**](exposure.md)

If the scan device supports automatic adjustment of various [**Exposure**](exposure.md) settings, the WSD Scan Service should return 1 (**true**); otherwise, it should return 0 (**false**).

You cannot extend the allowed values for this element.

## <span id="see_also"></span>See also


[**DeviceSettings**](devicesettings.md)

[**Exposure**](exposure.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20AutoExposureSupported%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





