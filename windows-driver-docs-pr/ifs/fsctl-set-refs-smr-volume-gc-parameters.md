---
title: FSCTL_SET_REFS_SMR_VOLUME_GC_PARAMETERS control code
description: The FSCTL\_SET\_REFS\_SMR\_VOLUME\_GC\_PARAMETERS control code controls the garbage collection on a Shingled Magnetic Recording (SMR) volume.
keywords: ["FSCTL_SET_REFS_SMR_VOLUME_GC_PARAMETERS control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_SET_REFS_SMR_VOLUME_GC_PARAMETERS
api_location:
- WinIoctl.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_SET\_REFS\_SMR\_VOLUME\_GC\_PARAMETERS control code


The **FSCTL\_SET\_REFS\_SMR\_VOLUME\_GC\_PARAMETERS** control code controls the garbage collection on a Shingled Magnetic Recording (SMR) volume.

```ManagedCPlusPlus
BOOL
   DeviceIoControl( (HANDLE)       hDevice,         // handle to volume
                    FSCTL_SET_REFS_SMR_VOLUME_GC_PARAMETERS, // dwIoControlCode
                    (LPDWORD)      lpInBuffer,      // input buffer
                    (DWORD)        nInBufferSize,   // size of input buffer
                     NULL,     // output buffer
                     0,  // size of output buffer
                    (LPDWORD)      lpBytesReturned, // number of bytes returned
                    (LPOVERLAPPED) lpOverlapped );  // OVERLAPPED structure
```

## Parameters

*hDevice* \[in\]  
A handle to the device. To obtain a device handle, call the [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) function.

*dwIoControlCode* \[in\]  
The control code for the operation. Use **FSCTL\_SET\_REFS\_SMR\_VOLUME\_GC\_PARAMETERS** for this operation.

*lpInBuffer*   
A pointer to a caller-allocated [**REFS\_SMR\_VOLUME\_GC\_PARAMETERS**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_refs_smr_volume_gc_parameters) structure.

*nInBufferSize* \[in\]  
The size of the input buffer, in bytes.

*lpOutBuffer* \[out\]  
Not used with this operation; set to **NULL**.

*nOutBufferSize* \[in\]  
Not used with this operation; set to zero.

*lpBytesReturned* \[out\]  
Not used with this operation; set to **NULL**.

*lpOverlapped* \[in\]  
A pointer to an [**OVERLAPPED**](/windows/win32/api/minwinbase/ns-minwinbase-overlapped) structure.

If *hDevice* was opened without specifying **FILE\_FLAG\_OVERLAPPED**, *lpOverlapped* is ignored.

If *hDevice* was opened with the **FILE\_FLAG\_OVERLAPPED** flag, the operation is performed as an overlapped (asynchronous) operation. In this case, *lpOverlapped* must point to a valid [**OVERLAPPED**](/windows/win32/api/minwinbase/ns-minwinbase-overlapped) structure that contains a handle to an event object. Otherwise, the function fails in unpredictable ways.

For overlapped operations, [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) returns immediately, and the event object is signaled when the operation has been completed. Otherwise, the function does not return until the operation has been completed or an error occurs.

## Return value

If the operation completes successfully, [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) returns a nonzero value.

If the operation fails or is pending, [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) returns zero. To get extended error information, call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available starting with Windows 10, version 1709.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">WinIoctl.h</td>
</tr>
</tbody>
</table>

## See also


[**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol)

 

