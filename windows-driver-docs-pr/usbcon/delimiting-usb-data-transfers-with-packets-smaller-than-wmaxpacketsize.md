---
Description: Delimiting USB Data Transfers With Packets Smaller Than wMaxPacketSize
MS-HAID:
- 'usb-io\_e563da6b-7191-4a05-9c95-f48760c2697b.xml'
- 'buses.delimiting\_usb\_data\_transfers\_with\_packets\_smaller\_than\_wmaxpacketsize'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: Delimiting USB Data Transfers With Packets Smaller Than wMaxPacketSize
author: windows-driver-content
---

# Delimiting USB Data Transfers With Packets Smaller Than wMaxPacketSize


Compliant USB 2.0/1.1 drivers must transmit packets of maximum size (*wMaxPacketSize*) and then either end the transmission by means of a packet of less than maximum size, or delimit the end of the transmission by means of a zero-length packet. The transmission is not complete until the driver sends a packet smaller than *wMaxPacketSize*. If the transfer size is an exact multiple of the maximum, the driver must send a zero-length delimiting packet to explicitly terminate the transfer

Delimiting the data transmission with zero-length packets, as required by the USB specification, is the responsibility of the device driver. The system USB stack will not generate these packets automatically.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Delimiting%20USB%20Data%20Transfers%20With%20Packets%20Smaller%20Than%20wMaxPacketSize%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


