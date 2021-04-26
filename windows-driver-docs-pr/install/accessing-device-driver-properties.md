---
title: Accessing Device Driver Properties
description: Accessing Device Driver Properties
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing Device Driver Properties


In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) includes device driver properties that characterize a device driver. The unified device property model uses [property keys](property-keys.md) to represent these properties.

Windows Server 2003, Windows XP, and Windows 2000 also support most of these device driver properties. However, these earlier versions of Windows do not support the property keys of the unified device property model. Instead, these versions of Windows use the following mechanisms to represent and access the corresponding property information:

-   [Accessing Device Driver Properties That Have Corresponding Registry Entry Values](#accessing-device-driver-properties-that-have-corresponding-registry-en)
-   [Using SetupDiGetDriverInstallParams to Retrieve Driver Rank](#using-setupdigetdriverinstallparams-to-retrieve-driver-rank)

To maintain compatibility with these earlier versions of Windows, Windows Vista and later versions also support these two ways to access information about a device interface. However, you should use the property keys to access these properties on Windows Vista and later versions.

For a list of the system-defined device driver properties, see [Device Driver Properties](/previous-versions/ff541205(v=vs.85)). The device driver properties are listed by the property key identifiers that you use to access the properties on Windows Vista and later versions. The information that is provided with the property keys includes the names of the corresponding system-defined registry entry values that you can use to access the property on Windows Server 2003, Windows XP, and Windows 2000.

For information about how to use property keys to access device driver properties on Windows Vista and later versions, see [Accessing Device Instance Properties (Windows Vista and Later)](accessing-device-instance-properties--windows-vista-and-later-.md).

### <a href="" id="accessing-device-driver-properties-that-have-corresponding-registry-en"></a> Accessing Device Driver Properties That Have Corresponding Registry Entry Values

To access device driver properties on Windows Server 2003, Windows XP, and Windows 2000, follow these steps:

1.  Call [**SetupDiOpenDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendevregkey) to retrieve a handle to the software key for a device instance. Supply the following parameter values:

    -   Set *DeviceInfoSet* to a handle to the device information set that contains the device information element for which to retrieve the global software key.
    -   Set *DeviceInfoData* to a pointer to an [**SP_DEVINFO_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_devinfo_data) structure that represents the device information element for which to retrieve the global software key.
    -   Set *Scope* to DICS_FLAG_GLOBAL.
    -   Set *HwProfile* to zero.
    -   Set *KeyType* to DIREG_DRV, which configures **SetupDiOpenDevRegKey** to retrieve a handle to the software key for a device instance.
    -   Set *samDesired* to a REGSAM-typed value that specifies the access that you require for this key. For all access, set *samDesired* to KEY_ALL_ACCESS.

    If the call to [**SetupDiOpenDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendevregkey) succeeds, **SetupDiOpenDevRegKey** returns a handle to the requested software key. If the function call fails, **SetupDiOpenDevRegKey** returns INVALID_HANDLE_VALUE. A subsequent call to [GetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) will return the most recently logged error code.

2.  Supply the handle in a call to [RegQueryValueEx](/windows/win32/api/winreg/nf-winreg-regqueryvalueexa) or to [RegSetValueEx](/windows/win32/api/winreg/nf-winreg-regsetvalueexa) to retrieve or set the registry entry value that corresponds to the device instance driver property.

3.  Call the [RegCloseKey](/windows/win32/api/winreg/nf-winreg-regclosekey) function to close the software registry key after access to the key is no longer required.

### <a href="" id="using-setupdigetdriverinstallparams-to-retrieve-driver-rank"></a> Using SetupDiGetDriverInstallParams to Retrieve Driver Rank

On Windows Server 2003, Windows XP, and Windows 2000, you can retrieve the rank of a driver that is currently installed for a device by calling [**SetupDiGetDriverInstallParams**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdriverinstallparamsa). **SetupDiGetDriverInstallParams** retrieves a pointer to an [**SP_DRVINSTALL_PARAMS**](/windows/win32/api/setupapi/ns-setupapi-sp_drvinstall_params) structure for the driver in the output parameter *DriverInstallParams*. The **Rank** member of the retrieved SP_DRVINSTALL_PARAMS structure contains the driver rank.

