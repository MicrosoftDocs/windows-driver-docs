---
title: JobId Element
description: The required JobId element uniquely identifies a job within a scanner.
keywords: ["JobId element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn JobId
api_type:
- Schema
ms.date: 04/28/2023
---

# JobId element

The required **JobId** element uniquely identifies a job within a scanner.

## Usage

```xml
<wscn:JobId>
  text
</wscn:JobId>
```

## Attributes

There are no attributes.

## Text value

Required. An integer value from 1 through 2147483648.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**CancelJobRequest**](canceljobrequest.md) |
| [**CreateScanJobResponse**](createscanjobresponse.md) |
| [**GetJobElementsRequest**](getjobelementsrequest.md) |
| [**JobEndState**](jobendstate.md) |
| [**JobStatus**](jobstatus.md) |
| [**JobSummary**](jobsummary.md) |
| [**RetrieveImageRequest**](retrieveimagerequest.md) |

## Remarks

The WSD Scan Service returns a **JobId** element to a client through a [**CreateScanJobResponse**](createscanjobresponse.md) operation element. The client uses the returned **JobId** when it initiates a scan request through the [**RetrieveImageRequest**](retrieveimagerequest.md) operation element.

**JobId** does not need to be globally unique. The WSD Scan Service should not reuse a recently assigned value so that a client does not confuse a current scan job with an older job.

You cannot extend the allowed values for the **JobId** element.

## See also

[**CancelJobRequest**](canceljobrequest.md)

[**CreateScanJobResponse**](createscanjobresponse.md)

[**GetJobElementsRequest**](getjobelementsrequest.md)

[**JobEndState**](jobendstate.md)

[**JobStatus**](jobstatus.md)

[**JobSummary**](jobsummary.md)

[**RetrieveImageRequest**](retrieveimagerequest.md)
