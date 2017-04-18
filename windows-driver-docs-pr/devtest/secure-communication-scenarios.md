---
title: Secure Communication Scenarios
description: Secure Communication Scenarios
ms.assetid: 0273f4e7-0b93-4ab1-8564-e51c14e91243
keywords: ["WSDBIT tool WDK , test scenarios", "WSDAPI Basic Interoperability Tool WDK , test scenarios", "scenarios WDK WSDBIT", "test scenarios WDK WSDBIT", "Secure Communication scenario WDK WSDBIT"]
---

# Secure Communication Scenarios


The Secure Communication scenario tests discovery, metadata exchange, and eventing by using the secure channel.

Before attempting these scenarios, you should have successfully completed the [Device and Service Inspection](device-and-service-inspection-scenarios.md) and [Eventing](eventing-scenarios.md) scenarios.

Before attempting these interoperability test cases, see [Using WSDAPI with a Secure Channel](http://go.microsoft.com/fwlink/p/?linkid=81271) and [Configuring WSDAPI Applications to Use a Secure Channel](http://go.microsoft.com/fwlink/p/?linkid=81272) for more information about secure channel.

Case
Client action
Server action
Pass-Fail criteria
**5.1**

**Call Probe for a secure device**

5.1.1

Send a wildcard Probe with

-   Use the default matching rule.

-   No **wsd:Types** element.

-   No **wsd:Scopes** element.

Responds with a ProbeMatches.

**Note**  
If a **wsd:XAddrs** is supplied, this address must be an https URI and the **wsa:EndpointReference/wsa:Address** must be the same as the **wsd:XAddrs**.

 

Go to step 5.1.2 (or 5.1.3).

5.1.2 \[optional

This step is only necessary if no wsd:XAddrs are supplied in the ProbeMatches in 5.1.1\]

Send a Resolve to the **wsa:EndpointReference/wsa:Address** that is specified in the ProbeMatches from 1.2.1.

Responds with a ResolveMatches.

**Note**  
The **wsd:XAddrs** must be an https URI and the **wsa:EndpointReference/wsa:Address** must be the same as the **wsd:XAddrs**.

 

Go to step 5.1.3.

5.1.3

Send a GetMetadataRequest to the TestDevice.

Responds with a GetMetadataResponse.

Go to step 5.1.4.

5.1.4

Display ThisDevice metadata.

Nothing

Corresponds to what was sent. For an example of the client output, see [Sample Metadata Response Output](sample-metadata-response-output.md).

5.1.5

Display ThisModel metadata.

Nothing

Corresponds to what was sent. For an example of the client output, see [Sample Metadata Response Output](sample-metadata-response-output.md).

5.1.6

Display Host, HostedService, EndpointReference.

Nothing

Corresponds to what was sent. For an example of the client output, see [Sample Metadata Response Output](sample-metadata-response-output.md).

**5.2**

**Directed Probes to a secure device**

5.2.1

Send a wildcard Probe as an HTTPS request with:

-   Use the default matching rule.

-   no wsd:Types element

-   no wsd:Scopes element

-   The HTTP address is supplied.

Responds with a ProbeMatches that uses the HTTPS response.

**Note**  
If a **wsd:XAddrs** is supplied, this address must be an https URI and the **wsa:EndpointReference/wsa:Address** must be the same as the **wsd:XAddrs**.

 

Confirm that the **wsa:EndpointReference/wsa:Address** for the TestDevice is correct.

**5.3**

**Subscription and renewal of events to a secure device**

Discovery of the secure device is determined by using the methods that are tested in 5.1 or 5.2.

5.3.1

Subscribes to SimpleEvent with:

-   **wse:Filter/@Dialect == "http://schemas.xmlsoap.org/ws/2006/02/devprof/Action"**

-   **wse:Filter == http://schemas.example.org/EventingService/SimpleEvent**

The client can choose to include an expiration of type **xs:duration**.

Sends SubscribeResponse with an expiration long enough to complete step 5.3.2. The expiration must be of type **xs:duration**.

For this test, the server is not required to use the same **xs:duration** as requested from the client.

Client receives the response and can go to step 5.3.2.

5.3.2

Nothing

Fires the SimpleEvent.

Event is received at the client.

5.3.3

Sends Renew to SimpleEvent.

When clients send renewals for events, they can choose to manually initiate the renewal or automatically send the renewal when half of the renewal period specified in the original SubscribeResponse message has elapsed.

Sends RenewResponse with an expiration long enough to complete step 5.3.4. The expiration must be of type **xs:duration**.

Response is received at the client and can go to step 5.3.4.

5.3.4

Nothing

Fires the SimpleEvent.

Event is received at the client.

5.3.5

Sends an Unsubscribe to the TestDevice for the SimpleEvent.

Sends an UnsubscribeResponse.

Client receives response and can go to step 5.3.6.

5.3.6

Nothing

Fires the SimpleEvent.

No event is received at the client.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Secure%20Communication%20Scenarios%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




