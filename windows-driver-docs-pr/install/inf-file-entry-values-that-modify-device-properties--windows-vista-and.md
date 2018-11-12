---
title: INF File Entry Values That Modify Device Properties
description: INF File Entry Values That Modify Device Properties
ms.assetid: 5ce0875f-2687-42d9-b980-ed184b552a62
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF File Entry Values That Modify Device Properties


The following are the INF file entry values that modify device properties on Windows Vista and later:

-   INF file entry values that set corresponding [system-defined device properties](system-defined-device-properties2.md).

-   [**INF AddReg directives**](inf-addreg-directive.md) and [**INF DelReg directives**](inf-delreg-directive.md) that set or delete system-defined registry entry values that correspond to system-defined device properties.

-   INF **AddReg** directives and INF **DelReg** directives that set or delete custom registry entry values

-   [**INF AddProperty directives**](inf-addproperty-directive.md) and **INF DelProperty directives** that set and delete device properties. For more information about how to use these directives, see [Using the INF AddProperty Directive and the INF DelProperty Directive](using-the-inf-addproperty-directive-and-the-inf-delproperty-directive.md).

For general information about the INF file sections that install device instances, [device setup classes](device-setup-classes.md), [device interface classes](device-interface-classes.md), and device interfaces, see the following topics:

[**INF *DDInstall* Section**](inf-ddinstall-section.md)

[**INF ClassInstall32 Section**](inf-classinstall32-section.md)

[**INF InterfaceInstall32 Section**](inf-interfaceinstall32-section.md)

[**INF *DDInstall*.Interfaces Section**](inf-ddinstall-interfaces-section.md)

### <a href="" id="inf-file-entry-values-that-set-corresponding-system-defined-device-pro"></a>INF File Entry Values That Set Corresponding System-Defined Device Properties

Some INF file entry values provide information that Windows uses to set corresponding system-defined device properties. The following are a few examples of device properties whose values are supplied by such INF file entry values:

-   The [**DEVPKEY_Device_DeviceDesc**](https://msdn.microsoft.com/library/windows/hardware/ff542407) property for a device instance is set by the *device-description* entry value in the [**INF Models Section**](inf-models-section.md).

-   The [**DEVPKEY_DeviceClass_ClassName**](https://msdn.microsoft.com/library/windows/hardware/ff542272) property for a [device setup class](device-setup-classes.md) is set by the *class-name* entry value in the INF **Class** directive in the [**INF Version Section**](inf-version-section.md).

-   The [**DEVPKEY_DeviceInterface_ClassGuid**](https://msdn.microsoft.com/library/windows/hardware/ff542349) property for a device interface is set by the *InterfaceClassGuid* entry value in the [**INF InterfaceInstall32 section**](inf-interfaceinstall32-section.md).

### <a href="" id="inf-addreg-directives-and-inf-delreg-directives-that-modify-system-def"></a>INF AddReg Directives and INF DelReg Directives That Modify System-Defined Device Properties

Many system-defined device properties have corresponding system-defined registry entry values. For a device property that has a corresponding registry entry value, using an [**INF AddReg directive**](inf-addreg-directive.md) to add the corresponding registry entry value sets the corresponding device property. Similarly, using an [**INF DelReg directive**](inf-delreg-directive.md) to delete a registry entry value, deletes the corresponding device property.

For example, the following **AddReg** directive would set the **DeviceCharacteristics** registry entry value and the corresponding DEVPKEY_Device_Characteristics property for a device instance that is installed by the "Abc_Device_Install.HW" section.

```cpp
[Abc_Device_Install.HW]
...
AddReg = Xxx_AddReg
...
[Xxx_AddReg]
...
[HKR,,DeviceCharacteristics,0x10001,0x00000001
] 
```

### <a href="" id="inf-addreg-directives-and-inf-delreg-directives-that-modify-custom-reg"></a>INF AddReg Directives and INF DelReg Directives That Modify Custom Registry Entry Values

Windows Vista and later versions support using the [**INF AddReg directive**](inf-addreg-directive.md) and the [**INF DelReg directive**](inf-delreg-directive.md) to modify custom registry entry values that represent custom device properties. However, creating custom registry entry values to represent device properties is not supported by the unified device property model. If you create custom registry entry values for a device, you must manage the registry entry values in the same manner as you manage them on Windows Server 2003, Windows XP, and Windows 2000. To simplify the management of custom device properties, you should create device property keys to represent custom device properties instead of creating custom registry entry values.









