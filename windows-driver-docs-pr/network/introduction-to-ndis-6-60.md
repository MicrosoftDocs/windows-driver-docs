---
title: Introduction to NDIS 6.60
description: This section introduces NDIS 6.60 and describes changes from NDIS 6.50. NDIS 6.60 is included in Windows 10, version 1607 and Windows Server 2016 and later.
ms.date: 06/01/2017
ms.localizationpriority: medium
---

# Introduction to NDIS 6.60

This topic introduces Network Driver Interface Specification (NDIS) 6.60 and describes its major design additions. NDIS 6.60 is included in Windows 10, version 1607 and Windows Server 2016 and later.

NDIS 6.60 is a minor version update to NDIS 6.50. For more information about porting NDIS 6.x drivers to NDIS 6.60, see [Porting NDIS 6.x drivers to NDIS 6.60](porting-ndis-6-x-drivers-to-ndis-6-60.md).

## Feature updates

NDIS 6.60 is an incremental update to NDIS 6.50 and does not contain any major new features.

## Implementing an NDIS 6.60 driver

An NDIS 6.60 driver must follow the requirements that are defined in [Implementing an NDIS 6.30 driver](implementing-an-ndis-6-30-driver.md).

In addition, an NDIS 6.60 driver must be compliant with the following requirements:

- An NDIS 6.60 driver must report the correct NDIS version when it registers with NDIS.
   
   You must update the major and minor NDIS version number in the NDIS_Xxx_DRIVER_CHARACTERISTICS structure to support NDIS 6.60. The MajorNdisVersion member must contain 6 and the MinorNdisVersion member must contain 60. This requirement applies to miniport, protocol, and filter drivers. You must also update the version information for the compiler (see [Compiling an NDIS 6.60 driver](#compiling-an-ndis-660-driver)).

- NDIS 6.60 miniport drivers for Windows 10, version 1607 and Windows Server 2016 and later must use the NDIS 6.60 versions of data structures. For more information, see [Using NDIS 6.60 data structures](#using-ndis-660-data-structures).

## Compiling an NDIS 6.60 driver

The WDK for Windows 10, version 1607 supports header versioning. Header versioning makes sure that NDIS 6.60 drivers use the appropriate NDIS 6.60 data structures at compile time.

Add the following compiler settings to the Visual Studio project for your driver:

- For a miniport driver, add ```NDIS660_MINIPORT=1```.
- For a filter or protocol driver, add ```NDIS660=1```.

For information on building a driver with the Windows 10, version 1607 release of the WDK, see [Building a Driver](../develop/building-a-driver.md).

## Using NDIS 6.60 data structures

### Updated data structures

The following data structures were updated in NDIS 6.60.

- [NDIS_NIC_SWITCH_CAPABILITIES](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities)
- [NDIS_RECEIVE_SCALE_PARAMETERS](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_scale_parameters)
- [NDIS_RECEIVE_SCALE_CAPABILITIES](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_scale_capabilities)
