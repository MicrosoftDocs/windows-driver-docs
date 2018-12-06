---
title: Creating a SCO Client Connection to a Remote Device
description: Creating a SCO Client Connection to a Remote Device
ms.assetid: e5a4ed14-1fb0-4a5f-b388-5e536d674c23
keywords:
- Synchronous Connection-Oriented WDK Bluetooth
- SCO profile drivers WDK Bluetooth
- initiating SCO connections
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a SCO Client Connection to a Remote Device


A SCO client profile driver is a profile driver that requests Synchronous Connection-Oriented (SCO) connection to a remote device. If the device accepts the connection, the SCO client profile driver is notified of any changes to the connection. For example, a SCO client profile driver can request a connection to a remote headset, and after the headset accepts the connection request, the Bluetooth driver stack can notify the profile driver when the headset is turned off or removed.

Because SCO connections are point-to-point connections between two Bluetooth devices, a SCO client profile driver needs only the Bluetooth address of the remote device to connect to.

To initiate a SCO connection to a remote device, profile drivers should [build and send](building-and-sending-a-brb.md) a [**BRB\_SCO\_OPEN\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff536626) request.

If the remote device accepts the profile driver's SCO connection request, the profile driver can then perform additional BRB commands across the newly connected channel by using IOCTL\_INTERNAL\_BTH\_SUBMIT\_BRB, including:

-   [**BRB\_SCO\_GET\_CHANNEL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff536624)

-   [**BRB\_SCO\_GET\_SYSTEM\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff536625)

-   [**BRB\_SCO\_TRANSFER**](https://msdn.microsoft.com/library/windows/hardware/ff536629)

**Note**  Profile drivers should [build and send](building-and-sending-a-brb.md) a **BRB\_SCO\_GET\_SYSTEM\_INFO** request during initialization to determine if the underlying hardware supports SCO and, if so, what the global SCO settings are.

 

When the profile driver no longer requires the SCO connection to the remote device, it should [build and send](building-and-sending-a-brb.md) a [**BRB\_SCO\_CLOSE\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff536622) request.

 

 





