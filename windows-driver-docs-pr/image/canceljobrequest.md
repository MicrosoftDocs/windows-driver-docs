---
title: CancelJobRequest Element
description: The required CancelJobRequest operation enables a client to cancel a scan job.
keywords: ["CancelJobRequest element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn CancelJobRequest
api_type:
- Schema
ms.date: 03/28/2023
---

# CancelJobRequest element

The required **CancelJobRequest** operation enables a client to cancel a scan job.

## Usage

```xml
<wscn:CancelJobRequest>
  child elements
</wscn:CancelJobRequest>
```

## Attributes

There are no attributes.

## Text value

None

## Child elements

| Element |
|--|
| [**JobId**](jobid.md) |

## Parent elements

There are no parent elements.

## Remarks

[**JobId**](jobid.md)

A client can cancel a scan job from the time the job is created up to the time it is completed, canceled, or aborted. The [**JobId**](jobid.md) element identifies the job that the client is trying to cancel.

The WSD Scan Service should move the specified job to the **Terminating** state if the job was at a **Pending** or **Active** state. It is an error to attempt to cancel a completed or canceled job or to try canceling any job that the client does not have rights to.

[**common WSD Scan Service operation error codes**](common-wsd-scan-service-operation-error-codes.md)[WSD Scan Service Operation Error Reporting](wsd-scan-service-operation-error-reporting.md)

This operation can return all of the [**common WSD Scan Service operation error codes**](common-wsd-scan-service-operation-error-codes.md). For more information about how to report errors, see [WSD Scan Service Operation Error Reporting](wsd-scan-service-operation-error-reporting.md).

**CancelJobRequest** can also return the following error code:

- **ClientErrorJobIdNotFound**

## See also

[**CancelJobResponse**](canceljobresponse.md)

[**JobId**](jobid.md)
