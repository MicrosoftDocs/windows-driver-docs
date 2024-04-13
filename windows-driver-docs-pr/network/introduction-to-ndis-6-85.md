---
title: Introduction to NDIS 6.85
description: This section introduces NDIS 6.85 and describes changes from NDIS 6.84. NDIS 6.85 is included in Windows 10, version 21H2.
ms.date: 06/14/2023
---

# Introduction to NDIS 6.85

This topic introduces Network Driver Interface Specification (NDIS) 6.85 and describes its major design additions. NDIS 6.85 is included in Windows 10, version 21H2 and Windows Server 2022 and later.

NDIS 6.85 is a minor version update to NDIS 6.84. For more information about porting NDIS 6.x drivers to NDIS 6.85, see [Porting NDIS 6.x drivers to NDIS 6.85](porting-ndis-6-x-drivers-to-ndis-6-85.md).

## Feature updates

### NDIS Poll mode

NDIS 6.85 introduces NDIS Poll Mode, an OS controlled polling execution model that drives the network interface datapath. Previously, NDIS drivers typically relied on Deferred Procedure Calls (DPCs) to implement their execution model. NDIS Poll Mode moves the complexity of scheduling decisions away from NIC drivers and into NDIS. For more information, see [NDIS Poll Mode](ndis-poll-mode.md).

### Network Virtualization using Generic Routing Encapsulation (NVGRE) with UDP segmentation offload (USO)

NDIS 6.85 introduces [Supporting NVGRE in UDP Segmentation Offload (USO)](nvgre-support-with-udp-segmentation-offload.md). NDIS miniport, protocol, and filter drivers, as well as NICs that perform USO, should support NVGRE and VXLAN encapsulations.
 
## Implementing an NDIS 6.85 driver

An NDIS 6.85 driver must follow the requirements that are defined in [Implementing an NDIS 6.30 driver](implementing-an-ndis-6-30-driver.md).

In addition, an NDIS 6.85 driver must be compliant with the following requirements:

* An NDIS 6.85 driver must report the correct NDIS version when it registers with NDIS.
   
  * You must update the major and minor NDIS version number in the NDIS_Xxx_DRIVER_CHARACTERISTICS structure to support NDIS 6.85. The MajorNdisVersion member must contain 6 and the MinorNdisVersion member must contain 85. This requirement applies to miniport, protocol, and filter drivers. You must also update the version information for the compiler (see [Compiling an NDIS 6.85 driver](#compiling-an-ndis-685-driver)).

  * Miniport drivers must set the **Header** member of [**NDIS_MINIPORT_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics): Set **Revision** to NDIS_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_3 and **Size** to NDIS_SIZEOF_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_3. 

  * Filter drivers must set the **Header** member of [**NDIS_FILTER_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_driver_characteristics): Set **Revision** to NDIS_FILTER_CHARACTERISTICS_REVISION_3 and **Size** to NDIS_SIZEOF_FILTER_DRIVER_CHARACTERISTICS_REVISION_3. 

  * Protocol drivers must set the **Header** member of [**NDIS_PROTOCOL_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_protocol_driver_characteristics): Set **Revision** to NDIS_PROTOCOL_CHARACTERISTICS_REVISION_2 and **Size** to NDIS_SIZEOF_PROTOCOL _DRIVER_CHARACTERISTICS_REVISION_2.

- NDIS 6.85 miniport drivers for Windows 10, version 21H2 and Windows Server 2022 and later must use the NDIS 6.85 versions of data structures.

## Compiling an NDIS 6.85 driver

The WDK for Windows 10, version 21H2 supports header versioning. Header versioning makes sure that NDIS 6.85 drivers use the appropriate NDIS 6.85 data structures at compile time.

Add the following compiler settings to the Visual Studio project for your driver:

- For a miniport driver, add `NDIS685_MINIPORT=1`.
- For a filter or protocol driver, add `NDIS685=1`.

For information on building a driver with the Windows 10, version 21H2 release of the WDK, see [Building a Driver](../develop/building-a-driver.md).
