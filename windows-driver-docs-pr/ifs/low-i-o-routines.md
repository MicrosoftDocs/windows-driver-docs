---
title: Low I/O Routines
author: windows-driver-content
description: Low I/O Routines
ms.assetid: 5317917d-9abc-43f9-ab4a-f070e491c816
keywords: ["RDBSS WDK file systems , low I/O routines", "Redirected Drive Buffering Subsystem WDK file systems , low I/O routines", "low I/O routines WDK RDBSS", "I/O WDK RDBSS"]
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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Low%20I/O%20Routines%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


