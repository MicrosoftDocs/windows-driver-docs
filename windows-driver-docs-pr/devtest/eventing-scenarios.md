---
title: Eventing Scenarios
description: Eventing Scenarios
ms.assetid: 6f7832ed-2b0b-4857-b47e-7db492a53855
keywords: ["WSDBIT tool WDK , test scenarios", "WSDAPI Basic Interoperability Tool WDK , test scenarios", "scenarios WDK WSDBIT", "test scenarios WDK WSDBIT", "Eventing scenario WDK WSDBIT"]
---

# Eventing Scenarios


The Eventing scenario tests Eventing, as constrained in the [Device Profile for Web Services (DPWS)](http://go.microsoft.com/fwlink/p/?linkid=81255).

The goal of this scenario is not discovery of the Hosted Service endpoints. This scenario assumes that these endpoints were discovered or provided before starting this scenario.

For the purposes of these scenarios, the NotifyTo and EndTo address formats should be physical addresses and not virtual addresses of the type **uuid: f014e8aa-fc6a-49f5-b862-1e53663a85ff**.

For more information, see the initial test device setup diagram in [WSDBIT Testing Environment](wsdbit-testing-environment.md).

Case
Client action
Server action
Pass-Fail criteria
**4.1**

**Subscription and renewal of events.**

4.1.1

Subscribes to SimpleEvent with:

-   **wse:Filter/@Dialect == "http://schemas.xmlsoap.org/ws/2006/02/devprof/Action"**

-   **wse:Filter == http://schemas.example.org/EventingService/SimpleEvent**

The client can include an expiration of type **xs:duration**.

Sends SubscribeResponse with an expiration long enough to complete step 4.1.2. The expiration must be of type **xs:duration**.

For this test, the server is not required to use the same **xs:duration** as requested from the client.

Client receives the response and can go to step 4.1.2.

4.1.2

Nothing

Fires the SimpleEvent.

Event is received at the client.

4.1.3

Sends Renew to SimpleEvent.

When clients send renewals for events, they can choose to manually initiate the renewal or automatically send the renewal when half of the renewal period specified in the original SubscribeResponse message has elapsed.

Sends RenewResponse with an expiration long enough to complete step 4.1.4. The expiration must be of type **xs:duration**.

Response is received at the client and can go to step 4.1.4.

4.1.4

Nothing

Fires the SimpleEvent.

Event is received at the client.

4.1.5

Sends an Unsubscribe to the TestDevice for the SimpleEvent.

Sends an UnsubscribeResponse.

Client receives response and can go to step 4.1.6.

4.1.6

Nothing

Fires the SimpleEvent.

No event is received at the client.

**4.2**

**Subscriptions with expiries**

4.2.1

Subscribes to SimpleEvent with an expiration with:

-   **wse:Filter/@Dialect == "http://schemas.xmlsoap.org/ws/2006/02/devprof/Action"**

-   **wse:Filter == http://schemas.example.org/EventingService/SimpleEvent**

-   The expiration duration must be long enough to complete step 4.2.2. The expiration must be of **xs:duration**.

wsdbit\_client uses 60 minutes as the duration.

Sends SubscribeResponse with:

-   The expiration that was sent in the Subscription request is returned in the SubscribeResponse.

Client receives the response with the correct expiration and can go to step 4.2.2.

4.2.2

Nothing

Fires the SimpleEvent.

Event is received at client.

4.2.3

Sends a Renew with an expiration to TestDevice for its SimpleEvent subscription. The expiration duration must be long enough to complete step 4.2.4. The expiration must be of **xs:duration**.

When clients send renewals for events, they can choose to manually initiate the renewal or automatically send the renewal when half of the renewal period specified in the original SubscribeResponse message has elapsed.

Sends a RenewResponse with:

-   The expiration that was sent in the Renew request is returned in the RenewResponse.

Client receives response with the correct expiration and can go to step 4.2.4.

4.2.4

Nothing

Fires the SimpleEvent.

Event is received at client.

**4.3**

**Subscriptions, renewals and expiries for multiple event sources**

4.3.1

Subscribes to SimpleEvent with

-   **wse:Filter/@Dialect == "http://schemas.xmlsoap.org/ws/2006/02/devprof/Action"**

-   **wse:Filter == http://schemas.example.org/EventingService/SimpleEvent**

The client can choose to include an expiration of type **xs:duration**.

Sends SubscribeResponse with an expiration long enough to complete step 4.3.3. The expiration must be of type xs:duration.

For this test, the server is not required to use the same **xs:duration** as requested from the client.

Client receives the response and can go to step 4.3.3.

4.3.2

Subscribes to SimpleEvent with:

-   **wse:Filter/@Dialect == "http://schemas.xmlsoap.org/ws/2006/02/devprof/Action"**

-   **wse:Filter == http://schemas.example.org/EventingService/IntegerEvent**

The client can choose to include an expiration of type **xs:duration**.

Sends SubscribeResponse with an expiration long enough to complete step 4.3.4. The expiration must be of type **xs:duration**.

For this test, the server is not required to use the same **xs:duration** as requested from the client.

Client receives the response and can go to step 4.3.4.

4.3.3

Nothing

Fires the SimpleEvent.

Event is received at client.

4.3.4

Nothing

Fires the IntegerEvent.

Event is received at client and the correct integer is displayed.

4.3.5

Sends Renew to IntegerEvent.

When clients send renewals for events, they can choose to manually initiate the renewal or automatically send the renewal when half of the renewal period specified in the original SubscribeResponse message has elapsed.

Sends RenewResponse with an expiration long enough to complete step 4.3.8. The expiration must be of type **xs:duration**.

Response is received at the client.

4.3.6

Sends an Unsubscribe to the TestDevice for the SimpleEvent.

Sends an UnsubscribeResponse.

Client receives response and can go to step 4.3.7.

4.3.7

Nothing

Fires the SimpleEvent.

No event is received at the client.

4.3.8

Nothing

Fires the IntegerEvent.

Event is received at client and the correct integer is displayed.

4.3.9

Sends an Unsubscribe to the TestDevice for the IntegerEvent.

Sends an UnsubscribeResponse.

Client receives response and can go to step 4.3.10.

4.3.10

Nothing

Fires the IntegerEvent.

No event is received at the client.

**4.4**

**Subscriptions failures and faults**

4.4.1

Subscribes to FaultingEvent with:

-   **wse:Filter/@Dialect == "http://schemas.xmlsoap.org/ws/2006/02/devprof/Action"**

-   **wse:Filter == http://schemas.example.org/EventingService/FaultingEvent**

Because this event is not supported, a **wsdp:FilterActionNotSupported** SOAP Fault must be sent.

The failure to subscribe is observed at the client.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Eventing%20Scenarios%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




