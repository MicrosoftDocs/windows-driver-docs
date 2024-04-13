---
title: GetActiveJobsRequest Element
description: The required GetActiveJobsRequest element requests a summary of all currently active jobs in the scan device.
keywords: ["GetActiveJobsRequest element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn GetActiveJobsRequest
api_type:
- Schema
ms.date: 11/28/2017
---

# GetActiveJobsRequest element


The required **GetActiveJobsRequest** element requests a summary of all currently active jobs in the scan device.

## Usage

```xml
<wscn:GetActiveJobsRequest/>
```

## Attributes

There are no attributes.

## Child elements


There are no child elements.

## Parent elements


There are no parent elements.

## Remarks

The WSD Scan Service must support the **GetActiveJobsRequest** operation.

A client calls **GetActiveJobsRequest** to retrieve a list that contains a summary of job-related variables for all currently active scan jobs. The WSD Scan Service must respond with a [**GetActiveJobsResponse**](getactivejobsresponse.md) element that contains the information that the client asked for or the appropriate error codes.

This operation can return all of the [**common WSD Scan Service operation error codes**](common-wsd-scan-service-operation-error-codes.md). For more information about how to report errors, see [WSD Scan Service Operation Error Reporting](wsd-scan-service-operation-error-reporting.md).

## Examples

The following code example shows a request for all active scan jobs.

```xml
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
  xmlns:soap="https://www.w3.org/2003/05/soap-envelope"
  xmlns:wsa="https://schemas.xmlsoap.org/ws/2003/03/addressing"
  xmlns:wscn="https://schemas.microsoft.com/windows/2006/01/wdp/scan"
  soap:encodingStyle='https://www.w3.org/2002/12/soap-encoding' >

  <soap:Header>
    <wsa:To>AddressofScannerService</wsa:To>
    <wsa:Action>
      https://schemas.microsoft.com/windows/2006/01/wdp/scan/GetActiveJobs
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>

  <soap:Body>
    <wscn:GetActiveJobsRequest />
  </soap:Body>
</soap:Envelope>
```

## See also


[**GetActiveJobsResponse**](getactivejobsresponse.md)

 

 






