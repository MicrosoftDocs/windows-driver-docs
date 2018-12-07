---
title: MRxCreate routine
description: TheMRxCreate routine is called by RDBSS to request that the network mini-redirector create a file system object.
ms.assetid: d1b664cf-37b6-4c65-8634-21695af2db21
keywords: ["MRxCreate routine Installable File System Drivers", "PMRX_CALLDOWN"]
topic_type:
- apiref
api_name:
- MRxCreate
api_location:
- mrx.h
api_type:
- UserDefined
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# MRxCreate routine


The*MRxCreate* routine is called by [RDBSS](https://msdn.microsoft.com/library/windows/hardware/ff556810) to request that the network mini-redirector create a file system object.

Syntax
------

```ManagedCPlusPlus
PMRX_CALLDOWN MRxCreate;

NTSTATUS MRxCreate(
  _Inout_ PRX_CONTEXT RxContext
)
{ ... }
```

Parameters
----------

*RxContext* \[in, out\]  
A pointer to the RX\_CONTEXT structure. This parameter contains the IRP that is requesting the operation.

Return value
------------

*MRxCreate* returns STATUS\_SUCCESS on success or an appropriate NTSTATUS value, such as one of the following:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Return code</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>STATUS_INSUFFICIENT_RESOURCES</strong></td>
<td align="left"><p>There were insufficient resources to complete the operation.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_NETWORK_ACCESS_DENIED</strong></td>
<td align="left"><p>Network access was denied. This error can be returned if the network mini-redirector was asked to open a new file on a read-only share.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_NOT_IMPLEMENTED</strong></td>
<td align="left"><p>A feature that is requested, such as remote boot or a remote page file, is not implemented.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_NOT_SUPPORTED</strong></td>
<td align="left"><p>A feature that is requested, such as extended attributes, is not supported.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_OBJECT_NAME_COLLISION</strong></td>
<td align="left"><p>The network mini-redirector was asked to create a file that already exists.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_OBJECT_NAME_NOT_FOUND</strong></td>
<td align="left"><p>The object name was not found. This error can be returned if the network mini-redirector was asked to open a file that doesn&#39;t exist.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_OBJECT_PATH_NOT_FOUND</strong></td>
<td align="left"><p>The object path was not found. This error can be returned if an NTFS stream object was requested and the remote file system does not support streams.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_REPARSE</strong></td>
<td align="left"><p>A reparse is required to handle a symbolic link.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_RETRY</strong></td>
<td align="left"><p>The operation should be retried. This error can be returned if the network mini-redirector encountered a sharing violation or an access denied error.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

*MRxCreate* is called by RDBSS to request that the network mini-redirector open a file system object across the network. This call is issued by RDBSS in response to receiving an [**IRP\_MJ\_CREATE**](irp-mj-create.md) request.

Before calling *MRxCreate*, RDBSS modifies the following members in the RX\_CONTEXT structure pointed to by the *RxContext* parameter:

**pRelevantSrvOpen** is set to the SRV\_OPEN structure.

**Create.pSrvCall** is set to the SRV\_CALL structure.

**Create.NtCreateParameters** is set to the requested NT\_CREATE\_PARAMETERS.

In the context of a network mini-redirector, a file object refers to the associated file control block (FCB) and file object extension (FOBX) structures. There is a one to one correspondence between file objects and FOBXs. Many file objects will refer to the same FCB, which represents a single file on a remote server. A client can have several different open requests (NtCreateFile requests) on the same FCB and each of these will create a new file object. RDBSS and network mini-redirectors can choose to send fewer *MRxCreate* requests than the NtCreateFile requests received, in effect sharing an SRV\_OPEN structure among several FOBXs.

If the *MRxCreate* request was for a file overwrite and *MRxCreate* returned STATUS\_SUCCESS, then RDBSS will acquire the paging I/O resource and truncate the file. If the file is being cached by cache manager, RDBSS will update the sizes the cache manager has with the ones just received from the server.

Before returning, *MRxCreate* must set the **CurrentIrp-&gt;IoStatus.Information** member of the RX\_CONTEXT structure pointed to by the *RxContext* parameter.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Mrx.h (include Mrx.h)</td>
</tr>
</tbody>
</table>

## See also


[**MRxAreFilesAliased**](https://msdn.microsoft.com/library/windows/hardware/ff549838)

[**MRxCleanupFobx**](https://msdn.microsoft.com/library/windows/hardware/ff549841)

[**MRxCloseSrvOpen**](https://msdn.microsoft.com/library/windows/hardware/ff549845)

[**MRxCollapseOpen**](mrxcollapseopen.md)

[**MRxCreate**](mrxcreate.md)

[**MRxDeallocateForFcb**](https://msdn.microsoft.com/library/windows/hardware/ff549871)

[**MRxDeallocateForFobx**](https://msdn.microsoft.com/library/windows/hardware/ff549872)

[**MRxExtendForCache**](https://msdn.microsoft.com/library/windows/hardware/ff549878)

[**MRxExtendForNonCache**](mrxextendfornoncache.md)

[**MRxFlush**](mrxflush.md)

[**MRxForceClosed**](https://msdn.microsoft.com/library/windows/hardware/ff550677)

[**MRxIsLockRealizable**](https://msdn.microsoft.com/library/windows/hardware/ff550691)

[**MRxShouldTryToCollapseThisOpen**](mrxshouldtrytocollapsethisopen.md)

[**MRxTruncate**](mrxtruncate.md)

[**MRxZeroExtend**](mrxzeroextend.md)

 

 






