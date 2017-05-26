---
title: Miscellaneous Routines
author: windows-driver-content
description: Miscellaneous Routines
ms.assetid: e065c86c-a784-49e1-a1d9-e2bcff3fcae4
keywords:
- RDBSS WDK file systems , miscellaneous routines
- Redirected Drive Buffering Subsystem WDK file systems , miscellaneous routines
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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


