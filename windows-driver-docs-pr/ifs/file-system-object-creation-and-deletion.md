---
title: File System Object Creation and Deletion
description: File System Object Creation and Deletion
ms.assetid: 71e342cf-455f-4b01-af55-12568bf06728
keywords:
- mini-redirectors WDK , object creation
- mini-redirectors WDK , object deletion
- file objects WDK mini-redirectors
- objects WDK mini-redirectors
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# File System Object Creation and Deletion


A number of routines implemented by a network mini-redirector are for file creation and deletion. RDBSS abstracts this process by creating several structures including the SRV\_OPEN, FCB, and FOBX structure that are reference counted. Creating or opening a file system object normally requires creating SRV\_OPEN, FCB, and FOBX structures. The normal procedure would be for RDBSS to call the [**MRxCreate**](https://msdn.microsoft.com/library/windows/hardware/ff549862) routine implemented by the network mini-redirector to fill information into these structures. It is also possible to collapse an open/create file request on an existing SRV\_OPEN structure using the [**MRxShouldTryToCollapseThisOpen**](https://msdn.microsoft.com/library/windows/hardware/ff550817) and [**MRxCollapseOpen**](https://msdn.microsoft.com/library/windows/hardware/ff549847) routines.

In the context of a network redirector, a file object refers to a file control block (FCB) structure and a file object extension (FOBX) structure. There is a one to one correspondence between file objects and FOBXs. Many file objects will refer to the same FCB structure, which represents a single file somewhere on a remote server. A client can have several different open requests (NtCreateFile requests) on the same FCB and each of these will create a new file object. RDBSS and network mini-redirectors can choose to send fewer [**MRxCreate**](https://msdn.microsoft.com/library/windows/hardware/ff549862) requests than the NtCreateFile requests that are received, in effect sharing a server open request (SRV\_OPEN) among several FOBXs.

RDBSS and a network mini-redirector do not necessarily close the SRV\_OPEN structures when the user closes a file. RDBSS can try to reuse the SRV\_OPEN structure and the data without any contact with the server. Some Windows applications can open, read, and close a file and then quickly reopen the same file. In these cases, reusing the SRV\_OPEN structures can improve performance.

There are several routines used to close and finalize these data structures and free any memory or other resources used when they are no longer needed. These routines include [**MRxCleanupFobx**](https://msdn.microsoft.com/library/windows/hardware/ff549841), [**MRxCloseSrvOpen**](https://msdn.microsoft.com/library/windows/hardware/ff549845), [**MRxDeallocateForFcb**](https://msdn.microsoft.com/library/windows/hardware/ff549871), [**MRxDeallocateForFobx**](https://msdn.microsoft.com/library/windows/hardware/ff549872), and [**MRxForceClosed**](https://msdn.microsoft.com/library/windows/hardware/ff550677).

The following table lists the routines that can be implemented by a network mini-redirector for file system object creation and deletion operations.

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
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff549838" data-raw-source="[&lt;strong&gt;MRxAreFilesAliased&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549838)"><strong>MRxAreFilesAliased</strong></a></td>
<td align="left"><p>RDBSS calls this routine to query the network mini-redirector if two FCB objects represent the same file. RDBSS calls this routine when processing two files that appear to be the same but have different names (an MS-DOS short name and a long name, for example).</p></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff549841" data-raw-source="[&lt;strong&gt;MRxCleanupFobx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549841)"><strong>MRxCleanupFobx</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector close a file system object extension. RDBSS issues this call in response to receiving an IRP_MJ_CLEANUP on a file object.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff549845" data-raw-source="[&lt;strong&gt;MRxCloseSrvOpen&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549845)"><strong>MRxCloseSrvOpen</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector close a SRV_OPEN object.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff549847" data-raw-source="[&lt;strong&gt;MRxCollapseOpen&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549847)"><strong>MRxCollapseOpen</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector collapse an open file system request onto an existing SRV_OPEN.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff549862" data-raw-source="[&lt;strong&gt;MRxCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549862)"><strong>MRxCreate</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector create a file system object. This call is issued by RDBSS in response to receiving an IRP_MJ_CREATE.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff549871" data-raw-source="[&lt;strong&gt;MRxDeallocateForFcb&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549871)"><strong>MRxDeallocateForFcb</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector deallocate an FCB. This call is in response to a request to close a file system object.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff549872" data-raw-source="[&lt;strong&gt;MRxDeallocateForFobx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549872)"><strong>MRxDeallocateForFobx</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that the network mini-redirector deallocate an FOBX. This call is in response to a request to close a file system object.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff549878" data-raw-source="[&lt;strong&gt;MRxExtendForCache&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549878)"><strong>MRxExtendForCache</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector extend a file when the file is being cached by cache manager.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff549879" data-raw-source="[&lt;strong&gt;MRxExtendForNonCache&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549879)"><strong>MRxExtendForNonCache</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector extend a file when the file is not being cached by cache manager.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550669" data-raw-source="[&lt;strong&gt;MRxFlush&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550669)"><strong>MRxFlush</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector flush a file system object. RDBSS issue this call in response to receiving an IRP_MJ_FLUSH_BUFFERS.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550677" data-raw-source="[&lt;strong&gt;MRxForceClosed&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550677)"><strong>MRxForceClosed</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector force a close. This routine is called when the condition of the SRV_OPEN is not good or the SRV_OPEN is marked as closed.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550691" data-raw-source="[&lt;strong&gt;MRxIsLockRealizable&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550691)"><strong>MRxIsLockRealizable</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector indicate whether byte-range locks are supported on this NET_ROOT.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550817" data-raw-source="[&lt;strong&gt;MRxShouldTryToCollapseThisOpen&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550817)"><strong>MRxShouldTryToCollapseThisOpen</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector indicate if RDBSS should try and collapse an open request onto an existing file system object.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550839" data-raw-source="[&lt;strong&gt;MRxTruncate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550839)"><strong>MRxTruncate</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector truncate a file system object.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550844" data-raw-source="[&lt;strong&gt;MRxZeroExtend&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550844)"><strong>MRxZeroExtend</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector extend a file system object filling the file with zeros on cleanup if the file size is greater than the valid data length of the FCB.</p></td>
</tr>
</tbody>
</table>

 

 

 




