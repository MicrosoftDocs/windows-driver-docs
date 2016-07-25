---
title: Installing a Null Driver
description: Installing a Null Driver
ms.assetid: 8684eade-3f25-48fe-94e7-a7e76d8072ad
keywords: ["Device setup WDK device installations , null drivers", "device installations WDK , null drivers", "installing devices WDK , null drivers", "null drivers WDK device installations", "nonexistent drivers WDK device installations"]
---

# Installing a Null Driver


## <a href="" id="ddk-installing-a-null-driver-dg"></a>


You might install a "null driver" (that is, nonexistent driver) for a device if the device is not used on the machine and should not be started. Such devices do not typically exist on a machine, but if they do, you can install a null driver. Additionally, the system installs null drivers for devices that do not have a [function driver](https://msdn.microsoft.com/library/windows/hardware/ff546516), if they are capable of executing in [*raw mode*](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-raw-mode).

To specify a null driver in an INF file, use entries like the following:

```
:
[MyModels]
%MyDeviceDescription% = MyNullInstallSection, &amp;BadDeviceHardwareID%
:

[MyNullInstallSection]
; The install section is typically empty, but can contain entries that
; copy files or modify the registry.

[MyNullInstallSection.Services]
AddService = ,2    ; no value for the service name
:
```

The hardware ID for the device in the *Models* section should identify the device specifically, using the subsystem vendor ID and whatever other information is relevant.

The operating system will create a device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) for the device, but if the device is not capable of executing in raw mode, the operating system will not start the device because a function driver has not been assigned to it. Note, however, that if the device has a [boot configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#logical-configuration-types-for-resource-lists), those resources will be reserved.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Installing%20a%20Null%20Driver%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




