---
title: IEC-61883 Protocol Driver
description: IEC-61883 Protocol Driver
MS-HAID:
- '61883\_dg\_d13a7214-2f08-4381-b28c-a9560e34c63f.xml'
- 'IEEE.iec\_61883\_protocol\_driver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d1e639f0-a22f-4005-86a7-fdbfe509265b
keywords: ["IEC-61883 client drivers WDK IEEE 1394 bus", "61883 WDK IEEE 1394 bus"]
---

# IEC-61883 Protocol Driver


## <a href="" id="ddk-iec-61883-protocol-driver-kg"></a>


The IEC-61883 protocol driver, *61883.sys*, supports function control protocol (FCP), common isochronous packet (CIP) format, and connection management procedures (CMP), as defined in the IEC 61883-1 specification. The protocol driver strips stream packet headers from requests, supports scatter/gather, and limits buffer copies to move large amounts of data efficiently.

To issue IEC-61883 commands to devices connected to the IEEE 1394 bus, IEC-61883 client drivers include *61883.h* and issue the [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766) IRP with the I/O control code [**IOCTL\_61883\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff537234). The client driver packages the parameters in an [**AV\_61883\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff537008) structure and passes a pointer to it in the **Parameters.Others.Argument1** member of the IRP. The **Function** member of the AV\_61883\_REQUEST structure determines the type of operation. The AV\_61883\_REQUEST structure contains request-specific parameters in a union of data structures, one per request type.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BIEEE\buses%5D:%20IEC-61883%20Protocol%20Driver%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




