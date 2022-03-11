---
title: Using Device Installation Functions
description: Using Device Installation Functions
keywords:
- SetupAPI functions WDK , device installation functions
- device installation functions WDK SetupAPI
ms.date: 03/11/2022
---

# Using Device Installation Functions

This section summarizes the [device installation functions](/previous-versions/ff541299(v=vs.85)). By using the device installation functions, the installation software can perform the following types of operations:

-   Install drivers

-   Handle DIF codes.

-   Manage device information sets.

-   Manage driver lists.

-   Manage device interfaces.

-   Manage icons and other bitmaps.

The following tables provide summaries of the following types of functions:

[Driver Installation Functions](#ddk-update-driver-function-dg)

[Device Information Functions](#ddk-setupdi-device-information-functions-dg)

[Driver Information Functions](#ddk-setupdi-driver-information-functions-dg)

[Device Installation Handlers](#ddk-setupdi-device-installation-handlers-dg)

[Device Installation Customization Functions](#ddk-setupdi-device-installation-customization-functions-dg)

[Setup Class Functions](#ddk-setupdi-setup-class-functions-dg)

[Bitmap and Icon Functions](#ddk-setupdi-class-bitmap-and-icon-functions-dg)

[Device Interface Functions](#ddk-setupdi-device-interface-functions-dg)

[Device Property Functions (Windows Vista and Later)](#ddk-setupdi-device-property-functions-dg)

[Registry Functions](#ddk-setupdi-registry-functions-dg)

[Other Functions](#ddk-other-setupdi-functions-dg)

### <a href="" id="ddk-update-driver-function-dg"></a>Driver Installation Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/newdev/nf-newdev-diinstalldevice" data-raw-source="[&lt;strong&gt;DiInstallDevice&lt;/strong&gt;](/windows/win32/api/newdev/nf-newdev-diinstalldevice)"><strong>DiInstallDevice</strong></a></p></td>
<td align="left"><p>Installs a specified driver package that is preinstalled in the <a href="driver-store.md" data-raw-source="[driver store](driver-store.md)">driver store</a> on a PnP device that is present in the system. (Windows Vista and later versions of Windows)</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/newdev/nf-newdev-diuninstalldevice" data-raw-source="[&lt;strong&gt;DiUninstallDevice&lt;/strong&gt;](/windows/win32/api/newdev/nf-newdev-diuninstalldevice)"><strong>DiUninstallDevice</strong></a></p></td>
<td align="left"><p>Uninstalls a device and removes its device node (<a href="/windows-hardware/drivers/#wdkgloss-devnode" data-raw-source="&lt;em&gt;devnode&lt;/em&gt;"><em>devnode</em></a>) from the system. (Windows 7 and later versions of Windows)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/newdev/nf-newdev-diinstalldriverw" data-raw-source="[&lt;strong&gt;DiInstallDriver&lt;/strong&gt;](/windows/win32/api/newdev/nf-newdev-diinstalldriverw)"><strong>DiInstallDriver</strong></a></p></td>
<td align="left"><p>Preinstalls a driver package in the driver store and then installs the driver package on matching PnP devices that are present in the system. (Windows Vista and later versions of Windows)</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/newdev/nf-newdev-diuninstalldriverw" data-raw-source="[&lt;strong&gt;DiUninstallDriver&lt;/strong&gt;](/windows/win32/api/newdev/nf-newdev-diuninstalldriverw)"><strong>DiUninstallDriver</strong></a></p></td>
<td align="left"><p>Removes a driver package from the Driver Store. (Windows 10 Version 1703 and later versions of Windows)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/newdev/nf-newdev-updatedriverforplugandplaydevicesa" data-raw-source="[&lt;strong&gt;UpdateDriverForPlugAndPlayDevices&lt;/strong&gt;](/windows/win32/api/newdev/nf-newdev-updatedriverforplugandplaydevicesa)"><strong>UpdateDriverForPlugAndPlayDevices</strong></a></p></td>
<td align="left"><p>Updates the driver package that is installed for matching PnP devices that are present in the system.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/newdev/nf-newdev-dirollbackdriver" data-raw-source="[&lt;strong&gt;DiRollbackDriver&lt;/strong&gt;](/windows/win32/api/newdev/nf-newdev-dirollbackdriver)"><strong>DiRollbackDriver</strong></a></p></td>
<td align="left"><p>Rolls back the driver package that is installed on a specified device to the backup driver package set for the device. (Windows Vista and later versions of Windows)</p></td>
</tr>
</tbody>
</table>

### <a href="" id="ddk-setupdi-device-information-functions-dg"></a>Device Information Functions

> [!NOTE]
> SetupApi is not supported on all editions of Windows.  When possible, you should use lower layer APIs such as those available via [CfgMgr32.dll](/windows/win32/api/cfgmgr32/).  See [Porting from SetupApi to CfgMgr32](porting-from-setupapi-to-cfgmgr32.md) for tips.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdicreatedeviceinfolist" data-raw-source="[&lt;strong&gt;SetupDiCreateDeviceInfoList&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdicreatedeviceinfolist)"><strong>SetupDiCreateDeviceInfoList</strong></a></p></td>
<td align="left"><p>Creates an empty <a href="device-information-sets.md" data-raw-source="[device information set](device-information-sets.md)">device information set</a>. This set can be associated with a class GUID.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdicreatedeviceinfolistexa" data-raw-source="[&lt;strong&gt;SetupDiCreateDeviceInfoListEx&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdicreatedeviceinfolistexa)"><strong>SetupDiCreateDeviceInfoListEx</strong></a></p></td>
<td align="left"><p>Creates an empty device information set. This set can be associated with a class GUID and can be for devices on a remote computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdicreatedeviceinfoa" data-raw-source="[&lt;strong&gt;SetupDiCreateDeviceInfo&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdicreatedeviceinfoa)"><strong>SetupDiCreateDeviceInfo</strong></a></p></td>
<td align="left"><p>Creates a new device information element and adds it as a new member to the specified device information set.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiopendeviceinfoa" data-raw-source="[&lt;strong&gt;SetupDiOpenDeviceInfo&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiopendeviceinfoa)"><strong>SetupDiOpenDeviceInfo</strong></a></p></td>
<td align="left"><p>Retrieves information about an existing device instance and adds it to the specified device information set.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdienumdeviceinfo" data-raw-source="[&lt;strong&gt;SetupDiEnumDeviceInfo&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdienumdeviceinfo)"><strong>SetupDiEnumDeviceInfo</strong></a></p></td>
<td align="left"><p>Returns a context structure for a device information element of a device information set.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinstanceida" data-raw-source="[&lt;strong&gt;SetupDiGetDeviceInstanceId&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinstanceida)"><strong>SetupDiGetDeviceInstanceId</strong></a></p></td>
<td align="left"><p>Retrieves the device instance ID associated with a device information element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinfolistclass" data-raw-source="[&lt;strong&gt;SetupDiGetDeviceInfoListClass&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinfolistclass)"><strong>SetupDiGetDeviceInfoListClass</strong></a></p></td>
<td align="left"><p>Retrieves the class GUID associated with a device information set if it has an associated class.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinfolistdetaila" data-raw-source="[&lt;strong&gt;SetupDiGetDeviceInfoListDetail&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinfolistdetaila)"><strong>SetupDiGetDeviceInfoListDetail</strong></a></p></td>
<td align="left"><p>Retrieves information associated with a device information set including the class GUID, remote computer handle, and remote computer name.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevpropertysheetsa" data-raw-source="[&lt;strong&gt;SetupDiGetClassDevPropertySheets&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevpropertysheetsa)"><strong>SetupDiGetClassDevPropertySheets</strong></a></p></td>
<td align="left"><p>Retrieves handles to the property sheets of a specified device information element or of the <a href="/windows-hardware/drivers/install/overview-of-device-setup-classes" data-raw-source="[device setup class](./overview-of-device-setup-classes.md)">device setup class</a> of a specified device information set.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsw" data-raw-source="[&lt;strong&gt;SetupDiGetClassDevs&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsw)"><strong>SetupDiGetClassDevs</strong></a></p></td>
<td align="left"><p>Returns a device information set that contains all devices of a specified class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsexa" data-raw-source="[&lt;strong&gt;SetupDiGetClassDevsEx&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsexa)"><strong>SetupDiGetClassDevsEx</strong></a></p></td>
<td align="left"><p>Returns a device information set that contains all devices of a specified class on a local or remote computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdisetselecteddevice" data-raw-source="[&lt;strong&gt;SetupDiSetSelectedDevice&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdisetselecteddevice)"><strong>SetupDiSetSelectedDevice</strong></a></p></td>
<td align="left"><p>Sets the specified device information element to be the currently-selected member of a device information set. This function is typically used by an installation wizard.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetselecteddevice" data-raw-source="[&lt;strong&gt;SetupDiGetSelectedDevice&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetselecteddevice)"><strong>SetupDiGetSelectedDevice</strong></a></p></td>
<td align="left"><p>Retrieves the currently-selected device for the specified device information set.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiregisterdeviceinfo" data-raw-source="[&lt;strong&gt;SetupDiRegisterDeviceInfo&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiregisterdeviceinfo)"><strong>SetupDiRegisterDeviceInfo</strong></a></p></td>
<td align="left"><p>Registers a newly created device instance with the Plug and Play manager.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdideletedeviceinfo" data-raw-source="[&lt;strong&gt;SetupDiDeleteDeviceInfo&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdideletedeviceinfo)"><strong>SetupDiDeleteDeviceInfo</strong></a></p></td>
<td align="left"><p>Deletes a member from the specified device information set. This function does not delete the actual device.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdidestroydeviceinfolist" data-raw-source="[&lt;strong&gt;SetupDiDestroyDeviceInfoList&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdidestroydeviceinfolist)"><strong>SetupDiDestroyDeviceInfoList</strong></a></p></td>
<td align="left"><p>Destroys a device information set and frees all associated memory.</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="ddk-setupdi-driver-information-functions-dg"></a>Driver Information Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdibuilddriverinfolist" data-raw-source="[&lt;strong&gt;SetupDiBuildDriverInfoList&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdibuilddriverinfolist)"><strong>SetupDiBuildDriverInfoList</strong></a></p></td>
<td align="left"><p>Builds a list of drivers associated with a specified device instance or with the device information set's global class driver list.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdienumdriverinfoa" data-raw-source="[&lt;strong&gt;SetupDiEnumDriverInfo&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdienumdriverinfoa)"><strong>SetupDiEnumDriverInfo</strong></a></p></td>
<td align="left"><p>Enumerates the members of a driver information list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetdriverinfodetaila" data-raw-source="[&lt;strong&gt;SetupDiGetDriverInfoDetail&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetdriverinfodetaila)"><strong>SetupDiGetDriverInfoDetail</strong></a></p></td>
<td align="left"><p>Retrieves detailed information for a specified driver information element.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdisetselecteddrivera" data-raw-source="[&lt;strong&gt;SetupDiSetSelectedDriver&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdisetselecteddrivera)"><strong>SetupDiSetSelectedDriver</strong></a></p></td>
<td align="left"><p>Sets the specified member of a driver list as the currently selected-driver. It can also be used to reset the driver list so that there is no currently-selected driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetselecteddrivera" data-raw-source="[&lt;strong&gt;SetupDiGetSelectedDriver&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetselecteddrivera)"><strong>SetupDiGetSelectedDriver</strong></a></p></td>
<td align="left"><p>Retrieves the member of a driver list that was selected as the driver to install.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdicanceldriverinfosearch" data-raw-source="[&lt;strong&gt;SetupDiCancelDriverInfoSearch&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdicanceldriverinfosearch)"><strong>SetupDiCancelDriverInfoSearch</strong></a></p></td>
<td align="left"><p>Cancels a driver list search that is currently underway in a different thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdidestroydriverinfolist" data-raw-source="[&lt;strong&gt;SetupDiDestroyDriverInfoList&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdidestroydriverinfolist)"><strong>SetupDiDestroyDriverInfoList</strong></a></p></td>
<td align="left"><p>Destroys a driver information list.</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="ddk-setupdi-device-installation-handlers-dg"></a>Device Installation Handlers

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdicallclassinstaller" data-raw-source="[&lt;strong&gt;SetupDiCallClassInstaller&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdicallclassinstaller)"><strong>SetupDiCallClassInstaller</strong></a></p></td>
<td align="left"><p>Calls the appropriate class installer, and any registered co-installers, with the specified installation request.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdichangestate" data-raw-source="[&lt;strong&gt;SetupDiChangeState&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdichangestate)"><strong>SetupDiChangeState</strong></a></p></td>
<td align="left"><p>The default handler for the DIF_PROPERTYCHANGE request. It can be used to change the state of an installed device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiregistercodeviceinstallers" data-raw-source="[&lt;strong&gt;SetupDiRegisterCoDeviceInstallers&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiregistercodeviceinstallers)"><strong>SetupDiRegisterCoDeviceInstallers</strong></a></p></td>
<td align="left"><p>Registers the device-specific co-installers listed in the INF file for the specified device. This function is the default handler for DIF_REGISTER_COINSTALLERS.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiinstalldevice" data-raw-source="[&lt;strong&gt;SetupDiInstallDevice&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiinstalldevice)"><strong>SetupDiInstallDevice</strong></a></p></td>
<td align="left"><p>The default handler for the DIF_INSTALLDEVICE request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiinstalldriverfiles" data-raw-source="[&lt;strong&gt;SetupDiInstallDriverFiles&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiinstalldriverfiles)"><strong>SetupDiInstallDriverFiles</strong></a></p></td>
<td align="left"><p>The default handler for the DIF_INSTALLDEVICEFILES request.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiinstalldeviceinterfaces" data-raw-source="[&lt;strong&gt;SetupDiInstallDeviceInterfaces&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiinstalldeviceinterfaces)"><strong>SetupDiInstallDeviceInterfaces</strong></a></p></td>
<td align="left"><p>The default handler for the DIF_INSTALLINTERFACES request. It installs the interfaces that are listed in a <em>DDInstall</em>.<strong>Interfaces</strong> section of a device INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/install/setupdimoveduplicatedevice" data-raw-source="[&lt;strong&gt;SetupDiMoveDuplicateDevice&lt;/strong&gt;](./setupdimoveduplicatedevice.md)"><strong>SetupDiMoveDuplicateDevice</strong></a></p></td>
<td align="left"><p>This function is obsolete and cannot be used in any version of Microsoft Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiremovedevice" data-raw-source="[&lt;strong&gt;SetupDiRemoveDevice&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiremovedevice)"><strong>SetupDiRemoveDevice</strong></a></p></td>
<td align="left"><p>The default handler for the DIF_REMOVEDEVICE request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiunremovedevice" data-raw-source="[&lt;strong&gt;SetupDiUnremoveDevice&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiunremovedevice)"><strong>SetupDiUnremoveDevice</strong></a></p></td>
<td align="left"><p>The default handler for the DIF_UNREMOVE request.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiregisterdeviceinfo" data-raw-source="[&lt;strong&gt;SetupDiRegisterDeviceInfo&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiregisterdeviceinfo)"><strong>SetupDiRegisterDeviceInfo</strong></a></p></td>
<td align="left"><p>The default handler for the DIF_REGISTERDEVICE request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiselectdevice" data-raw-source="[&lt;strong&gt;SetupDiSelectDevice&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiselectdevice)"><strong>SetupDiSelectDevice</strong></a></p></td>
<td align="left"><p>The default handler for the DIF_SELECTDEVICE request.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiselectbestcompatdrv" data-raw-source="[&lt;strong&gt;SetupDiSelectBestCompatDrv&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiselectbestcompatdrv)"><strong>SetupDiSelectBestCompatDrv</strong></a></p></td>
<td align="left"><p>The default handler for the DIF_SELECTBESTCOMPATDRV request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiselectdevice" data-raw-source="[&lt;strong&gt;SetupDiSelectDevice&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiselectdevice)"><strong>SetupDiSelectDevice</strong></a></p></td>
<td align="left"><p>Default handler for the DIF_SELECTDEVICE request.</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="ddk-setupdi-device-installation-customization-functions-dg"></a>Device Installation Customization Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetclassinstallparamsa" data-raw-source="[&lt;strong&gt;SetupDiGetClassInstallParams&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassinstallparamsa)"><strong>SetupDiGetClassInstallParams</strong></a></p></td>
<td align="left"><p>Retrieves class install parameters for a device information set or a particular device information element.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdisetclassinstallparamsa" data-raw-source="[&lt;strong&gt;SetupDiSetClassInstallParams&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdisetclassinstallparamsa)"><strong>SetupDiSetClassInstallParams</strong></a></p></td>
<td align="left"><p>Sets or clears class install parameters for a device information set or a particular device information element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinstallparamsa" data-raw-source="[&lt;strong&gt;SetupDiGetDeviceInstallParams&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinstallparamsa)"><strong>SetupDiGetDeviceInstallParams</strong></a></p></td>
<td align="left"><p>Retrieves device install parameters for a device information set or a particular device information element.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdisetdeviceinstallparamsa" data-raw-source="[&lt;strong&gt;SetupDiSetDeviceInstallParams&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdisetdeviceinstallparamsa)"><strong>SetupDiSetDeviceInstallParams</strong></a></p></td>
<td align="left"><p>Sets device install parameters for a device information set or a particular device information element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetdriverinstallparamsa" data-raw-source="[&lt;strong&gt;SetupDiGetDriverInstallParams&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetdriverinstallparamsa)"><strong>SetupDiGetDriverInstallParams</strong></a></p></td>
<td align="left"><p>Retrieves install parameters for the specified driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdisetdriverinstallparamsa" data-raw-source="[&lt;strong&gt;SetupDiSetDriverInstallParams&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdisetdriverinstallparamsa)"><strong>SetupDiSetDriverInstallParams</strong></a></p></td>
<td align="left"><p>Sets the installation parameters for the specified driver.</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="ddk-setupdi-setup-class-functions-dg"></a>Setup Class Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdibuildclassinfolist" data-raw-source="[&lt;strong&gt;SetupDiBuildClassInfoList&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdibuildclassinfolist)"><strong>SetupDiBuildClassInfoList</strong></a></p></td>
<td align="left"><p>Returns a list of setup class GUIDs that includes every class installed on the system.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdibuildclassinfolistexa" data-raw-source="[&lt;strong&gt;SetupDiBuildClassInfoListEx&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdibuildclassinfolistexa)"><strong>SetupDiBuildClassInfoListEx</strong></a></p></td>
<td align="left"><p>Returns a list of setup class GUIDs that includes every class installed on the local system or a remote system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdescriptiona" data-raw-source="[&lt;strong&gt;SetupDiGetClassDescription&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdescriptiona)"><strong>SetupDiGetClassDescription</strong></a></p></td>
<td align="left"><p>Retrieves the class description associated with the specified setup class GUID.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdescriptionexa" data-raw-source="[&lt;strong&gt;SetupDiGetClassDescriptionEx&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdescriptionexa)"><strong>SetupDiGetClassDescriptionEx</strong></a></p></td>
<td align="left"><p>Retrieves the description of a setup class installed on a local or remote computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetinfclassa" data-raw-source="[&lt;strong&gt;SetupDiGetINFClass&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetinfclassa)"><strong>SetupDiGetINFClass</strong></a></p></td>
<td align="left"><p>Retrieves the class of a specified device INF file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiclassguidsfromnamea" data-raw-source="[&lt;strong&gt;SetupDiClassGuidsFromName&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiclassguidsfromnamea)"><strong>SetupDiClassGuidsFromName</strong></a></p></td>
<td align="left"><p>Retrieves the GUIDs associated with the specified class name. This list is built based on what classes are currently installed on the system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiclassguidsfromnameexa" data-raw-source="[&lt;strong&gt;SetupDiClassGuidsFromNameEx&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiclassguidsfromnameexa)"><strong>SetupDiClassGuidsFromNameEx</strong></a></p></td>
<td align="left"><p>Retrieves the GUIDs associated with the specified class name. This resulting list contains the classes currently installed on a local or remote computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiclassnamefromguida" data-raw-source="[&lt;strong&gt;SetupDiClassNameFromGuid&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiclassnamefromguida)"><strong>SetupDiClassNameFromGuid</strong></a></p></td>
<td align="left"><p>Retrieves the class name associated with the class GUID.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiclassnamefromguidexa" data-raw-source="[&lt;strong&gt;SetupDiClassNameFromGuidEx&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiclassnamefromguidexa)"><strong>SetupDiClassNameFromGuidEx</strong></a></p></td>
<td align="left"><p>Retrieves the class name associated with a class GUID. The class can be installed on a local or remote computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiinstallclassa" data-raw-source="[&lt;strong&gt;SetupDiInstallClass&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiinstallclassa)"><strong>SetupDiInstallClass</strong></a></p></td>
<td align="left"><p>Installs the <strong>ClassInstall32</strong> section of the specified INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiinstallclassexa" data-raw-source="[&lt;strong&gt;SetupDiInstallClassEx&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiinstallclassexa)"><strong>SetupDiInstallClassEx</strong></a></p></td>
<td align="left"><p>Installs a class installer or an interface class.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiopenclassregkey" data-raw-source="[&lt;strong&gt;SetupDiOpenClassRegKey&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiopenclassregkey)"><strong>SetupDiOpenClassRegKey</strong></a></p></td>
<td align="left"><p>Opens the <a href="/windows-hardware/drivers/install/overview-of-device-setup-classes" data-raw-source="[device setup class](./overview-of-device-setup-classes.md)">device setup class</a> registry key, or a specific subkey of the class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiopenclassregkeyexa" data-raw-source="[&lt;strong&gt;SetupDiOpenClassRegKeyEx&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiopenclassregkeyexa)"><strong>SetupDiOpenClassRegKeyEx</strong></a></p></td>
<td align="left"><p>Opens the device setup class registry key, the device interface class registry key, or a specific subkey of the class. This function opens the specified key on the local computer or on a remote computer.</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="ddk-setupdi-class-bitmap-and-icon-functions-dg"></a>Bitmap and Icon Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetclassimagelist" data-raw-source="[&lt;strong&gt;SetupDiGetClassImageList&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassimagelist)"><strong>SetupDiGetClassImageList</strong></a></p></td>
<td align="left"><p>Builds an image list that contains bitmaps for every installed class and returns the list in a data structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetclassimagelistexa" data-raw-source="[&lt;strong&gt;SetupDiGetClassImageListEx&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassimagelistexa)"><strong>SetupDiGetClassImageListEx</strong></a></p></td>
<td align="left"><p>Builds an image list of bitmaps for every class installed on a local or remote computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetclassimageindex" data-raw-source="[&lt;strong&gt;SetupDiGetClassImageIndex&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassimageindex)"><strong>SetupDiGetClassImageIndex</strong></a></p></td>
<td align="left"><p>Retrieves the index within the class image list of a specified class.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetclassbitmapindex" data-raw-source="[&lt;strong&gt;SetupDiGetClassBitmapIndex&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassbitmapindex)"><strong>SetupDiGetClassBitmapIndex</strong></a></p></td>
<td align="left"><p>Retrieves the index of the mini-icon supplied for the specified class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdidrawminiicon" data-raw-source="[&lt;strong&gt;SetupDiDrawMiniIcon&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdidrawminiicon)"><strong>SetupDiDrawMiniIcon</strong></a></p></td>
<td align="left"><p>Draws the specified mini-icon at the location requested.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiloadclassicon" data-raw-source="[&lt;strong&gt;SetupDiLoadClassIcon&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiloadclassicon)"><strong>SetupDiLoadClassIcon</strong></a></p></td>
<td align="left"><p>Loads both the large and mini-icon for the specified class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiloaddeviceicon" data-raw-source="[&lt;strong&gt;SetupDiLoadDeviceIcon&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiloaddeviceicon)"><strong>SetupDiLoadDeviceIcon</strong></a></p></td>
<td align="left"><p>Loads a device icon for a specified device. (Windows Vista and later versions of Windows)</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdidestroyclassimagelist" data-raw-source="[&lt;strong&gt;SetupDiDestroyClassImageList&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdidestroyclassimagelist)"><strong>SetupDiDestroyClassImageList</strong></a></p></td>
<td align="left"><p>Destroys a class image list.</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="ddk-setupdi-device-interface-functions-dg"></a>Device Interface Functions

> [!NOTE]
> SetupApi is not supported on all editions of Windows.  When possible, you should use lower layer APIs such as those available via [CfgMgr32.dll](/windows/win32/api/cfgmgr32/).  See [Porting from SetupApi to CfgMgr32](porting-from-setupapi-to-cfgmgr32.md) for tips.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdicreatedeviceinterfacea" data-raw-source="[&lt;strong&gt;SetupDiCreateDeviceInterface&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdicreatedeviceinterfacea)"><strong>SetupDiCreateDeviceInterface</strong></a></p></td>
<td align="left"><p>Registers device functionality (a device interface) for a device.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiopendeviceinterfacea" data-raw-source="[&lt;strong&gt;SetupDiOpenDeviceInterface&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiopendeviceinterfacea)"><strong>SetupDiOpenDeviceInterface</strong></a></p></td>
<td align="left"><p>Retrieves information about an existing device interface and adds it to the specified device information set.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacealias" data-raw-source="[&lt;strong&gt;SetupDiGetDeviceInterfaceAlias&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacealias)"><strong>SetupDiGetDeviceInterfaceAlias</strong></a></p></td>
<td align="left"><p>Returns an alias of the specified device interface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsexa" data-raw-source="[&lt;strong&gt;SetupDiGetClassDevs&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsexa)"><strong>SetupDiGetClassDevs</strong></a></p></td>
<td align="left"><p>Returns a device information set that contains all devices of a specified class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsexa" data-raw-source="[&lt;strong&gt;SetupDiGetClassDevsEx&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsexa)"><strong>SetupDiGetClassDevsEx</strong></a></p></td>
<td align="left"><p>Returns a device information set that contains all devices of a specified class on a local or remote computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdienumdeviceinterfaces" data-raw-source="[&lt;strong&gt;SetupDiEnumDeviceInterfaces&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdienumdeviceinterfaces)"><strong>SetupDiEnumDeviceInterfaces</strong></a></p></td>
<td align="left"><p>Returns a context structure for a device interface element of a device information set. Each call returns information about one device interface.</p>
<p>The function can be called repeatedly to obtain information about several interfaces exposed by one or more devices.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacedetaila" data-raw-source="[&lt;strong&gt;SetupDiGetDeviceInterfaceDetail&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacedetaila)"><strong>SetupDiGetDeviceInterfaceDetail</strong></a></p></td>
<td align="left"><p>Returns details about a particular device interface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdicreatedeviceinterfaceregkeya" data-raw-source="[&lt;strong&gt;SetupDiCreateDeviceInterfaceRegKey&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdicreatedeviceinterfaceregkeya)"><strong>SetupDiCreateDeviceInterfaceRegKey</strong></a></p></td>
<td align="left"><p>Creates a registry subkey for storing information about a device interface instance and returns a handle to the key.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiopendeviceinterfaceregkey" data-raw-source="[&lt;strong&gt;SetupDiOpenDeviceInterfaceRegKey&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiopendeviceinterfaceregkey)"><strong>SetupDiOpenDeviceInterfaceRegKey</strong></a></p></td>
<td align="left"><p>Opens the registry subkey that is used by applications and drivers to store information that is specific to a device interface instance and returns a handle to the key.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdideletedeviceinterfaceregkey" data-raw-source="[&lt;strong&gt;SetupDiDeleteDeviceInterfaceRegKey&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdideletedeviceinterfaceregkey)"><strong>SetupDiDeleteDeviceInterfaceRegKey</strong></a></p></td>
<td align="left"><p>Deletes the registry subkey that was used by applications and drivers to store information that is specific to a device interface instance.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiinstalldeviceinterfaces" data-raw-source="[&lt;strong&gt;SetupDiInstallDeviceInterfaces&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiinstalldeviceinterfaces)"><strong>SetupDiInstallDeviceInterfaces</strong></a></p></td>
<td align="left"><p>Is the default handler for the DIF_INSTALLINTERFACES request. It installs the interfaces that are listed in a <em>DDInstall</em>.<strong>Interfaces</strong> section of a device INF file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiremovedeviceinterface" data-raw-source="[&lt;strong&gt;SetupDiRemoveDeviceInterface&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiremovedeviceinterface)"><strong>SetupDiRemoveDeviceInterface</strong></a></p></td>
<td align="left"><p>Removes a registered device interface from the system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdideletedeviceinterfacedata" data-raw-source="[&lt;strong&gt;SetupDiDeleteDeviceInterfaceData&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdideletedeviceinterfacedata)"><strong>SetupDiDeleteDeviceInterfaceData</strong></a></p></td>
<td align="left"><p>Deletes a device interface from a device information set.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdisetdeviceinterfacedefault" data-raw-source="[&lt;strong&gt;SetupDiSetDeviceInterfaceDefault&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdisetdeviceinterfacedefault)"><strong>SetupDiSetDeviceInterfaceDefault</strong></a></p></td>
<td align="left"><p>Sets a specified device interface as the default interface for a device class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiinstallclassexa" data-raw-source="[&lt;strong&gt;SetupDiInstallClassEx&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiinstallclassexa)"><strong>SetupDiInstallClassEx</strong></a></p></td>
<td align="left"><p>Installs a class installer or an interface class.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiopenclassregkeyexa" data-raw-source="[&lt;strong&gt;SetupDiOpenClassRegKeyEx&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiopenclassregkeyexa)"><strong>SetupDiOpenClassRegKeyEx</strong></a></p></td>
<td align="left"><p>Opens the <a href="/windows-hardware/drivers/install/overview-of-device-setup-classes" data-raw-source="[device setup class](./overview-of-device-setup-classes.md)">device setup class</a> registry key, the device interface class registry key, or a specific subkey of the class. This function opens the specified key on the local computer or on a remote computer.</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="ddk-setupdi-device-property-functions-dg"></a>Device Property Functions (Windows Vista and Later)

> [!NOTE]
> SetupApi is not supported on all editions of Windows.  When possible, you should use lower layer APIs such as those available via [CfgMgr32.dll](/windows/win32/api/cfgmgr32/).  See [Porting from SetupApi to CfgMgr32](porting-from-setupapi-to-cfgmgr32.md) for tips.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyw" data-raw-source="[&lt;strong&gt;SetupDiGetClassProperty&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyw)"><strong>SetupDiGetClassProperty</strong></a></p></td>
<td align="left"><p>Retrieves a device property that is set for a device setup class or a device interface class.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyexw" data-raw-source="[&lt;strong&gt;SetupDiGetClassPropertyEx&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertyexw)"><strong>SetupDiGetClassPropertyEx</strong></a></p></td>
<td align="left"><p>Retrieves a class property for a device setup class or a device interface class on a local or remote computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertykeys" data-raw-source="[&lt;strong&gt;SetupDiGetClassPropertyKeys&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertykeys)"><strong>SetupDiGetClassPropertyKeys</strong></a></p></td>
<td align="left"><p>Retrieves an array of the device property keys that represent the device properties that are set for a device setup class or a device interface class.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertykeysexw" data-raw-source="[&lt;strong&gt;SetupDiGetClassPropertyKeysEx&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetclasspropertykeysexw)"><strong>SetupDiGetClassPropertyKeysEx</strong></a></p></td>
<td align="left"><p>Retrieves an array of the device property keys that represent the device properties that are set for a device setup class or a device interface class on a local or a remote computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertyw" data-raw-source="[&lt;strong&gt;SetupDiGetDeviceInterfaceProperty&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertyw)"><strong>SetupDiGetDeviceInterfaceProperty</strong></a></p></td>
<td align="left"><p>Retrieves a device property that is set for a device interface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertykeys" data-raw-source="[&lt;strong&gt;SetupDiGetDeviceInterfacePropertyKeys&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertykeys)"><strong>SetupDiGetDeviceInterfacePropertyKeys</strong></a></p></td>
<td align="left"><p>Retrieves an array of device property keys that represent the device properties that are set for a device interface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw" data-raw-source="[&lt;strong&gt;SetupDiGetDeviceProperty&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)"><strong>SetupDiGetDeviceProperty</strong></a></p></td>
<td align="left"><p>Retrieves a device instance property.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertykeys" data-raw-source="[&lt;strong&gt;SetupDiGetDevicePropertyKeys&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertykeys)"><strong>SetupDiGetDevicePropertyKeys</strong></a></p></td>
<td align="left"><p>Retrieves an array of the device property keys that represent the device properties that are set for a device instance.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdisetclasspropertyw" data-raw-source="[&lt;strong&gt;SetupDiSetClassProperty&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdisetclasspropertyw)"><strong>SetupDiSetClassProperty</strong></a></p></td>
<td align="left"><p>Sets a class property for a device setup class or a device interface class.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdisetclasspropertyexw" data-raw-source="[&lt;strong&gt;SetupDiSetClassPropertyEx&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdisetclasspropertyexw)"><strong>SetupDiSetClassPropertyEx</strong></a></p></td>
<td align="left"><p>Sets a device property for a device setup class or a device interface class on a local or remote computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdisetdeviceinterfacepropertyw" data-raw-source="[&lt;strong&gt;SetupDiSetDeviceInterfaceProperty&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdisetdeviceinterfacepropertyw)"><strong>SetupDiSetDeviceInterfaceProperty</strong></a></p></td>
<td align="left"><p>Sets a device property of a device interface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdisetdevicepropertyw" data-raw-source="[&lt;strong&gt;SetupDiSetDeviceProperty&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdisetdevicepropertyw)"><strong>SetupDiSetDeviceProperty</strong></a></p></td>
<td align="left"><p>Sets a device instance property.</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="ddk-setupdi-registry-functions-dg"></a>Registry Functions

> [!NOTE]
> SetupApi is not supported on all editions of Windows.  When possible, you should use lower layer APIs such as those available via [CfgMgr32.dll](/windows/win32/api/cfgmgr32/).  See [Porting from SetupApi to CfgMgr32](porting-from-setupapi-to-cfgmgr32.md) for tips.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdicreatedevregkeya" data-raw-source="[&lt;strong&gt;SetupDiCreateDevRegKey&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdicreatedevregkeya)"><strong>SetupDiCreateDevRegKey</strong></a></p></td>
<td align="left"><p>Creates a registry storage key for device-specific configuration information and returns a handle to the key.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiopendevregkey" data-raw-source="[&lt;strong&gt;SetupDiOpenDevRegKey&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiopendevregkey)"><strong>SetupDiOpenDevRegKey</strong></a></p></td>
<td align="left"><p>Opens a registry storage key for device-specific configuration information and returns a handle to the key.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdideletedevregkey" data-raw-source="[&lt;strong&gt;SetupDiDeleteDevRegKey&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdideletedevregkey)"><strong>SetupDiDeleteDevRegKey</strong></a></p></td>
<td align="left"><p>Deletes the specified user-accessible registry key(s) associated with a device information element.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiopenclassregkey" data-raw-source="[&lt;strong&gt;SetupDiOpenClassRegKey&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiopenclassregkey)"><strong>SetupDiOpenClassRegKey</strong></a></p></td>
<td align="left"><p>Opens the setup class registry key, or a specific subkey of the class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiopenclassregkeyexa" data-raw-source="[&lt;strong&gt;SetupDiOpenClassRegKeyEx&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiopenclassregkeyexa)"><strong>SetupDiOpenClassRegKeyEx</strong></a></p></td>
<td align="left"><p>Opens the device setup class registry key, the device interface class registry key, or a specific subkey of the class.</p>
<p>This function opens the specified key on the local computer or on a remote computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdicreatedeviceinterfaceregkeya" data-raw-source="[&lt;strong&gt;SetupDiCreateDeviceInterfaceRegKey&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdicreatedeviceinterfaceregkeya)"><strong>SetupDiCreateDeviceInterfaceRegKey</strong></a></p></td>
<td align="left"><p>Creates a nonvolatile registry subkey for storing information about a device interface instance and returns a handle to the key.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdiopendeviceinterfaceregkey" data-raw-source="[&lt;strong&gt;SetupDiOpenDeviceInterfaceRegKey&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdiopendeviceinterfaceregkey)"><strong>SetupDiOpenDeviceInterfaceRegKey</strong></a></p></td>
<td align="left"><p>Opens the registry subkey that is used by applications and drivers to store information that is specific to a device interface instance and returns a handle to the key.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdideletedeviceinterfaceregkey" data-raw-source="[&lt;strong&gt;SetupDiDeleteDeviceInterfaceRegKey&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdideletedeviceinterfaceregkey)"><strong>SetupDiDeleteDeviceInterfaceRegKey</strong></a></p></td>
<td align="left"><p>Deletes the registry subkey that was used by applications and drivers to store information that is specific to a device interface instance.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdisetdeviceregistrypropertya" data-raw-source="[&lt;strong&gt;SetupDiSetDeviceRegistryProperty&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdisetdeviceregistrypropertya)"><strong>SetupDiSetDeviceRegistryProperty</strong></a></p></td>
<td align="left"><p>Sets the specified Plug and Play device property.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceregistrypropertya" data-raw-source="[&lt;strong&gt;SetupDiGetDeviceRegistryProperty&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceregistrypropertya)"><strong>SetupDiGetDeviceRegistryProperty</strong></a></p></td>
<td align="left"><p>Retrieves the specified Plug and Play device property.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetclassregistrypropertya" data-raw-source="[&lt;strong&gt;SetupDiGetClassRegistryProperty&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassregistrypropertya)"><strong>SetupDiGetClassRegistryProperty</strong></a></p></td>
<td align="left"><p>Retrieves a specified device class property from the registry.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdisetclassregistrypropertya" data-raw-source="[&lt;strong&gt;SetupDiSetClassRegistryProperty&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdisetclassregistrypropertya)"><strong>SetupDiSetClassRegistryProperty</strong></a></p></td>
<td align="left"><p>Sets a specified device class property in the registry.</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="ddk-other-setupdi-functions-dg"></a>Other Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetactualmodelssectiona" data-raw-source="[&lt;strong&gt;SetupDiGetActualModelsSection&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetactualmodelssectiona)"><strong>SetupDiGetActualModelsSection</strong></a></p></td>
<td align="left"><p>Retrieves the appropriate decorated <a href="inf-models-section.md" data-raw-source="[&lt;strong&gt;INF Models section&lt;/strong&gt;](inf-models-section.md)"><strong>INF Models section</strong></a> to use when installing a device from a device INF file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetactualsectiontoinstalla" data-raw-source="[&lt;strong&gt;SetupDiGetActualSectionToInstall&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetactualsectiontoinstalla)"><strong>SetupDiGetActualSectionToInstall</strong></a></p></td>
<td align="left"><p>Retrieves the appropriate <em>DDInstall</em> section to use when installing a device from a device INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigetactualsectiontoinstallexa" data-raw-source="[&lt;strong&gt;SetupDiGetActualSectionToInstallEx&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigetactualsectiontoinstallexa)"><strong>SetupDiGetActualSectionToInstallEx</strong></a></p></td>
<td align="left"><p>Retrieves the name of the INF <em>DDInstall</em> section that installs a device for a specified operating system and processor architecture.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigethwprofilefriendlynamea" data-raw-source="[&lt;strong&gt;SetupDiGetHwProfileFriendlyName&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigethwprofilefriendlynamea)"><strong>SetupDiGetHwProfileFriendlyName</strong></a></p></td>
<td align="left"><p>Retrieves the friendly name associated with a hardware profile ID.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigethwprofilefriendlynameexa" data-raw-source="[&lt;strong&gt;SetupDiGetHwProfileFriendlyNameEx&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigethwprofilefriendlynameexa)"><strong>SetupDiGetHwProfileFriendlyNameEx</strong></a></p></td>
<td align="left"><p>Retrieves the friendly name associated with a hardware profile ID on a local or remote computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigethwprofilelist" data-raw-source="[&lt;strong&gt;SetupDiGetHwProfileList&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigethwprofilelist)"><strong>SetupDiGetHwProfileList</strong></a></p></td>
<td align="left"><p>Retrieves a list of all currently defined hardware profile IDs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdigethwprofilelistexa" data-raw-source="[&lt;strong&gt;SetupDiGetHwProfileListEx&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdigethwprofilelistexa)"><strong>SetupDiGetHwProfileListEx</strong></a></p></td>
<td align="left"><p>Retrieves a list of all currently defined hardware profile IDs on a local or remote computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdirestartdevices" data-raw-source="[&lt;strong&gt;SetupDiRestartDevices&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdirestartdevices)"><strong>SetupDiRestartDevices</strong></a></p></td>
<td align="left"><p>Restarts a specified device or, if necessary, starts all devices that are operated by the same function and filter drivers as the specified device.</p></td>
</tr>
</tbody>
</table>

 

