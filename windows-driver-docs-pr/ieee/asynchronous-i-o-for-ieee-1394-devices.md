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


