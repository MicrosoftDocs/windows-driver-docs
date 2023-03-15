---
title: FSCTL_GET_WOF_VERSION control code
description: The FSCTL_GET_WOF_VERSION I/O control code (IOCTL) is used to query the version of the driver used to support a particular provider.
keywords: ["FSCTL_GET_WOF_VERSION control code Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FSCTL_GET_WOF_VERSION
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FSCTL_GET_WOF_VERSION control code

The **FSCTL_GET_WOF_VERSION** I/O control code (IOCTL) is used to query the version of the driver used to support a particular provider.

To perform this operation, call [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the following parameters.

``` syntax
BOOL 
   WINAPI 
   DeviceIoControl( (HANDLE)       hDevice,         // handle to device
                    (DWORD)        FSCTL_GET_WOF_VERSION, // dwIoControlCode
                    (LPDWORD)      lpInBuffer,      // input buffer
                    (DWORD)        nInBufferSize,   // size of input buffer
                    (LPDWORD)      lpOutBuffer,     // output buffer
                    (DWORD)        nOutBufferSize,  // size of output buffer
                    (LPDWORD)      lpBytesReturned, // number of bytes returned
                    (LPOVERLAPPED) lpOverlapped );  // OVERLAPPED structure
```

## Parameters

- **hDevice** [in]: A handle to the device. To obtain a device handle, call the [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) function or similar API.

- **dwIoControlCode** [in]: The control code for the operation. Use **FSCTL_GET_WOF_VERSION** for this operation.

- **lpInBuffer**: The input buffer for the operation. This is a pointer to a [**WOF_EXTERNAL_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_wof_external_info) structure.

- **nInBufferSize** [in]: The size, in bytes, of the input buffer. This should be **sizeof**([**WOF_EXTERNAL_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_wof_external_info)).

- **lpOutBuffer** [out]: The output buffer for the operation. This is a pointer to a [**WOF_VERSION_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_wof_version_info) structure.

- **nOutBufferSize** [in]: The size, in bytes, of the output buffer. This should be **sizeof**([**WOF_VERSION_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_wof_version_info)).

- **lpBytesReturned** [out]: A pointer to a variable that receives the size of the data stored in the output buffer, in bytes.

  If the output buffer is too small, the call fails, [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns **ERROR_INSUFFICIENT_BUFFER**, and **lpBytesReturned** is zero.

  If **lpOverlapped** is **NULL**, *lpBytesReturned* cannot be **NULL**. Even when an operation returns no output data and **lpOutBuffer** is **NULL**, [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) makes use of **lpBytesReturned**. After such an operation, the value of **lpBytesReturned** is meaningless.

  If **lpOverlapped** is not **NULL**, **lpBytesReturned** can be **NULL**. If this parameter is not **NULL** and the operation returns data, **lpBytesReturned** is meaningless until the overlapped operation has completed. To retrieve the number of bytes returned, call [**GetOverlappedResult**](/windows/win32/api/ioapiset/nf-ioapiset-getoverlappedresult). If the **hDevice** parameter is associated with an I/O completion port, you can retrieve the number of bytes returned by calling [**GetQueuedCompletionStatus**](/windows/win32/api/ioapiset/nf-ioapiset-getqueuedcompletionstatus).

- **lpOverlapped** [in]: A pointer to an [**OVERLAPPED**](/windows/win32/api/minwinbase/ns-minwinbase-overlapped) structure.

    If **hDevice** was opened without specifying **FILE_FLAG_OVERLAPPED**, **lpOverlapped** is ignored.

    If **hDevice** was opened with the **FILE_FLAG_OVERLAPPED** flag, the operation is performed as an overlapped (asynchronous) operation. In this case, **lpOverlapped** must point to a valid [**OVERLAPPED**](/windows/win32/api/minwinbase/ns-minwinbase-overlapped) structure that contains a handle to an event object. Otherwise, the function fails in unpredictable ways.

    For overlapped operations, [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) returns immediately, and the event object is signaled when the operation has been completed. Otherwise, the function does not return until the operation has been completed or an error occurs.

## Status block

If the operation completes successfully, [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) returns a nonzero value.

If the operation fails or is pending, [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) returns zero. To get extended error information, call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror).

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Minimum supported client | Windows 10 |
| Header | *Ntifs.h* (include *Ntifs.h* or *Fltkernel.h*) |
