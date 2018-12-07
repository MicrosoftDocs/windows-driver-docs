---
title: Client Scenarios for WSDBIT
description: Client Scenarios for WSDBIT
ms.assetid: fb692c83-b384-492d-84fb-10e00db9f30f
keywords:
- WSDBIT tool WDK , test scenarios
- WSDAPI Basic Interoperability Tool WDK , test scenarios
- scenarios WDK WSDBIT
- test scenarios WDK WSDBIT
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Client Scenarios for WSDBIT


All of the test scenarios are driven from the perspective of the client. In limited cases, device interaction is required for the completion of the scenario. This requirement is indicated in the respective scenarios.

Unless otherwise stated, assume that the test device (TestDevice) is already started and available on the network segment on which the scenarios are being run.

Some scenarios define interaction between the client and one (or more) of the Hosted Services in the TestDevice.

Clients can obtain the Hosted Service Endpoints in one of two ways

-   The Hosted Service Endpoints can be supplied by the user. This situation implies that after that the TestDevice has started, the endpoints are known and can be made known to the party that is running the client.

-   The Hosted Service Endpoints can be discovered dynamically. This situation implies discovering the TestDevice. Discovery of the TestDevice can occur through:

    -   A Hello (which is assumed to be initiated from the device and that there is an **XAddrs** field).
    -   A Probe\\Resolve exchange.
    -   A Resolve message (which assumes that the *urn:uuid* address of the Device Endpoint is known).

    Metadata can then be requested and subsequent examination of the HostedService metadata will reveal the endpoints.

Clients can choose to support either of these methods but the TestDevice must support both ways to obtain Hosted Service Endpoints.

Clients must be able to verify the attachment that is received from the TestDevice. The attachment should be verified by loading a copy of the expected attachment into memory and doing a byte-for-byte memory comparison on the received attachment.

When clients send renewals for events, they can choose to manually initiate the renewal or automatically send the renewal when half of the renewal period that is specified in the original SubscribeResponse message has elapsed.

**Note**   Because test cases might have dependencies on the results of prior test cases, the test cases should be run in order. (For example, 1.3.8 depends on the result of 1.2.1.) There are no dependencies between testing scenarios (for example, between the Eventing and Attachment scenarios). There is an implicit dependency for all the advanced scenarios on the first scenario (Device and Service inspection) because failing to discover the TestDevice and inspect its hosted services will prevent the particular advanced scenario from being exercised.

 

This section includes the following topics:

[Device and Service Inspection Scenarios](device-and-service-inspection-scenarios.md)

[Device Control Scenarios](device-control-scenarios.md)

[Attachments Scenarios](attachments-scenarios.md)

[Eventing Scenarios](eventing-scenarios.md)

[Secure Communication Scenarios](secure-communication-scenarios.md)

 

 





