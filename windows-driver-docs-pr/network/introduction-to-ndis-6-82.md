---
title: Introduction to NDIS 6.82
description: This section introduces NDIS 6.82 and describes changes from NDIS 6.81. NDIS 6.82 is included in Windows 10, version 1809.
ms.date: 08/16/2018
---

# Introduction to NDIS 6.82

This topic introduces Network Driver Interface Specification (NDIS) 6.82 and describes its major design additions. NDIS 6.82 is included in Windows 10, version 1809 and Windows Server 2019 and later.

NDIS 6.82 is a minor version update to NDIS 6.81. For more information about porting NDIS 6.x drivers to NDIS 6.82, see [Porting NDIS 6.x drivers to NDIS 6.82](porting-ndis-6-x-drivers-to-ndis-6-82.md).

## Feature updates

NDIS 6.82 is an incremental update to NDIS 6.81 and does not contain any major new features.

## Implementing an NDIS 6.82 driver

An NDIS 6.82 driver must follow the requirements that are defined in [Implementing an NDIS 6.30 driver](implementing-an-ndis-6-30-driver.md).

In addition, an NDIS 6.82 driver must be compliant with the following requirements:

* An NDIS 6.82 driver must report the correct NDIS version when it registers with NDIS.
   
  * You must update the major and minor NDIS version number in the NDIS_Xxx_DRIVER_CHARACTERISTICS structure to support NDIS 6.82. The MajorNdisVersion member must contain 6 and the MinorNdisVersion member must contain 82. This requirement applies to miniport, protocol, and filter drivers. You must also update the version information for the compiler (see [Compiling an NDIS 6.82 driver](#compiling-an-ndis-682-driver)).

  * Miniport drivers must set the **Header** member of [**NDIS_MINIPORT_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics): Set **Revision** to NDIS_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_3 and **Size** to NDIS_SIZEOF_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_3. 

  * Filter drivers must set the **Header** member of [**NDIS_FILTER_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_driver_characteristics): Set **Revision** to NDIS_FILTER_CHARACTERISTICS_REVISION_3 and **Size** to NDIS_SIZEOF_FILTER_DRIVER_CHARACTERISTICS_REVISION_3. 

  * Protocol drivers must set the **Header** member of [**NDIS_PROTOCOL_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_protocol_driver_characteristics): Set **Revision** to NDIS_PROTOCOL_CHARACTERISTICS_REVISION_2 and **Size** to NDIS_SIZEOF_PROTOCOL _DRIVER_CHARACTERISTICS_REVISION_2.

- NDIS 6.82 miniport drivers for Windows 10, version 1809 and Windows Server 2019 and later must use the NDIS 6.82 versions of data structures.

## Compiling an NDIS 6.82 driver

The WDK for Windows 10, version 1809 supports header versioning. Header versioning makes sure that NDIS 6.82 drivers use the appropriate NDIS 6.82 data structures at compile time.

Add the following compiler settings to the Visual Studio project for your driver:

- For a miniport driver, add `NDIS682_MINIPORT=1`.
- For a filter or protocol driver, add `NDIS682=1`.

For information on building a driver with the Windows 10, version 1809 release of the WDK, see [Building a Driver](../develop/building-a-driver.md).
