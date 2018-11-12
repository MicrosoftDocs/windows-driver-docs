---
title: Bluetooth Profile Drivers Overview
description: Bluetooth Profile Drivers Overview
ms.assetid: 86806113-28b6-470c-883c-506ac1205f85
keywords:
- Bluetooth WDK , about Bluetooth
- remote connections WDK Bluetooth
- connections WDK Bluetooth
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Bluetooth Profile Drivers Overview


This section describes the support that Microsoft provides for the wireless Bluetooth protocol. Bluetooth is an industry standard protocol that enables wireless connectivity for a variety of devices including computers, mobile phones, handheld devices, mouse devices, keyboards, and printers. This section also provides guidelines on how to develop Bluetooth profile drivers for your Bluetooth-enabled device. Details of the Bluetooth protocol are available on the [Bluetooth](http://go.microsoft.com/fwlink/p/?linkid=26268) website.

Microsoft provides support for the Bluetooth protocol in Microsoft Windows XP with Service Pack 2 (SP2) and later. Bluetooth drivers, known as profile drivers, are written by independent hardware vendors (IHVs) to support various protocols defined in the Bluetooth specifications. Profile drivers should follow the Windows Driver Model (WDM) architecture.

To support the Bluetooth protocol, Microsoft supplies several drivers and support files, including:

-   *BthPort.sys*

-   *BthEnum.sys*

-   *BthUsb.sys*

-   *BthProps.cpl*

IHVs must use Windows Vista or later to develop their profile drivers because earlier versions of Windows, including Windows XP with SP2, do not support profile driver development.

The Bluetooth driver stack provides device driver interfaces (DDIs) that enable profile drivers to access Synchronous Connection-Oriented (SCO) links and Logical Link Controller and Adaptation Protocol (L2CAP) links between the local system and remote Bluetooth devices.

### <span id="sco"></span><span id="SCO"></span>**SCO**

Synchronous connection-oriented (SCO) links are point-to-point connections between two Bluetooth devices. They are defined primarily to support time-bounded information like voice.

The Windows Vista Bluetooth driver stack has been enhanced to provide SCO kernel-mode DDIs. By using these interfaces, profile drivers can use the SCO DDIs to open, update, and close SCO connections, as well as perform read and write operations over an open SCO connection.

For more information about SCO, see [Creating a SCO Client Connection to a Remote Device](creating-a-sco-client-connection-to-a-remote-device.md) and [Accepting SCO Connections in a Bluetooth Profile Driver](accepting-sco-connections-in-a-bluetooth-profile-driver.md).

### <span id="l2cap_and_sdp"></span><span id="L2CAP_AND_SDP"></span>**L2CAP and SDP**

The L2CAP is designed to support asynchronous connectionless link (ACL) Bluetooth links. The Bluetooth driver stack provides support for connection-oriented services. Profile drivers use the Bluetooth L2CAP DDIs to open, update, and close L2CAP connections, as well as to perform read and write operations over an open L2CAP connection.

The Service Discovery Protocol (SDP) provides a way for a profile driver to advertise the services or discover services offered by the device it manages.

SDP records are advertised in a complex byte stream. Profile drivers can use the SDP DDIs to find an SDP record and convert it to a tree-based representation that is more easily interpreted for parsing. Profile drivers can also use the SDP DDIs to build a tree-based representation of an SDP record and then convert it to a stream to advertise it.

For more information about L2CAP and SDP, see [Creating a L2CAP Client Connection to a Remote Device](creating-a-l2cap-client-connection-to-a-remote-device.md), [Accepting L2CAP Connections in a Bluetooth Profile Driver](accepting-l2cap-connections-in-a-bluetooth-profile-driver.md) and [Communicating with SDP Servers](communicating-with-sdp-servers.md).

For more information about the Bluetooth driver stack, see [Bluetooth Driver Stack](bluetooth-driver-stack.md).

 

 





