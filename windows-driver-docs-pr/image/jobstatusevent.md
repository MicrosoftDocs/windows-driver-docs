---
title: JobStatusEvent Element
description: The required JobStatusEvent element informs the client that a job's status has changed.
keywords: ["JobStatusEvent element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn JobStatusEvent
api_type:
- Schema
ms.date: 04/28/2023
---

# JobStatusEvent element

The required **JobStatusEvent** element informs the client that a job's status has changed.

## Usage

```xml
<wscn:JobStatusEvent>
  child elements
</wscn:JobStatusEvent>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**JobStatus**](jobstatus.md) |

## Parent elements

There are no parent elements.

## Remarks

A WSD Scan Service sends a **JobStatusEvent** element to the client when a job's status has changed. **JobStatusEvent** contains a [**JobStatus**](jobstatus.md) element that defines all of the information about the job's current status. The first **JobStatusEvent** message will typically include the [**JobId**](jobid.md) element and a [**JobState**](jobstate.md) of **Started**.

## Examples

The following code example shows how the scan device notifies a client about the current state of Job 253.

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
      https://schemas.microsoft.com/windows/2006/01/wdp/scan/JobStatusEvent
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>

  <soap:Body>
    <wscn:JobStatusEvent>
      <wscn:JobStatus>
        <wscn:JobId>253</wscn:JobId>
        <wscn:JobState>Processing</wscn:JobState>
        <wscn:JobStateReasons>
          <wscn:JobStateReason>JobScanning</wscn:JobStateReason>
        </wscn:JobStateReasons>
        <wscn:ScansCompleted>4</wscn:ScansCompleted>
        <wscn:JobCreatedTime>2006-01-24T11:34:35.8345Z</wscn:JobCreatedTime>
      </wscn:JobStatus>
    </wscn:JobStatusEvent>
  </soap:Body
</soap:Envelope>
```

## See also

[**JobId**](jobid.md)

[**JobState**](jobstate.md)

[**JobStatus**](jobstatus.md)
