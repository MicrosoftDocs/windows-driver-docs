---
title: Introduction to NDIS 6.80
description: This section introduces NDIS 6.80 and describes changes from NDIS 6.70. NDIS 6.80 is included in Windows 10, version 1709.
ms.assetid: 5E6E12BF-DE34-4CDD-84BB-7708A59134E9
ms.author: windowsdriverdev
ms.date: 07/05/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to NDIS 6.80

This topic introduces Network Driver Interface Specification (NDIS) 6.80 and describes its major design additions. NDIS 6.80 is included in Windows 10, version 1709.

NDIS 6.80 is a minor version update to NDIS 6.70 for miniport, protocol, filter, and intermediate drivers. For more information about porting NDIS 6.x drivers to NDIS 6.80, see [Porting NDIS 6.x drivers to NDIS 6.80](porting-ndis-6-x-drivers-to-ndis-6-70.md).

For NIC drivers, the NetAdapter class extension (NetAdapterCx) has been updated from version 1.0 to version 1.1 in Windows 10, version 1709. For more information about the changes from NetAdapterCx 1.0 to NetAdapterCx 1.1, see [Introduction to NetAdapterCx 1.1](../netcx/introduction-to-netadaptercx-1-1.md).

## Feature updates

### Synchronous OID requests

NDIS 6.80 introduces a new feature for OIDs, Synchronous OID requests. Synchronous OID calls are low-latency, non-blocking, scalable, and reliable compared to regular OID requests. For more info, see [Synchronous OID Request Interface in NDIS 6.80](synchronous-oid-request-interface-in-ndis-6-80.md).

> [!WARNING]
> In Windows 10, version 1709, synchronous OID requests are supported only for miniport and protocol drivers.

### RSSv2

In NDIS 6.80, [Receive Side Scaling (RSS)](ndis-receive-side-scaling2.md) has been upgraded to RSS version 2 (RSSv2). RSSv2 improves on RSSv2 by enabling per-VPort spreading. For more info, see [Receive Side Scaling Version 2 (RSSv2) in NDIS 6.80](receive-side-scaling-version-2-rssv2-in-ndis-6-80.md).

### Other new networking features

NDIS forms the core foundation for the network driver platform on Windows. For a list of other network driver features that were updated at the same time as NDIS 6.80, see the Windows 10, version 1709 section for Networking on [What's new in driver development](../what-s-new-in-driver-development.md).

## Implementing an NDIS 6.80 driver

### NIC drivers

For more information about implementing a NIC driver with NetAdapterCx 1.1, see [Introduction to NetAdapterCx 1.1](../netcx/introduction-to-netadaptercx-1-1.md).

### Miniport, protocol, filter, and intermediate drivers

An NDIS 6.80 driver must follow the requirements that are defined in [Implementing an NDIS 6.30 driver](implementing-an-ndis-6-30-driver.md).

In addition, an NDIS 6.80 driver must be compliant with the following requirements:

- An NDIS 6.80 driver must report the correct NDIS version when it registers with NDIS.

   You must update the major and minor NDIS version number in the NDIS_Xxx_DRIVER_CHARACTERISTICS structure to support NDIS 6.80. The MajorNdisVersion member must contain 6 and the MinorNdisVersion member must contain 80. This requirement applies to miniport, protocol and filter drivers. You must also update the version information for the compiler (see [Compiling an NDIS 6.80 driver](#compiling-an-ndis-670-driver)).

## Compiling an NDIS 6.80 driver

### NIC drivers

For more information about compiling a NIC driver with the NetAdapterCx, see [Porting NDIS miniport drivers to NetAdapterCx (Compilation settings)](../netcx/porting-ndis-miniport-drivers-to-netadaptercx.md#compilation-settings).

### Miniport, protocol, and filter drivers

The WDK for Windows 10, version 1709 supports header versioning. Header versioning makes sure that NDIS 6.80 drivers use the appropriate NDIS 6.80 data structures at compile time.

Add the following compiler settings to the Visual Studio project for your driver:

- For a miniport driver, add ```NDIS680_MINIPORT=1```.
- For a filter or protocol driver, add ```NDIS680=1```.

For information on building a driver with the Windows 10, version 1709 release of the WDK, see [Building a Driver](../develop/building-a-driver.md).

## API and data structure changes

### NIC drivers

For more information about NetAdapterCx API and data structure changes, see [Introduction to NetAdapterCx 1.1](../netcx/introduction-to-netadaptercx-1-1.md).

### Miniport, protocol, filter, and intermediate drivers

#### New APIs and data structures

The following APIs and data structures are new in NDIS 6.80.

- [MINIPORT_SYNCHRONOUS_OID_REQUEST](https://msdn.microsoft.com/library/windows/hardware/0DDF9CF8-91F6-4D7C-A8E8-FC425BF155CB)
- [FILTER_SYNCHRONOUS_OID_REQUEST](https://msdn.microsoft.com/library/windows/hardware/AC84B27B-6FBF-429D-A8FA-F3C8F583F738)
- [FILTER_SYNCHRONOUS_OID_REQUEST_COMPLETE](https://msdn.microsoft.com/library/windows/hardware/E0749F52-CC7C-484D-8350-1986154957C1)
- [NdisFSynchronousOidRequest](https://msdn.microsoft.com/library/windows/hardware/01B625EB-AB6D-496F-95F2-22845460324A)
- [NdisSynchronousOidRequest](https://msdn.microsoft.com/library/windows/hardware/BF539DDA-59ED-4010-88BC-3C7D8DC475EF)
- [OID_GEN_RECEIVE_SCALE_PARAMETERS_V2](oid-gen-receive-scale-parameters-v2.md)
- [OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES](oid-gen-rss-set-indirection-table-entries.md)
- [NDIS_RECEIVE_SCALE_PARAMETERS_V2](https://msdn.microsoft.com/library/windows/hardware/96EAB6EE-BF9A-46AD-8DED-5D9BD2B6F219)
- [NDIS_RSS_SET_INDIRECTION_ENTRIES](https://msdn.microsoft.com/library/windows/hardware/9AB69EC6-FE78-4242-89C7-D36AA16676BF)
- [NDIS_RSS_SET_INDIRECTION_ENTRY](https://msdn.microsoft.com/library/windows/hardware/4430E19F-C603-4C52-8FC8-C36197FD2996)

#### Updated APIs and data structures

The following APIs and data structures were updated in NDIS 6.80.

- [NDIS_MINIPORT_DRIVER_CHARACTERISTICS](https://msdn.microsoft.com/library/windows/hardware/ff565958)
- [NDIS_FILTER_DRIVER_CHARACTERISTICS](https://msdn.microsoft.com/library/windows/hardware/ff565515)
- [NDIS_RECEIVE_SCALE_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff567220)

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")