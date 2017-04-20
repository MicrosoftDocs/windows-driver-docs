---
title: Control Nodes for Processing IP Data
author: windows-driver-content
description: Control Nodes for Processing IP Data
ms.assetid: 6195ffe9-d20c-4687-8d45-abbfc17ba2fa
keywords:
- control nodes WDK BDA
- nodes WDK BDA
- IP data processing WDK BDA
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Control Nodes for Processing IP Data


## <a href="" id="ddk-control-nodes-for-processing-ip-data-ksg"></a>


The following sequence and figure describe the data flow for IP data that is part of the received digital signal.

1.  The receiver device receives IP data and passes the IP data over the PC bus as part of the transport stream.

2.  The demultiplexer receives the transport stream and passes the private sections containing the IP data.

3.  The private sections are received by the multiprotocol encapsulation (MPE) parser, which removes the multiprotocol encapsulation and outputs the IP data. The MPE parser passes the IP data to the IPSink filter.

4.  The IPSink filter passes the IP data through a private interface to the broadcast NDISIP miniport driver.

5.  The NDISIP miniport driver is installed as a virtual NDIS miniport. The NDISIP miniport driver sends the IP data to NDIS.

6.  NDIS propagates the IP data through TCP/IP and Windows Sockets (WinSock) as it would for any other NDIS adapter.

**Note**   Starting with Windows Vista, the IPSink filter is not supported.

 

![diagram illustrating ip data flow](images/ipdata.png)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Control%20Nodes%20for%20Processing%20IP%20Data%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


