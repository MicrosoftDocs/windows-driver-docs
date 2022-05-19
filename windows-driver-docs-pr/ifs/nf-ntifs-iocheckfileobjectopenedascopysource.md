---
UID: NF:ntifs.IoCheckFileObjectOpenedAsCopySource
tech.root: kernel
title: IoCheckFileObjectOpenedAsCopySource function (ntifs.h)
ms.date: 05/24/2022
targetos: Windows
description: Learn more about the IoCheckFileObjectOpenedAsCopySource function.
prerelease: false
keywords: ["IoCheckFileObjectOpenedAsCopySource function"]
ms.keywords: IoCheckFileObjectOpenedAsCopySource
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
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.typenames: 
f1_keywords:
 - IoCheckFileObjectOpenedAsCopySource
 - ntifs/IoCheckFileObjectOpenedAsCopySource
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - DllExport
api_location:
 - NtosKrnl.exe
api_name:
 - IoCheckFileObjectOpenedAsCopySource
---

# IoCheckFileObjectOpenedAsCopySource function

## -description

The **IoCheckFileObjectOpenedAsCopySource** routine checks whether a file was previously opened with copy intent as the source file.

## -parameters

### -param FileObject [in]

Pointer to the source file object to check for copy intent.

## -returns

**IoCheckFileObjectOpenedAsCopySource** returns TRUE if the file object represents a source file that was previously opened with copy file intent; otherwise it returns FALSE.

## -remarks

The presence of the **EX_CREATE_FLAG_FILE_DEST_OPEN_FOR_COPY** flag is not enough to ensure that reads on the file object are trustworthy, as any user-mode process can provide these flags at create time.

The following example shows how to check if a file object was opened with copy intent.

``` C

typedef  
BOOLEAN (*PIO_CHECK_FILE_OBJECT_OPENED_AS_COPY_SOURCE)( 
    _In_ PFILE_OBJECT FileObject 
); 
typedef  
BOOLEAN (*PIO_CHECK_FILE_OBJECT_OPENED_AS_COPY_DESTINATION)( 
    _In_ PFILE_OBJECT FileObject 
); 

PIO_CHECK_FILE_OBJECT_OPENED_AS_COPY_SOURCE IoCheckFileObjectOpenedAsCopySource; 
PIO_CHECK_FILE_OBJECT_OPENED_AS_COPY_DESTINATION IoCheckFileObjectOpenedAsCopyDestination;

// First resolve the API 
RtlInitUnicodeString(&RoutineName, L"IoCheckFileObjectOpenedAsCopySource"); 
IoCheckFileObjectOpenedAsCopySource = (PIO_CHECK_FILE_OBJECT_OPENED_AS_COPY_SOURCE)MmGetSystemRoutineAddress(&RoutineName); 

RtlInitUnicodeString(&RoutineName, L"IoCheckFileObjectOpenedAsCopyDestination"); 
IoCheckFileObjectOpenedAsCopyDestination = (PIO_CHECK_FILE_OBJECT_OPENED_AS_COPY_DESTINATION)MmGetSystemRoutineAddress(&RoutineName); 

// Now use the API 
IoCheckFileObjectOpenedAsCopySource(FltObjects->FileObject); 
IoCheckFileObjectOpenedAsCopyDestination(FltObjects->FileObject);
```

See [Copying files in kernel mode](km-file-copy.md) for more information.

## -see-also

[**EXTENDED_CREATE_INFORMATION**](ns-ntifs-extended_create_information.md)

[**IoCheckFileObjectOpenedAsCopyDestination**](nf-ntifs-iocheckfileobjectopenedascopydestination.md)

[**NtCopyFileChunk**](nf-ntifs-ntcopyfilechunk.md)

[**NtCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile)
