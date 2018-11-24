---
title: WSDAPI Basic Interoperability Tool
description: WSDAPI Basic Interoperability Tool
ms.assetid: c4a610d4-3adf-406d-88d6-0879eb98b54f
keywords:
- tools WDK , testing drivers
- WSDBIT tool WDK
- WSDAPI Basic Interoperability Tool WDK
- DWPS WDK
- Device Profile for Web Services WDK
- Web Services for Devices API WDK
- WSDAPI WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WSDAPI Basic Interoperability Tool


The [Device Profile for Web Services (DPWS)](http://go.microsoft.com/fwlink/p/?linkid=81255) is a reference specification that assembles and constrains a number of Web Services (WS) specifications. The [Web Services on Devices (WSD)](http://go.microsoft.com/fwlink/p/?linkid=163865) API (WSDAPI) is an implementation of DPWS that is included with Windows. Windows uses WSDAPI to discover DPWS devices of any type, and also uses WSDAPI to issue control messages to several device classes, such as printers, scanners, and network projectors.

The WSDAPI Basic Interoperability Tool (WSDBIT) can be used to verify that Windows can interoperate with non-WSDAPI DPWS stacks. This tool is intended primarily for device developers who are implementing DPWS and who want to test interoperability with Windows. Some WSDBIT tests require that the device implement a special test interface that is used to exercise advanced DPWS functionality, such as [SOAP Message Transmission Optimization Mechanism (MTOM)](http://go.microsoft.com/fwlink/p/?linkid=81254) (which is used for message attachments) and [Web Services Eventing](http://go.microsoft.com/fwlink/p/?linkid=81245). These interfaces are not strictly required. However, they are the only way to cover this functionality in WSDBIT.

WSDAPI implements both the client and device sections of the specifications, and WSDBIT can be used to exercise WSDAPI as a client or as a device. WSDBIT can be used to test and verify a non-WSDAPI device or a non-WSDAPI client.

Before you read about the WSD interoperability tool, you should be familiar with the DPWS specification and its [referenced specifications](referenced-namespaces.md).

**Note**  WSDBIT may be used to assist with the implementation of DPWS on a device, but it is not intended to be a generic debugging tool. Other [WSDAPI development tools](http://go.microsoft.com/fwlink/p/?linkid=163866) (such as the [WSDAPI debugging tools](http://go.microsoft.com/fwlink/p/?linkid=163867)) are better suited to observing traffic and diagnosing failures. These tools are available in the Windows SDK for desktop apps, see [Downloads for developing desktop apps]( http://go.microsoft.com/fwlink/p/?linkid=309790).

 

This section includes the following topics:

[Introduction to WSDBIT](introduction-to-wsdbit.md)

[Referenced Namespaces](referenced-namespaces.md)

[WSDBIT Testing Environment](wsdbit-testing-environment.md)

[Client Scenarios for WSDBIT](client-scenarios-for-wsdbit.md)

[WSDBIT Reference](wsdbit-reference.md)

For more information about WSD and WSDAPI, see the following topics in the Windows Software Development Kit (SDK):

-   [WSD Device Development](http://go.microsoft.com/fwlink/p/?linkid=163868)

-   [WSD Application Development on Windows](http://go.microsoft.com/fwlink/p/?linkid=163869)

-   [WSDAPI Troubleshooting Guide](http://go.microsoft.com/fwlink/p/?linkid=163870)

 

 





