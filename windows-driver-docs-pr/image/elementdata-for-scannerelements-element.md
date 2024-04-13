---
title: ElementData for ScannerElements Element
description: The required ElementData element contains the data that is returned for a scanner-related schema request.
keywords: ["ElementData for ScannerElements element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ElementData Name "" Valid ""
api_type:
- Schema
ms.date: 04/24/2023
---

# ElementData for ScannerElements element

The required **ElementData** element contains the data that is returned for a scanner-related schema request.

## Usage

```xml
<wscn:ElementData Name="" Valid=""
  Name = "xs:string"
  Valid = "xs:string">
  child elements
</wscn:ElementData Name="" Valid="">
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **Name** | xs:string | No | Required. One of the following QNames:xmlns:ScannerDescriptionReturn the currentScannerDescription schema.xmlns:ScannerConfigurationReturn the current ScannerConfiguration schema.xmlns:ScannerStatusReturn the current ScannerStatus schema.xmlns:DefaultScanTicketReturn the current DefaultScanTicket schema.xmlns:VendorSectionReturn the identified section of a vendor-defined extension to the WSD Scan Service. |
| **Valid** | xs:string | No | Required. A Boolean value that must be 0, false, 1, or true. |

## Child elements

| Element |
|--|
| [**DefaultScanTicket**](defaultscanticket.md) |
| [**ScannerConfiguration**](scannerconfiguration.md) |
| [**ScannerDescription**](scannerdescription.md) |
| [**ScannerStatus**](scannerstatus.md) |

## Parent elements

| Element |
|--|
| [**ScannerElements**](scannerelements.md) |

## Remarks

A client calls [**GetScannerElementsRequest**](getscannerelementsrequest.md) to determine the values of scanner-related elements. The WSD Scan Service returns this information in the **ElementData** element through the [**GetScannerElementsResponse**](getscannerelementsresponse.md) operation.

The QName value for the **Name** attribute must be a schema keyword that represents the top-level section within the WSD Scan Service for which a client requested information. The Scan Service must specify both the namespace prefix and valid, colon-separated element name.

The **Valid** attribute indicates whether the schema keyword provided by the client was valid. The WSD Scan Service sets this attribute to **true** if it can map the requested schema keyword to a valid section of its schema; otherwise, it must set this attribute to **false**.

## See also

[**DefaultScanTicket**](defaultscanticket.md)

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**GetScannerElementsResponse**](getscannerelementsresponse.md)

[**ScannerConfiguration**](scannerconfiguration.md)

[**ScannerDescription**](scannerdescription.md)

[**ScannerElements**](scannerelements.md)

[**ScannerStatus**](scannerstatus.md)
