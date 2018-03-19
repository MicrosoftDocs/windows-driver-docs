---
title: SerCx2 I/O Transactions
author: windows-driver-content
description: SerCx2 simplifies the handling of read (IRP_MJ_READ) and write (IRP_MJ_WRITE) requests for your serial controller driver.
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

 

 

 




