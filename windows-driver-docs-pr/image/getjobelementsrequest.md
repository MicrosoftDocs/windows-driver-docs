---
title: GetJobElementsRequest Element
description: The required GetJobElementsRequest element requests information that is related to the job that the JobId element identifies.
keywords: ["GetJobElementsRequest element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn GetJobElementsRequest
api_type:
- Schema
ms.date: 04/25/2023
---

# GetJobElementsRequest element

The required **GetJobElementsRequest** element requests information that is related to the job that the [**JobId**](jobid.md) element identifies.

## Usage

```xml
<wscn:GetJobElementsRequest>
  child elements
</wscn:GetJobElementsRequest>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**JobId**](jobid.md) |
| [**RequestedElements**](requestedelements.md) |

## Parent elements

There are no parent elements.

## Remarks

The WSD Scan Service must support the **GetJobElementsRequest** operation.

A client can call **GetJobElementsRequest** to determine the values of job-related elements for the job that [**JobId**](jobid.md) identifies. The WSD Scan Service must respond with a **GetJobElementsResponse**. The information that the Scan Service returns must fully comply with the scan job-related portion of the schema.

This operation can return all of the [**common WSD Scan Service operation error codes**](common-wsd-scan-service-operation-error-codes.md). For more information about how to report errors, see [WSD Scan Service Operation Error Reporting](wsd-scan-service-operation-error-reporting.md).

**GetJobElementsRequest** might also return the following errors.

- **ClientErrorJobIdNotFound**

    The scanner cannot find a job that matches the JobId value or the JobId value is not within the defined range.

    | Fault property | Definition                         |
    |----------------|------------------------------------|
    | \[Code\]       | soap:Sender                        |
    | \[Subcode\]    | wscn:ClientErrorJobIdNotFound      |
    | \[Reason\]     | The specified JobId was not found. |
    | \[Detail\]     | JobId: Incorrect JobId             |

## Examples

The following code example requests the status of the scan job that Fault property 1 identifies.

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
      https://schemas.microsoft.com/windows/2006/01/wdp/scan/GetJobElements
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>

  <soap:Body>
    <wscn:GetJobElements>
      <wscn:JobId>1</wscn:JobId>
      <wscn:RequestedElements>
        <wscn:Name>JobStatus</wscn:Name>
      </wscn:RequestedElements>
    </wscn:GetJobElements>
  </soap:Body>
</soap:Envelope>
```

## See also

[**GetJobElementsResponse**](getjobelementsresponse.md)

[**JobId**](jobid.md)

[**RequestedElements**](requestedelements.md)
