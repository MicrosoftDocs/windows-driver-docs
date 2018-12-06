---
title: FSCTL_SUSPEND_OVERLAY control code
description: The FSCTL\_SUSPEND\_OVERLAY control code suspends a backing source attached to a volume, preventing access to the backing source and allowing it to be modified or removed.
ms.assetid: 5BC73E77-86A0-4A7D-BCBA-F3E8DA980701
keywords: ["FSCTL_SUSPEND_OVERLAY control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_SUSPEND_OVERLAY
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_SUSPEND\_OVERLAY control code


The **FSCTL\_SUSPEND\_OVERLAY** control code suspends a backing source attached to a volume, preventing access to the backing source and allowing it to be modified or removed.

To perform this operation, call [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) with the following parameters.

``` syntax
BOOL 
   WINAPI 
   DeviceIoControl( (HANDLE)       hDevice,         // handle to device
                    (DWORD)        FSCTL_SUSPEND_OVERLAY, // dwIoControlCode
                    (LPDWORD)      lpInBuffer,      // input buffer
                    (DWORD)        nInBufferSize,   // size of input buffer
                    (LPDWORD)      lpOutBuffer,     // output buffer
                    (DWORD)        nOutBufferSize,  // size of output buffer
                    (LPDWORD)      lpBytesReturned, // number of bytes returned
                    (LPOVERLAPPED) lpOverlapped );  // OVERLAPPED structure
```

**Parameters**

<a href="" id="instance--in-"></a>*Instance \[in\]*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. An opaque instance pointer for the caller. This parameter is required and cannot be NULL.

<a href="" id="fileobject--in-"></a>*FileObject \[in\]*  
[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) only. The file pointer object of the volume for which the overlay is updated. This parameter is required and cannot be NULL.

<a href="" id="filehandle--in-"></a>*FileHandle \[in\]*  
[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) only. The handle of the volume for which the overlay is updated. This parameter is required and cannot be NULL.

<a href="" id="fscontrolcode--in-"></a>*FsControlCode \[in\]*  
The control code for the operation. Use **FSCTL\_SUSPEND\_OVERLAY** for this operation.

<a href="" id="inputbuffer"></a>*InputBuffer*  
A pointer to the input buffer, which must contain a [**WOF\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632452) structure. When required, additional provider specific data is included immediately after **WOF\_EXTERNAL\_INFO**. If the provider is a WIM file, a [**WIM\_PROVIDER\_SUSPEND\_OVERLAY\_INPUT**](https://msdn.microsoft.com/library/windows/hardware/mt426740) structure is included after **WOF\_EXTERNAL\_INFO**.

<a href="" id="inputbufferlength--in-"></a>*InputBufferLength \[in\]*  
Set to **sizeof**([**WOF\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632452)) plus the size of any additional provider input data.

<a href="" id="outputbuffer--out-"></a>*OutputBuffer \[out\]*  
Not used. Set to NULL.

<a href="" id="outputbufferlength--in-"></a>*OutputBufferLength \[in\]*  
Set to 0.

Status block
------------

[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) returns STATUS\_SUCCESS if the operation succeeds. Otherwise, the appropriate function might return one of the following NTSTATUS values.

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
<td align="left"><p>The length of the input buffer pointed to by <em>InputBuffer</em>, and specified by <em>InputBufferLength</em>, is too small.</p></td>
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

 

Remarks
-------

When the backing source to remove is a Windows Imaging Format (WIM) file, the input buffer will contain a [**WOF\_EXTERNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn632452) structure followed by a [**WIM\_PROVIDER\_SUSPEND\_OVERLAY\_INPUT**](https://msdn.microsoft.com/library/windows/hardware/mt426740) structure. The *InputBufferLength* in this case will be **sizeof**(WOF\_EXTERNAL\_INFO) + **sizeof**([**WIM\_PROVIDER\_REMOVE\_OVERLAY\_INPUT**](https://msdn.microsoft.com/library/windows/hardware/dn632450)). The **DataSourceId** value in **WIM\_PROVIDER\_SUSPEND\_OVERLAY\_INPUT** must be for a WIM file previously added in an [**FSCTL\_ADD\_OVERLAY**](fsctl-add-overlay.md) request.

Additional backing providers will define their own specific input parameter structures.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ntifs.h (include Ntifs.h or Fltkernel.h)</td>
</tr>
</tbody>
</table>

## See also


[**FSCTL\_REMOVE\_OVERLAY**](fsctl-remove-overlay.md)

[**FSCTL\_UPDATE\_OVERLAY**](fsctl-update-overlay.md)

[**FSCTL\_GET\_EXTERNAL\_BACKING**](fsctl-get-external-backing.md)

[**FSCTL\_SET\_EXTERNAL\_BACKING**](fsctl-set-external-backing.md)

 

 






