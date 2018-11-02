---
title: Accessing Device Interface Class Properties
description: Accessing Device Interface Class Properties
ms.assetid: c9efe273-dc66-4585-8ab5-3842df1c95df
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing Device Interface Class Properties


In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) includes device interface class properties that characterize a device interface class. The unified device property model uses [property keys](property-keys.md) to represent these properties.

Windows Server 2003, Windows XP, and Windows 2000 also support most of these device interface class properties. However, these earlier versions of Windows do not support the property keys of the unified device property model. Instead, you can represent and access the corresponding property information on these versions of Windows by using the following methods:

-   [Accessing the Default Interface for a Device Interface Class](#accessing-the-default-interface-for-a-device-interface-class)

-   [Accessing Device Interface Class Properties That Have Registry Entry Values Under the Interface Class Registry Key](#accessing-device-interface-class-properties-that-have-registry-entry-v)

To maintain compatibility with these earlier versions of Windows, Windows Vista and later versions also support these two ways to access information about a device interface. However, you should use the property keys to access these properties in Windows Vista and later versions.

For a list of the system-defined device interface class properties, see [Device Interface Class Properties](https://msdn.microsoft.com/library/windows/hardware/ff541406). The [device setup class properties](accessing-device-setup-class-properties.md) are listed by the property key identifiers that you use to access the properties in Windows Vista and later versions. The information that is provided with the property keys also includes the corresponding registry entry values that you can use to access the properties on Windows Server 2003, Windows XP, and Windows 2000.

For information about how to use property keys to access device setup class properties in Windows Vista and later versions, see [Accessing Device Class Properties (Windows Vista and Later)](accessing-device-class-properties--windows-vista-and-later-.md).

### <a href="" id="accessing-the-default-interface-for-a-device-interface-class"></a> Accessing the Default Interface for a Device Interface Class

To retrieve the default interface for a device interface class, call [**SetupDiGetClassDevs**](https://msdn.microsoft.com/library/windows/hardware/ff551069) and supply the following parameter values:

-   Set *ClassGuid* to the GUID that represents the device interface class for which to retrieve the default interface.

-   Set *Enumerator***NULL**.

-   Set *hwndParent* to **NULL**.

-   Set *Flags* to (DIGCF_DEVICEINTERFACE | DIGCF_DEFAULT).

This call will return a device information set that contains a device information element. The device information element that is returned represents the device that supports the default interface for the specified device interface class.

To set the default interface for a device interface class, call [**SetupDiSetDeviceInterfaceDefault**](https://msdn.microsoft.com/library/windows/hardware/ff552149) and supply the following parameters values:

-   Set *DeviceInfoSet* to a handle to the device information set that contains the device interface to set as the default for a device interface class.

-   Set *DeviceInterfaceData* to a pointer to an [**SP_DEVICE_INTERFACE_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552342) structure that specifies the device interface in *DeviceInfoSet*.

### <a href="" id="accessing-device-interface-class-properties-that-have-registry-entry-v"></a> Accessing Device Interface Class Properties That Have Registry Entry Values Under the Interface Class Registry Key

To access properties of a device interface class that have corresponding registry entry values under the interface class registry key, follow these steps:

1.  Call the [**SetupDiOpenClassRegKeyEx**](https://msdn.microsoft.com/library/windows/hardware/ff552067) function to open the interface class registry key and supply the following parameter values:

    -   Set *ClassGuid* to a pointer to the GUID that identifies the device interface class of the requested class registry key.
    -   Set *samDesired* to a REGSAM-typed value that specifies the required access permission.
    -   Set *Flags* to DIOCR_INTERFACE.
    -   Set *MachineName* to a pointer to a NULL-terminated string that contains the name of the computer on which to open the requested class registry key. If the computer is the local computer, set *MachineName* to **NULL**.
    -   Set *Reserved* to **NULL**.

    If this call to [**SetupDiOpenClassRegKeyEx**](https://msdn.microsoft.com/library/windows/hardware/ff552067) succeeds, **SetupDiOpenClassRegKeyEx** returns the requested handle. If the function call fails, **SetupDiOpenClassRegKeyEx** returns INVALID_HANDLE_VALUE and a call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the logged error code.

2.  Supply the retrieved handle in a call to [RegQueryValueEx](http://go.microsoft.com/fwlink/p/?linkid=95398) and [RegSetValueEx](http://go.microsoft.com/fwlink/p/?linkid=95399) to retrieve or set the registry entry value that corresponds to the device interface class property.

3.  Call the [RegCloseKey](http://go.microsoft.com/fwlink/p/?linkid=194543) function to close the class registry key after access to the key is no longer required.

For information about how to install and use device interfaces, see [Device Interface Classes](device-interface-classes.md) and [**INF AddInterface Directive**](inf-addinterface-directive.md).

 

 





