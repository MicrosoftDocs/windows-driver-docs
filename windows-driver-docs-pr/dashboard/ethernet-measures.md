---
title: Ethernet measures
description: Ethernet measures guards against errors and bad user experiences
ms.date: 10/21/2025
ms.topic: concept-article
---

# Ethernet measures

## Description

Microsoft provides LAN device manufactures with the Network Driver Interface Specification (NDIS) and NetAdapter Windows Driver Framework (WDF) class extension.
An NDIS-compliant driver built with the Windows Driver Framework (WDF) enables manufacturers to develop a universal driver that works across device platforms.
It improves LAN driver quality and reduces the complexity of the driver package. A machine can use a NDIS/NetAdapter compliant driver so its network component
and Windows OS can communicate and enable networking connection for the end user. For more info about NDIS driver development,
see [Roadmap for Developing NDIS Drivers](../network/roadmap-for-developing-ndis-drivers.md); for WDF NetAdapter driver development, see
[Building a NetAdapterCx client driver](../netcx/building-a-netadaptercx-client-driver.md).

Ethernet measures provide insights into the performance and reliability of wired network connections across Windows devices. These metrics help ensure users experience fast and stable Internet connectivity when using physical Ethernet adapters.
