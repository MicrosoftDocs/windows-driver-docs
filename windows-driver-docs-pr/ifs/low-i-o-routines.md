---
title: Low I/O Routines
author: windows-driver-content
description: Low I/O Routines
ms.assetid: 5317917d-9abc-43f9-ab4a-f070e491c816
keywords:
- RDBSS WDK file systems , low I/O routines
- Redirected Drive Buffering Subsystem WDK file systems , low I/O routines
- low I/O routines WDK RDBSS
- I/O WDK RDBSS
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Low I/O Routines


## <span id="ddk_low_i_o_functions_if"></span><span id="DDK_LOW_I_O_FUNCTIONS_IF"></span>


Low I/O routines represent the basic IRP\_MJ\_XXX asynchronous operations on a file object (open, close, read, and write, for example). RDBSS provides some convenience routines that are used with low I/O operations by a network mini-redirector. The RDBSS low I/O routines include the following:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Routine</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>RxLowIoCompletion</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554525)</p></td>
<td align="left"><p>This routine must be called by the low I/O routines of a network mini-redirector driver when processing is complete, if the routine initially returned as pending.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxLowIoGetBufferAddress</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554529)</p></td>
<td align="left"><p>This routine returns the buffer that corresponds to the MDL from the <strong>LowIoContext</strong> structure of an RX_CONTEXT structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxMapSystemBuffer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554549)</p></td>
<td align="left"><p>This routine returns the system buffer address from the I/O request packet (IRP).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxNewMapUserBuffer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554591)</p></td>
<td align="left"><p>This routine returns the address of the user buffer used for low I/O. Note that this routine is only available on Windows XP and Windows 2000.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------


