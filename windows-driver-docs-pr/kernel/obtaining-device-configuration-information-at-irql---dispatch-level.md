---
title: Obtaining Device Configuration Information at IRQL DISPATCH_LEVEL
description: Obtaining Device Configuration Information at IRQL DISPATCH_LEVEL
ms.assetid: e168a12b-f32e-4b8d-8768-dc622b37b421
keywords: ["I/O WDK kernel , device configuration space", "device configuration space WDK I/O", "configuration space WDK I/O", "space WDK I/O", "DISPATCH_LEVEL WDK", "BUS_INTERFACE_STANDARD", "driver stacks WDK configuration info"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Obtaining Device Configuration Information at IRQL = DISPATCH\_LEVEL





The method illustrated in the [Obtaining Device Configuration Information at IRQL = PASSIVE\_LEVEL](obtaining-device-configuration-information-at-irql---passive-level.md) section makes use of I/O request packets (IRPs) and therefore is only valid for drivers running at IRQL = PASSIVE\_LEVEL. Drivers running at IRQL = DISPATCH\_LEVEL must use a bus interface to obtain device configuration space data. To obtain this data, you can use a bus-specific interface or the system-supplied bus-independent bus interface, **BUS\_INTERFACE\_STANDARD**.

The GUID_BUS_INTERFACE_STANDARD interface (defined in `wdmguids.h`) enables device drivers to make direct calls to parent bus driver routines instead of using I/O request packets (IRP) to communicate with the bus driver. In particular, this interface enables drivers to access routines that the bus driver provides for the following functions:

-    Translating bus addresses 
-    Retrieving a DMA adapter structure in cases where the bus adapter supports DMA 
-    Reading and setting the bus configuration space for a particular device on the bus 

To use this interface, send an IRP_MN_QUERY_INTERFACE IRP to your bus driver with InterfaceType = GUID_BUS_INTERFACE_STANDARD. The bus driver supplies a pointer to a BUS_INTERFACE_STANDARD structure that contains pointers to the individual routines of the interface.


It is preferable to use **BUS\_INTERFACE\_STANDARD** where possible, because a bus number is not required to retrieve configuration information when using **BUS\_INTERFACE\_STANDARD**, whereas drivers must often identify the bus number when retrieving bus-specific interfaces. Bus numbers for some buses, such as PCI, can change dynamically. Therefore, drivers should not depend on the bus number to access the PCI ports directly. Doing so might lead to system failure.

Three steps are required when accessing the configuration space of a PCI device at IRQL = DISPATCH\_LEVEL:

1.  Send an [**IRP\_MN\_QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff551687) request at IRQL = PASSIVE\_LEVEL to get the direct-call interface structure (**BUS\_INTERFACE\_STANDARD**) from the PCI bus driver. Store this in a nonpaged pool memory (typically in a device extension).

2.  Call the **BUS\_INTERFACE\_STANDARD** interface routines, [*SetBusData*](https://msdn.microsoft.com/library/windows/hardware/gg604856) and [*GetBusData*](https://msdn.microsoft.com/library/windows/hardware/gg604850), to access the PCI configuration space at IRQL = DISPATCH\_LEVEL.

3.  Dereference the interface. The PCI bus driver takes a reference count on the interface before it returns, so the driver that accesses the interface must dereference it, once it is no longer needed.

The following code sample demonstrates how to implement these three steps:

```cpp
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

```cpp
 bytes = busInterfaceStandard.GetBusData(
                    busInterfaceStandard.Context,
                    PCI_WHICHSPACE_CONFIG,
                    Buffer
                    Offset,
                    Length);
```

When the driver is done with the interface, it can use code similar to the following snippet to dereference the interface (step 3). Drivers must not call interface routines after dereferencing the interface.

```cpp
    (busInterfaceStandard.InterfaceDereference)(
                    (PVOID)busInterfaceStandard.Context);
```

The interface synchronizes the caller's access to the bus hardware with the PCI bus driver's access. The driver writer need not worry about creating spin locks to avoid contending with the PCI bus driver for access to bus hardware.

Note, that if all that is needed are bus, function, and device numbers, it is usually unnecessary to resort to a bus interface to obtain this information. This data can be retrieved indirectly by passing the PDO of the target device to the [**IoGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff549203) function as follows:

```cpp
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

 

 




