---
title: Asynchronous I/O for IEEE 1394 Devices
author: windows-driver-content
description: Asynchronous I/O for IEEE 1394 Devices
MS-HAID:
- '1394-async\_de0c6976-bdb6-4b30-8b83-aacdda499829.xml'
- 'IEEE.asynchronous\_i\_o\_for\_ieee\_1394\_devices'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 36ca83d9-83ed-4366-81e7-63c5337f8643
keywords: ["IEEE 1394 WDK buses , asynchronous I/O", "1394 WDK buses , asynchronous I/O", "asynchronous I/O WDK IEEE 1394 bus", "I/O WDK IEEE 1394 bus", "I/O request packets WDK IEEE 1394 bus", "IRPs WDK IEEE 1394 bus", "transferring data WDK IEEE 1394 bus", "PDOs WDK IEEE 1394 bus"]
---

# Asynchronous I/O for IEEE 1394 Devices


## <a href="" id="ddk-asynchronous-i-o-for-ieee-1394-devices-kg"></a>


Devices on the IEEE 1394 bus communicate, in asynchronous mode, by sending and receiving packets. Devices send read, write, and lock requests to specific addresses in another device's address space. To provide quality of service, when the receiving device completes the request, it sends a response packet back to the sending device, which then sends a response acknowledgment.

A driver can communicate to its device by sending asynchronous I/O requests to the device. The driver can also allocate ranges of addresses in the IEEE 1394 address space of the host computer, and receive requests to these addresses. Both are documented in the following sections:

[Sending Asynchronous I/O Request Packets on the IEEE 1394 Bus](https://msdn.microsoft.com/library/windows/hardware/ff538087)

[Receiving Asynchronous I/O Request Packets on the IEEE 1394 Bus](https://msdn.microsoft.com/library/windows/hardware/ff537626)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BIEEE\buses%5D:%20Asynchronous%20I/O%20for%20IEEE%201394%20Devices%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


