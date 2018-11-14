---
title: MRxDevFcbXXXControlFile routine
description: The MRxDevFcbXXXControlFile routine is called by RDBSS to pass a device FCB control request (an IOCTL or FSCTL request) to the network mini-redirector.
ms.assetid: d60449d0-17d0-4303-8d0d-cba091de2b07
keywords: ["MRxDevFcbXXXControlFile routine Installable File System Drivers", "PMRX_CALLDOWN"]
topic_type:
- apiref
api_name:
- MRxDevFcbXXXControlFile
api_location:
- mrx.h
api_type:
- UserDefined
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# MRxDevFcbXXXControlFile routine


The *MRxDevFcbXXXControlFile* routine is called by [RDBSS](https://msdn.microsoft.com/library/windows/hardware/ff556810) to pass a device FCB control request (an IOCTL or FSCTL request) to the network mini-redirector.

Syntax
------

```ManagedCPlusPlus
PMRX_CALLDOWN MRxDevFcbXXXControlFile;

NTSTATUS MRxDevFcbXXXControlFile(
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

*MRxDevFcbXXXControlFile* returns STATUS\_SUCCESS on success or an appropriate NTSTATUS value, such as one of the following:

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
<td align="left"><strong>STATUS_ACCESS_DENIED</strong></td>
<td align="left"><p>A request was made to stop or start the network mini-redirector, but the caller lacked the proper security for this operation.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_INVALID_DEVICE_REQUEST</strong></td>
<td align="left"><p>An invalid device request was sent to the network mini-redirector.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_REDIRECTOR_HAS_OPEN_HANDLES</strong></td>
<td align="left"><p>This was a request to stop the network mini-redirector, but the redirector has open handles that prevent it from stopping at this time.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_REDIRECTOR_NOT_STARTED</strong></td>
<td align="left"><p>This was a request to stop the network mini-redirector, but the redirector was not started.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_REDIRECTOR_STARTED</strong></td>
<td align="left"><p>This was a request to start the network mini-redirector, but the redirector was already started.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

*MRxDevFcbXXXControlFile* handles IOCTL and FSCTL requests related to the device FCB that are sent to the network mini-redirector.

Before calling *MRxDevFcbXXXControlFile*, RDBSS modifies the following member in the RX\_CONTEXT structure pointed to by the *RxContext* parameter:

**MajorFunction** is set to the major function of the IRP

If this was an IRP\_MJ\_FILE\_SYSTEM\_CONTROL request, then RDBSS modifies the following members in the RX\_CONTEXT structure pointed to by the *RxContext* parameter:

**LowIoContext.ParamsFor.FsCtl.MinorFunction** is set to the minor function code for the FSCTL code

**LowIoContext.ParamsFor.FsCtl.FsControlCode** is set to the FSCTL code for the IRP

If this was an IRP\_MJ\_DEVICE\_CONTROL or IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL request, then RDBSS modifies the following member in the RX\_CONTEXT structure pointed to by the *RxContext* parameter:

**LowIoContext.ParamsFor.FsCtl.FsControlCode** is set to the control code for the IRP.

If *MRxDevFcbXXXControlFile* returns STATUS\_SUCCESS, then the routine was successful. Any other return value indicates that an error occurred.

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


[**MRxStart**](https://msdn.microsoft.com/library/windows/hardware/ff550829)

[**MRxStop**](mrxstop.md)

 

 






