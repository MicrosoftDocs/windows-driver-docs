---
title: Introduction to NDIS 6.70
description: This section introduces NDIS 6.70 and describes changes from NDIS 6.60. NDIS 6.70 is included in Windows 10, version 1703.
ms.assetid: D846EE68-2C84-40E0-91DE-2034F75D576F
ms.author: windowsdriverdev
ms.date: 06/01/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to NDIS 6.70

This topic introduces Network Driver Interface Specification (NDIS) 6.70 and describes its major design additions. NDIS 6.70 is included in Windows 10, version 1703.

NDIS 6.70 is a minor version update to NDIS 6.60 for miniport, protocol, filter, and intermediate drivers. For more information about porting NDIS 6.x drivers to NDIS 6.70, see [Porting NDIS 6.x drivers to NDIS 6.70](porting-ndis-6-x-drivers-to-ndis-6-70.md).

## Feature updates

### NetAdapterCx

NDIS 6.70 includes a major new feature for NIC drivers, the Network Adapter WDF Class Extension, a.k.a. [NetAdapterCx](../netcx/index.md). NetAdapterCx is preview only in Windows 10, version 1703. The NetAdapterCx model enables NIC driver developers to harness the full functionality and simplified driver model of WDF, meaning NIC drivers are easier to write.

### Other feature updates

NDIS forms the core foundation for the network driver platform on Windows. For a list of other network driver features that were updated at the same time as NDIS 6.70, see the Windows 10, version 1703 section for Networking on [What's new in driver development](../what-s-new-in-driver-development.md).

## Feature deprecations

The following network driver features have been deprecated along with the release of NDIS 6.70:

- [TCP Chimney Offload](ndis-tcp-chimney-offload.md)
- [IPsec Offload Version 2](ipsec-offload-version-2.md)

## Implementing an NDIS 6.70 driver

### NIC drivers

For more information about implementing a NIC driver with the NetAdapterCx, see [NetAdapterCx](../netcx/index.md).

### Miniport, protocol, filter, and intermediate drivers

An NDIS 6.70 driver must follow the requirements that are defined in [Implementing an NDIS 6.60 driver](introduction-to-ndis-6-60.md#implementing-an-ndis-660-driver).

In addition, an NDIS 6.70 driver must be compliant with the following requirements:

- An NDIS 6.70 driver must report the correct NDIS version when it registers with NDIS.

   You must update the major and minor NDIS version number in the NDIS_Xxx_DRIVER_CHARACTERISTICS structure to support NDIS 6.70. The MajorNdisVersion member must contain 6 and the MinorNdisVersion member must contain 70. This requirement applies to miniport, protocol and filter drivers. You must also update the version information for the compiler (see [Compiling an NDIS 6.70 driver](#compiling-an-ndis-670-driver)).

## Compiling an NDIS 6.70 driver

### NIC drivers

For more information about compiling a NIC driver with the NetAdapterCx, see [Porting NDIS miniport drivers to NetAdapter Class Extension (Compilation settings)](../netcx/porting-ndis-to-netadapter-cx.md#compilation-settings).

### Miniport, protocol, and filter drivers

The WDK for Windows 10, version 1703 supports header versioning. Header versioning makes sure that NDIS 6.70 drivers use the appropriate NDIS 6.70 data structures at compile time.

Add the following compiler settings to the Visual Studio project for your driver:

- For a miniport driver, add ```NDIS670_MINIPORT=1```.
- For a filter or protocol driver, add ```NDIS670=1```.

For information on building a driver with the Windows 10, version 1703 release of the WDK, see [Building a Driver](../develop/building-a-driver.md).

## Using NDIS 6.70 driver data structures

### NIC drivers

For more information about NetAdapterCx data structures, see [NetAdapterCx](../netcx/index.md).

### Miniport, protocol, filter, and intermediate drivers

#### New data structures

The following data structures are new in NDIS 6.70.

- [NDIS_STATUS_WWAN_DEVICE_CAPS_EX](https://msdn.microsoft.com/library/windows/hardware/mt782396)

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")