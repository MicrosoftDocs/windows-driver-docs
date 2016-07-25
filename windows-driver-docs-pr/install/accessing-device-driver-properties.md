---
title: Accessing Device Driver Properties
description: Accessing Device Driver Properties
ms.assetid: 433ad114-46aa-470b-b529-e6b6fb7f6bd7
---

# Accessing Device Driver Properties


In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) includes device driver properties that characterize a device driver. The unified device property model uses [property keys](property-keys.md) to represent these properties.

Windows Server 2003, Windows XP, and Windows 2000 also support most of these device driver properties. However, these earlier versions of Windows do not support the property keys of the unified device property model. Instead, these versions of Windows use the following mechanisms to represent and access the corresponding property information:

-   [Accessing Device Driver Properties That Have Corresponding Registry Entry Values](#accessing-device-driver-properties-that-have-corresponding-registry-en)
-   [Using SetupDiGetDriverInstallParams to Retrieve Driver Rank](#using-setupdigetdriverinstallparams-to-retrieve-driver-rank)

To maintain compatibility with these earlier versions of Windows, Windows Vista and later versions also support these two ways to access information about a device interface. However, you should use the property keys to access these properties on Windows Vista and later versions.

For a list of the system-defined device driver properties, see [Device Driver Properties](https://msdn.microsoft.com/library/windows/hardware/ff541205). The device driver properties are listed by the property key identifiers that you use to access the properties on Windows Vista and later versions. The information that is provided with the property keys includes the names of the corresponding system-defined registry entry values that you can use to access the property on Windows Server 2003, Windows XP, and Windows 2000.

For information about how to use property keys to access device driver properties on Windows Vista and later versions, see [Accessing Device Instance Properties (Windows Vista and Later)](accessing-device-instance-properties--windows-vista-and-later-.md).

### <a href="" id="accessing-device-driver-properties-that-have-corresponding-registry-en"></a> Accessing Device Driver Properties That Have Corresponding Registry Entry Values

To access device driver properties on Windows Server 2003, Windows XP, and Windows 2000, follow these steps:

1.  Call [**SetupDiOpenDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552079) to retrieve a handle to the software key for a device instance. Supply the following parameter values:

    -   Set *DeviceInfoSet* to a handle to the device information set that contains the device information element for which to retrieve the global software key.
    -   Set *DeviceInfoData* to a pointer to an [**SP\_DEVINFO\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure that represents the device information element for which to retrieve the global software key.
    -   Set *Scope* to DICS\_FLAG\_GLOBAL.
    -   Set *HwProfile* to zero.
    -   Set *KeyType* to DIREG\_DRV, which configures **SetupDiOpenDevRegKey** to retrieve a handle to the software key for a device instance.
    -   Set *samDesired* to a REGSAM-typed value that specifies the access that you require for this key. For all access, set *samDesired* to KEY\_ALL\_ACCESS.

    If the call to [**SetupDiOpenDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552079) succeeds, **SetupDiOpenDevRegKey** returns a handle to the requested software key. If the function call fails, **SetupDiOpenDevRegKey** returns INVALID\_HANDLE\_VALUE. A subsequent call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the most recently logged error code.

2.  Supply the handle in a call to [RegQueryValueEx](http://go.microsoft.com/fwlink/p/?linkid=95398) or to [RegSetValueEx](http://go.microsoft.com/fwlink/p/?linkid=95399) to retrieve or set the registry entry value that corresponds to the device instance driver property.

3.  Call the [RegCloseKey](http://go.microsoft.com/fwlink/p/?linkid=194543) function to close the software registry key after access to the key is no longer required.

### <a href="" id="using-setupdigetdriverinstallparams-to-retrieve-driver-rank"></a> Using SetupDiGetDriverInstallParams to Retrieve Driver Rank

On Windows Server 2003, Windows XP, and Windows 2000, you can retrieve the rank of a driver that is currently installed for a device by calling [**SetupDiGetDriverInstallParams**](https://msdn.microsoft.com/library/windows/hardware/ff551978). **SetupDiGetDriverInstallParams** retrieves a pointer to an [**SP\_DRVINSTALL\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff553290) structure for the driver in the output parameter *DriverInstallParams*. The **Rank** member of the retrieved SP\_DRVINSTALL\_PARAMS structure contains the driver rank.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Accessing%20Device%20Driver%20Properties%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




