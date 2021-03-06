---
title: Minimum Requirements for Supporting Header-Data Split
description: Minimum Requirements for Supporting Header-Data Split
keywords:
- header-data split WDK , requirements
- Ethernet frame splitting WDK networking , requirements
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Minimum Requirements for Supporting Header-Data Split





This topic summarizes the minimum requirements that a provider must meet to support header-data split. For a complete listing of the rules that apply to splitting Ethernet frames, see [Splitting Ethernet Frames](splitting-ethernet-frames.md).

The following list contains the minimum requirements for header-data split support:

-   Providers must not split frames that the [Cases Where Header-Data Split Is Not Used](cases-where-header-data-split-is-not-used.md) topic describes.

-   Providers must move virtual LAN (VLAN) tags to the [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure OOB data. For more information about VLAN requirements, see [Receive Indications with Header-Data Split](receive-indications-with-header-data-split.md).

-   Providers must support splitting IPv4 frames without options. For more information about splitting IPv4 frames, see [Splitting IPv4 Frames](splitting-ipv4-frames.md).

-   Providers must support splitting IPv6 frames without extension headers. For more information about splitting IPv6 frames, see [Splitting IPv6 Frames](splitting-ipv6-frames.md).

-   Providers must support splitting TCP frames at the TCP payload with no TCP options and with only the timestamp option. For more information about splitting TCP frames, see [Splitting Frames at the TCP Payload](splitting-frames-at-the-tcp-payload.md).

-   Providers must support splitting UDP frames at the UDP payload. For more information about splitting UDP frames, see [Splitting Frames at the UDP Payload](splitting-frames-at-the-udp-payload.md).

-   Providers must support the header-data split initialization attributes. For more information about these attributes, see [Initializing a Header-Data Split Provider](initializing-a-header-data-split-provider.md).

-   Providers must support the header-data split receive indication requirements, including setting the header-data split flags in the **NblFlags** member of the [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures, header size requirements, and data backfill requirements. For more information about receive requirements, see [Receive Indications with Header-Data Split](receive-indications-with-header-data-split.md).

-   Providers must support the [OID\_GEN\_HD\_SPLIT\_PARAMETERS](./oid-gen-hd-split-parameters.md) OID, the [OID\_GEN\_HD\_SPLIT\_CURRENT\_CONFIG](./oid-gen-hd-split-current-config.md) OID, the [**NDIS\_STATUS\_HD\_SPLIT\_CURRENT\_CONFIG**](./ndis-status-hd-split-current-config.md) status indication, and registry settings. For more information about header-data split parameters and settings, see [Header-Data Split Administration and Configuration](setting-the-current-header-data-split-configuration.md).

For more information about header-data split requirements for protocol drivers and filter drivers, see [Supporting Header-Data Split in Protocol Driver and Filter Drivers](supporting-header-data-split-in-protocol-driver-and-filter-drivers.md).

 

