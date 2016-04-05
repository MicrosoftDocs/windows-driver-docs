---
title: Specifying the Reflector in an INF File
description: Specifying the Reflector in an INF File
ms.assetid: 3676c99d-4e13-4385-910a-251232b00d4c
keywords: ["reflectors WDK UMDF", "AddService", "INF files WDK UMDF , reflectors", "function drivers WDK UMDF", "filter drivers WDK UMDF", "loading reflectors WDK UMDF"]
---

# Specifying the Reflector in an INF File


To add the reflector (WUDFRd.sys) to the kernel-mode device stack, the INF file of a UMDF driver must include an [**AddService directive**](https://msdn.microsoft.com/library/windows/hardware/ff546326) in an [**INF DDInstall.Services section**](https://msdn.microsoft.com/library/windows/hardware/ff547349). The reflector can be an upper filter, a lower filter, or the service for the device, depending on the configuration of the user-mode stack.

The following code example shows how the INF file for a UMDF function driver might add the reflector.

```
[Skeleton_Install.Services]
AddService=WUDFRd,0x000001fa,WUDFRD_ServiceInstall
```

In this example, the driver specifies the 0x2 (SPSVCINST\_ASSOCSERVICE) flag (ORed into the *flags* parameter above) to assign the reflector as the function driver in the kernel-mode device stack.

The **AddService** directive also sets the 0x000001f8 flags to prevent overwriting any preexisting configuration for the service. For more information about these flags, see the *flags* parameter of the [**AddService directive**](https://msdn.microsoft.com/library/windows/hardware/ff546326).

The following code example, taken from the WUDFVhidmini sample, shows an **AddService** directive for a UMDF filter driver.

```
[hidumdf.win8.NT.Services]
AddService=WUDFRd,0x000001f8,WUDFRD_ServiceInstall  
AddService=mshidumdf, 0x000001fa, mshidumdf.AddService

[WudfVhidmini_AddReg]
HKR,,"LowerFilters",0x00010008,"WUDFRd" ; FLG_ADDREG_TYPE_MULTI_SZ | FLG_ADDREG_APPEND
```

In this case, the mshidumdf service is associated with the FDO for the device stack, and the reflector is a lower filter.

## Providing a service-install-section


The **AddService** directive references an service-install-section similar to the following code example. The **ServiceType** entry specifies 1 or 0x00000001, which indicates that the INF installs support for one or more devices. The **StartType** entry specifies when to start the driver. The **ErrorControl** entry specifies the level of error control that the driver provides. The **ServiceBinary** entry specifies the path to the binary (the reflector) for the service.

```
[WUDFRD_ServiceInstall]
DisplayName = "Windows Driver Frameworks - User-mode Driver Framework Reflector"
ServiceType=1
StartType=3
ErrorControl=1
ServiceBinary=%12%\WUDFRd.sys
```

## Specifying a unique service name


Although it is not required to do so, a UMDF driver that runs only on Windows 8 and later operating systems can specify a unique service name for the WUDFRd (reflector) service.

The following example shows how to specify a unique service name instead of WUDFRd.

```
[Echo_Install.NT.Services]
AddService=WudfEchoDriver,0x00000002,WUDFEchoDriver_ServiceInstall

[WUDFEchoDriver_ServiceInstall]
DisplayName = %WudfEchoDriverDisplayName%
ServiceType = 1
StartType = 3
ErrorControl = 1
ServiceBinary = %12%\WUDFRd.sys
StartName = \Driver\WudfRd
```

In the above example, the driver specifies a unique value for the service name in the **AddService** directive. (In this case, it's WudfEchoDriver, which is the name of the driver.) Next, the driver specifies a unique **DisplayName** value for the service. Finally, the driver adds the **StartName** entry and sets it to \\Driver\\WudfRd.

UMDF drivers cannot specify a unique service name for the reflector on operating systems earlier than Windows 8. If your driver specifies a unique service name but must also work on operating systems earlier than Windows 8, use operating system specific sections in the INF file, as shown in the following example.

```
[Manufacturer]
%MSFT% = Microsoft,NTx86.6.0,NTx86.6.2
[Microsoft.NTx86.6.0]
%Sensors.DeviceDesc% = Sensors_Install_VistaWin7,HID_DEVICE_UP:0020_U:0001
[Microsoft.NTx86.6.2]
%Sensors.DeviceDesc% = Sensors_Install_Win8,HID_DEVICE_UP:0020_U:0001
[Sensors_Install_VistaWin7]
--- Install the device this way on Vista/Win7 ---
[Sensors_Install_Win8]
--- Install the device in a different way on Win8 ---
```

If the reflector is not added, UMDF is never loaded. The device might start, but the host process is not present and the device will not operate properly.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Specifying%20%20the%20Reflector%20in%20an%20INF%20File%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




