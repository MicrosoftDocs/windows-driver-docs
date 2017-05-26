---
title: Creating a SCO Client Connection to a Remote Device
description: Creating a SCO Client Connection to a Remote Device
ms.assetid: e5a4ed14-1fb0-4a5f-b388-5e536d674c23
keywords:
- Synchronous Connection-Oriented WDK Bluetooth
- SCO profile drivers WDK Bluetooth
- initiating SCO connections
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[bltooth\bltooth]:%20Creating%20a%20SCO%20Client%20Connection%20to%20a%20Remote%20Device%20%20RELEASE:%20%283/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




