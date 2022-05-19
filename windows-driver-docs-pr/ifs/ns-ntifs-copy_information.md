---
UID: NS:ntifs.COPY_INFORMATION
tech.root: kernel
title: COPY_INFORMATION structure (ntifs.h)
ms.date: 05/24/2022
targetos: Windows
description: Learn more about the COPY_INFORMATION structure.
prerelease: false
keywords: ["COPY_INFORMATION structure"]
ms.keywords: COPY_INFORMATION
req.header: ntifs.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Windows 11, version 22H1
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
req.lib:
req.dll:
req.irql:
req.typenames: 
f1_keywords:
 - COPY_INFORMATION
 - ntifs/COPY_INFORMATION
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - DllExport
api_location:
 - NtosKrnl.exe
api_name:
 - COPY_INFORMATION
---

# COPY_INFORMATION structure

## -description

The **COPY_INFORMATION** structure correlates read and write calls to a copy operation from [**NtCopyFileChunk**](nf-ntifs-ntcopyfilechunk.md).

## -struct-fields

### -field SourceFileObject

The source file object of the copy.

### -field SourceFileOffset

The file offset of the source file of the copy. This value can be compared to the destination's file offset during write to ensure the copy is complete and faithful.

## -remarks

A copy's read and write operations contain the same information in their respective IRP extensions, so correlation can be done using **COPY_INFORMATION** for all writes that have the **IopCopyInformationType** IRP extension.

If the read and write operations are correlated and the copied data is verified, the written destination file can be considered a complete and faithful copy of the source. This means trust can be passed from the source file to the destination.

Copies generally happen in chunks. To validate the entire file copy:

* Each chunk (each call to [**NtCopyFileChunk**](nf-ntifs-ntcopyfilechunk.md)) must have its write operation correlated to a previous read operation.

* All chunks copied together should cover the entire range of the file.

A filter can verify the correctness of the copied data with the source information provided in the IRP extension of the write as follows:

* Verify that a matching read occurred on **SourceFileObject**.
* Verify that **SourceFileOffset** matches the write operation's file offset.

See [Copying files in kernel mode](km-file-copy.md) for more information.

## -see-also

[**FltGetCopyInformationFromCallbackData**](nf-fltkernel-fltgetcopyinformationfromcallbackdata.md)

[**IoCheckFileObjectOpenedAsCopySource**](nf-ntifs-iocheckfileobjectopenedascopysource.md)

[**IoCheckFileObjectOpenedAsCopyDestination**](nf-ntifs-iocheckfileobjectopenedascopydestination.md)

[**NtCopyFileChunk**](nf-ntifs-ntcopyfilechunk.md)

[**NtCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile)
