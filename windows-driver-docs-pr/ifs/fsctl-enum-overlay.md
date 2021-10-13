---
title: FSCTL_ENUM_OVERLAY control code
description: The FSCTL\_ENUM\_OVERLAY control code enumerates all the data sources from a backing provider for a specified volume.
keywords: ["FSCTL_ENUM_OVERLAY control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_ENUM_OVERLAY
api_location:
- ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_ENUM\_OVERLAY control code


The **FSCTL\_ENUM\_OVERLAY** control code enumerates all the data sources from a backing provider for a specified volume.

To perform this operation, call [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the following parameters.

**Parameters**

<a href="" id="instance--in-"></a>*Instance \[in\]*  
[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. Opaque instance pointer for the caller. This parameter is required and cannot be **NULL**.

<a href="" id="fileobject--in-"></a>*FileObject \[in\]*  
[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) only. The file pointer object specifying the volume to be dismounted. This parameter is required and cannot be **NULL**.

<a href="" id="filehandle--in-"></a>*FileHandle \[in\]*  
[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) only. The file handle of the volume to be dismounted. This parameter is required and cannot be **NULL**.

<a href="" id="fscontrolcode--in-"></a>*FsControlCode \[in\]*  
Control code for the operation. Use **FSCTL\_REMOVE\_OVERLAY** for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
A pointer to the input buffer, which must contain a [**WOF\_EXTERNAL\_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_wof_external_info) structure.

<a href="" id="inputbufferlength--in-"></a>*InputBufferLength \[in\]*  
Set to **sizeof**(WOF\_EXTERNAL\_INFO).

<a href="" id="outputbuffer--out-"></a>*OutputBuffer \[out\]*  
Pointer to an output buffer which will receive one or more [**WIM\_PROVIDER\_OVERLAY\_ENTRY**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_wim_provider_update_overlay_input) structures for data sources backing the volume.

<a href="" id="outputbufferlength--out-"></a>*OutputBufferLength \[out\]*  
Size of the buffer pointed to by *OutputBuffer*, in bytes.

<a href="" id="lengthreturned--out-"></a>*LengthReturned \[out\]*  
Specifies the number of bytes written into *OutputBuffer* on successful completion.

## Status block

[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) returns STATUS\_SUCCESS if the operation succeeds. Otherwise, the appropriate function might return one of the following NTSTATUS values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Term</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>STATUS_ACCESS_DENIED</strong></p></td>
<td align="left"><p>The requestor does not have administrative privileges.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_BUFFER_TOO_SMALL</strong></p></td>
<td align="left"><p>The length of the output buffer pointed to by <em>OutputBuffer</em> and specified by <em>OutputBufferLength</em> is too small.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>STATUS_INTERNAL_ERROR</strong></p></td>
<td align="left"><p>The requested volume is not accessible.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>STATUS_INVALID_DEVICE_REQUEST</strong></p></td>
<td align="left"><p>The backing service is not present or not started.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

When enumerating the data sources for the WIM provider, the output buffer will contain an array of [**WIM\_PROVIDER\_OVERLAY\_ENTRY**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_wim_provider_update_overlay_input) structures. The size of the output buffer must be large enough to contain all the overlay entries or the call will return STATUS\_BUFFER\_TOO\_SMALL.

Additional backing providers will define their own specific enumeration structures.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available starting with Windows 8.1 Update.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntifs.h (include Ntifs.h or Fltkernel.h)</td>
</tr>
</tbody>
</table>

## See also


[**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile)

[**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85))

[**FSCTL\_ADD\_OVERLAY**](fsctl-add-overlay.md)

[**WOF\_EXTERNAL\_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_wof_external_info)

 

