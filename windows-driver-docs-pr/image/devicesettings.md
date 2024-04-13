---
title: DeviceSettings Element
description: The required DeviceSettings element describes the basic capabilities of the scan device.
keywords: ["DeviceSettings element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn DeviceSettings
api_type:
- Schema
ms.date: 04/21/2023
---

# DeviceSettings element

The required **DeviceSettings** element describes the basic capabilities of the scan device.

## Usage

```xml
<wscn:DeviceSettings>
  child elements
</wscn:DeviceSettings>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**AutoExposureSupported**](autoexposuresupported.md) |
| [**BrightnessSupported**](brightnesssupported.md) |
| [**CompressionQualityFactorSupported**](compressionqualityfactorsupported.md) |
| [**ContentTypesSupported**](contenttypessupported.md) |
| [**ContrastSupported**](contrastsupported.md) |
| [**DocumentSizeAutoDetectSupported**](documentsizeautodetectsupported.md) |
| [**FormatsSupported**](formatssupported.md) |
| [**RotationsSupported**](rotationssupported.md) |
| [**ScalingRangeSupported**](scalingrangesupported.md) |

## Parent elements

| Element |
|--|
| [**ScannerConfiguration**](scannerconfiguration.md) |

## Remarks

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
