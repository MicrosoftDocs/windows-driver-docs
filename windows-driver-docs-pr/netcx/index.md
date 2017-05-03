---
title: Network Adapter WDF Class Extension (Cx)
---

# Network Adapter WDF Class Extension (Cx)


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Starting in Windows 10 Creators Update (version 1703), the Windows Driver Kit (WDK) includes a class extension module (NetAdapterCx) that enables you to write a KMDF-based driver (called the client driver in this section) for a Network Interface Controller (NIC).  NetAdapterCx gives you the power and flexibility of WDF and the networking performance of NDIS, and makes it easy to write a driver for your NIC.

In previous versions of Windows, WDF and NDIS had individual advantages, but did not interoperate well. The only way to write a NIC driver was to write an NDIS miniport driver. To use WDF in an NDIS miniport driver, you had to write extra code in your driver, and even then, you only had access to a small subset of WDF functionality.

With the NetAdapterCx model, conversely, you write a real WDF driver for your NIC.  This means that your NetAdapterCx driver has access to full WDF functionality, as well as networking-specific APIs and I/O support from the NetAdapter class extension.  As shown in the block diagram below, NetAdapterCx still works behind the scenes with NDIS, but it handles all the interaction with NDIS on your behalf.

<img src="images/architecture.png" alt="Drawing" style="width: 400px;"/>

<!--To watch a video that discusses the benefits of using NetAdapterCx, see [Network Adapter Class Extension: Overview](https://aka.ms/netadapter/video1).-->

To learn how to port an NDIS 6.x miniport driver into a Windows Driver Framework (WDF) networking client driver, see [Porting NDIS Miniport Drivers to NetAdapter Class Extension](porting-ndis-to-netadapter-cx.md).

To start working right away with driver samples on GitHub, clone our [NetAdapter-Cx-Driver-Samples](https://github.com/Microsoft/NetAdapter-Cx-Driver-Samples) repo.

To see the source code for NetAdapterCx itself, or perform step-through debugging, see our [Network-Adapter-Class-Extension](https://github.com/Microsoft/Network-Adapter-Class-Extension) repo on GitHub.

If you would like to work with Microsoft as you develop a NetAdapterCx client driver, or have feedback on the class extension, please send us an [email](mailto:netadapter@microsoft.com).

This section contains the following topics:

* [Porting NDIS Miniport Drivers to NetAdapter Class Extension](porting-ndis-to-netadapter-cx.md)
* [Building a NetAdapterCx Client Driver](building-a-netadaptercx-client-driver.md)
* [Device Initialization](device-initialization.md)
* [Accessing Configuration Information](accessing-configuration-information.md)
* [Transferring Network Data](transferring-network-data.md)
* [Handling Control Requests](handling-control-requests.md)
* [Debugging NetAdapterCx Client Drivers](debugging-netadaptercx-client-drivers.md)
* [Configuring Power Management](configuring-power-management.md)
* [Summary of Objects](summary-of-objects.md)
* [Power-Up Sequence for an Network Adapter WDF Client Driver](power-up-sequence-for-ndis-wdf-client-driver.md)
* [Power-Down Sequence for an Network Adapter WDF Client Driver](power-down-sequence-for-ndis-wdf-client-driver.md)
