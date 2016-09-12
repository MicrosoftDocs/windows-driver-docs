---
title: Network Monitor Operation Mode
description: Network Monitor Operation Mode
ms.assetid: 6c43ac27-afcf-4324-9e20-181eeb3850be
keywords: ["operation modes WDK Native 802.11", "Network Monitor WDK Native 802.11"]
---

# Network Monitor Operation Mode


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

In the Network Monitor (NetMon) operation mode, the 802.11 station operates as a wireless LAN (WLAN) device that is used to monitor packets that are sent over the WLAN media by other devices.

A miniport driver enters the NetMon mode when it receives an [OID\_DOT11\_CURRENT\_OPERATION\_MODE](https://msdn.microsoft.com/library/windows/hardware/ff569132) request with the **uCurrentOpMode** member of [**DOT11\_CURRENT\_OPERATION\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff547678) set to DOT11\_OPERATION\_MODE\_NETWORK\_MONITOR.

In order to operate in NetMon mode, the miniport driver must:

-   Support raw packet receive indications, as described in [Indicating Raw 802.11 Packets](indicating-raw-802-11-packets.md).

-   Support the promiscuous packet receive indications, as described in [Guidelines for 802.11 Promiscuous Receive Operations](guidelines-for-802-11-promiscuous-receive-operations.md).

-   Support all mandatory NDIS generic OIDs.

-   Support the following subset of Native 802.11 NDIS OID interfaces for the configuration of 802.11 MAC or PHY MIB attributes:

    <a href="" id="oid-dot11-current-channel"></a>[OID\_DOT11\_CURRENT\_CHANNEL](https://msdn.microsoft.com/library/windows/hardware/ff569127)  
    While in NetMon mode, the miniport driver must support changing to any 802.11b/g channel (channels 1-14) and must disable any channel validation that is being done for regulatory domain compliance.

    <a href="" id="oid-dot11-current-frequency"></a>[OID\_DOT11\_CURRENT\_FREQUENCY](https://msdn.microsoft.com/library/windows/hardware/ff569130)  
    While in NetMon mode, the miniport driver must support changing to any 802.11a channel and must disable any channel validation that is being done for regulatory domain compliance.

    <a href="" id="---------oid-dot11-current-operation-mode"></a>[OID\_DOT11\_CURRENT\_OPERATION\_MODE](https://msdn.microsoft.com/library/windows/hardware/ff569132)  
    Switches the miniport driver into another operational mode, for example Extensible Station (ExtSTA) mode.

    <a href="" id="oid-dot11-current-phy-id"></a>[OID\_DOT11\_CURRENT\_PHY\_ID](https://msdn.microsoft.com/library/windows/hardware/ff569135)  
    Sets or returns the PHY identifier of the ExtSTA MIB object.

    <a href="" id="oid-dot11-desired-phy-list"></a>[OID\_DOT11\_DESIRED\_PHY\_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569144)  
    Enables the PHYs on which the NIC should monitor traffic. If the NIC cannot support packet reception on multiple PHYs concurrently, it should monitor traffic on the first PHY in the desired PHY list. If the desired PHY list contains DOT11\_PHY\_ID\_ANY, the NIC can choose which PHY to monitor.

    <a href="" id="oid-dot11-statistics"></a>[OID\_DOT11\_STATISTICS](https://msdn.microsoft.com/library/windows/hardware/ff569420)  
    Provides statistics counters in NetMon mode.

In addition, while the driver is operating in NetMon mode, the 802.11 station must not:

-   Send an 802.11 ACK frame for each received packet.

-   Reject duplicate 802.11 packets.

-   Switch out of the 802.11 Constantly Awake Mode (CAM) power mode if it is in the D0 power state. For more information, see [802.11 Power Management](802-11-power-management.md).

While in NetMon mode, the miniport driver can only receive packets based on the current packet filter settings. The driver cannot send packets either on its own or through a call to its [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) function.

When the miniport driver enters NetMon mode, the NIC must disable any background scanning that it has implemented.

For more information about the 802.11 packet filter settings, see [OID\_GEN\_CURRENT\_PACKET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569575).

 

 





