---
title: JobStateReason element
description: The optional JobStateReason element specifies one reason why a job is in its current state.
keywords: ["JobStateReason element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobStateReason
api_type:
- Schema
ms.date: 09/27/2021
ms.localizationpriority: medium
---

# JobStateReason element

The optional **JobStateReason** element specifies one reason why a job is in its current state.

## Usage

```xml
<wscn:JobStateReason>
  text
</wscn:JobStateReason>
```

## Attributes

There are no attributes.

## Text value

Required. One of the following values:

| Term | Description |
|--|--|
| InvalidScanTicket | The job was rejected because the WSD Scan Service could not process the ScanTicket. |
| DocumentFormatError | The WSD Scan Service does not support the requested document format. |
| ImageTransferError | The data transfer of an image in a job failed. If this error occurs, the WSD Scan Service must abort the job. |
| JobCanceledAtDevice | The current scan job was canceled at the scan device's front panel. |
| JobCompletedWithErrors | The job completed with at least one error. |
| JobCompletedWithWarnings | The job completed with at least one warning. The job data is expected to be successfully transferred. This warning might indicate that the WSD Scan Service made alterations to the scan ticket to process the job. |
| JobScanning | The scanner is digitizing the job data. |
| JobScanningAndTransferring | The scanner is digitizing the job data, and the data is being transferred to the client. |
| JobTimedOut | The WSD Scan Service ended the job after no RetrieveImageRequest operations followed a CreateScanJobRequest operation in a timely fashion. |
| JobTransferring | The job data is being transferred to the client. |
| None | The job has no additional information about the state of the job. |
| ScannerStopped | The scan device is stopped because of an active condition and the job cannot continue until the condition is corrected. |

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**JobCompletedStateReasons**](jobcompletedstatereasons.md) |
| [**JobStateReasons**](jobstatereasons.md) |

## Remarks

You must support the values that represent conditions that WSD Scan Service implementations can detect. Therefore, you can support only a subset of allowed values if specific **JobStateReason** reasons are undetectable in your implementation.

You can extend the allowed values, but extending this list has implications on the client. The client typically localizes the **JobStateReason** value (as with other string variable values) to the language of the user. However, the client will not recognize a vendor-extended value. The client can display the value that is received "as is", but this value will appear in English, so some users might not understand the value.

## See also

[**CreateScanJobRequest**](createscanjobrequest.md)

[**JobCompletedStateReasons**](jobcompletedstatereasons.md)

[**JobStateReasons**](jobstatereasons.md)

[**RetrieveImageRequest**](retrieveimagerequest.md)
