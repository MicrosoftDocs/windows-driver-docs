---
title: InstallSelectedDriver function
description: The InstallSelectedDriver function installs a selected driver on a selected device.
ms.assetid: 8a27f4bb-6d1e-4fe8-810f-23513418254d
keywords: ["InstallSelectedDriver function Device and Driver Installation"]
topic_type:
- apiref
api_name:
- InstallSelectedDriver
api_location:
- Newdev.dll
api_type:
- DllExport
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# InstallSelectedDriver function


The **InstallSelectedDriver** function is deprecated. For Windows Vista and later, use [**DiInstallDevice**](https://msdn.microsoft.com/library/windows/hardware/ff544710) instead.

Syntax
------

```ManagedCPlusPlus
BOOL WINAPI InstallSelectedDriver(
  _In_  HWND     hwndParent,
  _In_  HDEVINFO DeviceInfoSet,
  _In_  LPCTSTR  Reserved,
  _In_  BOOL     Backup,
  _Out_ PDWORD   bReboot
);
```

Parameters
----------

*hwndParent* \[in\]  
A handle to the top-level window that the **InstallSelectedDriver** function uses to display user interface components that are associated with installing the driver.

*DeviceInfoSet* \[in\]  
A handle to a [device information set](https://msdn.microsoft.com/library/windows/hardware/ff541247) that contains a device information element that represents a selected device and a selected driver for the device. For more information about how to select a device and a driver for a device, see the following **Remarks** section.

*Reserved* \[in\]  
This parameter must be set to **NULL**.

*Backup* \[in\]  
A value of type BOOL that determines whether **InstallSelectedDriver** backs up the currently installed drivers for the selected device before the function installs the selected driver for the device. If the currently installed drivers are backed up and the user encounters a problem with the new driver, the user can roll back the installation of the new driver to the backed up driver. If the currently installed drivers are not backed up, the user cannot roll back the installation of the new driver to the previously installed driver. If *Backup* is set to **TRUE**, **InstallSelectedDriver** backs up the currently installed drivers; otherwise, the function does not back up the currently installed drivers. For more information about driver back up, see **DiRollbackDriver**.

*bReboot* \[out\]  
A pointer to a variable of type DWORD that **InstallSelectedDriver** sets to indicate whether a system restart is required to complete the installation. If the variable is set to DI\_NEEDREBOOT, a system restart is required; otherwise, a system restart is not required. The caller is responsible for restarting the system.

Return value
------------

**InstallSelectedDriver** returns **TRUE** if the selected driver was installed on the selected device; otherwise, the function returns **FALSE** and the logged error can be retrieved by making a call to **GetLastError**.

Some of the more common error values that **GetLastError** might return are as follows:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Return code</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>NO_ERROR</strong></td>
<td align="left"><p>The selected driver was a better match to the driver than the driver that was previously installed on the device.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>ERROR_IN_WOW64</strong></td>
<td align="left"><p>The calling application is a 32-bit application that is attempting to execute in a 64-bit environment, which is not allowed. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541255" data-raw-source="[Installing Devices on 64-Bit Systems](https://msdn.microsoft.com/library/windows/hardware/ff541255)">Installing Devices on 64-Bit Systems</a>.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

To access **InstallSelectedDriver**, call **LoadLibrary** to load *Newdev.dll* and then call **GetProcAddress** to obtain a function pointer to **InstallSelectedDriver**.

You should only call **InstallSelectedDriver** if it is necessary to install a specific driver on a specific device.

**Important**   For Windows Vista and later versions of Windows, call [**DiInstallDevice**](https://msdn.microsoft.com/library/windows/hardware/ff544710) instead of **InstallSelectedDriver** to perform this type of operation.

 

Other than the special applications that require the installation of a specific driver on a specific device, an installation application should install the driver that is the best match for a device. To install the driver that is the best match for a device, call [**DiInstallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff544717) or [**UpdateDriverForPlugAndPlayDevices**](https://msdn.microsoft.com/library/windows/hardware/ff553534). For more information about which of these functions to call to install a driver on a device, see [SetupAPI Functions that Simplify Driver Installation](https://msdn.microsoft.com/library/windows/hardware/ff550867).

Before calling **InstallSelectedDriver**, the caller must obtain a device information set that contains the device, select the device in the set, and select a driver for the device.

To create a device information set that contains the device, do one of the following:

-   Call [**SetupDiGetClassDevs**](https://msdn.microsoft.com/library/windows/hardware/ff551069) to retrieve a device information set that contains the device and then call [**SetupDiEnumDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff551010) to enumerate the devices in the device information set. On each call, **SetupDiEnumDeviceInfo** returns an SP\_DEVINFO\_DATA structure that represents the enumerated device in the device information set. To obtain specific information about the enumerated device, call [**SetupDiGetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551967) and supply the SP\_DEVINFO\_DATA structure that was returned by **SetupDiEnumDeviceInfo**.

    - OR -

-   Call [**SetupDiOpenDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff552071) to add a device with a known device instance ID to the device information set. **SetupDiOpenDeviceInfo** returns an [**SP\_DEVINFO\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure that represents the device in the device information set.

After obtaining the SP\_DEVINFO\_DATA structure for a device, call [**SetupDiSetSelectedDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552176) to select the device in the device information set.

To retrieve a driver for a device, call [**SetupDiBuildDriverInfoList**](https://msdn.microsoft.com/library/windows/hardware/ff550917) to build a list of compatible drivers for the device and then call [**SetupDiEnumDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff551018) to enumerate the elements of the driver list for the device. For each enumerated driver, **SetupDiEnumDriverInfo** retrieves an SP\_DRVINFO\_DATA structure that represents the driver. [**SetupDiGetDriverInfoDetail**](https://msdn.microsoft.com/library/windows/hardware/ff551973) can be called to retrieve additional details about an enumerated driver.

After obtaining an SP\_DRVINFO\_DATA structure for the driver, call [**SetupDiSetSelectedDriver**](https://msdn.microsoft.com/library/windows/hardware/ff552183) to select the driver for the device.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Microsoft Windows 2000 and later versions of Windows.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">None (The <strong>InstallSelectedDriver</strong> function is not defined in a public header file. For more information, see the <strong>Remarks</strong> section. )</td>
</tr>
<tr class="even">
<td align="left"><p>Library</p></td>
<td align="left">Newdev.lib</td>
</tr>
<tr class="odd">
<td align="left"><p>DLL</p></td>
<td align="left">Newdev.dll</td>
</tr>
</tbody>
</table>

## See also


[**DiInstallDevice**](https://msdn.microsoft.com/library/windows/hardware/ff544710)

[**DiInstallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff544717)

[**SetupDiBuildDriverInfoList**](https://msdn.microsoft.com/library/windows/hardware/ff550917)

[**SetupDiEnumDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff551010)

[**SetupDiEnumDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff551018)

[**SetupDiGetClassDevs**](https://msdn.microsoft.com/library/windows/hardware/ff551069)

[**SetupDiGetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551967)

[**SetupDiGetDriverInfoDetail**](https://msdn.microsoft.com/library/windows/hardware/ff551973)

[**SetupDiOpenDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff552071)

[**SetupDiSetSelectedDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552176)

[**SetupDiSetSelectedDriver**](https://msdn.microsoft.com/library/windows/hardware/ff552183)

[**UpdateDriverForPlugAndPlayDevices**](https://msdn.microsoft.com/library/windows/hardware/ff553534)

 

 






