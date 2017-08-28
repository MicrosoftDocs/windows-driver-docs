---
title: Network Adapter WDF Class Extension (NetAdapterCx)
description: Network Adapter WDF Class Extension (NetAdapterCx)
ms.assetid: 74719A80-AE66-410F-85B7-31B6F455A818
keywords:
- Network Adapter Class Extension, Network Adapter WDF Class Extension, NetAdapterCx, NetCx
ms.author: windowsdriverdev
ms.date: 06/05/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Network Adapter WDF Class Extension (NetAdapterCx)

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

## Overview

Starting in Windows 10, version 1703, the Windows Driver Kit (WDK) includes a Network Adapter WDF Class Extension module (NetAdapterCx) that enables you to write a KMDF-based client driver for a Network Interface Controller (NIC). NetAdapterCx gives you the power and flexibility of WDF and the networking performance of NDIS, and makes it easy to write a driver for your NIC.

In previous versions of Windows, WDF and NDIS had individual advantages, but did not interoperate well. The only way to write a NIC driver was to write an NDIS miniport driver. To use WDF in an NDIS miniport driver, you had to write extra code in your driver, and even then, you only had access to a small subset of WDF functionality.

With the NetAdapterCx model, conversely, you write a real WDF driver for your NIC. This means that your NetAdapterCx driver has access to full WDF functionality, as well as networking-specific APIs and I/O support from the NetAdapter class extension. As shown in the block diagram below, NetAdapterCx still works behind the scenes with NDIS, but it handles all the interaction with NDIS on your behalf.

<img src="images/architecture.png" alt="Drawing" style="width: 400px;"/>

## Additional info

To watch a video that discusses the benefits of using NetAdapterCx, see the [Network Adapter Class Extension: Overview](https://aka.ms/netadapter/video1) video on Channel 9.

To learn how to port an NDIS 6.x miniport driver to the NetAdapterCx NIC driver model, see [Porting NDIS miniport drivers to NetAdapterCx](porting-ndis-to-netadapter-cx.md).

To start working right away with driver samples on GitHub, clone our [NetAdapter-Cx-Driver-Samples](https://github.com/Microsoft/NetAdapter-Cx-Driver-Samples) repo.

To see the source code for NetAdapterCx itself, or perform step-through debugging, see our [Network-Adapter-Class-Extension](https://github.com/Microsoft/Network-Adapter-Class-Extension) repo on GitHub.

If you would like to work with Microsoft as you develop a NetAdapterCx client driver, or have feedback on the class extension, please send us an [email](mailto:netadapter@microsoft.com).

To watch a video that discusses the future roadmap and collaboration opportunities, see the [Network Adapter Class Extension: Roadmap and Collaboration](https://aka.ms/netadapter/video4) video on Channel 9.

## Topics

This section contains the following topics:

* [What's new in NetAdapterCx](whats-new-in-netadaptercx.md)
* [Porting NDIS miniport drivers to NetAdapterCx](porting-ndis-to-netadapter-cx.md)
* [Building a NetAdapterCx client driver](building-a-netadaptercx-client-driver.md)
* [Device initialization](device-initialization.md)
* [Accessing configuration information](accessing-configuration-information.md)
* [Transferring network data](transferring-network-data.md)
* [Handling control requests](handling-control-requests.md)
* [Debugging a NetAdapterCx client driver](debugging-netadaptercx-client-drivers.md)
* [Configuring power management](configuring-power-management.md)
* [NDIS-WDF function equivalents](ndis-wdf-function-equivalents.md)
* [Summary of objects](summary-of-objects.md)
* [Power-up sequence for a NetAdapterCx client driver](power-up-sequence-for-ndis-wdf-client-driver.md)
* [Power-down sequence for a NetAdapterCx client driver](power-down-sequence-for-ndis-wdf-client-driver.md)
* [NetAdapterCx limitations](class-extension--net--limitations.md)