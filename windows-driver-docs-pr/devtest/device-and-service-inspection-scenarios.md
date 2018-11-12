---
title: Device and Service Inspection Scenarios
description: Device and Service Inspection Scenarios
ms.assetid: 25e6ed92-e01c-4349-a614-b71bb08d71cd
keywords:
- WSDBIT tool WDK , test scenarios
- WSDAPI Basic Interoperability Tool WDK , test scenarios
- scenarios WDK WSDBIT
- test scenarios WDK WSDBIT
- Device and Service inspection scenario WDK WSDBIT
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device and Service Inspection Scenarios


The Device and Service inspection scenarios test Device Discovery and the subsequent Device and Service inspection.

The basic discovery of the device and the hosted services provides the infrastructure for the rest of the scenarios.

The Device must be using **xs:anyURI testdevice** as the **wsd:Scopes** element for discovery.

The following table describes this scenario.

Step
Client action
Server action
Pass-Fail criteria
**1.1**

**TestDevice boot\\shutdown**

1.1.1

Nothing

TestDevice starts and sends Hello.

Hello correctly received at client.

1.1.2

Nothing

TestDevice shuts down and sends Bye.

Bye correctly received at client. The **wsa:EndpointReference/wsa:Address** should be the same as the one used in step 1.1.1.

1.1.3

Nothing

TestDevice starts again and sends Hello.

Hello correctly received with same metadata version in 1.1.1. The **wsa:EndpointReference/wsa:Address** should be the same as the one used in step 1.1.1.

**1.2**

**Resolve for the TestDevice**

1.2.1

Send a Resolve.

Responds with a ResolveMatches.

Go to step 1.2.2.

1.2.2

Send a GetMetadaRequest to the TestDevice.

Responds with a GetMetadatResponse.

Go to step 1.2.3.

1.2.3

Display ThisDevice metadata.

Nothing

Corresponds to what was sent. For an example of the client output, see [Sample Metadata Response Output](sample-metadata-response-output.md).

1.2.4

Display ThisModel metadata.

Nothing

Corresponds to what was sent. For an example of the client output, see [Sample Metadata Response Output](sample-metadata-response-output.md).

1.2.5

Display Host, HostedService, EndpointReference.

Nothing

Corresponds to what was sent. For an example of the client output, see [Sample Metadata Response Output](sample-metadata-response-output.md).

1.2.6

Send a Resolve for urn:uuid:00000000-0000-0000-0000-000000000000 (which is i the **wsa:EndpointReference/wsa:Address** of the device).

Nothing. Because the device does not match this **wsa:EndpointReference/wsa:Address**, it should not respond

The server does not respond with any ResolveMatches message.

**1.3**

**Probe for the TestDevice**

1.3.1

Send a wildcard Probe:

-   Use the default Matching Rule.

-   No **wsd:Types** element.

-   No **wsd:Scopes** element.

Responds with a ProbeMatches.

Go to step 1.3.2 (or 1.3.3).

1.3.2 (Optional. This step is necessary only if no **wsd:XAddrs** is supplied in the ProbeMatches in 1.3.1.)

Send a Resolve to the **wsa:EndpointReference/wsa:Addres**s specified in the ProbeMatches from 1.2.1.

Responds with a ResolveMatches.

Go to step 1.3.3.

1.3.3

Send a GetMetadataRequest to the TestDevice.

Responds with a GetMetadataResponse.

Go to step 1.3.4.

1.3.4

Display ThisDevice metadata.

Nothing

Corresponds to what was sent. For an example of the client output, see [Sample Metadata Response Output](sample-metadata-response-output.md).

1.3.5

Display ThisModel metadata.

Nothing

Corresponds to what was sent. For an example of the client output, see [Sample Metadata Response Output](sample-metadata-response-output.md).

1.3.6

Display Host, HostedService, EndpointReference.

Nothing

Corresponds to what was sent. For an example of the client output, see [Sample Metadata Response Output](sample-metadata-response-output.md).

1.3.7

Send a Probe that specifies the following:

-   Use the default matching rule.

-   Type to be matched: **wsdp:Device**. (.See the namespace table above, as well as R1020 in the Device Profile for Web Services.)

-   No wsd:Scopes element.

Responds with a ProbeMatches.

The value for the **wsa:EndpointReference/wsa:Address** is the same as in step 1.2.1.

1.3.8

Send a Probe that specifies the following:

-   Use a matching rule that is defined in the [Web Services Dynamic Discovery (WS-Discovery)](http://go.microsoft.com/fwlink/p/?linkid=81240) specification.

-   No wsd:Types element.

-   Use the following as a scope *testdevice*.

Responds with a ProbeMatches.

The value for the **wsa:EndpointReference/wsa:Address** is the same as in step 1.2.1.

1.3.9

Send a Probe that specifies the following:

-   Use the [Devices Profile for Web Services](http://go.microsoft.com/fwlink/p/?linkid=163864) matching rule.

-   No **wsd:Types** element.

-   Use the following as a scope *testDEVICE*.

Nothing. This test does not respond with a ProbeMatches.

No message is received; wait 10 seconds.

1.3.10

Send a Probe that specifies the following:

-   Use the default matching rule.

-   Use a fictional type to be matched: (for example, http://example.org/this/wont/work:Device).

-   No **wsd:Scopes** element.

Nothing. This test does not respond with a ProbeMatches.

No message is received; wait 10 seconds.

**1.4**

**Directed Probes**

1.4.1

Send a wildcard Probe as an HTTP request:

-   Use the default matching rule.

-   No **wsd:Types** element.

-   No **wsd:Scopes** element.

-   The HTTP address is supplied.

Responds with a ProbeMatches that uses HTTP response.

Confirm that the **wsa:EndpointReference/wsa:Address** for the TestDevice is correct.

**1.5**

**Obtaining Metadata without discovery**

1.5.1

Send a GetMetadataRequest to the TestDevice.

Responds with a GetMetadataResponse.

Go to step 1.5.2.

1.5.2

Display ThisDevice metadata.

Nothing

Corresponds to what was sent. For an example of the client output, see [Sample Metadata Response Output](sample-metadata-response-output.md).

1.5.3

Display ThisModel metadata.

Nothing

Corresponds to what was sent. For an example of the client output, see [Sample Metadata Response Output](sample-metadata-response-output.md).

1.5.4

Display Host, HostedService, EndpointReference.

Nothing

Corresponds to what was sent. For an example of the client output, see [Sample Metadata Response Output](sample-metadata-response-output.md).

 

 

 





