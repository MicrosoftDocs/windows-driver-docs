---
title: FLT_PARAMETERS for IRP_MJ_DEVICE_CONTROL and IRP_MJ_INTERNAL_DEVICE_CONTROL Union
description: Union component used when the MajorFunction field of the FLT_IO_PARAMETER_BLOCK structure for the operation is IRP_MJ_DEVICE_CONTROL or IRP_MJ_INTERNAL_DEVICE_CONTROL.
keywords: ["FLT_PARAMETERS for IRP_MJ_DEVICE_CONTROL and IRP_MJ_INTERNAL_DEVICE_CONTROL union Installable File System Drivers", "FLT_PARAMETERS union Installable File System Drivers", "PFLT_PARAMETERS union pointer Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FLT_PARAMETERS
api_location:
- fltkernel.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FLT_PARAMETERS for IRP_MJ_DEVICE_CONTROL and IRP_MJ_INTERNAL_DEVICE_CONTROL union

Union component used when the **MajorFunction** field of the [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure for the operation is [**IRP_MJ_DEVICE_CONTROL**](irp-mj-device-control.md) or [**IRP_MJ_INTERNAL_DEVICE_CONTROL**](irp-mj-internal-device-control.md).

## Syntax

``` C
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

## Members

- **Common**: Union component used for all buffering methods (**Neither**, **Buffered**, and **FastIo**).

- **OutputBufferLength**: Length, in bytes, of the buffer that the **Neither.OutputBuffer**, **Direct.OutputBuffer**, or **FastIo.OutputBuffer** member points to.

- **InputBufferLength**: Length, in bytes, of the buffer that the **Neither.InputBuffer**, **Buffered.SystemBuffer**, **Direct.InputSystemBuffer**, or **FastIo.InputBuffer** member points to.

- **IoControlCode**: IOCTL function code to be passed to the device driver for the target device. For detailed information about IOCTL requests, see [Using I/O Control Codes](../kernel/introduction-to-i-o-control-codes.md) and "Device Input and Output Control Codes" in the Microsoft Windows SDK documentation. (This resource may not be available in some languages and countries.)

- **Neither**: Union component used when the buffering method is METHOD_NEITHER. For more information about buffering methods, see [Defining I/O Control Codes](../kernel/defining-i-o-control-codes.md) in the *Kernel Mode Architecture Guide*.

- **Neither.InputBuffer**: User-mode virtual address of the input buffer that the original requester of the operation supplied. The I/O Manager and Filter Manager do not validate these addresses. To ensure that user-space addresses are valid, the minifilter must use routines such as [**ProbeForRead**](/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforread), [**ProbeForWrite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforwrite), and [**FltLockUserBuffer**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltlockuserbuffer), enclosing all buffer references in **try/except** blocks. For more information, see [Using Neither Buffered Nor Direct I/O](../kernel/using-neither-buffered-nor-direct-i-o.md) and [Errors in Referencing User-Space Addresses](../kernel/errors-in-referencing-user-space-addresses.md).

- **Neither.OutputBuffer**: User-mode virtual address of the output buffer that the original requester of the operation supplied. The I/O Manager and Filter Manager do not validate these addresses. To ensure that user-space addresses are valid, the minifilter must use routines such as [**ProbeForRead**](/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforread), [**ProbeForWrite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforwrite), and [**FltLockUserBuffer**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltlockuserbuffer), enclosing all buffer references in **try/except** blocks. For more information, see [Using Neither Buffered Nor Direct I/O](../kernel/using-neither-buffered-nor-direct-i-o.md) and [Errors in Referencing User-Space Addresses](../kernel/errors-in-referencing-user-space-addresses.md) in the *Kernel Mode Architecture Guide*.

- **Neither.OutputMdlAddress**: Address of a memory descriptor list (MDL) that describes the buffer that the *Neither.OutputBuffer* member points to. This member is optional and can be **NULL**.

- **Buffered**: Union component used when the buffering method is METHOD_BUFFERED. For more information about buffering methods, see [Defining I/O Control Codes](../kernel/defining-i-o-control-codes.md).

- **Buffered.SystemBuffer**: Address of the system-allocated buffer for the operation. In METHOD_BUFFERED I/O, this buffer is used for both input and output. For more information, see [Methods for Accessing Data Buffers](../kernel/methods-for-accessing-data-buffers.md).

- **Direct**: Union component used when the buffering method is METHOD_IN_DIRECT or METHOD_OUT_DIRECT. For more information about buffering methods, see [Defining I/O Control Codes](../kernel/defining-i-o-control-codes.md).

- **Direct.InputSystemBuffer**: Address of the input buffer for the operation. This buffer is locked down by the operating system so that it is safe to access from kernel mode. For more information, see [Methods for Accessing Data Buffers](../kernel/methods-for-accessing-data-buffers.md).

- **Direct.OutputBuffer**: User-mode virtual address of the output buffer that the original requester of the operation supplied. In direct I/O, unlike METHOD_NEITHER I/O, the operating system locks down this buffer so that it is safe to access from kernel mode, as long as the minifilter is in the same process context as the original requester of the I/O operation. (Otherwise it must call [**MmGetSystemAddressForMdlSafe**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetsystemaddressformdlsafe) to get the system address from the memory descriptor list (MDL) that the **OutputMdlAddress** member points to.) For more information, see [Using Direct I/O](../kernel/using-direct-i-o.md) and [Errors in Direct I/O](../kernel/errors-in-direct-i-o.md).

- **Direct.OutputMdlAddress**: Address of an MDL that describes the buffer that the **Direct.OutputBuffer** member points to. This member is required and cannot be **NULL**.

- **FastIo**: Union component used when the [**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data) structure represents a fast I/O IRP_MJ_DEVICE_CONTROL operation.

- **FastIo.InputBuffer**: User-mode virtual address of the input buffer that the original requester of the operation supplied. The I/O Manager and Filter Manager do not validate these addresses. To ensure that user-space addresses are valid, the minifilter must use routines such as [**ProbeForRead**](/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforread), [**ProbeForWrite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforwrite), and [**FltLockUserBuffer**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltlockuserbuffer), enclosing all buffer references in **try/except** blocks. For more information, see [Errors in Referencing User-Space Addresses](../kernel/errors-in-referencing-user-space-addresses.md).

- **FastIo.OutputBuffer**: User-mode virtual address of the output buffer that the original requester of the operation supplied. The I/O Manager and Filter Manager do not validate these addresses. To ensure that user-space addresses are valid, the minifilter must use routines such as [**ProbeForRead**](/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforread), [**ProbeForWrite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforwrite), and [**FltLockUserBuffer**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltlockuserbuffer), enclosing all buffer references in **try/except** blocks. For more information, see [Errors in Referencing User-Space Addresses](../kernel/errors-in-referencing-user-space-addresses.md).

## Remarks

The [**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for [**IRP_MJ_DEVICE_CONTROL**](irp-mj-device-control.md) and [**IRP_MJ_INTERNAL_DEVICE_CONTROL**](irp-mj-internal-device-control.md) operations contains the parameters for an IRP-based device-I/O-control information operation represented by a callback data ([**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)) structure. It is contained in an [**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure.

IRP_MJ_DEVICE_CONTROL can be an IRP-based operation or a fast I/O operation.

IRP_MJ_INTERNAL_DEVICE_CONTROL is an IRP-based I/O operation.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Fltkernel.h* (include *Fltkernel.h*) |

## See also

[**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data)

[**FLT_IO_PARAMETER_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)

[**FLT_IS_FASTIO_OPERATION**](/windows-hardware/drivers/ddi/index)

[**FLT_IS_FS_FILTER_OPERATION**](/previous-versions/ff544648(v=vs.85))

[**FLT_IS_IRP_OPERATION**](/previous-versions/ff544654(v=vs.85))

[**FLT_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters)

[**FltDeviceIoControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdeviceiocontrolfile)

[**FltLockUserBuffer**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltlockuserbuffer)

[**IoBuildDeviceIoControlRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest)

[**IRP_MJ_DEVICE_CONTROL**](irp-mj-device-control.md)

[**IRP_MJ_INTERNAL_DEVICE_CONTROL**](irp-mj-internal-device-control.md)

[**MmGetSystemAddressForMdlSafe**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetsystemaddressformdlsafe)

[**MmProbeAndLockPages**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmprobeandlockpages)

[**ProbeForRead**](/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforread)

[**ProbeForWrite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-probeforwrite)

[**ZwDeviceIoControlFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwdeviceiocontrolfile)
