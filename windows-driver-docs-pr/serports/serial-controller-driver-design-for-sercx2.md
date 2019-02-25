---
title: Serial Controller Driver Design for SerCx2
description: To manage your serial controller, you write a serial controller driver that performs hardware-specific tasks and communicates with SerCx2.
ms.assetid: 67045E19-4EE1-4C31-A842-858E9A90233E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Serial Controller Driver Design for SerCx2


To manage your serial controller, you write a serial controller driver that performs hardware-specific tasks and communicates with SerCx2. Starting with Windows 8.1, SerCx2 is a system-supplied component that handles many of the processing tasks that are common to serial controllers. These tasks include managing time-outs and handling read and write requests sent by clients of the serial controller.

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
<td><p><a href="features-of-sercx2-based-serial-controller-drivers.md" data-raw-source="[Features of SerCx2-Based Serial Controller Drivers](features-of-sercx2-based-serial-controller-drivers.md)">Features of SerCx2-Based Serial Controller Drivers</a></p></td>
<td><p>A SerCx2-based serial controller driver is a KMDF driver that uses the methods and callbacks in KMDF to perform generic driver operations, and that communicates with SerCx2 to perform operations that are specific to serial controller drivers.</p></td>
</tr>
<tr class="even">
<td><p><a href="sercx2-i-o-transactions.md" data-raw-source="[SerCx2 I/O Transactions](sercx2-i-o-transactions.md)">SerCx2 I/O Transactions</a></p></td>
<td><p>SerCx2 simplifies the handling of read (<a href="https://msdn.microsoft.com/library/windows/hardware/ff546883" data-raw-source="[&lt;strong&gt;IRP_MJ_READ&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546883)"><strong>IRP_MJ_READ</strong></a>) and write (<a href="https://msdn.microsoft.com/library/windows/hardware/ff546904" data-raw-source="[&lt;strong&gt;IRP_MJ_WRITE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546904)"><strong>IRP_MJ_WRITE</strong></a>) requests for your serial controller driver. In response to a read or write request, SerCx2 issues one or more I/O transactions to the serial controller driver. From the driver&#39;s point of view, each transaction is a simple and complete I/O operation.</p></td>
</tr>
</tbody>
</table>

 

 

 




