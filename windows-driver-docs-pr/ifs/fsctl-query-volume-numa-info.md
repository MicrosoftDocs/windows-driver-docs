---
title: FSCTL_QUERY_VOLUME_NUMA_INFO Control Code
description: The FSCTL_QUERY_VOLUME_NUMA_INFO control code finds the current Non-Uniform Memory Architecture (NUMA) node index for a volume.
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
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_QUERY_VOLUME_NUMA_INFO control code

The **FSCTL_QUERY_VOLUME_NUMA_INFO** control code finds the current Non-Uniform Memory Architecture (NUMA) node index for a volume.

To perform this operation, call the [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) function with the following parameters.

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

## Parameters

- **hDevice** [in]: A handle to the device. To obtain a device handle, call the [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) function.

This can also be a handle to a file or directory in the device as well. This FSCTL would return the NUMA node for the volume that contains the file or directory.

- **dwIoControlCode** [in]: The control code for the operation. Use **FSCTL_QUERY_VOLUME_NUMA_INFO** for this operation.

- **lpInBuffer** [in]: Not used with this operation; set to **NULL**

- **nInBufferSize** [in]: Not used with this operation; set to zero.

- **lpOutBuffer** [out]: A pointer to a buffer that receives a [**FSCTL_QUERY_VOLUME_NUMA_INFO_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_query_volume_numa_info_output) structure which specifies a Non Uniform Memory Architecture (NUMA) volume's current node.

- **nOutBufferSize** [in]: The size of the output buffer, in bytes.

- **lpBytesReturned** [out]: A pointer to a variable that receives the size of the data stored in the output buffer, in bytes.

   If the output buffer is too small, the call fails, [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns **ERROR_INSUFFICIENT_BUFFER**, and **lpBytesReturned** is zero.

   If **lpOverlapped** is **NULL**, **lpBytesReturned** cannot be **NULL**. Even when an operation returns no output data and *lpOutBuffer* is **NULL**, [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) makes use of *lpBytesReturned*. After such an operation, the value of **lpBytesReturned** is meaningless.

   If **lpOverlapped** is not **NULL**, **lpBytesReturned** can be **NULL**. If this parameter is not **NULL** and the operation returns data, **lpBytesReturned** is meaningless until the overlapped operation has completed. To retrieve the number of bytes returned, call [**GetOverlappedResult**](/windows/win32/api/ioapiset/nf-ioapiset-getoverlappedresult). If the **hDevice** parameter is associated with an I/O completion port, you can retrieve the number of bytes returned by calling [**GetQueuedCompletionStatus**](/windows/win32/api/ioapiset/nf-ioapiset-getqueuedcompletionstatus).

- **lpOverlapped** [in]: A pointer to an [**OVERLAPPED**](/windows/win32/api/minwinbase/ns-minwinbase-overlapped) structure.

  If **hDevice** was opened without specifying **FILE_FLAG_OVERLAPPED**, **lpOverlapped** is ignored.

  If **hDevice** was opened with the **FILE_FLAG_OVERLAPPED** flag, the operation is performed as an overlapped (asynchronous) operation. In this case, **lpOverlapped** must point to a valid [**OVERLAPPED**](/windows/win32/api/minwinbase/ns-minwinbase-overlapped) structure that contains a handle to an event object. Otherwise, the function fails in unpredictable ways.

  For overlapped operations, [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) returns immediately, and the event object is signaled when the operation has been completed. Otherwise, the function does not return until the operation has been completed or an error occurs.

## Return value

If the operation completes successfully, [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) returns a nonzero value.

If the operation fails or is pending, [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) returns zero. To get extended error information, call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror).

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *WinIoctl.h*; *Ntifs.h* |

## See also

[**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol)

[**FSCTL_QUERY_VOLUME_NUMA_INFO_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsctl_query_volume_numa_info_output)
