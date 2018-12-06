---
title: FSCTL_QUERY_VOLUME_NUMA_INFO control code
description: The FSCTL\_QUERY\_VOLUME\_NUMA\_INFO control code finds the current Non-Uniform Memory Architecture (NUMA) node index for a volume.
ms.assetid: ADDA4A8C-0BF3-45F1-AFE5-956CE5D1FC01
keywords: ["FSCTL_QUERY_VOLUME_NUMA_INFO control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_QUERY_VOLUME_NUMA_INFO
api_location:
- WinIoctl.h
- Ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FSCTL\_QUERY\_VOLUME\_NUMA\_INFO control code


The **FSCTL\_QUERY\_VOLUME\_NUMA\_INFO** control code finds the current Non-Uniform Memory Architecture (NUMA) node index for a volume.

To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with the following parameters.

```ManagedCPlusPlus
BOOL 
   WINAPI 
   DeviceIoControl( (HANDLE)       hDevice,         
                    (DWORD)        FSCTL_QUERY_VOLUME_NUMA_INFO, // dwIoControlCode
                    (LPDWORD)      lpInBuffer,      // input buffer
                    (DWORD)        nInBufferSize,   // size of input buffer
                    (LPDWORD)      lpOutBuffer,     // output buffer
                    (DWORD)        nOutBufferSize,  // size of output buffer
                    (LPDWORD)      lpBytesReturned, // number of bytes returned
                    (LPOVERLAPPED) lpOverlapped );  // OVERLAPPED structure
```

Parameters
----------

*hDevice* \[in\]  
A handle to the device. To obtain a device handle, call the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) function.

This can also be a handle to a file or directory in the device as well. This FSCTL would return the NUMA node for the volume that contains the file or directory.

*dwIoControlCode* \[in\]  
The control code for the operation. Use **FSCTL\_QUERY\_VOLUME\_NUMA\_INFO** for this operation.

*lpInBuffer*   
Not used with this operation; set to **NULL**

*nInBufferSize* \[in\]  
Not used with this operation; set to zero.

*lpOutBuffer* \[out\]  
A pointer to a buffer that receives a [**FSCTL\_QUERY\_VOLUME\_NUMA\_INFO\_OUTPUT**](https://msdn.microsoft.com/library/windows/hardware/mt827087) structure which specifies a Non Uniform Memory Architecture (NUMA) volume's current node.

*nOutBufferSize* \[in\]  
The size of the output buffer, in bytes.

*lpBytesReturned* \[out\]  
A pointer to a variable that receives the size of the data stored in the output buffer, in bytes.

If the output buffer is too small, the call fails, [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) returns **ERROR\_INSUFFICIENT\_BUFFER**, and *lpBytesReturned* is zero.

If *lpOverlapped* is **NULL**, *lpBytesReturned* cannot be **NULL**. Even when an operation returns no output data and *lpOutBuffer* is **NULL**, [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) makes use of *lpBytesReturned*. After such an operation, the value of *lpBytesReturned* is meaningless.

If *lpOverlapped* is not **NULL**, *lpBytesReturned* can be **NULL**. If this parameter is not **NULL** and the operation returns data, *lpBytesReturned* is meaningless until the overlapped operation has completed. To retrieve the number of bytes returned, call [**GetOverlappedResult**](https://msdn.microsoft.com/library/windows/desktop/ms683209). If the *hDevice* parameter is associated with an I/O completion port, you can retrieve the number of bytes returned by calling [**GetQueuedCompletionStatus**](https://msdn.microsoft.com/library/windows/desktop/aa364986).

*lpOverlapped* \[in\]  
A pointer to an [**OVERLAPPED**](https://msdn.microsoft.com/library/windows/desktop/ms684342) structure.

If *hDevice* was opened without specifying **FILE\_FLAG\_OVERLAPPED**, *lpOverlapped* is ignored.

If *hDevice* was opened with the **FILE\_FLAG\_OVERLAPPED** flag, the operation is performed as an overlapped (asynchronous) operation. In this case, *lpOverlapped* must point to a valid [**OVERLAPPED**](https://msdn.microsoft.com/library/windows/desktop/ms684342) structure that contains a handle to an event object. Otherwise, the function fails in unpredictable ways.

For overlapped operations, [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) returns immediately, and the event object is signaled when the operation has been completed. Otherwise, the function does not return until the operation has been completed or an error occurs.

Return value
------------

If the operation completes successfully, [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) returns a nonzero value.

If the operation fails or is pending, [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) returns zero. To get extended error information, call [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360).

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
<td align="left">WinIoctl.h;
Ntifs.h</td>
</tr>
</tbody>
</table>

## See also


[**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216)

[**FSCTL\_QUERY\_VOLUME\_NUMA\_INFO\_OUTPUT**](https://msdn.microsoft.com/library/windows/hardware/mt827087)

 

 






