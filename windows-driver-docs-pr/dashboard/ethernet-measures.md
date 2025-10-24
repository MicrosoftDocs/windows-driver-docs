---
title: Ethernet Measures
description: Ethernet measures guards against errors and bad user experiences
ms.date: 10/21/2025
ms.topic: concept-article
---

# Ethernet measures

Ethernet measures are diagnostic metrics used to monitor and improve the performance of wired network connections on Windows devices. These measures help identify issues such as packet loss, driver failures, and unexpected disconnections, ensuring a stable and reliable user experience.

## Description

Ethernet measures provide insights into the performance and reliability of wired network connections across Windows devices. 
These metrics are collected during Windows flighting and diagnostic sessions. They help Microsoft and hardware partners identify trends, isolate faulty drivers, and improve future driver releases. By analyzing Ethernet measures, developers can reduce connection failures and improve compatibility across platforms. By understanding and applying these metrics, developers and OEMs can deliver better networking experiences to users.

## Driver Development

Microsoft provides LAN device manufactures with the Network Driver Interface Specification (NDIS) and NetAdapter Windows Driver Framework (WDF) class extension.
An NDIS-compliant driver built with the Windows Driver Framework (WDF) enables manufacturers to develop a universal driver that works across device platforms.
It improves LAN driver quality and reduces the complexity of the driver package. A machine can use a NDIS/NetAdapter compliant driver so its network component
and Windows OS can communicate and enable networking connection for the end user. For more information about NDIS driver development,
see [Roadmap for Developing NDIS Drivers](../network/roadmap-for-developing-ndis-drivers.md); for WDF NetAdapter driver development, see
[Building a NetAdapterCx client driver](../netcx/building-a-netadaptercx-client-driver.md).

