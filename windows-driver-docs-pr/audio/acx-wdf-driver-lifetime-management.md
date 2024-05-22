---
title: ACX WDF Driver Lifetime Management
description: This topic provides a summary of the ACX destruction and proper memory cleanup.
ms.date: 03/08/2024
ms.localizationpriority: medium
---

# ACX WDF driver lifetime management

This topic provides a summary of the ACX WDF driver lifetime management and proper memory cleanup. For a general overview of ACX, see [ACX audio class extensions overview](acx-audio-class-extensions-overview.md).

## ACX WDF initialization and startup

Proper ACX initialization, needs to occur, to allow proper clean up of ACX, WDF and memory resources. More detail on the major phases of device enumeration summarized here,  is available in [ACX device enumeration](acx-device-enumeration.md).

- WDM Driver Entry
- WDF Device Add
- WDF Prepare Hardware
- WDF Device D0 Entry
- ACX Circuit Creation Process (ACX Pins and Jacks objects are associated with the Circuit)
- ACX Stream Creation Process

### ACX WDF object cleanup

This topic describes the clean up of ACX WDF objects in this order.

- ACX Stream Close Process
- ACX Circuit Removal Process
- WDF Device Release Hardware
- WDF Driver Unload

There are multiple valid approaches to creating and cleaning up WDF and ACX objects, this topic covers some key elements of managing the lifetime of ACX/WDF objects.

### PnP Power events and object destruction

PnP Power events can cause object creation and destruction. For more information on PnP power events, see [ACX power management](acx-power-management.md) and WDF [PnP and Power Management Callback Sequences](../wdf/pnp-and-power-management-callback-sequences.md).

### WDF object reference lifetime management

WDF uses reference counts to help track the lifetime of objects. It may be appropriate in a cleanup call back function, to dereference object references. The framework call this cleanup call back function, so that the driver can call WdfObjectDereference if it had previously called WdfObjectReference for the object that is being deleted. For more information, see [WdfObjectReference](/windows-hardware/drivers/wdf/wdfobjectreference) and [WdfObjectDereference](/windows-hardware/drivers/wdf/wdfobjectdereference).

### Surface Team driver development best practices

For a description of common mistakes that are made in driver code with memory and object lifetime management, see those sections in [Surface Team driver development best practices](/windows-hardware/drivers/kernel/surface-team-driver-development-best-practices).

## ACX Stream Close Process

When the client closes the stream, the driver needs to work to close and clean up the resources that were associated with the stream. For more details, see [ACX Streaming - Stream close process](acx-streaming.md#stream-close-process). It is important that the driver does not clean up resources that support the stream, and that the clean up process be aware of impacts on the client.

## ACX Circuit Removal Process

ACX can create a dynamic circuit on demand. To do this, the driver allocates a [WDFDEVICE_INIT structure](../wdf/wdfdevice_init.md) by calling [WdfPdoInitAllocate](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitallocate). The driver then specifies any PnP/power callbacks it wants to receive and creates the device. The driver invokes [AcxDeviceRemoveCircuitDevice](/windows-hardware/drivers/ddi/acxdevice/nf-acxdevice-acxdeviceremovecircuitdevice) to remove the audio device from the device list.

For more information, see *ACX circuit dynamic removal* in [ACX Circuits](acx-circuits.md#acx-circuit-dynamic-removal).

## WDF Device Release Hardware

The [EVT_WDF_DEVICE_RELEASE_HARDWARE callback function](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware) is used to in a driver's EvtDeviceReleaseHardware event callback function to perform operations that are needed when a device is no longer accessible.

### WDF Device Context Cleanup

This code from the AudioCodec sample shows use of an [WDF_OBJECT_ATTRIBUTES structure](/windows-hardware/drivers/ddi/wdfobject/ns-wdfobject-_wdf_object_attributes) to set a EvtCleanupCallback.

```cpp
    WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&attributes, CODEC_DEVICE_CONTEXT);
    attributes.EvtCleanupCallback = Codec_EvtDeviceContextCleanup;
```

This example callback given a WdfDevice cleans up device context.

```cpp
VOID
Codec_EvtDeviceContextCleanup(
    _In_ WDFOBJECT      WdfDevice
)

{
    WDFDEVICE               device;
    PCODEC_DEVICE_CONTEXT   devCtx;

    device = (WDFDEVICE)WdfDevice;
    devCtx = GetCodecDeviceContext(device);
    ASSERT(devCtx != nullptr);

    if (devCtx->Capture)
    {
        CodecC_CircuitCleanup(devCtx->Capture);
    }
}
```

## WDF Driver Unload

When the driver is unloaded, it should release all remaining resources. For more information, see [Releasing Driver-Allocated Resources](/windows-hardware/drivers/kernel/releasing-driver-allocated-resources).

A driver registers an EvtDriverUnload callback function when it calls WdfDriverCreate. The EvtDriverUnload callback function must deallocate any non-device-specific system resources that the driver's DriverEntry routine allocated. For more information, see [EVT_WDF_DRIVER_UNLOAD callback function](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_unload).

This code from the AudioCodec sample shows the structure of a driver unload callback.

```cpp
EVT_WDF_DRIVER_UNLOAD               AudioCodecDriverUnload;

void AudioCodecDriverUnload(
    _In_ WDFDRIVER Driver
)
{
    PAGED_CODE();

    if (!Driver)
    {
        ASSERT(FALSE);
        return;
    }

    WPP_CLEANUP(WdfDriverWdmGetDriverObject(Driver));

// Here is where you would cleanup any allocated resources associated with the driver.

    return;
}
```

## See also

[ACX device enumeration](acx-device-enumeration.md)

[ACX power management](acx-power-management.md)

[PnP and Power Management Callback Sequences](../wdf/pnp-and-power-management-callback-sequences.md)

[Summary of ACX objects](acx-summary-of-objects.md)

[ACX audio class extensions overview](acx-audio-class-extensions-overview.md)

[ACX reference documentation](acx-reference.md)
