---
title: DEVPKEY_DrvPkg_Icon
description: DEVPKEY_DrvPkg_Icon
ms.assetid: 30aa817c-9dda-4504-b51a-78ef91d0cf01
keywords: ["DEVPKEY_DrvPkg_Icon Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DrvPkg_Icon
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_DrvPkg_Icon


The DEVPKEY_DrvPkg_Icon device property represents a list of device icons that Windows uses to visually represent a device instance.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_DrvPkg_Icon</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-string-list.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_STRING_LIST&lt;/strong&gt;](devprop-type-string-list.md)"><strong>DEVPROP_TYPE_STRING_LIST</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>Yes</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Each icon in the list is specified by a path of an icon file (\*.ico) or a reference to an icon resource in an executable file.

The first icon in the list is used as the default. Additional icons can be supplied that provide different visual representations of a device. Windows includes a user interface that allows a user to select which icon Windows displays. For example, the Microsoft DiscoveryCam 530 is available in blue, green, and red. Microsoft supplies an icon for each color. Windows uses the blue icon by default because it is the first one in the list. However, Windows users can also choose the green icon or the red icon.

The icon list is a NULL-separated list of icon specifiers. An icon specifier is either a path of an icon file (\*.ico) or an icon-resource specifier, as follows:

-   The format of the path to an icon file is *DirectoryPath\\filename.ico.*

-   An icon-resource specifier has the following entries:

    ```cpp
    @executable-file-path,resource-identifier
    ```

    The first character of icon-resource specifier is the at sign (@) followed by the path of an executable file (an *\*.exe* or a *\*.dll* file), followed by a comma separator (,), and then the *resource-identifier* entry.

For example, the icon specifier"@shell32.dll,-30" represents the executable file "shell32.dll" and the resource identifier "-30".

A resource identifier must be an integer value, which corresponds to a resource within the executable file, as follows:

-   If the supplied identifier is negative, Windows uses the resource in the executable file whose identifier is equal to the absolute value of the supplied identifier.

-   If the supplied identifier is zero, Windows uses the resource in the executable file whose identifier has the lowest value in the execuable file.

-   If the supplied identifier is positive, for example, the value *n*, Windows uses the resource in the executable file whose identifier is the n+1 lowest value in the executable file. For example, if the value of *n* is 1, Windows uses the resource whose identifier has the second lowest value in the executable file.

You can set the value of DEVPKEY_DrvPkg_Icon by an [**INF AddProperty directive**](https://msdn.microsoft.com/library/windows/hardware/ff546318) that is included in the [**INF *DDInstall* section**](https://msdn.microsoft.com/library/windows/hardware/ff547344) of the INF file that installs the device. You can retrieve the value of DEVPKEY_DrvPkg_Icon by calling [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963).

The following is an example of how to use an INF **AddProperty** directive to set DEVPKEY_DrvPkg_Icon for a device that is installed by an INF *DDInstall* section "SampleDDInstallSection":

```cpp
[SampleDDinstallSection]
...
AddProperty=SampleAddPropertySection
...

[SampleAddPropertySection] 
DeviceIcon,,,,"SomeResource.dll,-2","SomeIcon.icon"
...
```

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows Vista and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Devpkey.h (include Devpkey.h)</td>
</tr>
</tbody>
</table>

## See also


[**INF AddProperty Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546318)

[**INF *DDInstall* Section**](https://msdn.microsoft.com/library/windows/hardware/ff547344)

[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

 

 






