---
title: FLT_PARAMETERS for IRP_MJ_FILE_SYSTEM_CONTROL union
description: Union component used when the MajorFunction field of the FLT\_IO\_PARAMETER\_BLOCK structure for the operation is IRP\_MJ\_FILE\_SYSTEM\_CONTROL.
ms.assetid: d90b9f23-9fae-46e8-b68c-1ba11b3fa17a
keywords: ["FLT_PARAMETERS for IRP_MJ_FILE_SYSTEM_CONTROL union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FLT\_PARAMETERS for IRP\_MJ\_FILE\_SYSTEM\_CONTROL union


Union component used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure for the operation is [**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](irp-mj-file-system-control.md).

Syntax
------

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...   ;
  union {
    struct {
      PVPB           Vpb;
      PDEVICE_OBJECT DeviceObject;
    } VerifyVolume;
    struct {
      ULONG                   OutputBufferLength;
      ULONG POINTER_ALIGNMENT InputBufferLength;
      ULONG POINTER_ALIGNMENT FsControlCode;
    } Common;
    struct {
      ULONG                    OutputBufferLength;
      ULONG POINTER_ALIGNMENT  InputBufferLength;
      ULONG POINTER_ALIGNMENT  FsControlCode;
      PVOID                    InputBuffer;
      PVOID                    OutputBuffer;
      PMDL                     OutputMdlAddress;
    } Neither;
    struct {
      ULONG                   OutputBufferLength;
      ULONG POINTER_ALIGNMENT InputBufferLength;
      ULONG POINTER_ALIGNMENT FsControlCode;
      PVOID                   SystemBuffer;
    } Buffered;
    struct {
      ULONG                   OutputBufferLength;
      ULONG POINTER_ALIGNMENT InputBufferLength;
      ULONG POINTER_ALIGNMENT FsControlCode;
      PVOID                   InputSystemBuffer;
      PVOID                   OutputBuffer;
      PMDL                    OutputMdlAddress;
    } Direct;
  } FileSystemControl;
  ...   ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

Members
-------

**FileSystemControl**  
Structure containing the following members.

**VerifyVolume**  
Union component used for IRP\_MN\_VERIFY\_VOLUME operations.

**Vpb**  
Pointer to the volume parameter block (VPB) for the volume to be verified.

**DeviceObject**  
Pointer to the device object for the volume to be verified.

**Common**  
Union component used for all buffering methods for IRP\_MN\_KERNEL\_CALL and IRP\_MN\_USER\_FS\_REQUEST operations.

**OutputBufferLength**  
Length, in bytes, of the buffer that the **Neither.OutputBuffer** or **Direct.OutputBuffer** member points to.

**InputBufferLength**  
Length, in bytes, of the buffer that the **Neither.InputBuffer**, **Buffered.SystemBuffer**, or **Direct.InputSystemBuffer** member points to.

**FsControlCode**  
FSCTL function code to be passed to the file system, file system filter, or minifilter driver for the target device.

For detailed information about IOCTL and FSCTL requests, see [Using I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff565406) in the *Kernel Mode Architecture Guide* and "Device Input and Output Control Codes" in the Microsoft Windows SDK documentation. (This resource may not be available in some languages and countries.)

**Neither**  
Union component used for IRP\_MN\_KERNEL\_CALL and IRP\_MN\_USER\_FS\_REQUEST operations when the buffering method is METHOD\_NEITHER. For more information about buffering methods, see [Defining I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff543023) in the *Kernel Mode Architecture Guide*. (This resource may not be available in some languages and countries.)

**InputBuffer**  
User-mode virtual address of the input buffer that the original requester of the operation supplied. The I/O Manager and Filter Manager do not validate these addresses. To ensure that user-space addresses are valid, the minifilter must use routines such as [**ProbeForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559876), [**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879), and [**MmProbeAndLockPages**](https://msdn.microsoft.com/library/windows/hardware/ff554664), enclosing all buffer references in **try/except** blocks. For more information, see [Using Neither Buffered Nor Direct I/O](https://msdn.microsoft.com/library/windows/hardware/ff565432) and [Errors in Referencing User-Space Addresses](https://msdn.microsoft.com/library/windows/hardware/ff544308) in the *Kernel Mode Architecture Guide*. (This resource may not be available in some languages and countries.)

**OutputBuffer**  
User-mode virtual address of the output buffer that the original requester of the operation supplied. The I/O Manager and Filter Manager do not validate these addresses. To ensure that user-space addresses are valid, the minifilter must use routines such as [**ProbeForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559876), [**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879), and [**MmProbeAndLockPages**](https://msdn.microsoft.com/library/windows/hardware/ff554664), enclosing all buffer references in **try/except** blocks. For more information, see [Using Neither Buffered Nor Direct I/O](https://msdn.microsoft.com/library/windows/hardware/ff565432) and [Errors in Referencing User-Space Addresses](https://msdn.microsoft.com/library/windows/hardware/ff544308) in the *Kernel Mode Architecture Guide*. (This resource may not be available in some languages and countries.)

**OutputMdlAddress**  
Address of a memory descriptor list (MDL) that describes the buffer that the **Neither.OutputBuffer** member points to. This member is optional and can be **NULL**.

**Buffered**  
Union component used for IRP\_MN\_KERNEL\_CALL and IRP\_MN\_USER\_FS\_REQUEST operations when the buffering method is METHOD\_BUFFERED. For more information about buffering methods, see [Defining I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff543023) in the *Kernel Mode Architecture Guide*. (This resource may not be available in some languages and countries.)

**SystemBuffer**  
Address of the system-allocated buffer for the operation. In METHOD\_BUFFERED I/O, this buffer is used for both input and output. For more information, see [Methods for Accessing Data Buffers](https://msdn.microsoft.com/library/windows/hardware/ff554436) in the *Kernel Mode Architecture Guide*. (This resource may not be available in some languages and countries.)

**Direct**  
Union component used for IRP\_MN\_KERNEL\_CALL and IRP\_MN\_USER\_FS\_REQUEST operations when the buffering method is METHOD\_IN\_DIRECT or METHOD\_OUT\_DIRECT. For more information about buffering methods, see [Defining I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff543023) in the *Kernel Mode Architecture Guide*.

**InputSystemBuffer**  
Address of the input buffer for the operation. This buffer is locked down by the operating system so that it is safe to access from kernel mode. For more information, see [Methods for Accessing Data Buffers](https://msdn.microsoft.com/library/windows/hardware/ff554436) in the *Kernel Mode Architecture Guide*. (This resource may not be available in some languages and countries.)

**OutputBuffer**  
User-mode virtual address of the output buffer that the original requester of the operation supplied. In direct I/O, unlike METHOD\_NEITHER I/O, the operating system locks down this buffer so that it is safe to access from kernel mode, as long as the minifilter is in the same process context as the original requester of the I/O operation. (Otherwise it must call [**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559) to get the system address from the MDL that the **OutputMdlAddress** member points to.) For more information, see [Using Direct I/O](https://msdn.microsoft.com/library/windows/hardware/ff565372) and [Errors in Direct I/O](https://msdn.microsoft.com/library/windows/hardware/ff544300) in the *Kernel Mode Architecture Guide*. (This resource may not be available in some languages and countries.)

**OutputMdlAddress**  
Address of an MDL that describes the buffer that the **Direct.OutputBuffer** member points to. This member is required and cannot be **NULL**.

Remarks
-------

The [**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673) structure for [**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](irp-mj-file-system-control.md) operations contains the parameters for a file-system-control-information operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)) structure. It is contained in an [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure.

IRP\_MJ\_FILE\_SYSTEM\_CONTROL is an IRP-based operation.

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
<td align="left">Fltkernel.h (include Fltkernel.h)</td>
</tr>
</tbody>
</table>

## See also


[**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)

[**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638)

[**FLT\_IS\_FASTIO\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544645)

[**FLT\_IS\_FS\_FILTER\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544648)

[**FLT\_IS\_IRP\_OPERATION**](https://msdn.microsoft.com/library/windows/hardware/ff544654)

[**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673)

[**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988)

[**IoBuildAsynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548310)

[**IoBuildSynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548330)

[**IoVerifyVolume**](https://msdn.microsoft.com/library/windows/hardware/ff548559)

[**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](irp-mj-file-system-control.md)

[**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559)

[**MmProbeAndLockPages**](https://msdn.microsoft.com/library/windows/hardware/ff554664)

[**ProbeForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559876)

[**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879)

[**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462)

 

 






