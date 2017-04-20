---
title: File System Object Query and Set Routines
author: windows-driver-content
description: File System Object Query and Set Routines
ms.assetid: 34b97a6e-a155-443c-94dd-4d8f1fc4b430
keywords:
- mini-redirectors WDK , query operations
- mini-redirectors WDK , set operations
- query operations WDK network redirectors
- set operations WDK network redirectors
- file objects WDK mini-redirectors
- objects WDK mini-redirectors
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# File System Object Query and Set Routines


A number of routines that can be implemented by a network mini-redirector are for query and set operations on file system objects. RDBSS issues most of these calls in response to receiving an IRP to query or set information on a file object. So there is a direct correspondence between the IRP that RDBSS receives and the MRx query or set operation that RDBSS calls.

The following table lists the routines that can be implemented by a network mini-redirector for file system object query and set operations.

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
<td align="left">[<strong>MRxIsValidDirectory</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550696)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector indicate if a path is a valid directory.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxQueryDirectory</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550755)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query information on a file directory system object.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxQueryEaInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550759)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query extended attribute information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_QUERY_EA.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxQueryFileInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550770)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query file information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_QUERY_INFORMATION.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxQueryQuotaInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550773)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query quota information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_QUERY_QUOTA.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxQuerySdInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550776)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query security descriptor information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_QUERY_SECURITY.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxQueryVolumeInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550782)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query volume information. RDBSS issues this call in response to receiving an IRP_MJ_QUERY_VOLUME_INFORMATION.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxSetEaInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550786)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set extended attribute information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_SET_EA.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxSetFileInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550790)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set file information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_SET_INFORMATION.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxSetFileInfoAtCleanup</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550796)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector to set file information on a file system object at cleanup. RDBSS issues this call during cleanup when an application closes a handle but before the close.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxSetQuotaInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550800)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set quota information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_SET_QUOTA.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>MRxSetSdInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550805)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set security descriptor information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_SET_SECURITY.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>MRxSetVolumeInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550810)</td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set volume information. RDBSS issues this call in response to receiving an IRP_MJ_SET_VOLUME_INFORMATION.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------


