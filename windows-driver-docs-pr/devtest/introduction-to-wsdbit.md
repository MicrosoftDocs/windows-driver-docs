---
title: Introduction to WSDBIT
description: Introduction to WSDBIT
ms.assetid: 8a8ee9de-95b2-43df-ba96-3b09fcd5751c
keywords: ["WSDBIT tool WDK , about", "WSDAPI Basic Interoperability Tool WDK , about", "Web Services for Devices API WDK , about", "WSDAPI WDK , about", "interoperability testing WDK WSDBIT"]
---

# Introduction to WSDBIT


The Web Services for Devices (WSD) API (WSDAPI) enables the following types of message exchanges:

-   Discovering a DPWS device.

-   Describing a DPWS device. This is referred to as a *metadata exchange*.

-   Sending service-specific messages, along with binary attachments, to and from a DPWS service.

-   Subscribing to and receiving events from a DPWS service.

As shown in the following figure, the WSDAPI Basic Interoperability Tool (WSDBIT) uses WSDAPI to send and receive DPWS messages. WSDBIT can be used to test the interoperability between WSDAPI running in a client and a DPWS stack running in a device.

![diagram illustrating the wsdapi basic interoperability tool (wsdbit) and related components](images/wsdbit2.png)

The [interoperability scenarios](client-scenarios-for-wsdbit.md) are intended to verify the message format along with the protocols that are used in the preceding message exchanges. The scenarios are defined from the client perspective and are organized into the following categories:

-   *Device and Service inspection* tests and verifies DPWS device discovery and metadata exchange.

-   *Simple and Advanced Control* tests and verifies service-specific messages.

-   *Attachments* tests and verifies message attachments, as defined in the [SOAP Message Transmission Optimization Mechanism (MTOM)](http://go.microsoft.com/fwlink/p/?linkid=81254) specification.

-   *Eventing* tests and verifies [Web Services Eventing](http://go.microsoft.com/fwlink/p/?linkid=81245).

-   *Secure communication* includes elements of all the preceding scenarios.

Depending on the specific needs of the interoperability testing, you can implement the device, client, or both.

You can also selectively implement sections of the test cases. For example, you can implement only the [Device and Service inspection](device-and-service-inspection-scenarios.md) and the [Simple and Advanced Control](device-control-scenarios.md) interoperability test cases.

**Note**   At a minimum, you must implement the Device and Service inspection interoperability test cases because other test cases require it.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Introduction%20to%20WSDBIT%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




