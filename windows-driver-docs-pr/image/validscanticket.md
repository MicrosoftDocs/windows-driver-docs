---
title: ValidScanTicket Element
description: The optional ValidScanTicket element contains a valid ScanTicket.
keywords: ["ValidScanTicket element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ValidScanTicket
api_type:
- Schema
ms.date: 05/02/2023
---

# ValidScanTicket element

The optional **ValidScanTicket** element contains a valid [**ScanTicket**](scanticket.md).

## Usage

```xml
<wscn:ValidScanTicket>
  child elements
</wscn:ValidScanTicket>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**DocumentParameters**](documentparameters.md) |
| [**JobDescription**](jobdescription.md) |

## Parent elements

| Element |
|--|
| [**ValidationInfo**](validationinfo.md) |

## Remarks

A client submits a [**ScanTicket**](scanticket.md) for validation through the [**ValidateScanTicketRequest**](validatescanticketrequest.md) operation. If the submitted **ScanTicket** contains invalid settings, the WSD Scan Service must return a **ValidScanTicket** element in which it has changed any invalid settings to be valid settings. The Scan Service returns validation information, which includes **ValidScanTicket**, in [**ValidateScanTicketResponse**](validatescanticketresponse.md).

## See also

[**DocumentParameters**](documentparameters.md)

[**JobDescription**](jobdescription.md)

[**ScanTicket**](scanticket.md)

[**ValidateScanTicketRequest**](validatescanticketrequest.md)

[**ValidateScanTicketResponse**](validatescanticketresponse.md)

[**ValidationInfo**](validationinfo.md)
