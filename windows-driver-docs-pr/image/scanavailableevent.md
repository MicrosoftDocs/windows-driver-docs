---
title: ScanAvailableEvent Element
description: The required ScanAvailableEvent element informs a client that a scan device to which the client is subscribed is ready to scan a job.
keywords: ["ScanAvailableEvent element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ScanAvailableEvent
api_type:
- Schema
ms.date: 05/02/2023
---

# ScanAvailableEvent element

The required **ScanAvailableEvent** element informs a client that a scan device to which the client is subscribed is ready to scan a job.

## Usage

```xml
<wscn:ScanAvailableEvent>
  child elements
</wscn:ScanAvailableEvent>
```

## Attributes

There are no attributes.

## Child elements

| Element |
|--|
| [**ClientContext**](clientcontext.md) |
| [**ScanIdentifier**](scanidentifier.md) |

## Parent elements

There are no parent elements.

## Remarks

The WSD Scan Service sends a **ScanAvailableEvent** element to a registered client when a user has selected a scan destination and initiated a scan at the scan device.

A client must create a subscription with the WSD Scan Service to receive **ScanAvailableEvent** events. The client creates a subscription by sending a request message to the Scan Service through the **&lt;wse:Subscribe&gt;** request operation element.

The subscribe request contains one or more destinations in the [**ScanDestinations**](scandestinations.md) extension element. The Scan Service will use these destinations to filter down to a single client every time it sends a **ScanAvailableEvent** notification. This filter prevents the Scan Service from notifying every client when a user presses the scan button. The extension elements are defined in the WSD Scan Service namespace and then added to the **&lt;wse:Subscribe&gt;** request body.

If the WSD Scan Service accepts the client's request to create a subscription, the service must respond with a **&lt;wse:SubscribeResponse&gt;** response operation element. The subscribe response contains one or more destination responses in the [**DestinationResponses**](destinationresponses.md) extension element, which helps connect the subscription to the scan device that accepted it.

The **&lt;wse:Subscribe&gt;** and **&lt;wse:SubscribeResponse&gt;** elements are described in the specification.

## Examples

The following code example shows how a client subscribes to receive ScanAvailableEvent events from the WSD Scan Service.

```xml
<soap:Envelope
    xmlns:soap="https://www.w3.org/2003/05/soap-envelope"
    xmlns:wsa="https://schemas.xmlsoap.org/ws/2004/08/addressing"
    xmlns:wse="https://schemas.xmlsoap.org/ws/2004/08/eventing"
    xmlns:wscn="https://schemas.microsoft.com/windows/2006/01/wdp/scan>
    soap:encodingStyle='https://www.w3.org/2002/12/soap-encoding' >
  <soap:Header>
    <wsa:To>AddressofScannerService</wsa:To>
      <wsa:Action>
         https://schemas.xmlsoap.org/ws/2004/08/eventing/Subscribe
      </wsa:Action>
      <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
      <wsa:ReplyTo>
        <wsa:Address>https://www.example.com/MyEventSink</wsa:Address>
      </wsa:ReplyTo>
  </soap:Header>
  <soap:Body>
    <wse:Subscribe>
      <wse:Delivery>
        <wse:NotifyTo>
          <wsa:Address>
            https://www.example.com/MyEventSink/OnScanAvailableForMe
          </wsa:Address>
        </wse:NotifyTo>
      </wse:Delivery>
      <wse:Expires>P0Y0M0DT30H0M0S</wse:Expires>
      <wse:Filter xmlns:wscn="https://schemas.microsoft.com/windows/2006/01/wdp/scan">
        ScanAvailableEvent
      </wse:Filter>
      <wscn:ScanDestinations>
        <wscn:ScanDestination>
          <wscn:ClientDisplayString>Den Computer</wscn:ClientDisplayString>
          <wscn:ClientContext>App1ScanID2345</wscn:ClientContext>
        </wscn:ScanDestination>
      </wscn:ScanDestinations>
    </wse:Subscribe>
    </soap:Body
</soap:Envelope>
```

The following code example shows the WSD Scan Service's response to a client's subscription request.

```xml
<soap:Envelope
    xmlns:soap="https://www.w3.org/2003/05/soap-envelope"
    xmlns:wsa="https://schemas.xmlsoap.org/ws/2004/08/addressing"
    xmlns:wse="https://schemas.xmlsoap.org/ws/2004/08/eventing"
    xmlns:wscn="https://schemas.microsoft.com/windows/2006/01/wdp/scan">
    soap:encodingStyle='https://www.w3.org/2002/12/soap-encoding' >
  <soap:Header>
    <wsa:To>https://schemas.xmlsoap.org/ws/2003/03/addressing/role/anonymous</wsa:To>
    <wsa:Action>
      https://schemas.xmlsoap.org/ws/2004/08/eventing/SubscribeResponse
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
    <wsa:RelatesTo>uuid:MsgIdOfTheSubscribe</wsa:RelatesTo>
  </soap:Header>
  <soap:Body>
    <wse:SubscribeResponse>
        <wse:SubscriptionManager>
             <!-- Elements removed for clarity  -->
        </wse:SubscriptionManager>
        <wse:Expires>P0Y0M0DT30H0M0S</wse:Expires>
        <wscn:DestinationResponses>
          <wscn:DestinationResponse>
            <wscn:ClientContext>App1ScanID2345</wscn:ClientContext>
            <wscn:DestinationToken>Client3478</wscn:DestinationToken>
          </wscn:DestinationResponse>
        </wscn:DestinationResponses>
      </wse:SubscribeResponse>
    </soap:Body
</soap:Envelope>
```

The following code example shows how the WSD Scan Service sends a ScanAvailableEvent to a client.

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
      https://schemas.microsoft.com/windows/2006/01/wdp/scan/ScanAvailableEvent
    </wsa:Action>
    <wsa:MessageID>uuid:UniqueMsgId</wsa:MessageID>
  </soap:Header>

  <soap:Body>
    <wscn:ScanAvailableEvent>
      <wscn:ClientContext>App1ScanID2345</wscn:ClientContext>
      <wscn:ScanIdentifier>AnyUniqueIdentifierSuchAsAGUID</wscn:ScanIdentifier>
    </wscn:ScanAvailableEvent>
  </soap:Body
</soap:Envelope>
```

## See also

[**ClientContext**](clientcontext.md)

[**DestinationResponses**](destinationresponses.md)

[**ScanDestinations**](scandestinations.md)

[**ScanIdentifier**](scanidentifier.md)
