---
title: GetJobElementsResponse Element
description: The required GetJobElementsResponse element returns the job-related information that a client requests.
keywords: ["GetJobElementsResponse element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn GetJobElementsResponse
api_type:
- Schema
ms.date: 04/25/2023
---

# GetJobElementsResponse element

The required **GetJobElementsResponse** element returns the job-related information that a client requests.

## Usage

```xml
<wscn:GetJobElementsResponse>
  child elements
</wscn:GetJobElementsResponse>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**JobElements**](jobelements.md) |

## Parent elements

There are no parent elements.

## Remarks

The WSD Scan Service must support the **GetJobElementsResponse** operation.

A client calls **GetJobElementsRequest** to determine the values of job-related elements for the job that [**JobId**](jobid.md) identifies. The WSD Scan Service must respond with a **GetJobElementsResponse** element that contains the requested information. The information that the Scan Service returns must fully comply with the scan job-related portion of the schema.

## Examples

In the following code example, the Scan Service returns the job status for the job that JobId 1 identifies.

```xml
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope
  xmlns:soap="https://www.w3.org/2003/05/soap-envelope"
  xmlns:wsa="https://schemas.xmlsoap.org/ws/2003/03/addressing"
  xmlns:wscn="https://schemas.microsoft.com/windows/2006/01/wdp/scan"
  soap:encodingStyle='https://www.w3.org/2002/12/soap-encoding' >

  <soap:Header>
    <wsa:To>
      https://schemas.xmlsoap.org/ws/2003/03/addressing/role/anonymous
    </wsa:To>
    <wsa:Action>
      https://schemas.microsoft.com/windows/2006/01/wdp/scan/GetJobElements
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
    <wsa:RelatesTo>uuid:MsgIdOfTheGetJobElementsRequest</wsa:RelatesTo>
  </soap:Header>

  <soap:Body>
    <wscn:GetJobElementsResponse>
      <wscn:JobElements>
        <wscn:ElementData wscn:Name="JobStatus" wscn:Valid="true">
          <wscn:JobStatus>
            <wscn:JobId>1</wscn:JobId>
            <wscn:JobState>Completed</wscn:JobState>
            <wscn:JobStateReasons>
              <wscn:JobStateReason>None</wscn:JobStateReason>
            </wscn:JobStateReasons>
            <wscn:ScansCompleted>1</wscn:ScansCompleted>
          </wscn:JobStatus>
        </wscn:ElementData>
      </wscn:JobElements>
    </wscn:GetJobElementsResponse >
  </soap:Body>
</soap:Envelope>
```

## See also

[**GetJobElementsRequest**](getjobelementsrequest.md)

[**JobElements**](jobelements.md)

[**JobId**](jobid.md)
