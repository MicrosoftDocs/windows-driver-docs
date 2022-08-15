---
UID: NF:ntifs.IoCheckFileObjectOpenedAsCopyDestination
tech.root: kernel
title: IoCheckFileObjectOpenedAsCopyDestination function (ntifs.h)
ms.date: 05/24/2022
targetos: Windows
description: Learn more about the IoCheckFileObjectOpenedAsCopyDestination function.
prerelease: false
keywords: ["IoCheckFileObjectOpenedAsCopyDestination function"]
ms.keywords: IoCheckFileObjectOpenedAsCopyDestination
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
 - IoCheckFileObjectOpenedAsCopyDestination
 - ntifs/IoCheckFileObjectOpenedAsCopyDestination
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - DllExport
api_location:
 - NtosKrnl.exe
api_name:
 - IoCheckFileObjectOpenedAsCopyDestination
---

# IoCheckFileObjectOpenedAsCopyDestination function

## -description

The **IoCheckFileObjectOpenedAsCopyDestination** routine checks whether a file was previously opened with copy intent as a destination file.

## -parameters

### -param FileObject [in]

Pointer to the destination file object to check for copy intent.

## -returns

**IoCheckFileObjectOpenedAsCopyDestination** returns TRUE if the file object represents a destination file that was previously opened with copy file intent; otherwise it returns FALSE. A return value of TRUE only signals the intent at create time; it does not mean that all operations on the file object are all part of copies.

## -remarks

See [**IoCheckFileObjectOpenedAsCopySource**](nf-ntifs-iocheckfileobjectopenedascopysource.md)
 for sample code that shows how to check if a file object was opened with copy intent.

See [Kernel-mode file copy and detecting copy file scenarios](km-file-copy.md) for more information.

## -see-also

[**EXTENDED_CREATE_INFORMATION**](ns-ntifs-extended_create_information.md)

[**IoCheckFileObjectOpenedAsCopySource**](nf-ntifs-iocheckfileobjectopenedascopysource.md)

[**NtCopyFileChunk**](nf-ntifs-ntcopyfilechunk.md)

[**NtCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile)
