---
title: Accessing Device Driver Properties
description: Provides information about accessing device driver properties.
ms.date: 08/15/2022
---

# Accessing device driver properties

In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) includes device driver properties that characterize a device driver. The unified device property model uses [property keys](property-keys.md) to represent these properties.

Windows Server 2003, Windows XP, and Windows 2000 also support most of these device driver properties. However, these earlier versions of Windows do not support the property keys of the unified device property model. Instead, these versions of Windows use the following mechanisms to represent and access the corresponding property information:

- [Accessing Device Driver Properties That Have Corresponding Registry Entry Values](#accessing-device-driver-properties-that-have-corresponding-registry-entry-values)
- [Using SetupDiGetDriverInstallParams to Retrieve Driver Rank](#using-setupdigetdriverinstallparams-to-retrieve-driver-rank)

To maintain compatibility with these earlier versions of Windows, Windows Vista and later versions also support these two ways to access information about a device interface. However, you should use the property keys to access these properties on Windows Vista and later versions. For information about how to use property keys to access device driver properties on Windows Vista and later versions, see [Accessing Device Instance Properties (Windows Vista and Later)](accessing-device-instance-properties--windows-vista-and-later-.md).

## Accessing device driver properties that have corresponding registry entry values

To access device driver properties on Windows Server 2003, Windows XP, and Windows 2000, follow these steps:

1. Retrieve a handle to the software key for a device instance by calling [**CM_Open_DevNode_Key**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_open_devnode_key) with a *ulFlags* of CM_REGISTRY_SOFTWARE or [**SetupDiOpenDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendevregkey) with a *Scope* of DICS_FLAG_GLOBAL and a *KeyType* of DIREG_DRV.

1. Supply the handle in a call to [RegQueryValueEx](/windows/win32/api/winreg/nf-winreg-regqueryvalueexa) or to [RegSetValueEx](/windows/win32/api/winreg/nf-winreg-regsetvalueexa) to retrieve or set the registry entry value that corresponds to the device instance driver property.

1. Call the [RegCloseKey](/windows/win32/api/winreg/nf-winreg-regclosekey) function to close the software registry key after access to the key is no longer required.

A table of unified device property model properties and their corresponding registry values in the software key for a device is:

| Unified property model property | Software key registry value name (defined in *regstr.h*) |
|--|--|
| [**DEVPKEY_Device_DriverDate**](devpkey-device-driverdate.md) | REGSTR_VAL_DRIVERDATEDATA |
| [**DEVPKEY_Device_DriverVersion**](devpkey-device-driverversion.md) | REGSTR_VAL_DRIVERVERSION |
| [**DEVPKEY_Device_DriverDesc**](devpkey-device-driverdesc.md) | REGSTR_VAL_DRVDESC |
| [**DEVPKEY_Device_DriverInfPath**](devpkey-device-driverinfpath.md) | REGSTR_VAL_INFPATH |
| [**DEVPKEY_Device_DriverInfSection**](devpkey-device-driverinfsection.md) | REGSTR_VAL_INFSECTION |
| [**DEVPKEY_Device_DriverInfSectionExt**](devpkey-device-driverinfsectionext.md) | REGSTR_VAL_INFSECTIONEXT |
| [**DEVPKEY_Device_DriverProvider**](devpkey-device-driverprovider.md) | REGSTR_VAL_PROVIDER_NAME |

## Using SetupDiGetDriverInstallParams to retrieve driver rank

On Windows Server 2003, Windows XP, and Windows 2000, you can retrieve the rank of a driver that is currently installed for a device by calling [**SetupDiGetDriverInstallParams**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdriverinstallparamsa). **SetupDiGetDriverInstallParams** retrieves a pointer to an [**SP_DRVINSTALL_PARAMS**](/windows/win32/api/setupapi/ns-setupapi-sp_drvinstall_params) structure for the driver in the output parameter *DriverInstallParams*. The **Rank** member of the retrieved SP_DRVINSTALL_PARAMS structure contains the driver rank.
