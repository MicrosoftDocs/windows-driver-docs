---
Description: This section provides guidance concerning the careful management of USB bandwidth.
MS-HAID:
- 'usb-io\_7e866648-fdad-440f-8e3f-f8b9c05617b3.xml'
- 'buses.usb\_bandwidth\_allocation'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: USB Bandwidth Allocation
---

# USB Bandwidth Allocation


This section provides guidance concerning the careful management of USB bandwidth.

It is the responsibility of every USB client driver to minimize the USB bandwidth it uses, and return unused bandwidth to the free bandwidth pool as promptly as possible.

This section includes the following topics:

[Why is my USB driver getting out of bandwidth errors?](why-is-my-usb-driver-getting-out-of-bandwidth-errors-.md)

[USB Transfer and Packet Sizes](setting-usb-transfer-and-packet-sizes.md)

[Delimiting USB Data Transfers With Packets Smaller Than wMaxPacketSize](delimiting-usb-data-transfers-with-packets-smaller-than-wmaxpacketsize.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20USB%20Bandwidth%20Allocation%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



