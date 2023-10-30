---
title: ScanTicket element
description: The required ScanTicket element defines all of the description and processing parameters of the currently identified scan job.
keywords: ["ScanTicket element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ScanTicket
api_type:
- Schema
ms.date: 05/02/2023
---

# ScanTicket element

The required **ScanTicket** element defines all of the description and processing parameters of the currently identified scan job.

## Usage

```xml
<wscn:ScanTicket>
  child elements
</wscn:ScanTicket>
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
| [**CreateScanJobRequest**](createscanjobrequest.md) |
| [**Job**](job.md) |
| [**ValidateScanTicketRequest**](validatescanticketrequest.md) |

## Remarks

The **ScanTicket** element contains the values for the scanner settings for the current job that the client selected. The client constructs the **ScanTicket** by using only those values that the scanner supports. The client obtains such values by calling the [**GetScannerElementsRequest**](getscannerelementsrequest.md) operation and asking for the scanner's [**DefaultScanTicket**](defaultscanticket.md) element.

The member elements of **ScanTicket** map directly to an instance of a [**Job**](job.md) element, and they are exactly what the client needs to send to the scanner during a [**CreateScanJobRequest**](createscanjobrequest.md) operation.

The client can request the **ScanTicket** element for a particular job by calling.

## See also

[**CreateScanJobRequest**](createscanjobrequest.md)

[**DefaultScanTicket**](defaultscanticket.md)

[**DocumentParameters**](documentparameters.md)

[**GetJobElementsRequest**](getjobelementsrequest.md)

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**Job**](job.md)

[**JobDescription**](jobdescription.md)

[**ValidateScanTicketRequest**](validatescanticketrequest.md)
