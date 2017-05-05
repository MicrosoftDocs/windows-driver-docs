---
title: SerCx2 I/O Transactions
author: windows-driver-content
description: SerCx2 simplifies the handling of read (IRP\_MJ\_READ) and write (IRP\_MJ\_WRITE) requests for your serial controller driver.
ms.assetid: C1B3F059-A445-4224-8316-DBF194CE6A80
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# SerCx2 I/O Transactions


SerCx2 simplifies the handling of read ([**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff546883)) and write ([**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff546904)) requests for your serial controller driver. In response to a read or write request, SerCx2 issues one or more I/O transactions to the serial controller driver. From the driver's point of view, each transaction is a simple and complete I/O operation.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[Overview of SerCx2 I/O Transactions](overview-of-sercx2-i-o-transactions.md)</p></td>
<td><p>SerCx2 handles a read or write request from a client by issuing one or more I/O transactions to the serial controller driver. This driver treats each transaction as a self-contained I/O operation that transfers data between the serial controller and the data buffer in the request.</p></td>
</tr>
<tr class="even">
<td><p>[SerCx2 PIO-Receive Transactions](sercx2-pio-receive-transactions.md)</p></td>
<td><p>SerCx2 requires all serial controller drivers to implement support for receive transactions that use programmed I/O (PIO). To start a PIO-receive transaction, SerCx2 calls the driver's [<em>EvtSerCx2PioReceiveReadBuffer</em>](https://msdn.microsoft.com/library/windows/hardware/dn265214) event callback function and supplies a read buffer as a parameter.</p></td>
</tr>
<tr class="odd">
<td><p>[SerCx2 PIO-Transmit Transactions](sercx2-pio-transmit-transactions.md)</p></td>
<td><p>SerCx2 requires all serial controller drivers to implement support for transmit transactions that use programmed I/O (PIO). To start a PIO-transmit transaction, SerCx2 calls the driver's [<em>EvtSerCx2PioTransmitWriteBuffer</em>](https://msdn.microsoft.com/library/windows/hardware/dn265223) event callback function and supplies a write buffer as a parameter.</p></td>
</tr>
<tr class="even">
<td><p>[SerCx2 System-DMA-Receive Transactions](sercx2-system-dma-receive-transactions.md)</p></td>
<td><p>Some serial controller drivers implement support for receive transactions that use the system DMA controller. Such support is optional but can improve performance by relieving the main processor of the need to use programmed I/O (PIO) for long data transfers.</p></td>
</tr>
<tr class="odd">
<td><p>[SerCx2 System-DMA-Transmit Transactions](sercx2-system-dma-transmit-transactions.md)</p></td>
<td><p>Some serial controller drivers implement support for transmit transactions that use the system DMA controller. Such support is optional but can improve performance by relieving the main processor of the need to use programmed I/O (PIO) for long data transfers.</p></td>
</tr>
<tr class="even">
<td><p>[SerCx2 Custom-Receive Transactions](sercx2-custom-receive-transactions.md)</p></td>
<td><p>Some serial controller hardware might implement a data-transfer mechanism other than PIO or system DMA for reading data from a serial controller. A serial controller driver can support custom-receive transactions to make this data-transfer mechanism available to be used by SerCx2.</p></td>
</tr>
<tr class="odd">
<td><p>[SerCx2 Custom-Transmit Transactions](sercx2-custom-transmit-transactions.md)</p></td>
<td><p>Some serial controller hardware might implement a data-transfer mechanism other than PIO or system DMA for writing data to a serial controller. A serial controller driver can support custom-transmit transactions to make this data-transfer mechanism available to be used by SerCx2.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20SerCx2%20I/O%20Transactions%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


