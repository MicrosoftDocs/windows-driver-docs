---
title: JobDescription element
description: The required JobDescription element contains basic creation information for the currently identified job.
keywords: ["JobDescription element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn JobDescription
api_type:
- Schema
ms.date: 04/28/2023
---

# JobDescription element

The required **JobDescription** element contains basic creation information for the currently identified job.

## Usage

```xml
<wscn:JobDescription>
  child elements
</wscn:JobDescription>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**JobInformation**](jobinformation.md) |
| [**JobName**](jobname.md) |
| [**JobOriginatingUserName**](joboriginatingusername.md) |

## Parent elements

| Element |
|--|
| [**DefaultScanTicket**](defaultscanticket.md) |
| [**ScanTicket**](scanticket.md) |

## Remarks

A client sets the values for all **JobDescription** child elements and submits them in a [**CreateScanJobRequest**](createscanjobrequest.md) operation.

## See also

[**CreateScanJobRequest**](createscanjobrequest.md)

[**DefaultScanTicket**](defaultscanticket.md)

[**JobInformation**](jobinformation.md)

[**JobName**](jobname.md)

[**JobOriginatingUserName**](joboriginatingusername.md)

[**ScanTicket**](scanticket.md)
