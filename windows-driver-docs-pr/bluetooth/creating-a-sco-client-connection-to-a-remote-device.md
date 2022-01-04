---
title: Creating a SCO Client Connection to a Remote Device
description: Creating a SCO Client Connection to a Remote Device
keywords:
- Synchronous Connection-Oriented WDK Bluetooth
- SCO profile drivers WDK Bluetooth
- initiating SCO connections
ms.date: 04/20/2017
---

# Creating a SCO Client Connection to a Remote Device


A SCO client profile driver is a profile driver that requests Synchronous Connection-Oriented (SCO) connection to a remote device. If the device accepts the connection, the SCO client profile driver is notified of any changes to the connection. For example, a SCO client profile driver can request a connection to a remote headset, and after the headset accepts the connection request, the Bluetooth driver stack can notify the profile driver when the headset is turned off or removed.

Because SCO connections are point-to-point connections between two Bluetooth devices, a SCO client profile driver needs only the Bluetooth address of the remote device to connect to.

To initiate a SCO connection to a remote device, profile drivers should [build and send](building-and-sending-a-brb.md) a [**BRB\_SCO\_OPEN\_CHANNEL**](/previous-versions/ff536626(v=vs.85)) request.

If the remote device accepts the profile driver's SCO connection request, the profile driver can then perform additional BRB commands across the newly connected channel by using IOCTL\_INTERNAL\_BTH\_SUBMIT\_BRB, including:

-   [**BRB\_SCO\_GET\_CHANNEL\_INFO**](/previous-versions/ff536624(v=vs.85))

-   [**BRB\_SCO\_GET\_SYSTEM\_INFO**](/previous-versions/ff536625(v=vs.85))

-   [**BRB\_SCO\_TRANSFER**](/previous-versions/ff536629(v=vs.85))

**Note**  Profile drivers should [build and send](building-and-sending-a-brb.md) a **BRB\_SCO\_GET\_SYSTEM\_INFO** request during initialization to determine if the underlying hardware supports SCO and, if so, what the global SCO settings are.

 

When the profile driver no longer requires the SCO connection to the remote device, it should [build and send](building-and-sending-a-brb.md) a [**BRB\_SCO\_CLOSE\_CHANNEL**](/previous-versions/ff536622(v=vs.85)) request.

 

