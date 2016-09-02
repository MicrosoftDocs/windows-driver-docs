---
title: MAC/PHY Reset Operation
description: MAC/PHY Reset Operation
ms.assetid: f7d7c382-3c91-4609-a9e7-dabe25840c87
keywords: ["MAC/PHY reset WDK Native 802.11"]
---

# MAC/PHY Reset Operation


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

When a method request of [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409) is made, the parameters for the reset request are defined through the DOT11\_RESET\_REQUEST structure. Based on the values of the members of this structure, the miniport driver must:

-   Reset either the media access control (MAC) and/or the PHY layers on the 802.11 station. The **dot11ResetType** member defines which layers the driver will reset.

    If the miniport driver is operating in Extensible Station (ExtSTA) mode, only a reset of both the MAC and all PHY layers is allowed. The driver must fail the method request of [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409) by returning NDIS\_STATUS\_FAILURE from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function if the **dot11ResetType** member is not set to **dot11\_reset\_type\_phy\_and\_mac**.

-   Set the MAC address used by the 802.11 station to the address specified in the **dot11MacAddress** member. In this way, the 802.11 station can be configured with a locally administered MAC address to override the NIC's permanent MAC address.

-   If the **bSetDefaultMIB** member is **TRUE**, restore the 802.11 and Native 802.11 MIB objects to their specified default values for the IEEE layers undergoing a reset.

Regardless of the parameters for the reset request, the miniport driver must always do the following when a method request of [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409) is made:

-   If connected, disconnect from its basic service set (BSS) network connection.

    If the miniport driver is operating in Extensible Station (ExtSTA) mode, it must issue the indications required for the disconnection operation. For more information about the disconnection operation, see [Disconnection Operations](disconnection-operations.md).

-   Cancel any explicit scan operations in progress that were initiated through a set of [OID\_DOT11\_SCAN\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569413). The miniport driver is not required to terminate any implicit scan operations initiated by the 802.11 station.

    The miniport driver must also clear the cached list of BSS networks that it detected during the previous scan operations.

    For more information about the scan operation, see [Native 802.11 Scan Operations](native-802-11-scan-operations.md).

-   Flush all pending packets within its transmit queue and complete them through calls to [**NdisMSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563668). For each [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure completed through this call, the miniport driver must set the **Status** member to NDIS\_STATUS\_RESET\_IN\_PROGRESS.

-   Flush all pending packets from its receive queue that have not been indicated through calls to [**NdisMSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563668).

    In addition, the miniport driver must not complete the method request of [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409) until all previously indicated receive packets have been returned through calls to [*MiniportReturnNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559437).

-   Clear any cipher keys previously downloaded to the 802.11 station through set requests of Native 802.11 object identifiers (OIDs). The driver must clear all cipher key tables on the station, including the default cipher, per station and key-mapping keys.

-   Clear all entries from the pairwise master key identifier (PMKID) cache supported by the 802.11 station.

-   Transition to the initialization (INIT) state of the currently configured Native 802.11 operation mode.

If the miniport driver is operating in Extensible Station (ExtSTA) mode, it must do the following when a method request of [OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409) is made:

-   Reset and clear all statistical counters queried through [OID\_DOT11\_STATISTICS](https://msdn.microsoft.com/library/windows/hardware/ff569420). For more information about 802.11 statistics, see [Native 802.11 Statistics](native-802-11-statistics.md).

-   Cancel any pending network operations, such as a roaming or connection operations. For more information about these operations, see [Native 802.11 Network Operations](native-802-11-network-operations.md).

-   Clear the cache of BSS networks that have resulted from previous scan operations. The BSS network cache is queried through [OID\_DOT11\_ENUM\_BSS\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569360).

-   Clear the cache of pairwise master key identifiers (PMKID) if the 802.11 station supports PMKID caching. The PMKID cache is set or queried through [OID\_DOT11\_PMKID\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569400).

 

 





