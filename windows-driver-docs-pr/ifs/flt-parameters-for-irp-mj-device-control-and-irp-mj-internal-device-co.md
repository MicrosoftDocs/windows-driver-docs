---
title: FLT\_PARAMETERS for IRP\_MJ\_DEVICE\_CONTROL and IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL union
description: Union component used when the MajorFunction field of the FLT\_IO\_PARAMETER\_BLOCK structure for the operation is IRP\_MJ\_DEVICE\_CONTROL or IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL.
ms.assetid: ed2da1d5-838e-41a4-9a26-c61518da9cf3
keywords: ["FLT_PARAMETERS for IRP_MJ_DEVICE_CONTROL and IRP_MJ_INTERNAL_DEVICE_CONTROL union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# FLT\_PARAMETERS for IRP\_MJ\_DEVICE\_CONTROL and IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL union


Union component used when the **MajorFunction** field of the [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure for the operation is [**IRP\_MJ\_DEVICE\_CONTROL**](irp-mj-device-control.md) or [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](irp-mj-internal-device-control.md).

Syntax
------

```ManagedCPlusPlus
typedef union _FLT_PARAMETERS {
  ...   ;
  union {
    struct {
      ULONG                   OutputBufferLength;
      ULONG POINTER_ALIGNMENT InputBufferLength;
      ULONG POINTER_ALIGNMENT IoControlCode;
    } Common;
    struct {
      ULONG                   OutputBufferLength;
      ULONG POINTER_ALIGNMENT InputBufferLength;
      ULONG POINTER_ALIGNMENT IoControlCode;
      PVOID                   InputBuffer;
      PVOID                   OutputBuffer;
      PMDL                    OutputMdlAddress;
    } Neither;
    struct {
      ULONG                   OutputBufferLength;
      ULONG POINTER_ALIGNMENT InputBufferLength;
      ULONG POINTER_ALIGNMENT IoControlCode;
      PVOID                   SystemBuffer;
    } Buffered;
    struct {
      ULONG                   OutputBufferLength;
      ULONG POINTER_ALIGNMENT InputBufferLength;
      ULONG POINTER_ALIGNMENT IoControlCode;
      PVOID                   InputSystemBuffer;
      PVOID                   OutputBuffer;
      PMDL                    OutputMdlAddress;
    } Direct;
    struct {
      ULONG                   OutputBufferLength;
      ULONG POINTER_ALIGNMENT InputBufferLength;
      ULONG POINTER_ALIGNMENT IoControlCode;
      PVOID                   InputBuffer;
      PVOID                   OutputBuffer;
    } FastIo;
  } DeviceIoControl;
  ...   ;
} FLT_PARAMETERS, *PFLT_PARAMETERS;
```

Members
-------

**DeviceIoControl**  
**Common**  
Union component used for all buffering methods.

**OutputBufferLength**  
Length, in bytes, of the buffer that the **Neither.OutputBuffer**, **Direct.OutputBuffer**, or **FastIo.OutputBuffer** member points to.

**InputBufferLength**  
Length, in bytes, of the buffer that the **Neither.InputBuffer**, **Buffered.SystemBuffer**, **Direct.InputSystemBuffer**, or **FastIo.InputBuffer** member points to.

**IoControlCode**  
IOCTL function code to be passed to the device driver for the target device.

For detailed information about IOCTL requests, see [Using I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff565406) in the *Kernel Mode Architecture Guide* and "Device Input and Output Control Codes" in the Microsoft Windows SDK documentation. (This resource may not be available in some languages and countries.)

**Neither**  
Union component used when the buffering method is METHOD\_NEITHER. For more information about buffering methods, see [Defining I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff543023) in the *Kernel Mode Architecture Guide*.

**InputBuffer**  
User-mode virtual address of the input buffer that the original requester of the operation supplied. The I/O Manager and Filter Manager do not validate these addresses. To ensure that user-space addresses are valid, the minifilter must use routines such as [**ProbeForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559876), [**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879), and [**FltLockUserBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff543371), enclosing all buffer references in **try/except** blocks. For more information, see [Using Neither Buffered Nor Direct I/O](https://msdn.microsoft.com/library/windows/hardware/ff565432) and [Errors in Referencing User-Space Addresses](https://msdn.microsoft.com/library/windows/hardware/ff544308) in the *Kernel Mode Architecture Guide*. (This resource may not be available in some languages and countries.)

**OutputBuffer**  
User-mode virtual address of the output buffer that the original requester of the operation supplied. The I/O Manager and Filter Manager do not validate these addresses. To ensure that user-space addresses are valid, the minifilter must use routines such as [**ProbeForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559876), [**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879), and [**FltLockUserBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff543371), enclosing all buffer references in **try/except** blocks. For more information, see [Using Neither Buffered Nor Direct I/O](https://msdn.microsoft.com/library/windows/hardware/ff565432) and [Errors in Referencing User-Space Addresses](https://msdn.microsoft.com/library/windows/hardware/ff544308) in the *Kernel Mode Architecture Guide*.

**OutputMdlAddress**  
Address of a memory descriptor list (MDL) that describes the buffer that the *Neither.OutputBuffer* member points to. This member is optional and can be **NULL**.

**Buffered**  
Union component used when the buffering method is METHOD\_BUFFERED. For more information about buffering methods, see [Defining I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff543023) in the *Kernel Mode Architecture Guide*. (This resource may not be available in some languages and countries.)

**SystemBuffer**  
Address of the system-allocated buffer for the operation. In METHOD\_BUFFERED I/O, this buffer is used for both input and output. For more information, see [Methods for Accessing Data Buffers](https://msdn.microsoft.com/library/windows/hardware/ff554436) in the *Kernel Mode Architecture Guide*. (This resource may not be available in some languages and countries.)

**Direct**  
Union component used when the buffering method is METHOD\_IN\_DIRECT or METHOD\_OUT\_DIRECT. For more information about buffering methods, see [Defining I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff543023) in the *Kernel Mode Architecture Guide*. (This resource may not be available in some languages and countries.)

**InputSystemBuffer**  
Address of the input buffer for the operation. This buffer is locked down by the operating system so that it is safe to access from kernel mode. For more information, see [Methods for Accessing Data Buffers](https://msdn.microsoft.com/library/windows/hardware/ff554436) in the *Kernel Mode Architecture Guide*. (This resource may not be available in some languages and countries.)

**OutputBuffer**  
User-mode virtual address of the output buffer that the original requester of the operation supplied. In direct I/O, unlike METHOD\_NEITHER I/O, the operating system locks down this buffer so that it is safe to access from kernel mode, as long as the minifilter is in the same process context as the original requester of the I/O operation. (Otherwise it must call [**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559) to get the system address from the memory descriptor list (MDL) that the **OutputMdlAddress** member points to.) For more information, see [Using Direct I/O](https://msdn.microsoft.com/library/windows/hardware/ff565372) and [Errors in Direct I/O](https://msdn.microsoft.com/library/windows/hardware/ff544300) in the *Kernel Mode Architecture Guide*. (This resource may not be available in some languages and countries.)

**OutputMdlAddress**  
Address of an MDL that describes the buffer that the **Direct.OutputBuffer** member points to. This member is required and cannot be **NULL**.

**FastIo**  
Union component used when the [**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620) structure represents a fast I/O IRP\_MJ\_DEVICE\_CONTROL operation.

**InputBuffer**  
User-mode virtual address of the input buffer that the original requester of the operation supplied. The I/O Manager and Filter Manager do not validate these addresses. To ensure that user-space addresses are valid, the minifilter must use routines such as [**ProbeForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559876), [**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879), and [**FltLockUserBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff543371), enclosing all buffer references in **try/except** blocks. For more information, see [Errors in Referencing User-Space Addresses](https://msdn.microsoft.com/library/windows/hardware/ff544308) in the *Kernel Mode Architecture Guide*. (This resource may not be available in some languages and countries.)

**OutputBuffer**  
User-mode virtual address of the output buffer that the original requester of the operation supplied. The I/O Manager and Filter Manager do not validate these addresses. To ensure that user-space addresses are valid, the minifilter must use routines such as [**ProbeForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559876), [**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879), and [**FltLockUserBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff543371), enclosing all buffer references in **try/except** blocks. For more information, see [Errors in Referencing User-Space Addresses](https://msdn.microsoft.com/library/windows/hardware/ff544308) in the *Kernel Mode Architecture Guide*. (This resource may not be available in some languages and countries.)

Remarks
-------

The [**FLT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff544673) structure for [**IRP\_MJ\_DEVICE\_CONTROL**](irp-mj-device-control.md) and [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](irp-mj-internal-device-control.md) operations contains the parameters for an IRP-based device-I/O-control information operation represented by a callback data ([**FLT\_CALLBACK\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff544620)) structure. It is contained in an [**FLT\_IO\_PARAMETER\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff544638) structure.

IRP\_MJ\_DEVICE\_CONTROL can be an IRP-based operation or a fast I/O operation.

IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL is an IRP-based I/O operation.

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

[**FltDeviceIoControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542046)

[**FltLockUserBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff543371)

[**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318)

[**IRP\_MJ\_DEVICE\_CONTROL**](irp-mj-device-control.md)

[**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](irp-mj-internal-device-control.md)

[**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559)

[**MmProbeAndLockPages**](https://msdn.microsoft.com/library/windows/hardware/ff554664)

[**ProbeForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559876)

[**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879)

[**ZwDeviceIoControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566441)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FLT_PARAMETERS%20for%20IRP_MJ_DEVICE_CONTROL%20and%20IRP_MJ_INTERNAL_DEVICE_CONTROL%20union%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





