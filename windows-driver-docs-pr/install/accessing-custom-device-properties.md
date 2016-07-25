---
title: Accessing Custom Device Properties
description: Accessing Custom Device Properties
ms.assetid: 81170fd5-f1fb-4a06-a651-4651fc894070
---

# Accessing Custom Device Properties


In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) supports using [property keys](property-keys.md) to create and access custom device properties. For more information, see [Creating Custom Device Properties](creating-custom-device-properties.md).

On Windows Server 2003, Windows XP, and Windows 2000, you can create custom registry entry values under the system-supplied registry keys for a device-related component. The following list contains the SetupAPI function to call for each type of device component to open the corresponding system-supplied registry key. After you open the system-defined registry key, applications and installers can call the Windows-based registry functions to modify custom registry entry values under the open registry key.

-   A custom registry entry value for a device instance hardware property should be located under the hardware registry key of a device instance. Call [**SetupDiOpenDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552079) and supply DIREG\_DEV in the *Flags* parameter to retrieve a handle to the hardware key of a device instance. Custom registry entry values that are set under the hardware registry key for a device instance can be retrieved by calling the [**SetupDiGetCustomDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551099) function.

-   A custom registry entry value for a device instance software property should be located under the software registry key of a device instance. Call **SetupDiOpenDevRegKey** and supply DIREG\_DRV in the *Flags* parameter to retrieve a handle to the software key of a device instance.

-   A custom registry entry value for a [device setup class property](accessing-device-setup-class-properties.md) should be located under the device setup class registry key. Call [**SetupDiOpenClassRegKeyEx**](https://msdn.microsoft.com/library/windows/hardware/ff552067) and supply DIOCR\_INSTALLER in the *Flags* parameter to retrieve a handle to the registry key for a device setup class.

-   A custom registry entry value for a device interface class property should be located under the device interface class registry key. Call **SetupDiOpenClassRegKeyEx** and supply DIOCR\_INTERFACE in the *Flags* parameter to retrieve a handle to the registry key for a device interface class.

-   A custom registry entry value for a device interface property should be located under the device interface registry key. Call [**SetupDiOpenDeviceInterfaceRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552075) to retrieve a handle to the registry key for a device interface class.

After you retrieve a handle to a registry key, supply the handle in a call to [RegQueryValueEx](http://go.microsoft.com/fwlink/p/?linkid=95398) or [RegSetValueEx](http://go.microsoft.com/fwlink/p/?linkid=95399) to retrieve or set the custom registry entry value that corresponds to the custom device property.

Call the [RegCloseKey](http://go.microsoft.com/fwlink/p/?linkid=194543) function to close the registry key after access to the registry key is no longer required.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Accessing%20Custom%20Device%20Properties%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




