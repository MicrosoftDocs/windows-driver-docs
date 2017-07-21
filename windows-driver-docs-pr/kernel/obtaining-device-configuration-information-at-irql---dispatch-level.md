---
title: Obtaining Device Configuration Information at IRQL DISPATCH\_LEVEL
author: windows-driver-content
description: Obtaining Device Configuration Information at IRQL DISPATCH\_LEVEL
ms.assetid: e168a12b-f32e-4b8d-8768-dc622b37b421
keywords: ["I/O WDK kernel , device configuration space", "device configuration space WDK I/O", "configuration space WDK I/O", "space WDK I/O", "DISPATCH_LEVEL WDK", "BUS_INTERFACE_STANDARD", "driver stacks WDK configuration info"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Obtaining Device Configuration Information at IRQL = DISPATCH\_LEVEL


## <a href="" id="ddk-obtaining-device-configuration-information-at-irql-dispatch-level-"></a>


The method illustrated in the [Obtaining Device Configuration Information at IRQL = PASSIVE\_LEVEL](obtaining-device-configuration-information-at-irql---passive-level.md) section makes use of I/O request packets (IRPs) and therefore is only valid for drivers running at IRQL = PASSIVE\_LEVEL. Drivers running at IRQL = DISPATCH\_LEVEL must use a bus interface to obtain device configuration space data. To obtain this data, you can use a bus-specific interface or the system-supplied bus-independent bus interface, [**BUS\_INTERFACE\_STANDARD**](https://msdn.microsoft.com/library/windows/hardware/ff540707).

It is preferable to use **BUS\_INTERFACE\_STANDARD** where possible, because a bus number is not required to retrieve configuration information when using **BUS\_INTERFACE\_STANDARD**, whereas drivers must often identify the bus number when retrieving bus-specific interfaces. Bus numbers for some buses, such as PCI, can change dynamically. Therefore, drivers should not depend on the bus number to access the PCI ports directly. Doing so might lead to system failure.

Three steps are required when accessing the configuration space of a PCI device at IRQL = DISPATCH\_LEVEL:

1.  Send an [**IRP\_MN\_QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff551687) request at IRQL = PASSIVE\_LEVEL to get the direct-call interface structure (**BUS\_INTERFACE\_STANDARD**) from the PCI bus driver. Store this in a nonpaged pool memory (typically in a device extension).

2.  Call the **BUS\_INTERFACE\_STANDARD** interface routines, [*SetBusData*](https://msdn.microsoft.com/library/windows/hardware/gg604856) and [*GetBusData*](https://msdn.microsoft.com/library/windows/hardware/gg604850), to access the PCI configuration space at IRQL = DISPATCH\_LEVEL.

3.  Dereference the interface. The PCI bus driver takes a reference count on the interface before it returns, so the driver that accesses the interface must dereference it, once it is no longer needed.

The following code sample demonstrates how to implement these three steps:

```
NTSTATUS
GetPCIBusInterfaceStandard(
    IN  PDEVICE_OBJECT DeviceObject,
    OUT PBUS_INTERFACE_STANDARD BusInterfaceStandard
    )
/*++
Routine Description:
    This routine gets the bus interface standard information from the PDO.
Arguments:
    DeviceObject - Device object to query for this information.
    BusInterface - Supplies a pointer to the retrieved information.
Return Value:
    NT status.
--*/ 
{
    KEVENT event;
    NTSTATUS status;
    PIRP irp;
    IO_STATUS_BLOCK ioStatusBlock;
    PIO_STACK_LOCATION irpStack;
    PDEVICE_OBJECT targetObject;

    Bus_KdPrint(("GetPciBusInterfaceStandard entered.\n"));
    KeInitializeEvent(&event, NotificationEvent, FALSE);
    targetObject = IoGetAttachedDeviceReference(DeviceObject);
    irp = IoBuildSynchronousFsdRequest(IRP_MJ_PNP,
                                       targetObject,
                                       NULL,
                                       0,
                                       NULL,
                                       &event,
                                       &ioStatusBlock);
    if (irp == NULL) {
        status = STATUS_INSUFFICIENT_RESOURCES;
        goto End;
    }
    irpStack = IoGetNextIrpStackLocation( irp );
    irpStack->MinorFunction = IRP_MN_QUERY_INTERFACE;
    irpStack->Parameters.QueryInterface.InterfaceType = (LPGUID)&GUID_BUS_INTERFACE_STANDARD;
    irpStack->Parameters.QueryInterface.Size = sizeof(BUS_INTERFACE_STANDARD);
    irpStack->Parameters.QueryInterface.Version = 1;
    irpStack->Parameters.QueryInterface.Interface = (PINTERFACE)BusInterfaceStandard;
    irpStack->Parameters.QueryInterface.InterfaceSpecificData = NULL;

    // Initialize the status to error in case the bus driver does not 
    // set it correctly.
    irp->IoStatus.Status = STATUS_NOT_SUPPORTED;
    status = IoCallDriver(targetObject, irp);
    if (status == STATUS_PENDING) {
        KeWaitForSingleObject(&event, Executive, KernelMode, FALSE, NULL);
        status = ioStatusBlock.Status;
    }
End:
    // Done with reference
    ObDereferenceObject(targetObject);
    return status;
}
```

The following code snippet shows how to use the [*GetBusData*](https://msdn.microsoft.com/library/windows/hardware/gg604850) interface routine to get the configuration space data (step 2).

```
 bytes = busInterfaceStandard.GetBusData(
                    busInterfaceStandard.Context,
                    PCI_WHICHSPACE_CONFIG,
                    Buffer
                    Offset,
                    Length);
```

When the driver is done with the interface, it can use code similar to the following snippet to dereference the interface (step 3). Drivers must not call interface routines after dereferencing the interface.

```
    (busInterfaceStandard.InterfaceDereference)(
                    (PVOID)busInterfaceStandard.Context);
```

The interface synchronizes the caller's access to the bus hardware with the PCI bus driver's access. The driver writer need not worry about creating spin locks to avoid contending with the PCI bus driver for access to bus hardware.

Note, that if all that is needed are bus, function, and device numbers, it is usually unnecessary to resort to a bus interface to obtain this information. This data can be retrieved indirectly by passing the PDO of the target device to the [**IoGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff549203) function as follows:

```
    ULONG   propertyAddress, length;
    USHORT  FunctionNumber, DeviceNumber;

    // Get the BusNumber. Be warned that bus numbers may be
    // dynamic and therefore subject to change unpredictably!!!
    IoGetDeviceProperty(PhysicalDeviceObject,
                        DevicePropertyBusNumber,
                        sizeof(ULONG),
                        (PVOID)&BusNumber,
                        &length);

    // Get the DevicePropertyAddress
    IoGetDeviceProperty(PhysicalDeviceObject,
                        DevicePropertyAddress,
                        sizeof(ULONG),
                        (PVOID)&propertyAddress,
                        &length);

    // For PCI, the DevicePropertyAddress has device number 
    // in the high word and the function number in the low word. 
    FunctionNumber = (USHORT)((propertyAddress) & 0x0000FFFF);
    DeviceNumber = (USHORT)(((propertyAddress) >> 16) & 0x0000FFFF);
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Obtaining%20Device%20Configuration%20Information%20at%20IRQL%20=%20DISPATCH_LEVEL%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


