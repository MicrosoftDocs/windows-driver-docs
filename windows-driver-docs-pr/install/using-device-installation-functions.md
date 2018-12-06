---
title: Using Device Installation Functions
description: Using Device Installation Functions
ms.assetid: a7cfa359-a45c-45fa-a854-ee70de66b12e
keywords:
- SetupAPI functions WDK , device installation functions
- device installation functions WDK SetupAPI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Device Installation Functions





This section summarizes the [device installation functions](https://msdn.microsoft.com/library/windows/hardware/ff541299). By using the device installation functions, the installation software can perform the following types of operations:

-   Install drivers

-   Handle DIF codes.

-   Manage device information sets.

-   Manage driver lists.

-   Manage device interfaces.

-   Manage icons and other bitmaps.

To perform device installation operations that are not supported by the SetupAPI functions described in this section, call the appropriate [general Setup functions](https://msdn.microsoft.com/library/windows/hardware/ff544985) or [PnP Configuration Manager functions](https://msdn.microsoft.com/library/windows/hardware/ff549717) (CM_*Xxx* functions<em>).</em>

The following tables provide summaries of the following types of functions:

[Driver Installation Functions](#ddk-update-driver-function-dg)

[Device Information Functions](#ddk-setupdi-device-information-functions-dg)

[Driver Information Functions](#ddk-setupdi-driver-information-functions-dg)

[Driver Selection Functions](#ddk-setupdi-driver-selection-functions-dg)

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff544710" data-raw-source="[&lt;strong&gt;DiInstallDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544710)"><strong>DiInstallDevice</strong></a></p></td>
<td align="left"><p>Installs a specified driver that is preinstalled in the <a href="driver-store.md" data-raw-source="[driver store](driver-store.md)">driver store</a> on a PnP device that is present in the system. (Windows Vista and later versions of Windows)</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff544717" data-raw-source="[&lt;strong&gt;DiInstallDriver&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544717)"><strong>DiInstallDriver</strong></a></p></td>
<td align="left"><p>Preinstalls a driver in the driver store and then installs the driver on matching PnP devices that are present in the system. (Windows Vista and later versions of Windows)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff544721" data-raw-source="[&lt;strong&gt;DiRollbackDriver&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544721)"><strong>DiRollbackDriver</strong></a></p></td>
<td align="left"><p>Rolls back the driver that is installed on a specified device to the backup driver set for the device. (Windows Vista and later versions of Windows)</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff544727" data-raw-source="[&lt;strong&gt;DiShowUpdateDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544727)"><strong>DiShowUpdateDevice</strong></a></p></td>
<td align="left"><p>Displays the Hardware Update wizard for a specified device. (Windows Vista and later versions of Windows)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff544754" data-raw-source="[&lt;strong&gt;DiUninstallDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544754)"><strong>DiUninstallDevice</strong></a></p></td>
<td align="left"><p>Uninstalls a device and removes its device node (<a href="https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode" data-raw-source="[&lt;em&gt;devnode&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)"><em>devnode</em></a>) ) from the system. (Windows 7 and later versions of Windows)</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff547654" data-raw-source="[&lt;strong&gt;InstallSelectedDriver&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547654)"><strong>InstallSelectedDriver</strong></a></p></td>
<td align="left"><p>Installs a selected driver on a selected device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553534" data-raw-source="[&lt;strong&gt;UpdateDriverForPlugAndPlayDevices&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553534)"><strong>UpdateDriverForPlugAndPlayDevices</strong></a></p></td>
<td align="left"><p>Updates the function driver that is installed for matching PnP devices that are present in the system.</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="ddk-setupdi-device-information-functions-dg"></a>Device Information Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550956" data-raw-source="[&lt;strong&gt;SetupDiCreateDeviceInfoList&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550956)"><strong>SetupDiCreateDeviceInfoList</strong></a></p></td>
<td align="left"><p>Creates an empty <a href="device-information-sets.md" data-raw-source="[device information set](device-information-sets.md)">device information set</a>. This set can be associated with a class GUID.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550958" data-raw-source="[&lt;strong&gt;SetupDiCreateDeviceInfoListEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550958)"><strong>SetupDiCreateDeviceInfoListEx</strong></a></p></td>
<td align="left"><p>Creates an empty device information set. This set can be associated with a class GUID and can be for devices on a remote computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550952" data-raw-source="[&lt;strong&gt;SetupDiCreateDeviceInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550952)"><strong>SetupDiCreateDeviceInfo</strong></a></p></td>
<td align="left"><p>Creates a new device information element and adds it as a new member to the specified device information set.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552071" data-raw-source="[&lt;strong&gt;SetupDiOpenDeviceInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552071)"><strong>SetupDiOpenDeviceInfo</strong></a></p></td>
<td align="left"><p>Retrieves information about an existing device instance and adds it to the specified device information set.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551010" data-raw-source="[&lt;strong&gt;SetupDiEnumDeviceInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551010)"><strong>SetupDiEnumDeviceInfo</strong></a></p></td>
<td align="left"><p>Returns a context structure for a device information element of a device information set.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551106" data-raw-source="[&lt;strong&gt;SetupDiGetDeviceInstanceId&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551106)"><strong>SetupDiGetDeviceInstanceId</strong></a></p></td>
<td align="left"><p>Retrieves the device instance ID associated with a device information element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551101" data-raw-source="[&lt;strong&gt;SetupDiGetDeviceInfoListClass&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551101)"><strong>SetupDiGetDeviceInfoListClass</strong></a></p></td>
<td align="left"><p>Retrieves the class GUID associated with a device information set if it has an associated class.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551103" data-raw-source="[&lt;strong&gt;SetupDiGetDeviceInfoListDetail&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551103)"><strong>SetupDiGetDeviceInfoListDetail</strong></a></p></td>
<td align="left"><p>Retrieves information associated with a device information set including the class GUID, remote computer handle, and remote computer name.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551064" data-raw-source="[&lt;strong&gt;SetupDiGetClassDevPropertySheets&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551064)"><strong>SetupDiGetClassDevPropertySheets</strong></a></p></td>
<td align="left"><p>Retrieves handles to the property sheets of a specified device information element or of the <a href="device-setup-classes.md" data-raw-source="[device setup class](device-setup-classes.md)">device setup class</a> of a specified device information set.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551069" data-raw-source="[&lt;strong&gt;SetupDiGetClassDevs&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551069)"><strong>SetupDiGetClassDevs</strong></a></p></td>
<td align="left"><p>Returns a device information set that contains all devices of a specified class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551072" data-raw-source="[&lt;strong&gt;SetupDiGetClassDevsEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551072)"><strong>SetupDiGetClassDevsEx</strong></a></p></td>
<td align="left"><p>Returns a device information set that contains all devices of a specified class on a local or remote computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552176" data-raw-source="[&lt;strong&gt;SetupDiSetSelectedDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552176)"><strong>SetupDiSetSelectedDevice</strong></a></p></td>
<td align="left"><p>Sets the specified device information element to be the currently-selected member of a device information set. This function is typically used by an installation wizard.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552011" data-raw-source="[&lt;strong&gt;SetupDiGetSelectedDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552011)"><strong>SetupDiGetSelectedDevice</strong></a></p></td>
<td align="left"><p>Retrieves the currently-selected device for the specified device information set.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552091" data-raw-source="[&lt;strong&gt;SetupDiRegisterDeviceInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552091)"><strong>SetupDiRegisterDeviceInfo</strong></a></p></td>
<td align="left"><p>Registers a newly created device instance with the Plug and Play manager.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550978" data-raw-source="[&lt;strong&gt;SetupDiDeleteDeviceInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550978)"><strong>SetupDiDeleteDeviceInfo</strong></a></p></td>
<td align="left"><p>Deletes a member from the specified device information set. This function does not delete the actual device.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550996" data-raw-source="[&lt;strong&gt;SetupDiDestroyDeviceInfoList&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550996)"><strong>SetupDiDestroyDeviceInfoList</strong></a></p></td>
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550917" data-raw-source="[&lt;strong&gt;SetupDiBuildDriverInfoList&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550917)"><strong>SetupDiBuildDriverInfoList</strong></a></p></td>
<td align="left"><p>Builds a list of drivers associated with a specified device instance or with the device information set&#39;s global class driver list.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551018" data-raw-source="[&lt;strong&gt;SetupDiEnumDriverInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551018)"><strong>SetupDiEnumDriverInfo</strong></a></p></td>
<td align="left"><p>Enumerates the members of a driver information list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551973" data-raw-source="[&lt;strong&gt;SetupDiGetDriverInfoDetail&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551973)"><strong>SetupDiGetDriverInfoDetail</strong></a></p></td>
<td align="left"><p>Retrieves detailed information for a specified driver information element.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552183" data-raw-source="[&lt;strong&gt;SetupDiSetSelectedDriver&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552183)"><strong>SetupDiSetSelectedDriver</strong></a></p></td>
<td align="left"><p>Sets the specified member of a driver list as the currently selected-driver. It can also be used to reset the driver list so that there is no currently-selected driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552013" data-raw-source="[&lt;strong&gt;SetupDiGetSelectedDriver&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552013)"><strong>SetupDiGetSelectedDriver</strong></a></p></td>
<td align="left"><p>Retrieves the member of a driver list that was selected as the driver to install.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550928" data-raw-source="[&lt;strong&gt;SetupDiCancelDriverInfoSearch&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550928)"><strong>SetupDiCancelDriverInfoSearch</strong></a></p></td>
<td align="left"><p>Cancels a driver list search that is currently underway in a different thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551001" data-raw-source="[&lt;strong&gt;SetupDiDestroyDriverInfoList&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551001)"><strong>SetupDiDestroyDriverInfoList</strong></a></p></td>
<td align="left"><p>Destroys a driver information list.</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="ddk-setupdi-driver-selection-functions-dg"></a>Driver Selection Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550905" data-raw-source="[&lt;strong&gt;SetupDiAskForOEMDisk&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550905)"><strong>SetupDiAskForOEMDisk</strong></a></p></td>
<td align="left"><p>Displays a dialog that asks the user for the path of an OEM installation disk.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552121" data-raw-source="[&lt;strong&gt;SetupDiSelectOEMDrv&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552121)"><strong>SetupDiSelectOEMDrv</strong></a></p></td>
<td align="left"><p>Selects a driver for a device by using an OEM path supplied by the user.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552115" data-raw-source="[&lt;strong&gt;SetupDiSelectDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552115)"><strong>SetupDiSelectDevice</strong></a></p></td>
<td align="left"><p>Default handler for the DIF_SELECTDEVICE request.</p></td>
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550922" data-raw-source="[&lt;strong&gt;SetupDiCallClassInstaller&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550922)"><strong>SetupDiCallClassInstaller</strong></a></p></td>
<td align="left"><p>Calls the appropriate class installer, and any registered co-installers, with the specified installation request.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550930" data-raw-source="[&lt;strong&gt;SetupDiChangeState&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550930)"><strong>SetupDiChangeState</strong></a></p></td>
<td align="left"><p>The default handler for the DIF_PROPERTYCHANGE request. It can be used to change the state of an installed device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552085" data-raw-source="[&lt;strong&gt;SetupDiRegisterCoDeviceInstallers&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552085)"><strong>SetupDiRegisterCoDeviceInstallers</strong></a></p></td>
<td align="left"><p>Registers the device-specific co-installers listed in the INF file for the specified device. This function is the default handler for DIF_REGISTER_COINSTALLERS.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552039" data-raw-source="[&lt;strong&gt;SetupDiInstallDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552039)"><strong>SetupDiInstallDevice</strong></a></p></td>
<td align="left"><p>The default handler for the DIF_INSTALLDEVICE request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552048" data-raw-source="[&lt;strong&gt;SetupDiInstallDriverFiles&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552048)"><strong>SetupDiInstallDriverFiles</strong></a></p></td>
<td align="left"><p>The default handler for the DIF_INSTALLDEVICEFILES request.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552043" data-raw-source="[&lt;strong&gt;SetupDiInstallDeviceInterfaces&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552043)"><strong>SetupDiInstallDeviceInterfaces</strong></a></p></td>
<td align="left"><p>The default handler for the DIF_INSTALLINTERFACES request. It installs the interfaces that are listed in a <em>DDInstall</em>.<strong>Interfaces</strong> section of a device INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552062" data-raw-source="[&lt;strong&gt;SetupDiMoveDuplicateDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552062)"><strong>SetupDiMoveDuplicateDevice</strong></a></p></td>
<td align="left"><p>This function is obsolete and cannot be used in any version of Microsoft Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552097" data-raw-source="[&lt;strong&gt;SetupDiRemoveDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552097)"><strong>SetupDiRemoveDevice</strong></a></p></td>
<td align="left"><p>The default handler for the DIF_REMOVEDEVICE request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552193" data-raw-source="[&lt;strong&gt;SetupDiUnremoveDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552193)"><strong>SetupDiUnremoveDevice</strong></a></p></td>
<td align="left"><p>The default handler for the DIF_UNREMOVE request.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552091" data-raw-source="[&lt;strong&gt;SetupDiRegisterDeviceInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552091)"><strong>SetupDiRegisterDeviceInfo</strong></a></p></td>
<td align="left"><p>The default handler for the DIF_REGISTERDEVICE request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552115" data-raw-source="[&lt;strong&gt;SetupDiSelectDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552115)"><strong>SetupDiSelectDevice</strong></a></p></td>
<td align="left"><p>The default handler for the DIF_SELECTDEVICE request.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552112" data-raw-source="[&lt;strong&gt;SetupDiSelectBestCompatDrv&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552112)"><strong>SetupDiSelectBestCompatDrv</strong></a></p></td>
<td align="left"><p>The default handler for the DIF_SELECTBESTCOMPATDRV request.</p></td>
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551083" data-raw-source="[&lt;strong&gt;SetupDiGetClassInstallParams&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551083)"><strong>SetupDiGetClassInstallParams</strong></a></p></td>
<td align="left"><p>Retrieves class install parameters for a device information set or a particular device information element.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552122" data-raw-source="[&lt;strong&gt;SetupDiSetClassInstallParams&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552122)"><strong>SetupDiSetClassInstallParams</strong></a></p></td>
<td align="left"><p>Sets or clears class install parameters for a device information set or a particular device information element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551104" data-raw-source="[&lt;strong&gt;SetupDiGetDeviceInstallParams&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551104)"><strong>SetupDiGetDeviceInstallParams</strong></a></p></td>
<td align="left"><p>Retrieves device install parameters for a device information set or a particular device information element.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552141" data-raw-source="[&lt;strong&gt;SetupDiSetDeviceInstallParams&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552141)"><strong>SetupDiSetDeviceInstallParams</strong></a></p></td>
<td align="left"><p>Sets device install parameters for a device information set or a particular device information element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551978" data-raw-source="[&lt;strong&gt;SetupDiGetDriverInstallParams&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551978)"><strong>SetupDiGetDriverInstallParams</strong></a></p></td>
<td align="left"><p>Retrieves install parameters for the specified driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552172" data-raw-source="[&lt;strong&gt;SetupDiSetDriverInstallParams&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552172)"><strong>SetupDiSetDriverInstallParams</strong></a></p></td>
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550909" data-raw-source="[&lt;strong&gt;SetupDiBuildClassInfoList&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550909)"><strong>SetupDiBuildClassInfoList</strong></a></p></td>
<td align="left"><p>Returns a list of setup class GUIDs that includes every class installed on the system.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550911" data-raw-source="[&lt;strong&gt;SetupDiBuildClassInfoListEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550911)"><strong>SetupDiBuildClassInfoListEx</strong></a></p></td>
<td align="left"><p>Returns a list of setup class GUIDs that includes every class installed on the local system or a remote system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551053" data-raw-source="[&lt;strong&gt;SetupDiGetClassDescription&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551053)"><strong>SetupDiGetClassDescription</strong></a></p></td>
<td align="left"><p>Retrieves the class description associated with the specified setup class GUID.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551058" data-raw-source="[&lt;strong&gt;SetupDiGetClassDescriptionEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551058)"><strong>SetupDiGetClassDescriptionEx</strong></a></p></td>
<td align="left"><p>Retrieves the description of a setup class installed on a local or remote computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552010" data-raw-source="[&lt;strong&gt;SetupDiGetINFClass&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552010)"><strong>SetupDiGetINFClass</strong></a></p></td>
<td align="left"><p>Retrieves the class of a specified device INF file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550937" data-raw-source="[&lt;strong&gt;SetupDiClassGuidsFromName&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550937)"><strong>SetupDiClassGuidsFromName</strong></a></p></td>
<td align="left"><p>Retrieves the GUIDs associated with the specified class name. This list is built based on what classes are currently installed on the system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550941" data-raw-source="[&lt;strong&gt;SetupDiClassGuidsFromNameEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550941)"><strong>SetupDiClassGuidsFromNameEx</strong></a></p></td>
<td align="left"><p>Retrieves the GUIDs associated with the specified class name. This resulting list contains the classes currently installed on a local or remote computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550947" data-raw-source="[&lt;strong&gt;SetupDiClassNameFromGuid&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550947)"><strong>SetupDiClassNameFromGuid</strong></a></p></td>
<td align="left"><p>Retrieves the class name associated with the class GUID.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550950" data-raw-source="[&lt;strong&gt;SetupDiClassNameFromGuidEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550950)"><strong>SetupDiClassNameFromGuidEx</strong></a></p></td>
<td align="left"><p>Retrieves the class name associated with a class GUID. The class can be installed on a local or remote computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552024" data-raw-source="[&lt;strong&gt;SetupDiInstallClass&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552024)"><strong>SetupDiInstallClass</strong></a></p></td>
<td align="left"><p>Installs the <strong>ClassInstall32</strong> section of the specified INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552032" data-raw-source="[&lt;strong&gt;SetupDiInstallClassEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552032)"><strong>SetupDiInstallClassEx</strong></a></p></td>
<td align="left"><p>Installs a class installer or an interface class.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552065" data-raw-source="[&lt;strong&gt;SetupDiOpenClassRegKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552065)"><strong>SetupDiOpenClassRegKey</strong></a></p></td>
<td align="left"><p>Opens the <a href="device-setup-classes.md" data-raw-source="[device setup class](device-setup-classes.md)">device setup class</a> registry key, or a specific subkey of the class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552067" data-raw-source="[&lt;strong&gt;SetupDiOpenClassRegKeyEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552067)"><strong>SetupDiOpenClassRegKeyEx</strong></a></p></td>
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551080" data-raw-source="[&lt;strong&gt;SetupDiGetClassImageList&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551080)"><strong>SetupDiGetClassImageList</strong></a></p></td>
<td align="left"><p>Builds an image list that contains bitmaps for every installed class and returns the list in a data structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551081" data-raw-source="[&lt;strong&gt;SetupDiGetClassImageListEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551081)"><strong>SetupDiGetClassImageListEx</strong></a></p></td>
<td align="left"><p>Builds an image list of bitmaps for every class installed on a local or remote computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551074" data-raw-source="[&lt;strong&gt;SetupDiGetClassImageIndex&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551074)"><strong>SetupDiGetClassImageIndex</strong></a></p></td>
<td align="left"><p>Retrieves the index within the class image list of a specified class.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551047" data-raw-source="[&lt;strong&gt;SetupDiGetClassBitmapIndex&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551047)"><strong>SetupDiGetClassBitmapIndex</strong></a></p></td>
<td align="left"><p>Retrieves the index of the mini-icon supplied for the specified class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551005" data-raw-source="[&lt;strong&gt;SetupDiDrawMiniIcon&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551005)"><strong>SetupDiDrawMiniIcon</strong></a></p></td>
<td align="left"><p>Draws the specified mini-icon at the location requested.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552053" data-raw-source="[&lt;strong&gt;SetupDiLoadClassIcon&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552053)"><strong>SetupDiLoadClassIcon</strong></a></p></td>
<td align="left"><p>Loads both the large and mini-icon for the specified class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552057" data-raw-source="[&lt;strong&gt;SetupDiLoadDeviceIcon&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552057)"><strong>SetupDiLoadDeviceIcon</strong></a></p></td>
<td align="left"><p>Loads a device icon for a specified device. (Windows Vista and later versions of Windows)</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550995" data-raw-source="[&lt;strong&gt;SetupDiDestroyClassImageList&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550995)"><strong>SetupDiDestroyClassImageList</strong></a></p></td>
<td align="left"><p>Destroys a class image list.</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="ddk-setupdi-device-interface-functions-dg"></a>Device Interface Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550965" data-raw-source="[&lt;strong&gt;SetupDiCreateDeviceInterface&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550965)"><strong>SetupDiCreateDeviceInterface</strong></a></p></td>
<td align="left"><p>Registers device functionality (a device interface) for a device.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552074" data-raw-source="[&lt;strong&gt;SetupDiOpenDeviceInterface&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552074)"><strong>SetupDiOpenDeviceInterface</strong></a></p></td>
<td align="left"><p>Retrieves information about an existing device interface and adds it to the specified device information set.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551108" data-raw-source="[&lt;strong&gt;SetupDiGetDeviceInterfaceAlias&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551108)"><strong>SetupDiGetDeviceInterfaceAlias</strong></a></p></td>
<td align="left"><p>Returns an alias of the specified device interface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551072" data-raw-source="[&lt;strong&gt;SetupDiGetClassDevs&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551072)"><strong>SetupDiGetClassDevs</strong></a></p></td>
<td align="left"><p>Returns a device information set that contains all devices of a specified class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551072" data-raw-source="[&lt;strong&gt;SetupDiGetClassDevsEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551072)"><strong>SetupDiGetClassDevsEx</strong></a></p></td>
<td align="left"><p>Returns a device information set that contains all devices of a specified class on a local or remote computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551015" data-raw-source="[&lt;strong&gt;SetupDiEnumDeviceInterfaces&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551015)"><strong>SetupDiEnumDeviceInterfaces</strong></a></p></td>
<td align="left"><p>Returns a context structure for a device interface element of a device information set. Each call returns information about one device interface.</p>
<p>The function can be called repeatedly to obtain information about several interfaces exposed by one or more devices.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551120" data-raw-source="[&lt;strong&gt;SetupDiGetDeviceInterfaceDetail&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551120)"><strong>SetupDiGetDeviceInterfaceDetail</strong></a></p></td>
<td align="left"><p>Returns details about a particular device interface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550967" data-raw-source="[&lt;strong&gt;SetupDiCreateDeviceInterfaceRegKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550967)"><strong>SetupDiCreateDeviceInterfaceRegKey</strong></a></p></td>
<td align="left"><p>Creates a registry subkey for storing information about a device interface instance and returns a handle to the key.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552075" data-raw-source="[&lt;strong&gt;SetupDiOpenDeviceInterfaceRegKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552075)"><strong>SetupDiOpenDeviceInterfaceRegKey</strong></a></p></td>
<td align="left"><p>Opens the registry subkey that is used by applications and drivers to store information that is specific to a device interface instance and returns a handle to the key.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550986" data-raw-source="[&lt;strong&gt;SetupDiDeleteDeviceInterfaceRegKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550986)"><strong>SetupDiDeleteDeviceInterfaceRegKey</strong></a></p></td>
<td align="left"><p>Deletes the registry subkey that was used by applications and drivers to store information that is specific to a device interface instance.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552043" data-raw-source="[&lt;strong&gt;SetupDiInstallDeviceInterfaces&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552043)"><strong>SetupDiInstallDeviceInterfaces</strong></a></p></td>
<td align="left"><p>Is the default handler for the DIF_INSTALLINTERFACES request. It installs the interfaces that are listed in a <em>DDInstall</em>.<strong>Interfaces</strong> section of a device INF file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552102" data-raw-source="[&lt;strong&gt;SetupDiRemoveDeviceInterface&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552102)"><strong>SetupDiRemoveDeviceInterface</strong></a></p></td>
<td align="left"><p>Removes a registered device interface from the system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550984" data-raw-source="[&lt;strong&gt;SetupDiDeleteDeviceInterfaceData&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550984)"><strong>SetupDiDeleteDeviceInterfaceData</strong></a></p></td>
<td align="left"><p>Deletes a device interface from a device information set.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552149" data-raw-source="[&lt;strong&gt;SetupDiSetDeviceInterfaceDefault&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552149)"><strong>SetupDiSetDeviceInterfaceDefault</strong></a></p></td>
<td align="left"><p>Sets a specified device interface as the default interface for a device class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552032" data-raw-source="[&lt;strong&gt;SetupDiInstallClassEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552032)"><strong>SetupDiInstallClassEx</strong></a></p></td>
<td align="left"><p>Installs a class installer or an interface class.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552067" data-raw-source="[&lt;strong&gt;SetupDiOpenClassRegKeyEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552067)"><strong>SetupDiOpenClassRegKeyEx</strong></a></p></td>
<td align="left"><p>Opens the <a href="device-setup-classes.md" data-raw-source="[device setup class](device-setup-classes.md)">device setup class</a> registry key, the device interface class registry key, or a specific subkey of the class. This function opens the specified key on the local computer or on a remote computer.</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="ddk-setupdi-device-property-functions-dg"></a>Device Property Functions (Windows Vista and Later)

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551086" data-raw-source="[&lt;strong&gt;SetupDiGetClassProperty&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551086)"><strong>SetupDiGetClassProperty</strong></a></p></td>
<td align="left"><p>Retrieves a device property that is set for a device setup class or a device interface class.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551090" data-raw-source="[&lt;strong&gt;SetupDiGetClassPropertyEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551090)"><strong>SetupDiGetClassPropertyEx</strong></a></p></td>
<td align="left"><p>Retrieves a class property for a device setup class or a device interface class on a local or remote computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551091" data-raw-source="[&lt;strong&gt;SetupDiGetClassPropertyKeys&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551091)"><strong>SetupDiGetClassPropertyKeys</strong></a></p></td>
<td align="left"><p>Retrieves an array of the device property keys that represent the device properties that are set for a device setup class or a device interface class.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551093" data-raw-source="[&lt;strong&gt;SetupDiGetClassPropertyKeysEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551093)"><strong>SetupDiGetClassPropertyKeysEx</strong></a></p></td>
<td align="left"><p>Retrieves an array of the device property keys that represent the device properties that are set for a device setup class or a device interface class on a local or a remote computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551122" data-raw-source="[&lt;strong&gt;SetupDiGetDeviceInterfaceProperty&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551122)"><strong>SetupDiGetDeviceInterfaceProperty</strong></a></p></td>
<td align="left"><p>Retrieves a device property that is set for a device interface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551959" data-raw-source="[&lt;strong&gt;SetupDiGetDeviceInterfacePropertyKeys&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551959)"><strong>SetupDiGetDeviceInterfacePropertyKeys</strong></a></p></td>
<td align="left"><p>Retrieves an array of device property keys that represent the device properties that are set for a device interface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551963" data-raw-source="[&lt;strong&gt;SetupDiGetDeviceProperty&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551963)"><strong>SetupDiGetDeviceProperty</strong></a></p></td>
<td align="left"><p>Retrieves a device instance property.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551965" data-raw-source="[&lt;strong&gt;SetupDiGetDevicePropertyKeys&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551965)"><strong>SetupDiGetDevicePropertyKeys</strong></a></p></td>
<td align="left"><p>Retrieves an array of the device property keys that represent the device properties that are set for a device instance.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552128" data-raw-source="[&lt;strong&gt;SetupDiSetClassProperty&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552128)"><strong>SetupDiSetClassProperty</strong></a></p></td>
<td align="left"><p>Sets a class property for a device setup class or a device interface class.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552132" data-raw-source="[&lt;strong&gt;SetupDiSetClassPropertyEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552132)"><strong>SetupDiSetClassPropertyEx</strong></a></p></td>
<td align="left"><p>Sets a device property for a device setup class or a device interface class on a local or remote computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552158" data-raw-source="[&lt;strong&gt;SetupDiSetDeviceInterfaceProperty&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552158)"><strong>SetupDiSetDeviceInterfaceProperty</strong></a></p></td>
<td align="left"><p>Sets a device property of a device interface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552163" data-raw-source="[&lt;strong&gt;SetupDiSetDeviceProperty&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552163)"><strong>SetupDiSetDeviceProperty</strong></a></p></td>
<td align="left"><p>Sets a device instance property.</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="ddk-setupdi-registry-functions-dg"></a>Registry Functions

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550973" data-raw-source="[&lt;strong&gt;SetupDiCreateDevRegKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550973)"><strong>SetupDiCreateDevRegKey</strong></a></p></td>
<td align="left"><p>Creates a registry storage key for device-specific configuration information and returns a handle to the key.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552079" data-raw-source="[&lt;strong&gt;SetupDiOpenDevRegKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552079)"><strong>SetupDiOpenDevRegKey</strong></a></p></td>
<td align="left"><p>Opens a registry storage key for device-specific configuration information and returns a handle to the key.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550991" data-raw-source="[&lt;strong&gt;SetupDiDeleteDevRegKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550991)"><strong>SetupDiDeleteDevRegKey</strong></a></p></td>
<td align="left"><p>Deletes the specified user-accessible registry key(s) associated with a device information element.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552065" data-raw-source="[&lt;strong&gt;SetupDiOpenClassRegKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552065)"><strong>SetupDiOpenClassRegKey</strong></a></p></td>
<td align="left"><p>Opens the setup class registry key, or a specific subkey of the class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552067" data-raw-source="[&lt;strong&gt;SetupDiOpenClassRegKeyEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552067)"><strong>SetupDiOpenClassRegKeyEx</strong></a></p></td>
<td align="left"><p>Opens the device setup class registry key, the device interface class registry key, or a specific subkey of the class.</p>
<p>This function opens the specified key on the local computer or on a remote computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550967" data-raw-source="[&lt;strong&gt;SetupDiCreateDeviceInterfaceRegKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550967)"><strong>SetupDiCreateDeviceInterfaceRegKey</strong></a></p></td>
<td align="left"><p>Creates a nonvolatile registry subkey for storing information about a device interface instance and returns a handle to the key.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552075" data-raw-source="[&lt;strong&gt;SetupDiOpenDeviceInterfaceRegKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552075)"><strong>SetupDiOpenDeviceInterfaceRegKey</strong></a></p></td>
<td align="left"><p>Opens the registry subkey that is used by applications and drivers to store information that is specific to a device interface instance and returns a handle to the key.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff550986" data-raw-source="[&lt;strong&gt;SetupDiDeleteDeviceInterfaceRegKey&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550986)"><strong>SetupDiDeleteDeviceInterfaceRegKey</strong></a></p></td>
<td align="left"><p>Deletes the registry subkey that was used by applications and drivers to store information that is specific to a device interface instance.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552169" data-raw-source="[&lt;strong&gt;SetupDiSetDeviceRegistryProperty&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552169)"><strong>SetupDiSetDeviceRegistryProperty</strong></a></p></td>
<td align="left"><p>Sets the specified Plug and Play device property.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551967" data-raw-source="[&lt;strong&gt;SetupDiGetDeviceRegistryProperty&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551967)"><strong>SetupDiGetDeviceRegistryProperty</strong></a></p></td>
<td align="left"><p>Retrieves the specified Plug and Play device property.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551097" data-raw-source="[&lt;strong&gt;SetupDiGetClassRegistryProperty&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551097)"><strong>SetupDiGetClassRegistryProperty</strong></a></p></td>
<td align="left"><p>Retrieves a specified device class property from the registry.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552135" data-raw-source="[&lt;strong&gt;SetupDiSetClassRegistryProperty&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552135)"><strong>SetupDiSetClassRegistryProperty</strong></a></p></td>
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551029" data-raw-source="[&lt;strong&gt;SetupDiGetActualModelsSection&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551029)"><strong>SetupDiGetActualModelsSection</strong></a></p></td>
<td align="left"><p>Retrieves the appropriate decorated <a href="inf-models-section.md" data-raw-source="[&lt;strong&gt;INF Models section&lt;/strong&gt;](inf-models-section.md)"><strong>INF Models section</strong></a> to use when installing a device from a device INF file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551039" data-raw-source="[&lt;strong&gt;SetupDiGetActualSectionToInstall&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551039)"><strong>SetupDiGetActualSectionToInstall</strong></a></p></td>
<td align="left"><p>Retrieves the appropriate <em>DDInstall</em> section to use when installing a device from a device INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551045" data-raw-source="[&lt;strong&gt;SetupDiGetActualSectionToInstallEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551045)"><strong>SetupDiGetActualSectionToInstallEx</strong></a></p></td>
<td align="left"><p>Retrieves the name of the INF <em>DDInstall</em> section that installs a device for a specified operating system and processor architecture.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551983" data-raw-source="[&lt;strong&gt;SetupDiGetHwProfileFriendlyName&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551983)"><strong>SetupDiGetHwProfileFriendlyName</strong></a></p></td>
<td align="left"><p>Retrieves the friendly name associated with a hardware profile ID.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551989" data-raw-source="[&lt;strong&gt;SetupDiGetHwProfileFriendlyNameEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551989)"><strong>SetupDiGetHwProfileFriendlyNameEx</strong></a></p></td>
<td align="left"><p>Retrieves the friendly name associated with a hardware profile ID on a local or remote computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551997" data-raw-source="[&lt;strong&gt;SetupDiGetHwProfileList&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551997)"><strong>SetupDiGetHwProfileList</strong></a></p></td>
<td align="left"><p>Retrieves a list of all currently defined hardware profile IDs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552006" data-raw-source="[&lt;strong&gt;SetupDiGetHwProfileListEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552006)"><strong>SetupDiGetHwProfileListEx</strong></a></p></td>
<td align="left"><p>Retrieves a list of all currently defined hardware profile IDs on a local or remote computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552104" data-raw-source="[&lt;strong&gt;SetupDiRestartDevices&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552104)"><strong>SetupDiRestartDevices</strong></a></p></td>
<td align="left"><p>Restarts a specified device or, if necessary, starts all devices that are operated by the same function and filter drivers as the specified device.</p></td>
</tr>
</tbody>
</table>

 

 

 





