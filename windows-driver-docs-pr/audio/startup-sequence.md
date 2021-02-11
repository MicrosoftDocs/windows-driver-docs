---
title: Startup Sequence
description: Startup Sequence
keywords:
- adapter drivers WDK audio , startup sequences
- startup sequences WDK audio
- audio adapters WDK , startup sequences
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Startup Sequence


## <span id="startup_sequence"></span><span id="STARTUP_SEQUENCE"></span>


Because the adapter driver is installed as a kernel-mode driver service, the operating system loads the adapter driver at system-startup time and calls the driver's [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine. The **DriverEntry** routine receives two parameters: a driver object and a registry path name. **DriverEntry** should call the PortCls function [**PcInitializeAdapterDriver**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcinitializeadapterdriver) with the driver-object and registry-path name parameters plus a third parameter, which is a pointer to the adapter driver's [**AddDevice**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) function.

In the following example, the driver's [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) function passes the function pointer `MyAddDevice`, which points to the driver's [**AddDevice**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) function, as the third parameter to the [**PcInitializeAdapterDriver**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcinitializeadapterdriver) routine.

```cpp
NTSTATUS 
  DriverEntry( 
    PDRIVER_OBJECT  DriverObject,
    PUNICODE_STRING  RegistryPath
    )
  {
      return PcInitializeAdapterDriver(DriverObject, RegistryPath, MyAddDevice);
  }
```

The [**PcInitializeAdapterDriver**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcinitializeadapterdriver) routine installs the supplied [**AddDevice**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine in the driver object's driver extension and installs the PortCls driver's IRP handlers in the driver object itself.

The following code is an example implementation of the driver's `MyAddDevice` function.

```cpp
#define MAX_MINIPORTS 6    // maximum number of miniports
NTSTATUS
  MyAddDevice(
    PDRIVER_OBJECT  DriverObject,
    PDEVICE_OBJECT  PhysicalDeviceObject 
    )
  {
      return PcAddAdapterDevice(DriverObject, PhysicalDeviceObject, MyStartDevice,
                                MAX_MINIPORTS, 0);
  }
```

This function calls the PortCls function [**PcAddAdapterDevice**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcaddadapterdevice), which creates the specified adapter device, associates a driver with the device, and stores a pointer to the adapter driver's `MyStartDevice` function, which is called when the operating system starts the device (see [Starting a Device](../kernel/starting-a-device.md)). The **PcAddAdapterDevice** routine creates a *functional device object (FDO)* and associates it with the *physical device object (PDO)* that is supplied by the system. The new FDO is created with an extension that PortCls uses to store context information about the device. This context includes the `MyStartDevice` function pointer that is supplied by `MyAddDevice`.

After the operating system determines what resources (interrupts, DMA channels, I/O port addresses, and so on) to assign to the device, it sends the device a request to start ([**IRP\_MN\_START\_DEVICE**](../kernel/irp-mn-start-device.md)). In response to this request, the request handler in the PortCls driver calls the adapter driver's `MyStartDevice` function, which is shown in the following example code:

```cpp
NTSTATUS
  MyStartDevice(
    PDEVICE_OBJECT DeviceObject,
    PIRP Irp,
    PRESOURCELIST ResourceList
    )
  {
    ...
  }
```

The request handler supplies `MyStartDevice` with pointers to the device object, IRP\_MN\_START\_DEVICE request, and resource list (see [IResourceList](/windows-hardware/drivers/ddi/portcls/nn-portcls-iresourcelist)). The `MyStartDevice` function partitions the resource list into the resources that are required for each miniport driver that needs to be started. The function then starts each miniport driver and returns control to PortCls, which completes the IRP and returns control to the operating system.

For more examples of driver startup code, see the sample audio adapter drivers in the Microsoft Windows Driver Kit (WDK).

