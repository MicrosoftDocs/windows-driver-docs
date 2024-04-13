---
title: JobToken Element
description: The required JobToken element contains the device-created token for a new scan job.
keywords: ["JobToken element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn JobToken
api_type:
- Schema
ms.date: 05/01/2023
---

# JobToken element

The required **JobToken** element contains the device-created token for a new scan job.

## Usage

```xml
<wscn:JobToken>
  text
</wscn:JobToken>
```

## Attributes

There are no attributes.

## Text value

Required. Any valid character string.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**CreateScanJobResponse**](createscanjobresponse.md) |
| [**RetrieveImageRequest**](retrieveimagerequest.md) |

## Remarks

The **JobToken** element is paired with the [**JobId**](jobid.md) element to uniquely represent a specific scan job. **JobToken** is passed to the scan device in the [**RetrieveImageRequest**](retrieveimagerequest.md) operation element to enable the device to verify that the scan requester actually created the scan job.

## See also

[**CreateScanJobResponse**](createscanjobresponse.md)

[**JobId**](jobid.md)

[**RetrieveImageRequest**](retrieveimagerequest.md)
