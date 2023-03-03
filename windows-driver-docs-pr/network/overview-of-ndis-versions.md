---
title: Overview of NDIS versions
description: The Windows operating system, Microsoft Windows Driver Kit (WDK), and Driver Development Kit (DDK) version support for NDIS versions. Support for major NDIS features across NDIS versions.
keywords:
- network drivers WDK , NDIS versions
- NDIS WDK , versions in network drivers
- backward compatibility WDK networking
- compatibility WDK networking
ms.date: 03/02/2023
ms.custom: contperf-fy21q4
---

# Overview of NDIS versions

If you're writing an NDIS driver for more than one version of Microsoft Windows, be sure the features that you're using are supported on each Windows version. New features have been added to NDIS with each release. Other features became obsolete and were removed from later NDIS versions.

This set of design guide documentation is targeted at Windows Vista and later operating systems and NDIS 6.0 and later drivers. Documentation for earlier Windows and NDIS versions is contained in prior releases of the documentation. For the Windows XP and NDIS 5.1 documentation, see [Windows 2000 and Windows XP Networking Design Guide](/previous-versions/windows/hardware/network/ff565849(v=vs.85)).

> [!NOTE]
> A driver can query the NDIS version by calling the [**NdisReadConfiguration**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisreadconfiguration) function with the *Keyword* parameter set to **NdisVersion**. 

The following table describes Windows operating system, Microsoft Windows Driver Kit (WDK), and Driver Development Kit (DDK) version support for NDIS versions. This table also describes support for major NDIS features across NDIS versions.

| Operating system | Development Kit | Supported NDIS version | CoNDIS | Deserialized driver | Intermediate driver |
| --- | --- | --- | --- | --- | --- |
| Windows 11, version 21H2 | See [Download kits for Windows hardware development](https://go.microsoft.com/fwlink/p/?linkid=239721). | 6.86. For more information about NDIS 6.86 features, see [Introduction to NDIS 6.86](introduction-to-ndis-6-86.md). | X | X | X |
| Windows Server 2022 | See [Download kits for Windows hardware development](https://go.microsoft.com/fwlink/p/?linkid=239721). | 6.85. For more information about NDIS 6.85 features, see [Introduction to NDIS 6.85](introduction-to-ndis-6-85.md). | X | X | X |
| Windows 10, version 2004 | See [Download kits for Windows hardware development](https://go.microsoft.com/fwlink/p/?linkid=239721). | 6.84. For more information about NDIS 6.84 features, see [Introduction to NDIS 6.84](introduction-to-ndis-6-84.md). | X | X | X |
| Windows 10, version 1903 | See [Download kits for Windows hardware development](https://go.microsoft.com/fwlink/p/?linkid=239721). | 6.83. For more information about NDIS 6.83 features, see [Introduction to NDIS 6.83](introduction-to-ndis-6-83.md). | X | X | X |
| Windows 10, version 1809 | See [Download kits for Windows hardware development](https://go.microsoft.com/fwlink/p/?linkid=239721). | 6.82. For more information about NDIS 6.82 features, see [Introduction to NDIS 6.82](introduction-to-ndis-6-82.md). | X | X | X |
| Windows 10, version 1803 | See [Download kits for Windows hardware development](https://go.microsoft.com/fwlink/p/?linkid=239721). | 6.81. For more information about NDIS 6.81 features, see [Introduction to NDIS 6.81](introduction-to-ndis-6-81.md). | X | X | X |
| Windows 10, version 1803 | See [Download kits for Windows hardware development](https://go.microsoft.com/fwlink/p/?linkid=239721). | 6.81. For more information about NDIS 6.81 features, see [Introduction to NDIS 6.81](introduction-to-ndis-6-81.md). | X | X | X |
| Windows 10, version 1709 | See [Download kits for Windows hardware development](https://go.microsoft.com/fwlink/p/?linkid=239721). | 6.80. For more information about NDIS 6.80 features, see [Introduction to NDIS 6.80](introduction-to-ndis-6-80.md). | X | X | X |
| Windows 10, version 1703 | See [Download kits for Windows hardware development](https://go.microsoft.com/fwlink/p/?linkid=239721). | 6.70. NDIS 6.70 coincided with a preview release of the Network Adapter WDF Class Extension, also known as [NetAdapterCx](../netcx/index.md).<p>For more information about NDIS 6.70 features, see [Introduction to NDIS 6.70](introduction-to-ndis-6-70.md) | X | X | X |
| Windows 10, version 1607 and Windows Server 2016 | See [Download kits for Windows hardware development](https://go.microsoft.com/fwlink/p/?linkid=239721). | 6.60. For more information about NDIS 6.60 features, see [Introduction to NDIS 6.60](introduction-to-ndis-6-60.md). | X | X | X |
| Windows 10, version 1511 | See [Download kits for Windows hardware development](https://go.microsoft.com/fwlink/p/?linkid=239721). | 6.51 | X | X | X |
| Windows 10, version 1507 | See [Download kits for Windows hardware development](https://go.microsoft.com/fwlink/p/?linkid=239721). | 6.50. For more information about NDIS 6.50 features, see [Introduction to NDIS 6.50](introduction-to-ndis-6-50.md). | X | X | X |
| Windows 8.1 and Windows Server 2012 R2 | See [Download kits for Windows hardware development](https://go.microsoft.com/fwlink/p/?linkid=239721). | 6.40. For information about NDIS 6.40 features, see [Introduction to NDIS 6.40](introduction-to-ndis-6-40.md). | X | X | X |
| Windows 8 and Windows Server 2012 | See [Download kits for Windows hardware development](https://go.microsoft.com/fwlink/p/?linkid=239721). | 6.30. For information about NDIS 6.30 features, see [Introduction to NDIS 6.30](introduction-to-ndis-6-30.md). | X | X | X |
| Windows 7 and Windows Server 2008 R2 | See [Download kits for Windows hardware development](https://go.microsoft.com/fwlink/p/?linkid=239721). | 6.20. For information about NDIS 6.20 features, see [Introduction to NDIS 6.20](introduction-to-ndis-6-20.md). For information about backward compatibility and obsolete features that aren't supported in NDIS 6.20 drivers, see [NDIS 6.20 Backward Compatibility](ndis-6-20-backward-compatibility.md). | X | X | X |
| Windows Vista with Service Pack 1 (SP1) and Windows Server 2008 | See [Download kits for Windows hardware development](https://go.microsoft.com/fwlink/p/?linkid=239721). | 6.1. For information about NDIS 6.1 features, see [Introduction to NDIS 6.1](introduction-to-ndis-6-1.md). | X | X | X |
| Windows Vista | See [Download kits for Windows hardware development](https://go.microsoft.com/fwlink/p/?linkid=239721) | 6.0. Major improvements in the following provide significant performance gains for both clients and servers: <ul><li>Network data packaging</li><li>Send and receive paths</li><li>Run-time reconfiguration capabilities</li><li>Scatter/gather DMA</li><li>Filter drivers</li><li>Multiprocessor scaling of received data handling</li><li>Offloading TCP tasks to NICs</li></ul><br> The following improvements simplify driver development: <ul><li>Streamlined driver initialization</li><li>Versioning support for NDIS interfaces</li><li>Simplified reset handling</li><li>A standard interface for obtaining management information</li><li>A filter driver model to replace filter intermediate drivers</li></ul><br> For more information about NDIS 6.0 features, see [Introduction to NDIS 6.0](introduction-to-ndis-6-0.md).<p>For information about backward compatibility and obsolete features that aren't supported in NDIS 6.0 drivers, see [NDIS 6.0 Backward Compatibility](/previous-versions/windows/hardware/network/ndis-6-0-backward-compatibility).</p>| X | X | X |
| Windows XP | See [Download kits for Windows hardware development](https://go.microsoft.com/fwlink/p/?linkid=239721) | 5.1. Added support for: New miniport driver attribute flags, 64-bit statistical counters, Remote NDIS, Scatter/gather support for both serialized and deserialized miniport drivers, Packet stacking for intermediate drivers, VLAN tagging, Offloading the Processing of UDP-Encapsulated ESP Packets (Windows Server 2003 only), Wi-Fi Protected Access (WPA) in Windows XP SP1.<p>Dropped support for: Full Mac drivers, NDIS 3.0 protocols, **NdisQueryMapRegisterCount**, EISA bus| X | X | X |
| Windows 2000 | Windows 2000 DDK | 5.0 | X | X | X |
| Windows NT 4.0 SP3 | Windows NT DDK with updated NDIS header and library | 4.1 | X | X | X |
| Windows NT 4.0 | Windows NT 4.0 DDK | 4.0 |  |  |  |
| Windows NT 3.5 | Windows NT 3.5 DDK | 3.0 |  |  |  |
| Windows Me | Windows NT 4.0 DDK or Windows 98 DDK for Vxds | 5.0 | X | X | X |
| Windows 98 SE | Windows NT 4.0 DDK or Windows 98 DDK | 5.0. Added support for new INF file format compatible with Windows 95/98/Me, Plug and Play and Power Management, WMI, LBFO, and scatter/gather DMA support for deserialized miniport drivers. | X | X | X |
| Windows 98 | Windows NT 4.0 DDK or Windows 98 DDK | 4.1. Protocol driver is a vxd-type driver. | X | X | X |
| Windows 95 OSR2 | Windows NT 4.0 DDK or Windows 95 DDK | 4.0. Protocol driver is a vxd-type driver. Added these features: [**MiniportSendPackets**](/previous-versions/windows/hardware/network/ff550524(v=vs.85)), [**ProtocolReceivePacket**](/previous-versions/windows/hardware/network/ff563251(v=vs.85)), [**MiniportAllocateComplete**](/previous-versions/windows/hardware/network/ff549352(v=vs.85)).|  |  |  |
| Windows 95 | Windows NT 4.0 DDK or Windows 95 DDK | 3.1. Added support for miniport drivers and Plug and Play. |  |  |  |



