---
title: File System Object Query and Set Routines
description: File System Object Query and Set Routines
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
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_chkdir_calldown" data-raw-source="[&lt;strong&gt;MRxIsValidDirectory&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_chkdir_calldown)"><strong>MRxIsValidDirectory</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector indicate if a path is a valid directory.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxquerydirectory" data-raw-source="[&lt;strong&gt;MRxQueryDirectory&lt;/strong&gt;](./mrxquerydirectory.md)"><strong>MRxQueryDirectory</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query information on a file directory system object.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxqueryeainfo" data-raw-source="[&lt;strong&gt;MRxQueryEaInfo&lt;/strong&gt;](./mrxqueryeainfo.md)"><strong>MRxQueryEaInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query extended attribute information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_QUERY_EA.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxqueryfileinfo" data-raw-source="[&lt;strong&gt;MRxQueryFileInfo&lt;/strong&gt;](./mrxqueryfileinfo.md)"><strong>MRxQueryFileInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query file information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_QUERY_INFORMATION.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxqueryquotainfo" data-raw-source="[&lt;strong&gt;MRxQueryQuotaInfo&lt;/strong&gt;](./mrxqueryquotainfo.md)"><strong>MRxQueryQuotaInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query quota information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_QUERY_QUOTA.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxquerysdinfo" data-raw-source="[&lt;strong&gt;MRxQuerySdInfo&lt;/strong&gt;](./mrxquerysdinfo.md)"><strong>MRxQuerySdInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query security descriptor information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_QUERY_SECURITY.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxqueryvolumeinfo" data-raw-source="[&lt;strong&gt;MRxQueryVolumeInfo&lt;/strong&gt;](./mrxqueryvolumeinfo.md)"><strong>MRxQueryVolumeInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector query volume information. RDBSS issues this call in response to receiving an IRP_MJ_QUERY_VOLUME_INFORMATION.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxseteainfo" data-raw-source="[&lt;strong&gt;MRxSetEaInfo&lt;/strong&gt;](./mrxseteainfo.md)"><strong>MRxSetEaInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set extended attribute information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_SET_EA.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxsetfileinfo" data-raw-source="[&lt;strong&gt;MRxSetFileInfo&lt;/strong&gt;](./mrxsetfileinfo.md)"><strong>MRxSetFileInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set file information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_SET_INFORMATION.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxsetfileinfoatcleanup" data-raw-source="[&lt;strong&gt;MRxSetFileInfoAtCleanup&lt;/strong&gt;](./mrxsetfileinfoatcleanup.md)"><strong>MRxSetFileInfoAtCleanup</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector to set file information on a file system object at cleanup. RDBSS issues this call during cleanup when an application closes a handle but before the close.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxsetquotainfo" data-raw-source="[&lt;strong&gt;MRxSetQuotaInfo&lt;/strong&gt;](./mrxsetquotainfo.md)"><strong>MRxSetQuotaInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set quota information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_SET_QUOTA.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxsetsdinfo" data-raw-source="[&lt;strong&gt;MRxSetSdInfo&lt;/strong&gt;](./mrxsetsdinfo.md)"><strong>MRxSetSdInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set security descriptor information on a file system object. RDBSS issues this call in response to receiving an IRP_MJ_SET_SECURITY.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxsetvolumeinfo" data-raw-source="[&lt;strong&gt;MRxSetVolumeInfo&lt;/strong&gt;](./mrxsetvolumeinfo.md)"><strong>MRxSetVolumeInfo</strong></a></td>
<td align="left"><p>RDBSS calls this routine to request that a network mini-redirector set volume information. RDBSS issues this call in response to receiving an IRP_MJ_SET_VOLUME_INFORMATION.</p></td>
</tr>
</tbody>
</table>

 

