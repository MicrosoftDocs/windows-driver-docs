---
title: ElementData for JobElements Element
description: The required ElementData element contains the data that is returned for a job-related schema request.
keywords: ["ElementData for JobElements element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ElementData Name "" Valid ""
api_type:
- Schema
ms.date: 04/24/2023
---

# ElementData for JobElements element

The required **ElementData** element contains the data that is returned for a job-related schema request.

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
| **Name** | xs:string | No | Required. One of the following QName values:xmlns:JobStatusReturn the current JobStatusschema.xmlns:ScanTicketReturn the ScanTicket element.xmlns:DocumentsReturn the Documents element.xmlns:VendorSectionGet the identified section of a vendor-defined extension to the WSD Scan Service. |
| **Valid** | xs:string | No | Required. A Boolean value that must be 0, false, 1, or true. |

## Child elements

| Element |
|--|
| [**Documents**](documents.md) |
| [**JobStatus**](jobstatus.md) |
| [**ScanTicket**](scanticket.md) |

## Parent elements

| Element |
|--|
| [**JobElements**](jobelements.md) |

## Remarks

The WSD Scan Service returns the **ElementData** element in a [**GetJobElementsResponse**](getjobelementsresponse.md) operation element.

## See also

[**Documents**](documents.md)

[**GetJobElementsResponse**](getjobelementsresponse.md)

[**JobElements**](jobelements.md)

[**JobStatus**](jobstatus.md)

[**ScanTicket**](scanticket.md)
