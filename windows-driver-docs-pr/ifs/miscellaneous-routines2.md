---
title: Miscellaneous Routines
author: windows-driver-content
description: Miscellaneous Routines
ms.assetid: e065c86c-a784-49e1-a1d9-e2bcff3fcae4
keywords: ["RDBSS WDK file systems , miscellaneous routines", "Redirected Drive Buffering Subsystem WDK file systems , miscellaneous routines"]
---

# Miscellaneous Routines


## <span id="ddk_miscellaneous_functions_if"></span><span id="DDK_MISCELLANEOUS_FUNCTIONS_IF"></span>


RDBSS includes a number of utility routines that do not fall into a particular category.

The RDBSS miscellaneous routines include the following:

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
<td align="left"><p>[<strong>RxFsdDispatch</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554468)</p></td>
<td align="left"><p>This routine implements the file system driver (FSD) dispatch for RDBSS to process an I/O request packet (IRP). This routine is called by a network mini-redirector in the driver dispatch routines to initiate RDBSS processing of a request.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxFsdPostRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554472)</p></td>
<td align="left"><p>This routine queues the IRP specified by an RX_CONTEXT structure to the worker queue for processing by the file system process (FSP).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxGetRDBSSProcess</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554481)</p></td>
<td align="left"><p>This routine returns a pointer to the process of the main thread used by the RDBSS kernel process.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxIsThisACscAgentOpen</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554508)</p></td>
<td align="left"><p>This routine determines if a file open request was made by a user-mode client-side caching agent.</p>
<p>This routine is only available on Windows Server 2003.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxMakeLateDeviceAvailable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554532)</p></td>
<td align="left"><p>This routine modifies the device object to make a &quot;late device&quot; available. A late device is one that is not created in the driver's load routine.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxPrepareToReparseSymbolicLink</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554649)</p></td>
<td align="left"><p>This routine sets up the file object name to facilitate a reparse. This routine is used by the network mini-redirectors to traverse symbolic links. This routine should not be used by network mini-redirectors.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Miscellaneous%20Routines%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


