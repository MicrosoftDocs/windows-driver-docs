---
title: DocumentParameters element
description: The optional DocumentParameters element specifies the image processing functions to apply to documents in a job.
keywords: ["DocumentParameters element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn DocumentParameters
api_type:
- Schema
ms.date: 04/24/2023
---

# DocumentParameters element

The optional **DocumentParameters** element specifies the image processing functions to apply to documents in a job.

## Usage

```xml
<wscn:DocumentParameters>
  child elements
</wscn:DocumentParameters>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**CompressionQualityFactor**](compressionqualityfactor.md) |
| [**ContentType**](contenttype.md) |
| [**Exposure**](exposure.md) |
| [**FilmScanMode**](filmscanmode.md) |
| [**Format**](format.md) |
| [**ImagesToTransfer**](imagestotransfer.md) |
| [**InputSize**](inputsize.md) |
| [**InputSource**](inputsource.md) |
| [**MediaSides**](mediasides.md) |
| [**Rotation**](rotation.md) |
| [**Scaling**](scaling.md) |

## Parent elements

| Element |
|--|
| [**DefaultScanTicket**](defaultscanticket.md) |
| [**ScanTicket**](scanticket.md) |

## Remarks

The **DocumentParameters** element specifies the image processing functions and their values that will be applied against the job or document.

A client can optionally provide document processing parameters within the **ScanTicket** element during a [**CreateScanJobRequest**](createscanjobrequest.md) operation. The WSD Scan Service must validate all data that a client provides to ensure that each child element is set to a valid value that is specified in the [**ScannerConfiguration**](scannerconfiguration.md) element.

The WSD Scan Service should use its default **DocumentParameters** values if the client does not provide any.

## See also

[**CompressionQualityFactor**](compressionqualityfactor.md)

[**ContentType**](contenttype.md)

[**CreateScanJobRequest**](createscanjobrequest.md)

[**DefaultScanTicket**](defaultscanticket.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**Exposure**](exposure.md)

[**FilmScanMode**](filmscanmode.md)

[**Format**](format.md)

[**ImagesToTransfer**](imagestotransfer.md)

[**InputSize**](inputsize.md)

[**InputSource**](inputsource.md)

[**MediaSides**](mediasides.md)

[**Rotation**](rotation.md)

[**Scaling**](scaling.md)

[**ScanTicket**](scanticket.md)

[**ScannerConfiguration**](scannerconfiguration.md)
