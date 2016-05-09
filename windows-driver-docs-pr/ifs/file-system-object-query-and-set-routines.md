---
title: File System Object Query and Set Routines
author: windows-driver-content
description: File System Object Query and Set Routines
ms.assetid: 34b97a6e-a155-443c-94dd-4d8f1fc4b430
keywords: ["mini-redirectors WDK , query operations", "mini-redirectors WDK , set operations", "query operations WDK network redirectors", "set operations WDK network redirectors", "file objects WDK mini-redirectors", "objects WDK mini-redirectors"]
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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20File%20System%20Object%20Query%20and%20Set%20Routines%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


