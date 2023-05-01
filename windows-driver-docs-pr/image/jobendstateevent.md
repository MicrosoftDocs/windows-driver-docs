---
title: JobEndStateEvent element
description: The required JobEndStateEvent element informs the client that the scanner has finished processing a job.
keywords: ["JobEndStateEvent element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn JobEndStateEvent
api_type:
- Schema
ms.date: 04/28/2023
---

# JobEndStateEvent element

The required **JobEndStateEvent** element informs the client that the scanner has finished processing a job.

## Usage

```xml
<wscn:JobEndStateEvent>
  child elements
</wscn:JobEndStateEvent>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**JobEndState**](jobendstate.md) |

## Parent elements

There are no parent elements.

## Remarks

The WSD Scan Service sends a **JobEndStateEvent** event element to the client when the scanner has finished processing a job. **JobEndStateEvent** contains data elements that identify the completed job and details about its completion.

## Examples

The following code example shows how the scan device notifies the client of the final state and status of Job 253.

```xml
<soap:Envelope
  xmlns:soap="https://www.w3.org/2003/05/soap-envelope"
  xmlns:wsa="https://schemas.xmlsoap.org/ws/2004/08/addressing"
  xmlns:wse="https://schemas.xmlsoap.org/ws/2004/08/eventing"
  xmlns:wscn="https://schemas.microsoft.com/windows/2006/01/wdp/scan"
  soap:encodingStyle='https://www.w3.org/2002/12/soap-encoding'>

  <soap:Header>
    <wsa:To>AddressofEventSink</wsa:To>
    <wsa:Action>
      https://schemas.microsoft.com/windows/2006/01/wdp/scan/JobEndStateEvent
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>

  <soap:Body>
    <wscn:JobEndStateEvent>
      <wscn:JobEndState>
        <wscn:JobId>253</wscn:JobId>
        <wscn:JobCompletedState>Completed</wscn:JobCompletedState>
        <wscn:JobCompletedStateReasons>
          <wscn:JobStateReason>JobCompletedWithWarnings</wscn:JobStateReason>
        </wscn:JobCompletedStateReasons>
        <wscn:JobName>Scan from Imaging App</wscn:JobName>
        <wscn:JobOriginatingUserName>User</wscn:JobOriginatingUserName>
        <wscn:ScansCompleted>7</wscn:ScansCompleted>
        <wscn:JobCompletedTime>2006-01-24T11:37:05.673Z</wscn:JobCompletedTime>
      </wscn:JobEndState>
    </wscn:JobEndStateEvent>
  </soap:Body
</soap:Envelope>
```

## See also

[**JobEndState**](jobendstate.md)
