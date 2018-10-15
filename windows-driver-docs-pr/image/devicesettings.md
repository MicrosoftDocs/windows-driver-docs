---
title: DeviceSettings element
description: The required DeviceSettings element describes the basic capabilities of the scan device.
ms.assetid: d12d25f0-fa94-4840-bb1a-cc1a5352767c
keywords: ["DeviceSettings element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn DeviceSettings
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# DeviceSettings element


The required **DeviceSettings** element describes the basic capabilities of the scan device.

Usage
-----

```xml
<wscn:DeviceSettings>
  child elements
</wscn:DeviceSettings>
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
<td><p>[<strong>AutoExposureSupported</strong>](autoexposuresupported.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>BrightnessSupported</strong>](brightnesssupported.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>CompressionQualityFactorSupported</strong>](compressionqualityfactorsupported.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ContentTypesSupported</strong>](contenttypessupported.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ContrastSupported</strong>](contrastsupported.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>DocumentSizeAutoDetectSupported</strong>](documentsizeautodetectsupported.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>FormatsSupported</strong>](formatssupported.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>RotationsSupported</strong>](rotationssupported.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ScalingRangeSupported</strong>](scalingrangesupported.md)</p></td>
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
<td><p>[<strong>ScannerConfiguration</strong>](scannerconfiguration.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **DeviceSettings** element contains the supported values for many of the imaging options that can be set in a [**ScanTicket**](scanticket.md) element for a scan operation. A client can use the values that are returned in **DeviceSettings** to create valid **ScanTicket** elements.

## See also


[**AutoExposureSupported**](autoexposuresupported.md)

[**BrightnessSupported**](brightnesssupported.md)

[**CompressionQualityFactorSupported**](compressionqualityfactorsupported.md)

[**ContentTypesSupported**](contenttypessupported.md)

[**ContrastSupported**](contrastsupported.md)

[**DocumentSizeAutoDetectSupported**](documentsizeautodetectsupported.md)

[**FormatsSupported**](formatssupported.md)

[**RotationsSupported**](rotationssupported.md)

[**ScalingRangeSupported**](scalingrangesupported.md)

[**ScanTicket**](scanticket.md)

[**ScannerConfiguration**](scannerconfiguration.md)

 

 






