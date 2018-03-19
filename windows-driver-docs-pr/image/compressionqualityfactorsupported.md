---
title: CompressionQualityFactorSupported element
description: The required CompressionQualityFactorSupported element specifies the range of compression quality factors that the scan device supports.
ms.assetid: f82ae450-b948-463e-a6a8-aaea0575ddb9
keywords: ["CompressionQualityFactorSupported element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn CompressionQualityFactorSupported
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CompressionQualityFactorSupported element


The required **CompressionQualityFactorSupported** element specifies the range of compression quality factors that the scan device supports.

Usage
-----

``` syntax
<wscn:CompressionQualityFactorSupported>
  child elements
</wscn:CompressionQualityFactorSupported>
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
<td><p>[<strong>MaxValue</strong>](maxvalue.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>MinValue</strong>](minvalue.md)</p></td>
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

The compression quality factor is an integer value that you use for a lossy compression type to determine the amount of acceptable image loss during compression. The higher the requested fidelity, the larger the resulting file size will be.

[**MinValue**](minvalue.md)[**MaxValue**](maxvalue.md)

The minimum and maximum compression quality factors that the scan device supports are specified in the [**MinValue**](minvalue.md) and [**MaxValue**](maxvalue.md) elements, respectively. **MinValue** and **MaxValue** must be integers from 1 through 100. A value of 100 means that the device should use the least amount of compression that it supports to produce the highest quality image. Currently, JPEG compression is the only supported lossy compression type.

## <span id="see_also"></span>See also


[**DeviceSettings**](devicesettings.md)

[**MaxValue**](maxvalue.md)

[**MinValue**](minvalue.md)

 

 






