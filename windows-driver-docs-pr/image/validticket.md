---
title: ValidTicket Element
description: The required ValidTicket element indicates whether a client's ScanTicket was valid.
keywords: ["ValidTicket element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ValidTicket
api_type:
- Schema
ms.date: 05/02/2023
---

# ValidTicket element

The required **ValidTicket** element indicates whether a client's [**ScanTicket**](scanticket.md) was valid.

## Usage

```xml
<wscn:ValidTicket>
  text
</wscn:ValidTicket>
```

## Attributes

There are no attributes.

## Text value

Required. A Boolean value that must be 0, false, 1, or true.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**ValidationInfo**](validationinfo.md) |

## Remarks

A client submits a [**ScanTicket**](scanticket.md) for validation through the [**ValidateScanTicketRequest**](validatescanticketrequest.md) operation. The WSD Scan Service returns validation information, which includes **ValidTicket**, in [**ValidateScanTicketResponse**](validatescanticketresponse.md).

## See also

[**ScanTicket**](scanticket.md)

[**ValidateScanTicketRequest**](validatescanticketrequest.md)

[**ValidateScanTicketResponse**](validatescanticketresponse.md)

[**ValidationInfo**](validationinfo.md)
