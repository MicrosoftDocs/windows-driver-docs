---
title: Wake-Up Events
description: Wake-Up Events
ms.assetid: fd237adf-84fe-4e23-acce-1dfc7ff9c9d0
keywords:
- wake-up events WDK Native 802.11
- wake-on-wireless LAN WDK Native 802.11 , wake-up events
- wake-up capabilities WDK networking , Native 802.11 wireless LAN
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Wake-Up Events


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

This section applies only to NDIS 6.20 and later.

The NIC should wake up the host computer whenever any of the following events occur:

### WOL Packet Received

In this case, the NIC (or the Native 802.11 Wireless LAN infrastructure) receives a pattern that matches a previously set wake-on-LAN (WOL) pattern. WOL pattern matching should be performed on IEEE 802.11 data packets (except 802.11 null data packets) with configured IPv4, IPv6, IPSec, TCP and Teredo wake-up patterns. If the NIC provides the pattern matching, it must be done after the packets have been decrypted and the message integrity code (MIC) is verified. If the matching is performed in the infrastructure, it must be done before the packets are encrypted and MIC-protected.

### WOL Magic Pattern Received

In this case, the NIC receives a packet that matches the WOL [magic packet](https://msdn.microsoft.com/library/windows/hardware/hh205426) wake-up pattern. The hardware vendor should define the method for transmitting the magic packets used for WOL. Although most implementations will use IEEE 802.11 data packets, transmitting magic packets in IEEE 802.11 management or control frames is not prohibited.

### AP Association Lost

In this case, the NIC loses the association with its current AP. The unreachable timeout threshold is NIC dependent but must not exceed 5 minutes. After the host computer wakes up, the miniport driver must report the AP disassociation to the operating system.

### GTK Handshake Error

In this case, the NIC encounters an error in a two-way handshake.

### <a href="" id="-802-1x-eap-request-identity-packet-received"></a>802.1x EAP-Request/Identity Packet Received

In this case, the operating system attempts WPA2-Enterprise authentication by sending an 802.1x EAP-Request/Identity WOL pattern.

### Four-way Handshake Request Received

In this case, the NIC receives a request from the associated AP to perform a four-way handshake authentication. When the host computer is awake, the operating system performs the four-way pairwise transient key (PTK) handshake procedure.

 

 





