---
UID: NF:ntifs.NtCopyFileChunk
tech.root: kernel
title: NtCopyFileChunk function (ntifs.h)
ms.date: 08/02/2022
targetos: Windows
description: Learn more about the NtCopyFileChunk function.
prerelease: false
req.construct-type: function
keywords: ["NtCopyFileChunk function"]
ms.keywords: NtCopyFileChunk
req.header: ntifs.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Windows 11, version 22H2
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance:
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.typenames: 
f1_keywords:
 - NtCopyFileChunk
 - ntifs/NtCopyFileChunk
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - DllExport
api_location:
 - NtosKrnl.exe
api_name:
 - NtCopyFileChunk
---

# NtCopyFileChunk function

The **NtCopyFileChunk** routine copies data from the source file into the destination file. Available starting with Windows 11, version 22H2.

## Parameters

### SourceHandle [in]

The HANDLE of the source file to be read.

### DestHandle [in]

The HANDLE of the destination file. The data from **SourceHandle**'s file is copied into **DestHandle**'s file. Completion ports can be used on this handle.

### Event [in, optional]

An optional event to be signaled when the copy operation is complete.

### IoStatusBlock [out]

A pointer to an [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure that receives the final completion status and other information about the copy operation.

### Length [in]

The length of the data to copy, in bytes.

### SourceOffset [in]

The starting byte offset within the source file to begin the read operation.

### DestOffset [in]

The starting byte offset within the destination file to begin the write operation.

### SourceKey [in, optional]

An optional key to be used if there are oplocks associated with the source file.

### DestKey [in, optional]

An optional key to be used if there are oplocks associated with the destination file.

### Flags [in]

Optional flags. Currently there are no valid flag values.

## -returns

**NtCopyFileChunk** returns STATUS_SUCCESS if the copy is successfully completed, or an NTSTATUS code such as one of the following:

| Code | Meaning |
| ---- | ------- |
| STATUS_PENDING | The copy is in progress. Callers must wait on the event or file object to get the final status. |
| STATUS_[*ERROR*] | Various errors can occur similar to [**NtReadFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntreadfile) and [**NtWriteFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntwritefile). |

Once the write completes the status of the operation can be determined by examining the **Status** field of **IoStatusBlock**.

See **Remarks** for details regarding the handling of synchronous/asynchronous I/O.

## Remarks

**NtCopyFileChunk** copies data from a source file into a destination file using the provided file offsets for the requested length. If the length surpasses the end of file (EOF) on the source file, then **NtCopyFileChunk** will only read and copy the data to the destination up to the source’s EOF. Callers can get the actual number of bytes written from the **IoStatusBlock**.

**NtCopyFileChunk** includes two I/O operations: a read of the source file and a write to the destination file. While each I/O internally has its own completion, the caller’s event (or destination file handle if no event is provided) will be signaled when the copy operation is complete.

The source and destination files can be opened asynchronously or synchronously. While it is recommended that callers are consistent between the two handles, it is not required. Depending on the handles provided, **NtCopyFileChunk** will return at different points in the copy operation as specified in the following table.

| Source Handle | Destination Handle | Return Conditions |
| ------------- | ------------------ | ----------------- |
| Asynchronous  | Asynchronous       | Once the read has been successfully queued OR if there are errors prior to queuing the read. |
| Asynchronous  | Synchronous        | Once the write has finished OR if there are errors prior to write completion. |
| Synchronous   | Synchronous        | Once the write has finished OR if there are errors prior to write completion. |
| Synchronous   | Asynchronous       | Once the write has been successfully queued OR if there are errors prior to queueing the write. |

If STATUS_PENDING is returned, the called must wait for the operation to complete before looking at the I/O status block for the final status. If STATUS_SUCCESS is returned or the I/O status block indicates success, the caller should look at the **IoStatusBlock** to determine how many bytes were copied.

If either file is opened for non-cached I/O, the caller must ensure that the requested length is sector-aligned with whichever file is opened as non-cached. If both, the length should be aligned with the larger sector size of the two.

All read and write operations from **NtCopyFileChunk** will have:

* The IRP's requestor mode set to **KernelMode**
* An IRP extension of type **IopCopyInformationType**.

Filters do not have access to the IRP extensions directly but can check the presence of this extension and get copy information from the callback data by calling [**FltGetCopyInformationFromCallbackData**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetcopyinformationfromcallbackdata).

Fast IO is not available in this copy because the copy information is present in the IRP extension (and Fast IO doesn't create IRPs).

**NtCopyFileChunk** is used internally by [**CopyFile**](/windows/win32/api/winbase/nf-winbase-copyfile) for most forms of copy. Current exceptions include cloud copies, SMB offload and ODX.

The following example shows how to use **NtCopyFileChunk**.

``` C

// Input parameters to NtCopyFileChunk. Opening
// the file handles is done using NtCreateFile
// and creating the event is done with CreateEvent.
// This is not shown in this code sample. 

HANDLE sourceHandle; 
HANDLE destHandle; 
HANDLE event; 
IO_STATUS_BLOCK ioStatusBlock; 
ULONG length; 
LARGE_INTEGER sourceOffset; 
LARGE_INTEGER destOffset; 

// Copy the data 

status = NtCopyFileChunk( sourceHandle, 
                          destHandle, 
                          event, 
                          &ioStatusBlock, 
                          length, 
                          &sourceOffset, 
                          &destOffset, 
                          NULL, 
                          NULL, 
                          0 ); 

// Wait for the copy to complete 

if (status == STATUS_PENDING) { 
    status = NtWaitForSingleObject( event, FALSE, NULL ); 

    if (NT_SUCCESS(status)) { 
        status = ioStatusBlock.Status; 
    } 
}

```

See [Kernel-mode file copy and detecting copy file scenarios](km-file-copy.md) for more information.

## See Also

[**FltGetCopyInformationFromCallbackData**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetcopyinformationfromcallbackdata)

[**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block)

[**NtCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile)
