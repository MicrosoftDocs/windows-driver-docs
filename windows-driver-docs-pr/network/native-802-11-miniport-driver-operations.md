---
title: Native 802.11 Miniport Driver Operations
description: Native 802.11 Miniport Driver Operations
ms.assetid: 1e84f902-b949-433d-ac84-56447331c9ea
keywords:
- Native 802.11 miniport drivers WDK networking , operations performed
- miniport drivers WDK Native 802.11 , operations performed
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Native 802.11 Miniport Driver Operations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The Native 802.11 miniport driver and 802.11 station perform the following operations:

<a href="" id="scan-operations"></a>**Scan Operations**  
The 802.11 station performs the scan operation in order to detect the various basic service set (BSS) networks within range. The operating system can request a scan operation through a set request of [OID\_DOT11\_SCAN\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569413). In addition, the 802.11 station can initiate the scan operation itself in order to refresh its list of detected BSS networks.

For more information about scan operations, see [Native 802.11 Scan Operations](native-802-11-scan-operations.md).

<a href="" id="bss-network-operations"></a>**BSS Network Operations**  
After it has been configured for 802.11 BSS operations, the 802.11 station performs the following types of operations to join, start, or leave a BSS network:

<a href="" id="connection-operations"></a>**Connection Operations**  
Through the connection operation, the 802.11 station determines the best BSS network to join based on the current 802.11 configuration. If configured to operate in an independent BSS (IBSS) network, the operating system might request that the 802.11 station start a new IBSS network if the station has not detected a candidate network. For more information about this operation, see [Connection Operations](connection-operations.md).

<a href="" id="roaming-operations"></a>**Roaming Operations**  
After it has been connected to a BSS network, the 802.11 station performs a roaming operation if it needs to either associate with a different access point (AP) (for infrastructure BSS networks) or another group of peer stations (for IBSS networks) within the same BSS network. For more information about this operation, see [Roaming Operations](roaming-operations.md).

<a href="" id="association-operations"></a>**Association Operations**  
The 802.11 station performs an association operation to associate with an AP or peer station. For more information about this operation, see [Association Operations](association-operations.md).

If configured for infrastructure BSS network operations, the 802.11 station performs only the association operation during either the connection or roaming operations. If configured for IBSS network operations, the 802.11 station can perform this operation whenever it associates with a peer station.

<a href="" id="disassociation-operations"></a>**Disassociation Operations**  
After it completes the association operation with an AP or peer station, the 802.11 station performs this operation whenever it disassociates with the AP or a peer station. For more information about this operation, see [Disassociation Operations](disassociation-operations.md).

<a href="" id="disconnection-operations"></a>**Disconnection Operations**  
After it has connected to a BSS network, the 802.11 station performs this operation to stop all network activity, including association and roaming operations, on the BSS network. For more information about this operation, see [Disconnection Operations](disconnection-operations.md).

<a href="" id="authentication-operations"></a>**Authentication Operations**  
If the miniport driver is operating in Extensible Station (ExtSTA) mode, the 802.11 station performs this operation when authenticating with either an AP or peer station. For more information about the authentication operation, see [Native 802.11 Authentication Operations](native-802-11-authentication-operations.md).

<a href="" id="cipher-operations"></a>**Cipher Operations**  
If the miniport driver is operating in Extensible Station (ExtSTA) mode, the 802.11 station performs this operation when encrypting or decrypting packet data. For more information about the cipher operation, see [Native 802.11 Cipher Operations](native-802-11-cipher-operations.md).

<a href="" id="send-operations"></a>**Send Operations**  
The 802.11 station performs this operation when sending packets over the BSS network. The operating system initiates the send operation through calls to the miniport driver's [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) function.

For more information about the send operation, see [Native 802.11 Send Operations](native-802-11-send-operations.md).

<a href="" id="receive-operations"></a>**Receive Operations**  
The 802.11 station performs this operation when receiving packets over the BSS network. The miniport driver indicates the received packets to the operating system through calls to the driver's [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) function.

For more information about the receive operation, see [Native 802.11 Receive Operations](native-802-11-receive-operations.md).

 

 





