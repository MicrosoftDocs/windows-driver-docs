---
title: Accessing Device Interface Properties
description: Accessing Device Interface Properties
ms.assetid: 48b47d01-ec07-49ca-a03c-c4c387dcfb19
---

# Accessing Device Interface Properties


In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) includes device interface properties that characterize a device interface. The unified device property model uses [property keys](property-keys.md) to represent these properties.

Windows Server 2003, Windows XP, and Windows 2000 support most of these device interface class properties. However, these earlier versions of Windows do not support the property keys of the unified device property model. Instead, these versions of Windows use the following mechanisms to represent and access device interface properties:

-   [Accessing Device Interface Properties That Have Corresponding Registry Entry Values](#accessing-device-interface-properties-that-have-corresponding-registry)

-   [Using SetupDiEnumDeviceInterfaces to Retrieve Information About a Device Interface](#using-setupdienumdeviceinterfaces-to-retrieve-information-about-a-devi).

To maintain compatibility with these earlier versions of Windows, Windows Vista and later versions also support these two ways to access information about a device interface. However, you should use the property keys to access these properties in Windows Vista and later versions.

For a list of the system-defined device interface class properties, see [Device Interface Properties](https://msdn.microsoft.com/library/windows/hardware/ff541409). The device interface class properties are listed by their corresponding property keys that you use to access the properties in Windows Vista and later versions. The information that is provided with the property keys includes the corresponding registry entry values, if any, that you can use to access the properties on Windows Server 2003, Windows XP, and Windows 2000.

For information about how to use property keys to access device setup class properties in Windows Vista and later versions, see [Accessing Device Interface Properties (Windows Vista and Later)](accessing-device-interface-properties--windows-vista-and-later-.md).

For information about how to install and use device interfaces, see [Device Interface Classes](device-interface-classes.md) and [**INF AddInterface Directive**](inf-addinterface-directive.md).

### <a href="" id="accessing-device-interface-properties-that-have-corresponding-registry"></a> Accessing Device Interface Properties That Have Corresponding Registry Entry Values

To access device interface properties by using registry entry values on Windows Server 2003, Windows XP, and Windows 2000, first call [**SetupDiOpenDeviceInterfaceRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552075)and supply the following parameters:

-   Set *DeviceInfoSet* to a pointer to a device information set that contains the device interface.

-   Set *DeviceInterfaceData* to a pointer to an [**SP\_DEVICE\_INTERFACE\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552342) structure that identifies the device interface.

-   Set *Reserved* to zero.

-   Set *samDesired* to a REGSAM-typed value that specifies the required access permissions.

If this call to [**SetupDiOpenDeviceInterfaceRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552075) succeeds, **SetupDiOpenDeviceInterfaceRegKey** returns the requested handle. If the function call fails, **SetupDiOpenDeviceInterfaceRegKey** returns INVALID\_HANDLE\_VALUE and a call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the logged error code.

After you retrieve a handle to the device interface registry key, supply the handle in a call to [RegQueryValueEx](http://go.microsoft.com/fwlink/p/?linkid=95398) or [RegSetValueEx](http://go.microsoft.com/fwlink/p/?linkid=95399) to retrieve or set the registry entry value that corresponds to the device interface property.

Call the [RegCloseKey](http://go.microsoft.com/fwlink/p/?linkid=194543) function to close the class registry key after access to the key is no longer required.

### <a href="" id="using-setupdienumdeviceinterfaces-to-retrieve-information-about-a-devi"></a> Using SetupDiEnumDeviceInterfaces to Retrieve Information About a Device Interface

Another way to retrieve information about a device interface on Windows Server 2003, Windows XP, and Windows 2000 is by calling [**SetupDiEnumDeviceInterfaces**](https://msdn.microsoft.com/library/windows/hardware/ff551015) to retrieve an [**SP\_DEVICE\_INTERFACE\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552342) structure for the interface. An SP\_DEVICE\_INTERFACE\_DATA structure contains the following information:

-   The **Flags** member indicates whether a device interface is active or removed, and whether the device is the default interface for the interface class.

-   The **InterfaceClassGuild** member identifies the interface class GUID.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Accessing%20Device%20Interface%20Properties%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




