---
title: NDIS Versions in Network Drivers
description: NDIS Versions in Network Drivers
ms.assetid: 6ecd4040-2831-4238-8080-97edc6a7c3ba
keywords: ["network drivers WDK , NDIS versions", "NDIS WDK , versions in network drivers", "backward compatibility WDK networking", "compatibility WDK networking"]
---

# NDIS Versions in Network Drivers


## <a href="" id="ddk-ndis-versions-ng"></a>


If you are writing an NDIS driver for more than one version of Microsoft Windows, be sure the features that you are using are supported on each Windows version. New features have been added to NDIS with each release. Other features became obsolete and were removed from later NDIS versions.

This set of design guide documentation is targeted at Windows Vista and later operating systems and NDIS 6.0 and later drivers. Documentation for earlier Windows and NDIS versions is contained in prior releases of the documentation. For the Windows XP and NDIS 5.1 documentation, see [Windows 2000 and Windows XP Networking Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff565849).

**Note**  A driver can query the NDIS version by calling the [**NdisReadConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff564511) function with the *Keyword* parameter set to **NdisVersion**.

 

Windows operating system, Microsoft Windows Driver Kit (WDK), and Driver Development Kit (DDK) version support for NDIS versions, as well as support for major NDIS features across NDIS versions, are described in the following table.

Operating system
Development Kit
Supported NDIS version
CoNDIS
Deserialized driver
Intermediate driver
Windows 95/

Windows NT 4.0 DDK or Windows 95 DDK

3.1

Added support for miniport drivers and Plug and Play.

Windows 95 OSR2

Windows NT 4.0 DDK or Windows 95 DDK

4.0

Protocol driver is a vxd-type driver.

Windows 98

Windows NT 4.0 DDK or Windows 98 DDK

4.1

X

X

X

Protocol driver is a vxd-type driver.

Windows 98 SE

Windows NT 4.0 DDK or Windows 98 DDK

5.0

X

X

X

Added support for Power Management and WMI.

Windows Me

Windows NT 4.0 DDK or Windows 98 DDK for Vxds

5.0

X

X

X

Windows NT 3.5

Windows NT 3.5 DDK

3.0

Windows NT 4.0

Windows NT 4.0 DDK

4.0

Added these features:

-   [**MiniportSendPackets**](https://msdn.microsoft.com/library/windows/hardware/ff550524)

-   [**ProtocolReceivePacket**](https://msdn.microsoft.com/library/windows/hardware/ff563251)

-   [**MiniportAllocateComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549352)

Windows NT 4.0 SP3

Windows NT DDK with updated NDIS header and library

4.1

X

X

X

Windows 2000

Windows 2000 DDK

5.0

X

X

X

Added support for:

-   New INF file format compatible with Windows 95/98/Me

-   Plug and Play and Power Management

-   WMI

-   LBFO

-   Scatter/gather DMA support for deserialized miniport drivers

Windows XP

See [Windows 8.1: Download kits and tools](http://go.microsoft.com/fwlink/p/?linkid=239721).

5.1

X

X

X

Added support for:

-   [**MiniportCancelSendPackets**](https://msdn.microsoft.com/library/windows/hardware/ff549359)

-   [**MiniportPnPEventNotify**](https://msdn.microsoft.com/library/windows/hardware/ff550487)

-   [**MiniportShutdown**](https://msdn.microsoft.com/library/windows/hardware/ff550533)

-   [**NdisCancelSendPackets**](https://msdn.microsoft.com/library/windows/hardware/ff550821)

-   [**NdisCopyFromPacketToPacketSafe**](https://msdn.microsoft.com/library/windows/hardware/ff551071)

-   [**NdisGeneratePartialCancelId**](https://msdn.microsoft.com/library/windows/hardware/ff562623)

-   [**NdisGetFirstBufferFromPacketSafe**](https://msdn.microsoft.com/library/windows/hardware/ff552066)

-   [**NdisGetPoolFromPacket**](https://msdn.microsoft.com/library/windows/hardware/ff552090)

-   [**NdisGetSharedDataAlignment**](https://msdn.microsoft.com/library/windows/hardware/ff562671)

-   [**NdisIMGetCurrentPacketStack**](https://msdn.microsoft.com/library/windows/hardware/ff552155)

-   [**NdisIMNotifyPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff552203)

-   [**NdisQueryPendingIOCount**](https://msdn.microsoft.com/library/windows/hardware/ff554456)

-   [**NDIS\_GET\_PACKET\_CANCEL\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff556988)

-   [**NDIS\_SET\_PACKET\_CANCEL\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff557195)

-   [OID\_GEN\_MACHINE\_NAME](https://msdn.microsoft.com/library/windows/hardware/ff569596)

-   New miniport driver attribute flags

-   64-bit statistical counters

-   Remote NDIS

-   Scatter/gather support for both serialized and deserialized miniport drivers

-   Packet stacking for intermediate drivers

-   VLAN tagging

-   Offloading the Processing of UDP-Encapsulated ESP Packets (Windows Server 2003 only)

-   Wi-Fi Protected Access (WPA) in Windows XP SP1

Dropped support for:

-   Full Mac drivers

-   NDIS 3.0 protocols

-   **NdisQueryMapRegisterCount**

-   EISA bus

Windows Vista

See [Windows 8.1: Download kits and tools](http://go.microsoft.com/fwlink/p/?linkid=239721).

6.0

X

X

X

Major improvements in the following provide significant performance gains for both clients and servers:

-   Network data packaging

-   Send and receive paths

-   Run-time reconfiguration capabilities

-   Scatter/gather DMA

-   Filter drivers

-   Multiprocessor scaling of received data handling

-   Offloading TCP tasks to NICs

The following improvements simplify driver development:

-   Streamlined driver initialization

-   Versioning support for NDIS interfaces

-   Simplified reset handling

-   A standard interface for obtaining management information

-   A filter driver model to replace filter intermediate drivers

For more information about NDIS 6.0 features, see [Introduction to NDIS 6.0](introduction-to-ndis-6-0.md).

For information about backward compatibility and obsolete features that are not supported in NDIS 6.0 drivers, see [NDIS 6.0 Backward Compatibility](ndis-6-0-backward-compatibility.md).

Windows Vista with Service Pack 1 (SP1) and Windows Server 2008

See [Windows 8.1: Download kits and tools](http://go.microsoft.com/fwlink/p/?linkid=239721).

6.1

X

X

X

For information about NDIS 6.1 features, see [Introduction to NDIS 6.1](introduction-to-ndis-6-1.md).

Windows 7 and Windows Server 2008 R2

See [Windows 8.1: Download kits and tools](http://go.microsoft.com/fwlink/p/?linkid=239721).

6.20

X

X

X

For information about NDIS 6.20 features, see [Introduction to NDIS 6.20](introduction-to-ndis-6-20.md).

For information about backward compatibility and obsolete features that are not supported in NDIS 6.20 drivers, see [NDIS 6.20 Backward Compatibility](ndis-6-20-backward-compatibility.md).

Windows 8

and Windows Server 2012
See [Windows 8.1: Download kits and tools](http://go.microsoft.com/fwlink/p/?linkid=239721).

6.30

X

X

X

For information about NDIS 6.30 features, see [Introduction to NDIS 6.30](introduction-to-ndis-6-30.md).

Windows 8.1 and Windows Server 2012 R2

See [Windows 8.1: Download kits and tools](http://go.microsoft.com/fwlink/p/?linkid=239721).

6.40

X

X

X

For information about NDIS 6.40 features, see [Introduction to NDIS 6.40](introduction-to-ndis-6-40.md).

 

 

 





