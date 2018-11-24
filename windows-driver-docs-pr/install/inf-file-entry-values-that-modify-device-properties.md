---
title: INF File Entry Values That Modify Device Properties before Windows Vista
description: INF File Entry Values That Modify Device Properties before Windows Vista
ms.assetid: b2a1f265-fc9b-47fb-83af-b4f66d79da83
keywords:
- device properties WDK device installations , modifying
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF File Entry Values That Modify Device Properties before Windows Vista


The following are the INF file entry values that modify device properties on Windows Server 2003, Windows XP, and Windows 2000:

-   INF file entry values that set device properties that correspond to the [system-defined device properties](https://msdn.microsoft.com/library/windows/hardware/ff553413) that are part of the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) in Windows Vista and later versions of Windows.

-   [**INF AddReg directives**](inf-addreg-directive.md) and [**INF DelReg directives**](inf-delreg-directive.md) that set or delete system-defined registry entry values that correspond to the system-defined device properties that are part of the unified device property model in Windows Vista and later versions.

-   INF **AddReg** directives and INF **DelReg** directives that set or delete custom registry entry values that correspond to custom device properties.

For general information about the INF file sections that install device instances, [device setup classes](device-setup-classes.md), [device interface classes](device-interface-classes.md), and device interfaces, see the following topics:

[**INF *DDInstall* Section**](inf-ddinstall-section.md)

[**INF ClassInstall32 Section**](inf-classinstall32-section.md)

[**INF InterfaceInstall32 Section**](inf-interfaceinstall32-section.md)

[**INF *DDInstall*.Interfaces Section**](inf-ddinstall-interfaces-section.md)

### <a href="" id="inf-file-entry-values-that-correspond-to-system-defined-device-propert"></a>INF File Entry Values That Correspond to System-Defined Device Properties

Some INF file entry values provide information that Windows uses to set the system-defined registry entry values that correspond to device instance properties and device interface properties. The following are a few examples of registry entry values that are supplied by such INF file entry values:

-   The [**INF Models section**](inf-models-section.md) of an INF file includes a *device-description* entry value. This value corresponds to the [**DEVPKEY_Device_DeviceDesc**](https://msdn.microsoft.com/library/windows/hardware/ff542407) property in the unified device property model and can be retrieved by calling [**SetupDiGetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551967) and setting the *Property* parameter to SPDRP_DEVICEDESC.

-   The INF **Class** directive of an [**INF Version section**](inf-version-section.md) includes a *class-name* entry value that supplies the name of a [device setup class](device-setup-classes.md). This value corresponds to the [**DEVPKEY_DeviceClass_ClassName**](https://msdn.microsoft.com/library/windows/hardware/ff542272) property in the unified device property model. The class name for a device setup class can be retrieved by calling [**SetupDiClassNameFromGuid**](https://msdn.microsoft.com/library/windows/hardware/ff550947), and the class name of a device instance can be retrieved by calling [**SetupDiGetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551967) and setting the *Property* parameter to SPDRP_CLASS.

-   The [**INF InterfaceInstall32 section**](inf-interfaceinstall32-section.md) includes an *InterfaceClassGuid* entry value that supplies the GUID of a device interface. This value corresponds to the DEVPKEY_DeviceInterface_ClassGuid property in the unified device property model. The GUIDs of installed device interface classes can be retrieved by querying the subkeys of the root of the interface key, which can be opened by a calling [**SetupDiOpenClassRegKeyEx**](https://msdn.microsoft.com/library/windows/hardware/ff552067) and setting the *ClassGuid* parameter to **NULL** and the *Flags* parameter to DIOCR_INTERFACE. The GUID of a device interface can be retrieved by calling [**SetupDiEnumDeviceInterfaces**](https://msdn.microsoft.com/library/windows/hardware/ff551015), which retrieves an [**SP_DEVICE_INTERFACE_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552342) structure for the device interfaces that are associated with a device instance. The **InterfaceClassGuid** member of the SP_DEVICE_INTERFACE_DATA structure identifies the interface class GUID.

### <a href="" id="inf-addreg-directives-and-inf-delreg-directives-that-modify-system-def"></a>INF AddReg Directives and INF DelReg Directives That Modify System-Defined Device Properties

Many system-defined device properties have corresponding system-defined registry entry values. For device properties that have corresponding registry entry values, using an [**INF AddReg directive**](inf-addreg-directive.md) to add the corresponding registry entry value sets the corresponding device property. Similarly, using an [**INF DelReg directive**](inf-delreg-directive.md) to delete the corresponding registry entry value, also deletes the corresponding device property.

For example, the INF **AddReg** directive in the following "Abc_Device_Install.HW" section would set the **DeviceCharacteristics** registry entry value for a device instance:

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

The **DeviceCharacteristics** registry entry value corresponds to the [**DEVPKEY_Device_Characteristics**](https://msdn.microsoft.com/library/windows/hardware/ff542375) property in the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) in Windows Vista and later versions of Windows.

### <a href="" id="inf-addreg-directives-and-inf-delreg-directives-that-modify-custom-reg"></a>INF AddReg Directives and INF DelReg Directives That Modify Custom Registry Entry Values

Windows manages the correspondence between system-defined registry entry values and system-defined device properties. However, Windows does not manage the correspondence between custom registry entry values and custom device properties. An [**INF AddReg directive**](inf-addreg-directive.md) or an [**INF DelReg directive**](inf-delreg-directive.md) that modifies a custom registry entry value does not affect the system-defined properties that Windows manages.

Custom device instance properties that are set as shown in the following example, can be retrieved by calling [**SetupDiGetCustomDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551099).

```cpp
[XxxDDInstall.HW]
...
AddReg = Xxx_AddReg
...
[Xxx_AddReg]
...
[HKR,,CustomPropertyName,0x10001,0x00000001
] 
```

For more information about how to access custom device properties that have corresponding custom registry entry values, see [Accessing Custom Device Properties](accessing-custom-device-properties.md).









