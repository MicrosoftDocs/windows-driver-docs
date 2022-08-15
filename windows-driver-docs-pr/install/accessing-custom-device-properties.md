---
title: Accessing Custom Settings
description: Accessing Custom Device Settings
ms.date: 04/05/2022
---

# Accessing Custom Settings

In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) supports using [property keys](property-keys.md) to create and access custom device properties. For more information, see [Creating Custom Device Properties](creating-custom-device-properties.md).

On Windows Server 2003, Windows XP, and Windows 2000, you can create custom registry entry values under the system-supplied registry keys for a device-related component. The following list contains the SetupAPI function to call for each type of device component to open the corresponding system-supplied registry key. After you open the system-defined registry key, applications and installers can call the Windows-based registry functions to modify custom registry entry values under the open registry key.

-   A custom registry entry value for a device instance hardware property should be located under the hardware registry key of a device instance. Call [**SetupDiOpenDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendevregkey) and supply DIREG_DEV in the *Flags* parameter to retrieve a handle to the hardware key of a device instance. Custom registry entry values that are set under the hardware registry key for a device instance can be retrieved by calling the [**SetupDiGetCustomDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetcustomdevicepropertya) function.

-   A custom registry entry value for a device instance software property should be located under the software registry key of a device instance. Call **SetupDiOpenDevRegKey** and supply DIREG_DRV in the *Flags* parameter to retrieve a handle to the software key of a device instance.

-   A custom registry entry value for a [device setup class property](accessing-device-setup-class-properties.md) should be located under the device setup class registry key. Call [**SetupDiOpenClassRegKeyEx**](/windows/win32/api/setupapi/nf-setupapi-setupdiopenclassregkeyexa) and supply DIOCR_INSTALLER in the *Flags* parameter to retrieve a handle to the registry key for a device setup class.

-   A custom registry entry value for a device interface class property should be located under the device interface class registry key. Call **SetupDiOpenClassRegKeyEx** and supply DIOCR_INTERFACE in the *Flags* parameter to retrieve a handle to the registry key for a device interface class.

-   A custom registry entry value for a device interface property should be located under the device interface registry key. Call [**SetupDiOpenDeviceInterfaceRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendeviceinterfaceregkey) to retrieve a handle to the registry key for a device interface class.

After you retrieve a handle to a registry key, supply the handle in a call to [RegQueryValueEx](/windows/win32/api/winreg/nf-winreg-regqueryvalueexa) or [RegSetValueEx](/windows/win32/api/winreg/nf-winreg-regsetvalueexa) to retrieve or set the custom registry entry value that corresponds to the custom device property.

Call the [RegCloseKey](/windows/win32/api/winreg/nf-winreg-regclosekey) function to close the registry key after access to the registry key is no longer required.
