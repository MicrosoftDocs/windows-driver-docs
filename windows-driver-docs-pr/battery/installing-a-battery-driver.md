---
title: Installing a Battery Driver
description: Installing a Battery Driver
ms.assetid: 09db4d88-0cac-4171-8d05-d15a2cf4dab4
keywords: ["battery miniclass drivers WDK , installing", "battery class drivers WDK , installing"]
---

# Installing a Battery Driver


## <span id="ddk_installing_a_battery_driver_dg"></span><span id="DDK_INSTALLING_A_BATTERY_DRIVER_DG"></span>


A battery driver's INF file specifies information about the driver and the devices it controls. All battery devices are members of the Battery class and the battery class installer installs the driver.

This section describes battery-specific entries in the INF file. For more information about creating and distributing INF files and installing drivers, see [Creating an INF File](https://msdn.microsoft.com/library/windows/hardware/ff549520) and [INF File Sections and Directives](https://msdn.microsoft.com/library/windows/hardware/ff547433).

A battery driver's INF file includes the sections described below.

### <span id="Version"></span><span id="version"></span><span id="VERSION"></span>Version

A battery driver's INF file specifies the Battery class and its GUID, using the [**INF Version section**](https://msdn.microsoft.com/library/windows/hardware/ff547502), as shown in the following example:

``` syntax
[Version]
Signature="$WINDOWS NT$"
Class=Battery
ClassGuid={72631e54-78a4-11d0-bcf7-00aa00b7b32a}
Provider=%MyCo%
```

Note that %MyCo% must be defined in an [**INF Strings section**](https://msdn.microsoft.com/library/windows/hardware/ff547485) (not shown).

### <span id="DestinationDirs"></span><span id="destinationdirs"></span><span id="DESTINATIONDIRS"></span>DestinationDirs

In the [**INF DestinationDirs section**](https://msdn.microsoft.com/library/windows/hardware/ff547383), a battery driver's INF specifies the Drivers directory (12) as the default for all files.

``` syntax
[DestinationDirs]
DefaultDestDir = 12
```

### <span id="Manufacturer"></span><span id="manufacturer"></span><span id="MANUFACTURER"></span>Manufacturer

The [**INF Manufacturer section**](https://msdn.microsoft.com/library/windows/hardware/ff547454) defines the manufacturer of the device.

``` syntax
[Manufacturer]
%MyCo%=MyCompany
```

### <span id="Models"></span><span id="models"></span><span id="MODELS"></span>*Models*

The [**INF *Models* section**](https://msdn.microsoft.com/library/windows/hardware/ff547456) specifies the PnP hardware ID of the battery (shown as *pnpid* in the example). If the device is enumerated through ACPI, this section must also specify the EISA-style ID (shown as *acpidevnum*). For information about creating these IDs, see the *Advanced Configuration and Power Interface Specification*, which is available through the [ACPI / Power Management](http://go.microsoft.com/fwlink/p/?linkid=8760) website.

``` syntax
[MyCompany]
%pnpid.DeviceDesc% = NewBatt_Inst,pnpid
%ACPI\acpidevnum.DeviceDesc% = NewBatt_Inst,ACPI\acpidevnum
```

### <span id="DDInstall"></span><span id="ddinstall"></span><span id="DDINSTALL"></span>*DDInstall*

In the [**INF *DDInstall* section**](https://msdn.microsoft.com/library/windows/hardware/ff547344) (named NewBatt\_Inst in the example), an [**INF CopyFiles directive**](https://msdn.microsoft.com/library/windows/hardware/ff546346) copies the battery class driver (*Battc.sys*) and the new miniclass driver (*NewBatt.sys*) to the destination specified in the **DestinationDirs** directive.

``` syntax
[NewBatt_Inst]
CopyFiles = @NewBatt.sys
CopyFiles = @battc.sys
```

### <span id="DDInstall.Services"></span><span id="ddinstall.services"></span><span id="DDINSTALL.SERVICES"></span>*DDInstall*.Services

The [**INF *DDInstall*.Services section**](https://msdn.microsoft.com/library/windows/hardware/ff547349) includes an [**INF AddService directive**](https://msdn.microsoft.com/library/windows/hardware/ff546326) that specifies additional information about the battery driver. A battery driver's INF file should indicate that the driver is a kernel driver that uses normal error handling and starts during initialization of the operating system. Battery drivers specify the load order group Extended Base.

``` syntax
[NewBatt_Inst.Services]
AddService = NewBatt,2,NewBatt_Service_Inst    ; function driver for the device
 
[NewBatt_Service_Inst]
DisplayName    = %NewBatt.SvcDesc%
ServiceType    = 1 ;    SERVICE_KERNEL_DRIVER
StartType      = 3 ;    SERVICE_DEMAND_START
ErrorControl   = 1 ;    SERVICE_ERROR_NORMAL%
ServiceBinary  = %12%\NewBatt.sys
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20Installing%20a%20Battery%20Driver%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




