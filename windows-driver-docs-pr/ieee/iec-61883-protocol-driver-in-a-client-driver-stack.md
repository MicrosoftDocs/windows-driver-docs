---
title: IEC-61883 Protocol Driver in a Client Driver Stack
description: IEC-61883 Protocol Driver in a Client Driver Stack
MS-HAID:
- '61883\_dg\_69d368d7-7090-4001-8108-f09f00805c44.xml'
- 'IEEE.iec\_61883\_protocol\_driver\_in\_a\_client\_driver\_stack'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: cee0c0ee-7326-421c-af5a-b483c878b289
keywords: ["IEC-61883 client drivers WDK IEEE 1394 bus", "61883 WDK IEEE 1394 bus"]
---

# IEC-61883 Protocol Driver in a Client Driver Stack


## <a href="" id="ddk-iec-61883-protocol-driver-in-a-client-driver-stack-kg"></a>


IEC-61883 client drivers rely on *61883.sys* to communicate with their devices using the IEC-61883 protocol.

The following diagram shows an example of the *61883.sys* in an AV/C driver stack. The vendor-supplied AV/C subunit driver is the IEC-61883 client in this example.

![diagram illustrating an iec-61883 client driver stack](images/61883stk.png)

Starting from the top of the diagram:

-   The stream class driver, *stream.sys*, supports kernel streaming drivers for devices such as DVD, video capture, and external sound devices. The stream class driver is documented in the [Streaming Minidrivers](https://msdn.microsoft.com/library/windows/hardware/ff568277).

-   In this example, the IEC-61883 client is a vendor-supplied AV/C subunit driver. This is a [Writing a Stream Minidriver](https://msdn.microsoft.com/library/windows/hardware/ff568794) that uses facilities provided by lower drivers in the AV/C stack to control its device. (For more information about AV/C subunit drivers, see [AV/C Client Drivers](https://msdn.microsoft.com/library/windows/hardware/ff556367).)

    AV/C subunit drivers set up plug connections and streams, and expose subunit control, status, and notification. They use the kernel streaming framework to expose a generic pin property set and device-specific property and event sets.

-   The AV/C stream filter driver, *avcstrm.sys*, is an optional WDM filter driver that isolates stream-specific format handling for subunit drivers. The AV/C stream filter driver is specified as a lower driver by third-party INF files. It supports DV and MPEG stream format for subunit drivers and supplies CMP helper functions in conjunction with *avc.sys*. It also provides kernel-streaming data structures and data intersection handlers.

-   The AV/C protocol driver, *avc.sys*, maps AV/C commands to WDM IRPs, retries requests (for example, if a subunit is busy), handles interim responses as pending IRPs, and routes responses to the correct subunit driver based on type, ID, and operation code. For Microsoft Windows XP and later, *avc.sys* also provides plug connection management. (For more information about support that Microsoft provides for the AV/C protocol, see [AV/C Client Drivers](https://msdn.microsoft.com/library/windows/hardware/ff556367).)

-   The IEC-61883 protocol driver, *61883.sys*, handles function control protocol (FCP), common isochronous packet (CIP) format, and connection management procedures (CMP) requests sent down the AV/C driver stack.

-   The 1394 bus driver, *1394bus.sys*, enumerates devices on the IEEE 1394 bus and responds to Plug and Play and power management IRPs on their behalf.

-   The port driver for the host controller provides a hardware-independent interface to the IEEE 1394 bus. The port driver handles some IRPs and forwards others to the port driver for the motherboard's host controller. Microsoft supplies a standard port driver, *ohci1394.sys*, for host controllers that satisfy the *1394 Open Host Controller Interface Specification*, which is available for download from the [IEEE 1394 technology](http://go.microsoft.com/fwlink/p/?linkid=8729) website.

AV/C subunit drivers are just one of the possible types of IEC-61883 client drivers. Another example would be a driver that utilizes the HAVi protocol layered above IEC-61883. Although *61883.sys* and the IEC-61883 protocol do not have any AV/C or HAVi dependencies, clients of *61883.sys* can operate under different constraints. For example, AV/C subunit drivers are usually clients of *avc.sys*, which provides FCP-related functions and blocks upper-level drivers from sending FCP-related requests down the stack to be handled by *61883.sys*.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BIEEE\buses%5D:%20IEC-61883%20Protocol%20Driver%20in%20a%20Client%20Driver%20Stack%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




