---
title: AV/C Streaming Overview
author: windows-driver-content
description: AV/C Streaming Overview
MS-HAID:
- 'avcsguide\_c32b1696-8e9e-4441-a8dc-31dce2fb4c69.xml'
- 'stream.av\_c\_streaming\_overview'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c500fad7-26b7-4507-953e-258dd9c91253
keywords: ["AV/C WDK , Stream filter driver", "Stream filter driver WDK AV/C", "Avcstrm.sys streaming filter driver WDK", "Avcstrm.sys streaming filter driver WDK , about Avcstrm.sys streaming filter driver", "filter drivers WDK AV/C streaming"]
---

# AV/C Streaming Overview


## <a href="" id="ddk-av-c-streaming-ksg"></a>


This section describes the AV/C Streaming filter driver, *Avcstrm.sys*, that Microsoft provides to assist with streaming media data from an AV/C subunit if that data is in either SDDV or MPEG2TS formats. These formats are the two most common methods for storing the digital data in the media signal.

*Avcstrm.sys* is a lower-level subunit filter driver that is located immediately above *Avc.sys* and *61883.sys* in the driver stack and below any subunit drivers. The AV/C Stream filter driver provides additional support for the AV/C protocol driver. It is optional for a vendor to use this support.

The tape subunit specifications (located at the [1394 Trade Association](http://go.microsoft.com/fwlink/p/?LinkId=518448) website) support different transport state controls, such as play, pause, record and stop, regardless of its media signal. However, the data format for the same subunit type can be the same or different. For example, both DV and DVHS devices contain tape subunits. However, DV generally uses the SDDV data format that is based on the IEC 61883-2 specification, whereas, DVHS uses the MPEG2TS data format that is based on the 61883-4 specification. A filter driver for tape subunits must therefore support both SDDV and MPEG2TS data formats but use the same device control for the tape subunit. This implies that every subunit driver must duplicate the same functionality to provide format-aware streaming capability.

Controlling an AV/C subunit driver on the 61883 and AV/C subunit driver stacks requires driver functions to receive or transmit data streams using device driver interfaces (DDIs) provided by the 61883 protocol driver. These driver functions perform the following operations:

-   Allocate isochronous resources and make an isochronous connection

-   Queue data buffers

-   Attach and complete receiving or transmitting data buffers

-   Synchronize stream state across threads

The AV/C Stream filter driver relies on the *61883.sys* protocol driver. *Avcstrm.sys* uses DDIs provided by *61883.sys* to perform isochronous connection and isochronous data streaming, and it uses *Avc.sys* to issue AV/C commands for external device control.

For more information about the AV/C protocol upon which the AV/C Streaming filter driver is built, see [AV/C Overview](av-c-overview.md). For more information about the 61883 protocol, see [IEC-61883 Client Drivers](https://msdn.microsoft.com/library/windows/hardware/ff537188).

For more information and resources see the following links:

[Windows Driver Model technology](http://go.microsoft.com/fwlink/p/?linkid=8771) website

[IEEE 1394 technology](http://go.microsoft.com/fwlink/p/?linkid=8728) website

[1394 Trade Association specifications](http://go.microsoft.com/fwlink/p/?linkid=518448) website

[IEC](http://go.microsoft.com/fwlink/p/?linkid=8732) website

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20AV/C%20Streaming%20Overview%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


