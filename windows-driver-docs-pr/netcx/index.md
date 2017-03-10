---
title: Network Adapter WDF Class Extension (Cx)
---

# Network Adapter WDF Class Extension (Cx)


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Starting in Windows 10, version 1703, the Windows Driver Kit (WDK) includes a class extension module (NetAdapterCx) that enables you to write a KMDF-based driver (called the client driver in this section) for a network adapter.
In previous versions of Windows, you needed to write an NDIS miniport driver.

To learn how to port an NDIS 6.x miniport driver into a Windows Driver Framework (WDF) networking client miniport driver, see [Porting NDIS Miniport Drivers to NetAdapter Class Extension](porting-ndis-to-netadapter-cx.md).

This section contains the following topics:

* [Porting NDIS Miniport Drivers to NetAdapter Class Extension](porting-ndis-to-netadapter-cx.md)
* [Building a NetAdapterCx Client Driver](building-a-netadaptercx-client-driver.md)
* [Device Initialization](device-initialization.md)
* [Accessing Configuration Information](accessing-configuration-information.md)
* [Handling Control Requests](handling-control-requests.md)
* [Debugging NetAdapterCx Client Drivers](debugging-netadaptercx-client-drivers.md)
* [Handling I/O Requests](handling-i-o-requests.md)
* [Configuring Power Management](configuring-power-management.md)
* [Summary of Objects](summary-of-objects.md)
* [Power-Up Sequence for an Network Adapter WDF Client Driver](power-up-sequence-for-ndis-wdf-client-driver.md)
* [Power-Down Sequence for an Network Adapter WDF Client Driver](power-down-sequence-for-ndis-wdf-client-driver.md)
