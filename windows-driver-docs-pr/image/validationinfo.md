---
title: ValidationInfo element
description: The required ValidationInfo element contains all ScanTicket validation information in response to a client's ValidateScanTicketRequest.
keywords: ["ValidationInfo element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ValidationInfo
api_type:
- Schema
ms.date: 05/02/2023
---

# ValidationInfo element

The required **ValidationInfo** element contains all [**ScanTicket**](scanticket.md) validation information in response to a client's [**ValidateScanTicketRequest**](validatescanticketrequest.md).

## Usage

```xml
<wscn:ValidationInfo>
  child elements
</wscn:ValidationInfo>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**ImageInformation**](imageinformation.md) |
| [**ValidScanTicket**](validscanticket.md) |
| [**ValidTicket**](validticket.md) |

## Parent elements

| Element |
|--|
| [**ValidateScanTicketResponse**](validatescanticketresponse.md) |

## Remarks

The **ValidationInfo** element contains elements that define whether the client's [**ScanTicket**](scanticket.md) is valid and, if not, what data the WSD Scan Service changed to make the ticket valid. The Scan Service returns this information in its [**ValidateScanTicketResponse**](validatescanticketresponse.md) operation.

## See also

[**ImageInformation**](imageinformation.md)

[**ScanTicket**](scanticket.md)

[**ValidScanTicket**](validscanticket.md)

[**ValidTicket**](validticket.md)

[**ValidateScanTicketRequest**](validatescanticketrequest.md)

[**ValidateScanTicketResponse**](validatescanticketresponse.md)
