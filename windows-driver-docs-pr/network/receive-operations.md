---
title: Receive Operations
description: Receive Operations
ms.assetid: 9ec2ba38-36dd-42d2-b0a8-0abe4d1bb847
keywords:
- receive operations WDK Native 802.11 IHV Extensions DLL
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Receive Operations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

When performing a post-association operation, initiated through a call to [*Dot11ExtIhvPerformPostAssociate*](https://msdn.microsoft.com/library/windows/hardware/ff547492), the operating system calls the [*Dot11ExtIhvReceivePacket*](https://msdn.microsoft.com/library/windows/hardware/ff547513) function to forward packets to the HV Extensions DLL received through the wireless LAN (WLAN) adapter. For more information about the post-association operation, see [Post-Association Operations](post-association-operations.md).

In order to receive packets, the IHV Extensions DLL must call [**Dot11ExtSetEtherTypeHandling**](https://msdn.microsoft.com/library/windows/hardware/ff547587) to register a list of one or more IEEE EtherTypes. When a packet is received with an EtherType that matches an entry in this list, the operating system calls the [*Dot11ExtIhvReceivePacket*](https://msdn.microsoft.com/library/windows/hardware/ff547513) function and passes the packet buffer through the function's *pvInBuffer* parameter.

**Note**  The IHV Extensions DLL must call [**Dot11ExtSetEtherTypeHandling**](https://msdn.microsoft.com/library/windows/hardware/ff547587) before the DLL completes a pre-association operation. For more information about this operation, see [Pre-Association Operations](pre-association-operations.md).

 

When [*Dot11ExtIhvReceivePacket*](https://msdn.microsoft.com/library/windows/hardware/ff547513) is called, the *pvInBuffer* parameter points to a buffer allocated by the operating system that contains the entire 802.11 packet, including media access control (MAC) header, LLC encapsulation (if necessary), and payload data.

The IHV Extensions DLL can send a response to the received packet from within the call to [*Dot11ExtIhvReceivePacket*](https://msdn.microsoft.com/library/windows/hardware/ff547513). In this situation, the DLL must follow the guidelines described in [Send Operations](send-operations.md).

 

 





