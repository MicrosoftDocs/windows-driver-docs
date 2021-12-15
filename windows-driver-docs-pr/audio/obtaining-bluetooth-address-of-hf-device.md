---
title: Obtaining Bluetooth Address of HF Device
description: The Obtaining Bluetooth Address of HF Device topic demonstrate how the audio driver can obtain the Bluetooth address of a paired Hands-free (HF) device.
ms.date: 04/20/2017
---

# Obtaining Bluetooth Address of HF Device


The Obtaining Bluetooth Address of HF Device topic demonstrate how the audio driver can obtain the Bluetooth address of a paired Hands-free (HF) device.

The address string can be useful for uniquely identifying a particular paired HF device. For example, the address string can be used as the *ReferenceString* parameter that is passed to IoRegisterDeviceInterface, the *RefString* parameter that is passed to KsCreateFilterFactory, or the *Name* parameter that is passed to PcRegisterSubdevice.

Note that the GUID\_DEVINTERFACE\_BLUETOOTH\_HFP\_SCO\_HCIBYPASS device interface symbolic link is also unique for each paired HF device, but this string can be too long for some purposes.

The IoHelperGetDevicePdo routine shown in the following code example is a utility function used by IoHelperGetDeviceBluetoothAddress. Such functions can be called while the audio driver is handling a PnP interface arrival notification. The audio driver gets the device object from IoGetDeviceObjectPointer and passes it to IoHelperGetDeviceBluetoothAddress.

```ManagedCPlusPlus
_IRQL_requires_(PASSIVE_LEVEL)
NTSTATUS
IoHelperGetDevicePdo(
    _In_ PDEVICE_OBJECT DeviceObject,
    _Out_ PDEVICE_OBJECT *PhysicalDeviceObject
    )

/*++

Routine description:
    Returns a pointer to the physical device object in a driver stack and
    increments the reference count on that object.

Parameters:
    DeviceObject
        Pointer to the device object for which the physical device object is
        retrieved. 

    PhysicalDeviceObject
        Returns a pointer to the physical device object in a stack of device
        objects after incrementing the reference count on the object.

Return value:
    A status code.

Remarks:
    This routine uses IRP_MN_QUERY_DEVICE_RELATIONS TargetDeviceRelation to
    get the physical device object from the device stack.

Requirements:
    IRQL    = PASSIVE_LEVEL

--*/

{
    NTSTATUS status;
    PIRP irp = NULL;
    PDEVICE_RELATIONS deviceRelations = NULL;
    PIO_STACK_LOCATION ioStack;
    KEVENT completionEvent;

    PAGED_CODE();

    irp = IoAllocateIrp(DeviceObject->StackSize, FALSE);
    if (irp == NULL)
    {
        status = STATUS_INSUFFICIENT_RESOURCES;
        goto Exit;
    }

    irp->IoStatus.Status = STATUS_NOT_SUPPORTED;

    ioStack = IoGetNextIrpStackLocation(irp);
    ioStack->MajorFunction = IRP_MJ_PNP;
    ioStack->MinorFunction = IRP_MN_QUERY_DEVICE_RELATIONS;
    ioStack->Parameters.QueryDeviceRelations.Type = TargetDeviceRelation;

    KeInitializeEvent(&completionEvent, SynchronizationEvent, FALSE);

    IoSetCompletionRoutine(irp, OnRequestComplete, &completionEvent, TRUE, TRUE, TRUE);

    status = IoCallDriver(DeviceObject, irp);
    if (status == STATUS_PENDING) {
        // wait for irp to complete
        KeWaitForSingleObject(
            &completionEvent,
            Suspended,
            KernelMode,
            FALSE,
            NULL);
        status = irp->IoStatus.Status;
    }

    if (NT_SUCCESS(status))
    {
        deviceRelations = (PDEVICE_RELATIONS)irp->IoStatus.Information;
        *PhysicalDeviceObject = deviceRelations->Objects[0];
    }

Exit:
    if (deviceRelations != NULL)
    {
        ExFreePool(deviceRelations);
    }
    if (irp != NULL)
    {
        IoFreeIrp(irp);
    }
    return status;
}

_IRQL_requires_(PASSIVE_LEVEL)
NTSTATUS IoHelperGetDeviceBluetoothAddress(
    _In_ PDEVICE_OBJECT DeviceObject,
    _Outptr_ PWSTR *BluetoothAddress,
    _In_ ULONG Tag
    )

/*++

Routine description:
    Returns the Bluetooth address string for the physical device object in the
    device stack.

Parameters:
    DeviceObject
        Pointer to a device object in a device stack whose physical object has
        a Bluetooth address property.

    BluetoothAddress
        Returns a string allocated from NonPagedPoolNx pool. 

    Tag

Return value:
    A status code.

Remarks:
    This routine retrieves the DEVPKEY_Bluetooth_DeviceAddress property from
    the physical device object in the device stack containing the specified
    device object.

Requirements:
    IRQL    = PASSIVE_LEVEL

--*/

{
    NTSTATUS status;
    PDEVICE_OBJECT physicalDeviceObject = NULL;
    PWSTR bluetoothAddress = NULL;
    ULONG requiredSize;
    DEVPROPTYPE devPropType;

    PAGED_CODE();

    status = IoHelperGetDevicePdo(DeviceObject, &physicalDeviceObject);
    if (!NT_SUCCESS(status))
    {
        goto Exit;
    }

    status = IoGetDevicePropertyData(physicalDeviceObject, &DEVPKEY_Bluetooth_DeviceAddress, LOCALE_NEUTRAL, 0, 0, NULL, &requiredSize, &devPropType);
    if (NT_SUCCESS(status) || devPropType != DEVPROP_TYPE_STRING)
    {
        status = STATUS_UNSUCCESSFUL;
        goto Exit;
    }
    if (status != STATUS_BUFFER_TOO_SMALL)
    {
        goto Exit;
    }

    bluetoothAddress = (PWCH)ExAllocatePoolWithTag(NonPagedPoolNx, requiredSize, Tag);
    if (bluetoothAddress == NULL)
    {
        status = STATUS_INSUFFICIENT_RESOURCES;
        goto Exit;
    }

    status = IoGetDevicePropertyData(physicalDeviceObject, &DEVPKEY_Bluetooth_DeviceAddress, LOCALE_NEUTRAL, 0, requiredSize, bluetoothAddress, &requiredSize, &devPropType);
    if (!NT_SUCCESS(status))
    {
        goto Exit;
    }

    *BluetoothAddress = bluetoothAddress;
    bluetoothAddress = NULL;
    status = STATUS_SUCCESS;

Exit:
    if (bluetoothAddress != NULL)
    {
        ExFreePoolWithTag(bluetoothAddress, Tag);
    }
    if (physicalDeviceObject != NULL)
    {
        ObDereferenceObject(physicalDeviceObject);
    }
    return status;
}
```

## <span id="related_topics"></span>Related topics
[Related Design Guidelines](related-design-guidelines.md)  



