---
title: Introduction to NDIS 6.70
description: This section introduces NDIS 6.70 and describes changes from NDIS 6.60. NDIS 6.70 is included in Windows 10, version 1703.
ms.date: 03/02/2023
---

# Introduction to NDIS 6.70

This topic introduces Network Driver Interface Specification (NDIS) 6.70 and describes its major design additions. NDIS 6.70 is included in Windows 10, version 1703.

NDIS 6.70 is a minor version update to NDIS 6.60 for miniport, protocol, filter, and intermediate drivers. For more information about porting NDIS 6.x drivers to NDIS 6.70, see [Porting NDIS 6.x drivers to NDIS 6.70](porting-ndis-6-x-drivers-to-ndis-6-70.md).

## Feature updates

### NetAdapterCx

Alongside NDIS 6.70, Windows 10, version 1703 includes a major new feature for NIC drivers called the Network Adapter WDF Class Extension, a.k.a. [NetAdapterCx](../netcx/index.md). NetAdapterCx is preview only in Windows 10, version 1703. The NetAdapterCx model enables NIC driver developers to harness the full functionality and simplified driver model of WDF, meaning NIC drivers are easier to write.

### Other feature updates

NDIS forms the core foundation for the network driver platform on Windows. For a list of other network driver features that were updated at the same time as NDIS 6.70, see the Windows 10, version 1703 section for Networking on [What's new in driver development](../what-s-new-in-driver-development.md).

## Feature deprecations

The following network driver features have been deprecated along with the release of NDIS 6.70:

- [TCP Chimney Offload](/previous-versions/windows/hardware/network/ndis-tcp-chimney-offload)
- [IPsec Offload Version 2](./introduction-to-ipsec-offload-version-2.md)

## Implementing an NDIS 6.70 driver

### NIC drivers

For more information about implementing a NIC driver with the NetAdapterCx, see [NetAdapterCx](../netcx/index.md).

### Miniport, protocol, filter, and intermediate drivers

An NDIS 6.70 driver must follow the requirements that are defined in [Implementing an NDIS 6.30 driver](implementing-an-ndis-6-30-driver.md).

In addition, an NDIS 6.70 driver must be compliant with the following requirements:

- An NDIS 6.70 driver must report the correct NDIS version when it registers with NDIS.

   * You must update the major and minor NDIS version number in the NDIS_Xxx_DRIVER_CHARACTERISTICS structure to support NDIS 6.70. The MajorNdisVersion member must contain 6 and the MinorNdisVersion member must contain 70. This requirement applies to miniport, protocol and filter drivers. You must also update the version information for the compiler (see [Compiling an NDIS 6.70 driver](#compiling-an-ndis-670-driver)).

  * Miniport drivers must set the **Header** member of [**NDIS_MINIPORT_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics): Set **Revision** to NDIS_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_2 and **Size** to NDIS_SIZEOF_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_2. 

  * Filter drivers must set the **Header** member of [**NDIS_FILTER_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_driver_characteristics): Set **Revision** to NDIS_FILTER_CHARACTERISTICS_REVISION_2 and **Size** to NDIS_SIZEOF_FILTER_DRIVER_CHARACTERISTICS_REVISION_2. 

  * Protocol drivers must set the **Header** member of [**NDIS_PROTOCOL_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_protocol_driver_characteristics): Set **Revision** to NDIS_PROTOCOL_CHARACTERISTICS_REVISION_2 and **Size** to NDIS_SIZEOF_PROTOCOL _DRIVER_CHARACTERISTICS_REVISION_2.

## Compiling an NDIS 6.70 driver

### NIC drivers

For more information about compiling a NIC driver with the NetAdapterCx, see [Porting NDIS miniport drivers to NetAdapterCx (Compilation settings)](../netcx/porting-ndis-miniport-drivers-to-netadaptercx.md#compilation-settings).

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

- [NDIS_STATUS_WWAN_DEVICE_CAPS_EX](./ndis-status-wwan-device-caps-ex.md)
