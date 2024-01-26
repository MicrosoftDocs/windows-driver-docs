---
title: Network Adapter WDF Class Extension (NetAdapterCx)
description: Network Adapter WDF Class Extension (NetAdapterCx)
ms.assetid: 74719A80-AE66-410F-85B7-31B6F455A818
keywords:
- Network Adapter Class Extension, Network Adapter WDF Class Extension, NetAdapterCx, NetCx
ms.date: 08/27/2019
ms.topic: article
ms.custom: 19H1
---

# Network Adapter WDF Class Extension (NetAdapterCx)

## Overview

Starting in Windows 10, version 2004, the Windows Driver Kit (WDK) includes a Network Adapter WDF Class Extension module (NetAdapterCx) that enables you to write a KMDF-based client driver for a Network Interface Controller (NIC). Starting in Windows 11_NEXT, the [UMDF version of NetAdapterCx](user-mode-netcx.md) enables NIC drivers to operate in user-mode. NetAdapterCx gives you the power and flexibility of WDF and the networking performance of NDIS, and makes it easy to write a driver for your NIC.

In previous versions of Windows, WDF and NDIS had individual advantages, but did not interoperate well. The only way to write a NIC driver was to write an NDIS miniport driver. To use WDF in an NDIS miniport driver, you had to write extra code in your driver, and even then, you only had access to a small subset of WDF functionality.

With the NetAdapterCx model, conversely, you write a real WDF driver for your NIC. This means that your NetAdapterCx driver has access to full WDF functionality, as well as networking-specific APIs and I/O support from the NetAdapter class extension. As shown in the block diagram below, NetAdapterCx still works behind the scenes with NDIS, but it handles all the interaction with NDIS on your behalf.

:::image type="content" source="images/netcx-architecture.png" alt-text="Diagram that shows the NetAdapterCx architecture.":::

## Additional info

The following video [Network Adapter Class Extension: Overview](https://www.microsoft.com/videoplayer/embed/RE5daTH) discusses the benefits of using NetAdapterCx.

> [!VIDEO https://www.microsoft.com/videoplayer/embed/RE5daTH]

To learn how to port an NDIS 6.x miniport driver to the NetAdapterCx NIC driver model, see [Porting NDIS miniport drivers to NetAdapterCx](porting-ndis-miniport-drivers-to-netadaptercx.md).

To start working right away with driver samples on GitHub, clone our [NetAdapter-Cx-Driver-Samples](https://github.com/Microsoft/NetAdapter-Cx-Driver-Samples) repo.

To see the source code for NetAdapterCx itself, or perform step-through debugging, see our [Network-Adapter-Class-Extension](https://github.com/Microsoft/Network-Adapter-Class-Extension) repo on GitHub.

If you would like to work with Microsoft as you develop a NetAdapterCx client driver, or have feedback on the class extension, please send us an [email](mailto:netadapter@microsoft.com).

The following video [Network Adapter Class Extension: Roadmap and Collaboration](https://www.microsoft.com/videoplayer/embed/RE5ddHE) discusses future roadmap and collaboration opportunities.

> [!VIDEO https://www.microsoft.com/videoplayer/embed/RE5ddHE]

## Topics

This section contains the following topics:

* [Porting NDIS miniport drivers to NetAdapterCx](porting-ndis-miniport-drivers-to-netadaptercx.md)
* [Building a NetAdapterCx client driver](building-a-netadaptercx-client-driver.md)
* [INF files for NetAdapterCx client drivers](inf-files-for-netadaptercx-client-drivers.md)
* [Managing the lifetime of objects in NetAdapterCx](summary-of-netadaptercx-objects.md)
* [Accessing configuration information](accessing-configuration-information.md)
* [Debugging a NetAdapterCx client driver](debugging-a-netadaptercx-client-driver.md)
* [Transferring network data](transferring-network-data.md)
* [NetAdapterCx receive side scaling (RSS)](netadaptercx-receive-side-scaling-rss-.md)
* [Configuring power management](configuring-power-management.md)
* [NDIS-WDF function equivalents](ndis-wdf-function-equivalents.md)
* [NetAdapterCx limitations](netadaptercx-limitations.md)
* [Mobile Broadband (MBB) WDF class extension (MBBCx)](mobile-broadband-mbb-wdf-class-extension-mbbcx.md)
* [Wi-Fi WDF class extension (WiFiCx)](wifi-wdf-class-extension-wificx.md)