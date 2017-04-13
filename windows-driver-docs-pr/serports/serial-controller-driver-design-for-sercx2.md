---
title: Serial Controller Driver Design for SerCx2
author: windows-driver-content
description: To manage your serial controller, you write a serial controller driver that performs hardware-specific tasks and communicates with SerCx2.
ms.assetid: 67045E19-4EE1-4C31-A842-858E9A90233E
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
<td><p>[Features of SerCx2-Based Serial Controller Drivers](features-of-sercx2-based-serial-controller-drivers.md)</p></td>
<td><p>A SerCx2-based serial controller driver is a KMDF driver that uses the methods and callbacks in KMDF to perform generic driver operations, and that communicates with SerCx2 to perform operations that are specific to serial controller drivers.</p></td>
</tr>
<tr class="even">
<td><p>[SerCx2 I/O Transactions](sercx2-i-o-transactions.md)</p></td>
<td><p>SerCx2 simplifies the handling of read ([<strong>IRP_MJ_READ</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546883)) and write ([<strong>IRP_MJ_WRITE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546904)) requests for your serial controller driver. In response to a read or write request, SerCx2 issues one or more I/O transactions to the serial controller driver. From the driver's point of view, each transaction is a simple and complete I/O operation.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Serial%20Controller%20Driver%20Design%20for%20SerCx2%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


