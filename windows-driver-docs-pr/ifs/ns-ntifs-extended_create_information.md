---
UID: NS:ntifs.EXTENDED_CREATE_INFORMATION
tech.root: kernel
title: EXTENDED_CREATE_INFORMATION structure (ntifs.h)
ms.date: 05/24/2022
targetos: Windows
description: Learn more about the EXTENDED_CREATE_INFORMATION structure.
prerelease: false
keywords: ["EXTENDED_CREATE_INFORMATION structure"]
ms.keywords: EXTENDED_CREATE_INFORMATION
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
req.lib:
req.dll:
req.irql:
req.typenames: 
f1_keywords:
 - EXTENDED_CREATE_INFORMATION
 - ntifs/EXTENDED_CREATE_INFORMATION
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - DllExport
api_location:
 - NtosKrnl.exe
api_name:
 - EXTENDED_CREATE_INFORMATION
---

# EXTENDED_CREATE_INFORMATION structure

## -description

The **EXTENDED_CREATE_INFORMATION** structure is the **EaBuffer** field in [**NtCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile) when the **FILE_CONTAINS_EXTENDED_CREATE_INFORMATION** flag is set in **NtCreateFile**'s **CreateOption** parameter.

## -struct-fields

### -field ExtendedCreateFlags

Flags for the extended create. **ExtendedCreateFlags** can be one of the following values. When either of these flags are specified, [**NtCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile)'s file object is marked as opened for copy intent in its **FileObjectExtension**. Filters can check for this stored state by calling [**IoCheckFileObjectOpenedAsCopySource**](nf-ntifs-iocheckfileobjectopenedascopysource.md) or [**IoCheckFileObjectOpenedAsCopyDestination**](nf-ntifs-iocheckfileobjectopenedascopydestination.md)

| Flag | Meaning |
| ---- | ------- |
| **EX_CREATE_FLAG_FILE_SOURCE_OPEN_FOR_COPY** (0x00000001) | Signals that the file is being opened as the source file for a file copy. |
| **EX_CREATE_FLAG_FILE_DEST_OPEN_FOR_COPY** (0x00000002) | Signals that the file is being opened as the destination file for a file copy. |

> [!NOTE]
> The presence of one of the above flags is not enough to ensure that read/writes (I/O operations) on the file object are trustworthy, as any user-mode process can provide these flags at create time.

### -field EaBuffer

Pointer to the extended attributes buffer.

### -field EaLength

Length of the buffer that **EaBuffer** points to.

## -remarks

The following example shows how to provide an **EXTENDED_CREATE_INFORMATION** struct to [**NtCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile), properly wrapping the **EaBuffer** and **EaLength** internally.

``` C
// Input parameters to NtCreateFile. Obtaining these
// values is not shown in this sample.

HANDLE SourceFile; 
ACCESS_MASK DesiredAccess; 
OBJECT_ATTRIBUTES ObjectAttributes; 
IO_STATUS_BLOCK IoStatus; 
ULONG FileAttributes; 
ULONG ShareAccess; 
ULONG CreateDisposition; 
ULONG CreateOptions; 
PVOID EaBuffer = NULL; 
ULONG EaLength = 0; 
EXTENDED_CREATE_INFORMATION ExtendedCreateInfo; 

// Populate the extended create info. The
// ExtendedCreateFlags field could also be
// EX_CREATE_FLAG_FILE_DESTINATION_OPEN_FOR_COPY.
 
ExtendedCreateInfo.EaBuffer = EaBuffer; 
ExtendedCreateInfo.EaLength = EaLength; 
ExtendedCreateInfo.ExtendedCreateFlags = EX_CREATE_FLAG_FILE_SOURCE_OPEN_FOR_COPY; 

// Set the create option flag to indicate the
// EaBuffer actually contains extended create info.
 
CreateOptions |= FILE_CONTAINS_EXTENDED_CREATE_INFORMATION; 

// Open the file 

Status = NtCreateFile(&SourceFile, 
                      DesiredAccess, 
                      &ObjectAttributes, 
                      &IoStatus, 
                      NULL, 
                      FileAttributes, 
                      SharseAccess, 
                      CreateDisposition, 
                      CreateOptions, 
                      &ExtendedCreateInfo, 
                      sizeof(EXTENDED_CREATE_INFORMATION));
```

See [Copying files in kernel mode](km-file-copy.md) for more information.

## -see-also

[**IoCheckFileObjectOpenedAsCopyDestination**](nf-ntifs-iocheckfileobjectopenedascopydestination.md)

[**IoCheckFileObjectOpenedAsCopySource**](nf-ntifs-iocheckfileobjectopenedascopysource.md)

[**NtCopyFileChunk**](nf-ntifs-ntcopyfilechunk.md)

[**NtCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile)
