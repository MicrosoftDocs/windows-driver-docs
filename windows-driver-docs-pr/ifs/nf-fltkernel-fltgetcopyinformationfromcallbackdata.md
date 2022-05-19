---
UID: NF:fltkernel.FltGetCopyInformationFromCallbackData
tech.root: ifsk
title: FltGetCopyInformationFromCallbackData function
ms.date: 05/24/2022
targetos: Windows
description: Learn more about the FltGetCopyInformationFromCallbackData function.
prerelease: false
keywords: ["FltGetCopyInformationFromCallbackData function"]
ms.keywords: FltGetCopyInformationFromCallbackData
req.header: fltkernel.h
req.include-header:
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
req.irql: <= DISPATCH_LEVEL
req.typenames: 
f1_keywords:
 - FltGetCopyInformationFromCallbackData
 - fltkernel/FltGetCopyInformationFromCallbackData
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - DllExport
api_location:
 - NtosKrnl.exe
api_name:
 - FltGetCopyInformationFromCallbackData
---

# FltGetCopyInformationFromCallbackData function

## -description

The **FltGetCopyInformationFromCallbackData** routine retrieves copy information from the callback data, if present. The copy information is in the IRP extension for read/write calls coming from [**NtCopyFileChunk**](nf-ntifs-ntcopyfilechunk.md).

## -parameters

### -param Data [in]

Pointer to a [**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data) structure that holds the callback data.

### -param CopyInformation [out]

Pointer to a [**COPY_INFORMATION**](ns-ntifs-copy_information.md) structure into which the copy information will be written.

## -returns

**FltGetCopyInformationFromCallbackData** returns STATUS_SUCCESS upon success, or an error code such as the following.

| Error code | Meaning |
| ---------- | ------- |
| STATUS_INVALID_PARAMETER | The callback data is not for an IRP operation. |
| STATUS_NOT_FOUND | The copy information IRP extension was not set on the IRP. |

## -remarks

Any trusted read or write operations from [**NtCopyFileChunk**](nf-ntifs-ntcopyfilechunk.md) will have the following:

* The IRP's requestor mode set to **KernelMode**.
* An IRP extension with an **IopCopyInformationType** type and [information about the copy operation](ns-ntifs-copy_information.md).

Filters do not have access to IRP extensions directly, but can check for the presence of the copy extension and get copy information by calling **FltGetCopyInformationFromCallbackData**.

See [Copying files in kernel mode](km-file-copy.md) for more information.

## -see-also

[**COPY_INFORMATION**](ns-ntifs-copy_information.md)

[**IoCheckFileObjectOpenedAsCopyDestination**](nf-ntifs-iocheckfileobjectopenedascopydestination.md)

[**IoCheckFileObjectOpenedAsCopySource**](nf-ntifs-iocheckfileobjectopenedascopysource.md)

[**NtCopyFileChunk**](nf-ntifs-ntcopyfilechunk.md)

[**NtCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile)
