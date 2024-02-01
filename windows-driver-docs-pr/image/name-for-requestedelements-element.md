---
title: Name for RequestedElements Element
description: This required Name element identifies the section of the WSD Scan Service schema that the client wants data for when it calls GetScannerElementsRequest or GetJobElementsRequest.
keywords: ["Name for RequestedElements element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn Name
api_type:
- Schema
ms.date: 09/28/2021
---

# Name for RequestedElements element

This required **Name** element identifies the section of the WSD Scan Service schema that the client wants data for when it calls [**GetScannerElementsRequest**](getscannerelementsrequest.md) or [**GetJobElementsRequest**](getjobelementsrequest.md).

## Usage

```xml
<wscn:Name>
  text
</wscn:Name>
```

## Attributes

There are no attributes.

## Text value

Required.

For [**GetScannerElementsRequest**](getscannerelementsrequest.md), one of the following QName values:

| QName | Description |
|--|--|
| wscn:ScannerDescription | Get all of the descriptive information for the scan device. |
| wscn:ScannerConfiguration | Get all of the configuration information for the scan device. |
| wscn:ScannerStatus | Get the entire status section, including [**ActiveConditions**](activeconditions.md) and [**ConditionHistory**](conditionhistory.md). |
| xmlns:VendorSection | Get the identified section of a vendor-defined extension to the WSD Scan Service. |

For [**GetJobElementsRequest**](getjobelementsrequest.md), one of the following QName values:

| QName | Description |
|--|--|
| wscn:JobStatus | Get the current [**JobStatus**](jobstatus.md) element data for the specified job. |
| wscn:ScanTicket | Get the [**ScanTicket**](scanticket.md) element data for the specified job. |
| wscn:Documents | Get the [**Documents**](documents.md) element data for the specified job. |
| xmlns:VendorSection | Get the identified section of a vendor-defined extension to the WSD Scan Service. |

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**RequestedElements**](requestedelements.md) |

## Remarks

The Qname must identify the top-level element within the WSD Scan Service schema that the client wants information for. The client must specify both the schema namespace and element name.

## See also

[**GetJobElementsRequest**](getjobelementsrequest.md)

[**ActiveConditions**](activeconditions.md)

[**ConditionHistory**](conditionhistory.md)

[**Documents**](documents.md)

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**JobStatus**](jobstatus.md)

[**RequestedElements**](requestedelements.md)

[**ScanTicket**](scanticket.md)
