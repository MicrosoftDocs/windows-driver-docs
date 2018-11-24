---
title: File System Object Query and Set Routines
description: File System Object Query and Set Routines
ms.assetid: 34b97a6e-a155-443c-94dd-4d8f1fc4b430
keywords:
- mini-redirectors WDK , query operations
- mini-redirectors WDK , set operations
- query operations WDK network redirectors
- set operations WDK network redirectors
- file objects WDK mini-redirectors
- objects WDK mini-redirectors
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550696" data-raw-source="[&lt;strong&gt;MRxIsValidDirectory&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550696)"><strong>MRxIsValidDirectory</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector indicate if a path is a valid directory.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550755" data-raw-source="[&lt;strong&gt;MRxQueryDirectory&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550755)"><strong>MRxQueryDirectory</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query information on a file directory system object.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550759" data-raw-source="[&lt;strong&gt;MRxQueryEaInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550759)"><strong>MRxQueryEaInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query extended attribute information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_QUERY_EA.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550770" data-raw-source="[&lt;strong&gt;MRxQueryFileInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550770)"><strong>MRxQueryFileInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query file information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_QUERY_INFORMATION.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550773" data-raw-source="[&lt;strong&gt;MRxQueryQuotaInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550773)"><strong>MRxQueryQuotaInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query quota information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_QUERY_QUOTA.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550776" data-raw-source="[&lt;strong&gt;MRxQuerySdInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550776)"><strong>MRxQuerySdInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query security descriptor information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_QUERY_SECURITY.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550782" data-raw-source="[&lt;strong&gt;MRxQueryVolumeInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550782)"><strong>MRxQueryVolumeInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query volume information. RDBSS issues this call in response to receiving an IRP_MJ_QUERY_VOLUME_INFORMATION.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550786" data-raw-source="[&lt;strong&gt;MRxSetEaInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550786)"><strong>MRxSetEaInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set extended attribute information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_SET_EA.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550790" data-raw-source="[&lt;strong&gt;MRxSetFileInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550790)"><strong>MRxSetFileInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set file information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_SET_INFORMATION.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550796" data-raw-source="[&lt;strong&gt;MRxSetFileInfoAtCleanup&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550796)"><strong>MRxSetFileInfoAtCleanup</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector to set file information on a file system object at cleanup. RDBSS issues this call during cleanup when an application closes a handle but before the close.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550800" data-raw-source="[&lt;strong&gt;MRxSetQuotaInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550800)"><strong>MRxSetQuotaInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set quota information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_SET_QUOTA.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550805" data-raw-source="[&lt;strong&gt;MRxSetSdInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550805)"><strong>MRxSetSdInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set security descriptor information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_SET_SECURITY.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff550810" data-raw-source="[&lt;strong&gt;MRxSetVolumeInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550810)"><strong>MRxSetVolumeInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set volume information. RDBSS issues this call in response to receiving an IRP_MJ_SET_VOLUME_INFORMATION.</p></td>
</tr>
</tbody>
</table>

 

 

 




