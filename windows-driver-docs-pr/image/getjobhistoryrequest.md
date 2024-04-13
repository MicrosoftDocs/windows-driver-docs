---
title: GetJobHistoryRequest Element
description: The required GetJobHistoryRequest element requests a summary of job-related variables for previously completed jobs.
keywords: ["GetJobHistoryRequest element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn GetJobHistoryRequest
api_type:
- Schema
ms.date: 11/28/2017
---

# GetJobHistoryRequest element


The required **GetJobHistoryRequest** element requests a summary of job-related variables for previously completed jobs.

## Usage

```xml
<wscn:GetJobHistoryRequest/>
```

## Attributes

There are no attributes.

## Child elements


There are no child elements.

## Parent elements


There are no parent elements.

## Remarks

The WSD Scan Service must support the **GetJobHistoryRequest** operation element.

A client can call **GetJobHistoryRequest** to retrieve a list that contains a summary of job-related variables for previously completed jobs. The WSD Scan Service must respond with a [**GetJobHistoryResponse**](getjobhistoryresponse.md) operation element that contains the information that the client asked for or the appropriate error codes.

The amount of job history that the WSD Scan Service keeps is implementation-specific.

This operation can return all of the [**common WSD Scan Service operation error codes**](common-wsd-scan-service-operation-error-codes.md). For more information about how to report errors, see [WSD Scan Service Operation Error Reporting](wsd-scan-service-operation-error-reporting.md).

## Examples

The following code example contains a request for job history.

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
      https://schemas.microsoft.com/windows/2006/01/wdp/scan/GetJobHistory
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>

  <soap:Body>
    <wscn:GetJobHistoryRequest />
  </soap:Body>
</soap:Envelope>
```

## See also


[**GetJobHistoryResponse**](getjobhistoryresponse.md)

 

 






