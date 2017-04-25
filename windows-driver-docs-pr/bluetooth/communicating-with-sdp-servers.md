---
title: Communicating with SDP Servers
description: Communicating with SDP Servers
ms.assetid: 833f2eea-d7e6-4f19-979e-3bb4db47fa43
keywords:
- Bluetooth WDK , SDP server communication
- SDP WDK Bluetooth
- Service Discovery Protocol WDK Bluetooth
- profile drivers WDK Bluetooth
- browsing services WDK Bluetooth
- searching services WDK Bluetooth
- services browsing WDK Bluetooth
- advertising services WDK Bluetooth
- services advertising WDK Bluetooth
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Communicating with SDP Servers


The Bluetooth driver stack supports the Service Discovery Protocol (SDP). This protocol allows profile drivers to search or browse for services that are offered by Bluetooth devices that are in range of the local radio. SDP uses the Logical Link Control and Adaptation Protocol (L2CAP) as its transport protocol and follows a client-server model.

A service is any entity that can provide information, perform an action, or control a resource on behalf of another entity. A service might be implemented as software, hardware, or a combination of hardware and software. The service record consists entirely of a list of service attributes.

After a L2CAP server profile driver registers itself to accept incoming L2CAP connection requests, it can advertise its services with the SDP protocol by using [**IOCTL\_BTH\_SDP\_SUBMIT\_RECORD**](https://msdn.microsoft.com/library/windows/hardware/ff536693) or [**IOCTL\_BTH\_SDP\_SUBMIT\_RECORD\_WITH\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff536694). Each SDP record is submitted as a stream. If the profile driver uses IOCTL\_BTH\_SDP\_SUBMIT\_RECORD\_WITH\_INFO, the profile driver prepends a [**BTH\_SDP\_RECORD**](https://msdn.microsoft.com/library/windows/hardware/ff536650) structure to the raw stream, which contains extra attributes that are not part of the SDP record itself. These include security requirements for a requesting client, publication options for the SDP record, class-of-device (CoD) information, the length of the record, and the record itself.

After the profile driver has advertised its services, other Bluetooth devices can search or browse for these services. For more information about SDP services, see [Accessing SDP Service Information](accessing-sdp-service-information.md).

To stop advertising services with SDP, a profile driver uses [**IOCTL\_BTH\_SDP\_REMOVE\_RECORD**](https://msdn.microsoft.com/library/windows/hardware/ff536690).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[bltooth\bltooth]:%20Communicating%20with%20SDP%20Servers%20%20RELEASE:%20%283/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




