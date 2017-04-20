---
title: Using Device Installation Functions
description: Using Device Installation Functions
ms.assetid: a7cfa359-a45c-45fa-a854-ee70de66b12e
keywords:
- SetupAPI functions WDK , device installation functions
- device installation functions WDK SetupAPI
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using Device Installation Functions


## <a href="" id="ddk-using-device-installation-functions-dg"></a>


This section summarizes the [device installation functions](https://msdn.microsoft.com/library/windows/hardware/ff541299). By using the device installation functions, the installation software can perform the following types of operations:

-   Install drivers

-   Handle DIF codes.

-   Manage device information sets.

-   Manage driver lists.

-   Manage device interfaces.

-   Manage icons and other bitmaps.

To perform device installation operations that are not supported by the SetupAPI functions described in this section, call the appropriate [general Setup functions](https://msdn.microsoft.com/library/windows/hardware/ff544985) or [PnP Configuration Manager functions](https://msdn.microsoft.com/library/windows/hardware/ff549717) (CM\_*Xxx* functions*).*

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
<td align="left"><p>[<strong>DiInstallDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544710)</p></td>
<td align="left"><p>Installs a specified driver that is preinstalled in the [driver store](driver-store.md) on a PnP device that is present in the system. (Windows Vista and later versions of Windows)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DiInstallDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544717)</p></td>
<td align="left"><p>Preinstalls a driver in the driver store and then installs the driver on matching PnP devices that are present in the system. (Windows Vista and later versions of Windows)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DiRollbackDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544721)</p></td>
<td align="left"><p>Rolls back the driver that is installed on a specified device to the backup driver set for the device. (Windows Vista and later versions of Windows)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DiShowUpdateDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544727)</p></td>
<td align="left"><p>Displays the Hardware Update wizard for a specified device. (Windows Vista and later versions of Windows)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DiUninstallDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544754)</p></td>
<td align="left"><p>Uninstalls a device and removes its device node ([<em>devnode</em>](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) ) from the system. (Windows 7 and later versions of Windows)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>InstallSelectedDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547654)</p></td>
<td align="left"><p>Installs a selected driver on a selected device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>UpdateDriverForPlugAndPlayDevices</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553534)</p></td>
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
<td align="left"><p>[<strong>SetupDiCreateDeviceInfoList</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550956)</p></td>
<td align="left"><p>Creates an empty [device information set](device-information-sets.md). This set can be associated with a class GUID.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiCreateDeviceInfoListEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550958)</p></td>
<td align="left"><p>Creates an empty device information set. This set can be associated with a class GUID and can be for devices on a remote computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiCreateDeviceInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550952)</p></td>
<td align="left"><p>Creates a new device information element and adds it as a new member to the specified device information set.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiOpenDeviceInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552071)</p></td>
<td align="left"><p>Retrieves information about an existing device instance and adds it to the specified device information set.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiEnumDeviceInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551010)</p></td>
<td align="left"><p>Returns a context structure for a device information element of a device information set.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiGetDeviceInstanceId</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551106)</p></td>
<td align="left"><p>Retrieves the device instance ID associated with a device information element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiGetDeviceInfoListClass</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551101)</p></td>
<td align="left"><p>Retrieves the class GUID associated with a device information set if it has an associated class.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiGetDeviceInfoListDetail</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551103)</p></td>
<td align="left"><p>Retrieves information associated with a device information set including the class GUID, remote computer handle, and remote computer name.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiGetClassDevPropertySheets</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551064)</p></td>
<td align="left"><p>Retrieves handles to the property sheets of a specified device information element or of the [device setup class](device-setup-classes.md) of a specified device information set.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiGetClassDevs</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551069)</p></td>
<td align="left"><p>Returns a device information set that contains all devices of a specified class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiGetClassDevsEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551072)</p></td>
<td align="left"><p>Returns a device information set that contains all devices of a specified class on a local or remote computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiSetSelectedDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552176)</p></td>
<td align="left"><p>Sets the specified device information element to be the currently-selected member of a device information set. This function is typically used by an installation wizard.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiGetSelectedDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552011)</p></td>
<td align="left"><p>Retrieves the currently-selected device for the specified device information set.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiRegisterDeviceInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552091)</p></td>
<td align="left"><p>Registers a newly created device instance with the Plug and Play manager.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiDeleteDeviceInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550978)</p></td>
<td align="left"><p>Deletes a member from the specified device information set. This function does not delete the actual device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiDestroyDeviceInfoList</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550996)</p></td>
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
<td align="left"><p>[<strong>SetupDiBuildDriverInfoList</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550917)</p></td>
<td align="left"><p>Builds a list of drivers associated with a specified device instance or with the device information set's global class driver list.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiEnumDriverInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551018)</p></td>
<td align="left"><p>Enumerates the members of a driver information list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiGetDriverInfoDetail</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551973)</p></td>
<td align="left"><p>Retrieves detailed information for a specified driver information element.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiSetSelectedDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552183)</p></td>
<td align="left"><p>Sets the specified member of a driver list as the currently selected-driver. It can also be used to reset the driver list so that there is no currently-selected driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiGetSelectedDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552013)</p></td>
<td align="left"><p>Retrieves the member of a driver list that was selected as the driver to install.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiCancelDriverInfoSearch</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550928)</p></td>
<td align="left"><p>Cancels a driver list search that is currently underway in a different thread.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiDestroyDriverInfoList</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551001)</p></td>
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
<td align="left"><p>[<strong>SetupDiAskForOEMDisk</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550905)</p></td>
<td align="left"><p>Displays a dialog that asks the user for the path of an OEM installation disk.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiSelectOEMDrv</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552121)</p></td>
<td align="left"><p>Selects a driver for a device by using an OEM path supplied by the user.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiSelectDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552115)</p></td>
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
<td align="left"><p>[<strong>SetupDiCallClassInstaller</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550922)</p></td>
<td align="left"><p>Calls the appropriate class installer, and any registered co-installers, with the specified installation request.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiChangeState</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550930)</p></td>
<td align="left"><p>The default handler for the DIF_PROPERTYCHANGE request. It can be used to change the state of an installed device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiRegisterCoDeviceInstallers</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552085)</p></td>
<td align="left"><p>Registers the device-specific co-installers listed in the INF file for the specified device. This function is the default handler for DIF_REGISTER_COINSTALLERS.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiInstallDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552039)</p></td>
<td align="left"><p>The default handler for the DIF_INSTALLDEVICE request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiInstallDriverFiles</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552048)</p></td>
<td align="left"><p>The default handler for the DIF_INSTALLDEVICEFILES request.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiInstallDeviceInterfaces</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552043)</p></td>
<td align="left"><p>The default handler for the DIF_INSTALLINTERFACES request. It installs the interfaces that are listed in a <em>DDInstall</em>.<strong>Interfaces</strong> section of a device INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiMoveDuplicateDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552062)</p></td>
<td align="left"><p>This function is obsolete and cannot be used in any version of Microsoft Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiRemoveDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552097)</p></td>
<td align="left"><p>The default handler for the DIF_REMOVEDEVICE request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiUnremoveDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552193)</p></td>
<td align="left"><p>The default handler for the DIF_UNREMOVE request.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiRegisterDeviceInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552091)</p></td>
<td align="left"><p>The default handler for the DIF_REGISTERDEVICE request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiSelectDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552115)</p></td>
<td align="left"><p>The default handler for the DIF_SELECTDEVICE request.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiSelectBestCompatDrv</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552112)</p></td>
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
<td align="left"><p>[<strong>SetupDiGetClassInstallParams</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551083)</p></td>
<td align="left"><p>Retrieves class install parameters for a device information set or a particular device information element.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiSetClassInstallParams</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552122)</p></td>
<td align="left"><p>Sets or clears class install parameters for a device information set or a particular device information element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiGetDeviceInstallParams</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551104)</p></td>
<td align="left"><p>Retrieves device install parameters for a device information set or a particular device information element.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiSetDeviceInstallParams</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552141)</p></td>
<td align="left"><p>Sets device install parameters for a device information set or a particular device information element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiGetDriverInstallParams</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551978)</p></td>
<td align="left"><p>Retrieves install parameters for the specified driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiSetDriverInstallParams</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552172)</p></td>
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
<td align="left"><p>[<strong>SetupDiBuildClassInfoList</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550909)</p></td>
<td align="left"><p>Returns a list of setup class GUIDs that includes every class installed on the system.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiBuildClassInfoListEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550911)</p></td>
<td align="left"><p>Returns a list of setup class GUIDs that includes every class installed on the local system or a remote system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiGetClassDescription</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551053)</p></td>
<td align="left"><p>Retrieves the class description associated with the specified setup class GUID.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiGetClassDescriptionEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551058)</p></td>
<td align="left"><p>Retrieves the description of a setup class installed on a local or remote computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiGetINFClass</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552010)</p></td>
<td align="left"><p>Retrieves the class of a specified device INF file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiClassGuidsFromName</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550937)</p></td>
<td align="left"><p>Retrieves the GUIDs associated with the specified class name. This list is built based on what classes are currently installed on the system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiClassGuidsFromNameEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550941)</p></td>
<td align="left"><p>Retrieves the GUIDs associated with the specified class name. This resulting list contains the classes currently installed on a local or remote computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiClassNameFromGuid</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550947)</p></td>
<td align="left"><p>Retrieves the class name associated with the class GUID.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiClassNameFromGuidEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550950)</p></td>
<td align="left"><p>Retrieves the class name associated with a class GUID. The class can be installed on a local or remote computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiInstallClass</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552024)</p></td>
<td align="left"><p>Installs the <strong>ClassInstall32</strong> section of the specified INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiInstallClassEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552032)</p></td>
<td align="left"><p>Installs a class installer or an interface class.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiOpenClassRegKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552065)</p></td>
<td align="left"><p>Opens the [device setup class](device-setup-classes.md) registry key, or a specific subkey of the class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiOpenClassRegKeyEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552067)</p></td>
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
<td align="left"><p>[<strong>SetupDiGetClassImageList</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551080)</p></td>
<td align="left"><p>Builds an image list that contains bitmaps for every installed class and returns the list in a data structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiGetClassImageListEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551081)</p></td>
<td align="left"><p>Builds an image list of bitmaps for every class installed on a local or remote computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiGetClassImageIndex</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551074)</p></td>
<td align="left"><p>Retrieves the index within the class image list of a specified class.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiGetClassBitmapIndex</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551047)</p></td>
<td align="left"><p>Retrieves the index of the mini-icon supplied for the specified class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiDrawMiniIcon</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551005)</p></td>
<td align="left"><p>Draws the specified mini-icon at the location requested.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiLoadClassIcon</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552053)</p></td>
<td align="left"><p>Loads both the large and mini-icon for the specified class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiLoadDeviceIcon</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552057)</p></td>
<td align="left"><p>Loads a device icon for a specified device. (Windows Vista and later versions of Windows)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiDestroyClassImageList</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550995)</p></td>
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
<td align="left"><p>[<strong>SetupDiCreateDeviceInterface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550965)</p></td>
<td align="left"><p>Registers device functionality (a device interface) for a device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiOpenDeviceInterface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552074)</p></td>
<td align="left"><p>Retrieves information about an existing device interface and adds it to the specified device information set.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiGetDeviceInterfaceAlias</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551108)</p></td>
<td align="left"><p>Returns an alias of the specified device interface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiGetClassDevs</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551072)</p></td>
<td align="left"><p>Returns a device information set that contains all devices of a specified class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiGetClassDevsEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551072)</p></td>
<td align="left"><p>Returns a device information set that contains all devices of a specified class on a local or remote computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiEnumDeviceInterfaces</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551015)</p></td>
<td align="left"><p>Returns a context structure for a device interface element of a device information set. Each call returns information about one device interface.</p>
<p>The function can be called repeatedly to obtain information about several interfaces exposed by one or more devices.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiGetDeviceInterfaceDetail</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551120)</p></td>
<td align="left"><p>Returns details about a particular device interface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiCreateDeviceInterfaceRegKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550967)</p></td>
<td align="left"><p>Creates a registry subkey for storing information about a device interface instance and returns a handle to the key.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiOpenDeviceInterfaceRegKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552075)</p></td>
<td align="left"><p>Opens the registry subkey that is used by applications and drivers to store information that is specific to a device interface instance and returns a handle to the key.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiDeleteDeviceInterfaceRegKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550986)</p></td>
<td align="left"><p>Deletes the registry subkey that was used by applications and drivers to store information that is specific to a device interface instance.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiInstallDeviceInterfaces</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552043)</p></td>
<td align="left"><p>Is the default handler for the DIF_INSTALLINTERFACES request. It installs the interfaces that are listed in a <em>DDInstall</em>.<strong>Interfaces</strong> section of a device INF file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiRemoveDeviceInterface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552102)</p></td>
<td align="left"><p>Removes a registered device interface from the system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiDeleteDeviceInterfaceData</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550984)</p></td>
<td align="left"><p>Deletes a device interface from a device information set.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiSetDeviceInterfaceDefault</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552149)</p></td>
<td align="left"><p>Sets a specified device interface as the default interface for a device class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiInstallClassEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552032)</p></td>
<td align="left"><p>Installs a class installer or an interface class.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiOpenClassRegKeyEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552067)</p></td>
<td align="left"><p>Opens the [device setup class](device-setup-classes.md) registry key, the device interface class registry key, or a specific subkey of the class. This function opens the specified key on the local computer or on a remote computer.</p></td>
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
<td align="left"><p>[<strong>SetupDiGetClassProperty</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551086)</p></td>
<td align="left"><p>Retrieves a device property that is set for a device setup class or a device interface class.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiGetClassPropertyEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551090)</p></td>
<td align="left"><p>Retrieves a class property for a device setup class or a device interface class on a local or remote computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiGetClassPropertyKeys</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551091)</p></td>
<td align="left"><p>Retrieves an array of the device property keys that represent the device properties that are set for a device setup class or a device interface class.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiGetClassPropertyKeysEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551093)</p></td>
<td align="left"><p>Retrieves an array of the device property keys that represent the device properties that are set for a device setup class or a device interface class on a local or a remote computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiGetDeviceInterfaceProperty</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551122)</p></td>
<td align="left"><p>Retrieves a device property that is set for a device interface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiGetDeviceInterfacePropertyKeys</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551959)</p></td>
<td align="left"><p>Retrieves an array of device property keys that represent the device properties that are set for a device interface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiGetDeviceProperty</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551963)</p></td>
<td align="left"><p>Retrieves a device instance property.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiGetDevicePropertyKeys</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551965)</p></td>
<td align="left"><p>Retrieves an array of the device property keys that represent the device properties that are set for a device instance.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiSetClassProperty</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552128)</p></td>
<td align="left"><p>Sets a class property for a device setup class or a device interface class.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiSetClassPropertyEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552132)</p></td>
<td align="left"><p>Sets a device property for a device setup class or a device interface class on a local or remote computer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiSetDeviceInterfaceProperty</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552158)</p></td>
<td align="left"><p>Sets a device property of a device interface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiSetDeviceProperty</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552163)</p></td>
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
<td align="left"><p>[<strong>SetupDiCreateDevRegKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550973)</p></td>
<td align="left"><p>Creates a registry storage key for device-specific configuration information and returns a handle to the key.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiOpenDevRegKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552079)</p></td>
<td align="left"><p>Opens a registry storage key for device-specific configuration information and returns a handle to the key.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiDeleteDevRegKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550991)</p></td>
<td align="left"><p>Deletes the specified user-accessible registry key(s) associated with a device information element.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiOpenClassRegKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552065)</p></td>
<td align="left"><p>Opens the setup class registry key, or a specific subkey of the class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiOpenClassRegKeyEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552067)</p></td>
<td align="left"><p>Opens the device setup class registry key, the device interface class registry key, or a specific subkey of the class.</p>
<p>This function opens the specified key on the local computer or on a remote computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiCreateDeviceInterfaceRegKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550967)</p></td>
<td align="left"><p>Creates a nonvolatile registry subkey for storing information about a device interface instance and returns a handle to the key.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiOpenDeviceInterfaceRegKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552075)</p></td>
<td align="left"><p>Opens the registry subkey that is used by applications and drivers to store information that is specific to a device interface instance and returns a handle to the key.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiDeleteDeviceInterfaceRegKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550986)</p></td>
<td align="left"><p>Deletes the registry subkey that was used by applications and drivers to store information that is specific to a device interface instance.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiSetDeviceRegistryProperty</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552169)</p></td>
<td align="left"><p>Sets the specified Plug and Play device property.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiGetDeviceRegistryProperty</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551967)</p></td>
<td align="left"><p>Retrieves the specified Plug and Play device property.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiGetClassRegistryProperty</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551097)</p></td>
<td align="left"><p>Retrieves a specified device class property from the registry.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiSetClassRegistryProperty</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552135)</p></td>
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
<td align="left"><p>[<strong>SetupDiGetActualModelsSection</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551029)</p></td>
<td align="left"><p>Retrieves the appropriate decorated [<strong>INF Models section</strong>](inf-models-section.md) to use when installing a device from a device INF file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiGetActualSectionToInstall</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551039)</p></td>
<td align="left"><p>Retrieves the appropriate <em>DDInstall</em> section to use when installing a device from a device INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiGetActualSectionToInstallEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551045)</p></td>
<td align="left"><p>Retrieves the name of the INF <em>DDInstall</em> section that installs a device for a specified operating system and processor architecture.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiGetHwProfileFriendlyName</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551983)</p></td>
<td align="left"><p>Retrieves the friendly name associated with a hardware profile ID.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiGetHwProfileFriendlyNameEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551989)</p></td>
<td align="left"><p>Retrieves the friendly name associated with a hardware profile ID on a local or remote computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiGetHwProfileList</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551997)</p></td>
<td align="left"><p>Retrieves a list of all currently defined hardware profile IDs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupDiGetHwProfileListEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552006)</p></td>
<td align="left"><p>Retrieves a list of all currently defined hardware profile IDs on a local or remote computer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDiRestartDevices</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552104)</p></td>
<td align="left"><p>Restarts a specified device or, if necessary, starts all devices that are operated by the same function and filter drivers as the specified device.</p></td>
</tr>
</tbody>
</table>

 

 

 





