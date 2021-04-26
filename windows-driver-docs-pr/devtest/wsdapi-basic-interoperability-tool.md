---
title: WSDAPI Basic Interoperability Tool
description: WSDAPI Basic Interoperability Tool
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

The [Devices Profile for Web Services (DPWS)](https://docs.oasis-open.org/ws-dd/ns/dpws/2009/01) is a reference specification that assembles and constrains a number of Web Services (WS) specifications. The [Web Services on Devices (WSD)](/windows/win32/wsdapi/wsd-portal) API (WSDAPI) is an implementation of DPWS that is included with Windows. Windows uses WSDAPI to discover DPWS devices of any type, and also uses WSDAPI to issue control messages to several device classes, such as printers, scanners, and network projectors.

The WSDAPI Basic Interoperability Tool (WSDBIT) can be used to verify that Windows can interoperate with non-WSDAPI DPWS stacks. This tool is intended primarily for device developers who are implementing DPWS and who want to test interoperability with Windows. Some WSDBIT tests require that the device implement a special test interface that is used to exercise advanced DPWS functionality, such as [SOAP Message Transmission Optimization Mechanism (MTOM)](https://www.w3.org/TR/2005/REC-soap12-mtom-20050125/) (which is used for message attachments) and [Web Services Eventing](/previous-versions/ms951233(v=msdn.10)). These interfaces are not strictly required. However, they are the only way to cover this functionality in WSDBIT.

WSDAPI implements both the client and device sections of the specifications, and WSDBIT can be used to exercise WSDAPI as a client or as a device. WSDBIT can be used to test and verify a non-WSDAPI device or a non-WSDAPI client.

Before you read about the WSD interoperability tool, you should be familiar with the DPWS specification and its [referenced specifications](referenced-namespaces.md).

>[!NOTE]
>WSDBIT may be used to assist with the implementation of DPWS on a device, but it is not intended to be a generic debugging tool. Other [WSDAPI development tools](/windows/win32/wsdapi/wsdapi-development-tools) (such as the [WSDAPI debugging tools](/windows/win32/wsdapi/debugging-tools)) are better suited to observing traffic and diagnosing failures. These tools are available in the Windows SDK for desktop apps, see [Downloads for developing desktop apps](https://developer.microsoft.com/windows/downloads/windows-10-sdk/).

This section includes the following topics:

[Introduction to WSDBIT](introduction-to-wsdbit.md)

[Referenced Namespaces](referenced-namespaces.md)

[WSDBIT Testing Environment](wsdbit-testing-environment.md)

[Client Scenarios for WSDBIT](client-scenarios-for-wsdbit.md)

[WSDBIT Reference](wsdbit-reference.md)

For more information about WSD and WSDAPI, see the following topics in the Windows Software Development Kit (SDK):

- [WSD Device Development](/windows/win32/wsdapi/wsd-device-development)

- [WSD Application Development on Windows](/windows/win32/wsdapi/wsd-application-development-on-windows)

- [WSDAPI Troubleshooting Guide](/windows/win32/wsdapi/wsdapi-troubleshooting-guide)
