---
title: Introduction to NDIS 6.80
description: This section introduces NDIS 6.80 and describes changes from NDIS 6.70. NDIS 6.80 is included in Windows 10, version 1709.
ms.date: 03/02/2023
---

# Introduction to NDIS 6.80

This topic introduces Network Driver Interface Specification (NDIS) 6.80 and describes its major design additions. NDIS 6.80 is included in Windows 10, version 1709.

NDIS 6.80 is a minor version update to NDIS 6.70 for miniport, protocol, filter, and intermediate drivers. For more information about porting NDIS 6.x drivers to NDIS 6.80, see [Porting NDIS 6.x drivers to NDIS 6.80](porting-ndis-6-x-drivers-to-ndis-6-70.md).

For NIC drivers, the NetAdapter class extension (NetAdapterCx) has been updated from version 1.0 to version 1.1 in Windows 10, version 1709.

## Feature updates

### Synchronous OID requests

NDIS 6.80 introduces a new feature for OIDs, Synchronous OID requests. Synchronous OID calls are low-latency, non-blocking, scalable, and reliable compared to regular OID requests. For more info, see [Synchronous OID Request Interface in NDIS 6.80](synchronous-oid-request-interface-in-ndis-6-80.md).

### RSSv2

In NDIS 6.80, [Receive Side Scaling (RSS)](./receive-side-scaling-version-2-rssv2-.md) has been upgraded to RSS version 2 (RSSv2). RSSv2 improves on RSSv2 by offering per-VPort spreading. For more info, see [Receive Side Scaling Version 2 (RSSv2) in NDIS 6.80](receive-side-scaling-version-2-rssv2-in-ndis-6-80.md).

RSSv2 is preview only in Windows 10, version 1709.

### Other new networking features

NDIS forms the core foundation for the network driver platform on Windows. For a list of other network driver features that were updated at the same time as NDIS 6.80, see the Windows 10, version 1709 section for Networking on [What's new in driver development](../what-s-new-in-driver-development.md).

## Implementing an NDIS 6.80 driver

An NDIS 6.80 driver must follow the requirements that are defined in [Implementing an NDIS 6.30 driver](implementing-an-ndis-6-30-driver.md).

In addition, an NDIS 6.80 driver must be compliant with the following requirements:

- An NDIS 6.80 driver must report the correct NDIS version when it registers with NDIS.

  * You must update the major and minor NDIS version number in the NDIS_Xxx_DRIVER_CHARACTERISTICS structure to support NDIS 6.80. The MajorNdisVersion member must contain 6 and the MinorNdisVersion member must contain 80. This requirement applies to miniport, protocol and filter drivers. 

  * You must also update the version information for the compiler (see [Compiling an NDIS 6.80 driver](#compiling-an-ndis-680-driver)).

  * Miniport drivers must set the **Header** member of [**NDIS_MINIPORT_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics): Set **Revision** to NDIS_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_3 and **Size** to NDIS_SIZEOF_MINIPORT_DRIVER_CHARACTERISTICS_REVISION_3. 

  * Filter drivers must set the **Header** member of [**NDIS_FILTER_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_driver_characteristics): Set **Revision** to NDIS_FILTER_CHARACTERISTICS_REVISION_3 and **Size** to NDIS_SIZEOF_FILTER_DRIVER_CHARACTERISTICS_REVISION_3. 

  * Protocol drivers must set the **Header** member of [**NDIS_PROTOCOL_DRIVER_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_protocol_driver_characteristics): Set **Revision** to NDIS_PROTOCOL_CHARACTERISTICS_REVISION_2 and **Size** to NDIS_SIZEOF_PROTOCOL _DRIVER_CHARACTERISTICS_REVISION_2.

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

### New APIs and data structures

The following APIs and data structures are new in NDIS 6.80.

- [MINIPORT_SYNCHRONOUS_OID_REQUEST](/windows-hardware/drivers/ddi/ndis/nf-ndis-miniport_synchronous_oid_request)
- [FILTER_SYNCHRONOUS_OID_REQUEST](/windows-hardware/drivers/ddi/ndis/nf-ndis-filter_synchronous_oid_request)
- [FILTER_SYNCHRONOUS_OID_REQUEST_COMPLETE](/windows-hardware/drivers/ddi/ndis/nf-ndis-filter_synchronous_oid_request_complete)
- [NdisFSynchronousOidRequest](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfsynchronousoidrequest)
- [NdisSynchronousOidRequest](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissynchronousoidrequest)
- [OID_GEN_RECEIVE_SCALE_PARAMETERS_V2](oid-gen-receive-scale-parameters-v2.md)
- [OID_GEN_RSS_SET_INDIRECTION_TABLE_ENTRIES](oid-gen-rss-set-indirection-table-entries.md)
- [NDIS_RECEIVE_SCALE_PARAMETERS_V2](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_scale_parameters_v2)
- [NDIS_RSS_SET_INDIRECTION_ENTRIES](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_rss_set_indirection_entries)
- [NDIS_RSS_SET_INDIRECTION_ENTRY](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_rss_set_indirection_entry)

### Updated APIs and data structures

The following APIs and data structures were updated in NDIS 6.80.

- [NDIS_MINIPORT_DRIVER_CHARACTERISTICS](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics)
- [NDIS_FILTER_DRIVER_CHARACTERISTICS](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_driver_characteristics)
- [NDIS_RECEIVE_SCALE_CAPABILITIES](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_scale_capabilities)
