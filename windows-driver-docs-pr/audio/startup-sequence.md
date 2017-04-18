---
title: Startup Sequence
description: Startup Sequence
ms.assetid: bf88b9de-f4c4-4f9c-9355-603789b9ad3d
keywords: ["adapter drivers WDK audio , startup sequences", "startup sequences WDK audio", "audio adapters WDK , startup sequences"]
---

# Startup Sequence


## <span id="startup_sequence"></span><span id="STARTUP_SEQUENCE"></span>


Because the adapter driver is installed as a kernel-mode driver service, the operating system loads the adapter driver at system-startup time and calls the driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine. The **DriverEntry** routine receives two parameters: a driver object and a registry path name. **DriverEntry** should call the PortCls function [**PcInitializeAdapterDriver**](https://msdn.microsoft.com/library/windows/hardware/ff537703) with the driver-object and registry-path name parameters plus a third parameter, which is a pointer to the adapter driver's [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) function.

In the following example, the driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) function passes the function pointer `MyAddDevice`, which points to the driver's [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) function, as the third parameter to the [**PcInitializeAdapterDriver**](https://msdn.microsoft.com/library/windows/hardware/ff537703) routine.

```
NTSTATUS 
  DriverEntry( 
    PDRIVER_OBJECT  DriverObject,
    PUNICODE_STRING  RegistryPath
    )
  {
      return PcInitializeAdapterDriver(DriverObject, RegistryPath, MyAddDevice);
  }
```

The [**PcInitializeAdapterDriver**](https://msdn.microsoft.com/library/windows/hardware/ff537703) routine installs the supplied [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine in the driver object's driver extension and installs the PortCls driver's IRP handlers in the driver object itself.

The following code is an example implementation of the driver's `MyAddDevice` function.

```
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

This function calls the PortCls function [**PcAddAdapterDevice**](https://msdn.microsoft.com/library/windows/hardware/ff537683), which creates the specified adapter device, associates a driver with the device, and stores a pointer to the adapter driver's `MyStartDevice` function, which is called when the operating system starts the device (see [Starting a Device](https://msdn.microsoft.com/library/windows/hardware/ff563849)). The **PcAddAdapterDevice** routine creates a [*functional device object (FDO)*](https://msdn.microsoft.com/library/windows/hardware/ff556280#wdkgloss_functional_device_object__fdo_) and associates it with the [*physical device object (PDO)*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss_physical_device_object__pdo_) that is supplied by the system. The new FDO is created with an extension that PortCls uses to store context information about the device. This context includes the `MyStartDevice` function pointer that is supplied by `MyAddDevice`.

After the operating system determines what resources (interrupts, DMA channels, I/O port addresses, and so on) to assign to the device, it sends the device a request to start ([**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749)). In response to this request, the request handler in the PortCls driver calls the adapter driver's `MyStartDevice` function, which is shown in the following example code:

```
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

The request handler supplies `MyStartDevice` with pointers to the device object, IRP\_MN\_START\_DEVICE request, and resource list (see [IResourceList](https://msdn.microsoft.com/library/windows/hardware/ff536976)). The `MyStartDevice` function partitions the resource list into the resources that are required for each miniport driver that needs to be started. The function then starts each miniport driver and returns control to PortCls, which completes the IRP and returns control to the operating system.

For more examples of driver startup code, see the sample audio adapter drivers in the Microsoft Windows Driver Kit (WDK).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Startup%20Sequence%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


