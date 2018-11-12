---
title: Using the INF AddProperty Directive and INF DelProperty Directive
description: Using the INF AddProperty Directive and the INF DelProperty Directive
ms.assetid: e5ae8d66-b2dc-409e-bdac-9034a9e24672
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using the INF AddProperty Directive and the INF DelProperty Directive


In Windows Vista and later versions of Windows, you can use [**INF AddProperty directives**](inf-addproperty-directive.md) and [**INF DelProperty directives**](inf-delproperty-directive.md) to set and delete properties for device instances, [device setup classes](device-setup-classes.md), [device interface classes](device-interface-classes.md), and device interfaces. This includes [system-defined device properties](system-defined-device-properties2.md) and [custom device properties](creating-custom-device-properties.md). However, you should use the following guidelines when you use **AddProperty** and **DelProperty** directives instead of [**INF AddReg directives**](inf-addreg-directive.md) and [**INF DelReg directives**](inf-delreg-directive.md) to set and delete device properties:

-   For device properties that were introduced on Windows Vista and later versions of Windows, you should use **AddProperty** and **DelProperty** directives to set and delete device properties.

-   For device properties that were introduced on Windows Server 2003, Windows XP, or Windows 2000, and that can be set by the **AddReg** directive and deleted by the **DelReg** directive, you should continue to use **AddReg** and **DelReg** directives to set and delete these device properties. You should not use **AddProperty** and **DelProperty** directives.

You can include the INF **AddProperty** directive and the INF **DelProperty** directive in the following INF file sections to set and delete properties for device instances, device setup classes, device interface classes, and device interfaces:

-   [**INF DDInstall Section**](inf-ddinstall-section.md)

-   [**INF ClassInstall32 Section**](inf-classinstall32-section.md)

-   An *install-interface-section* that is referenced by an [**INF InterfaceInstall32 section**](inf-interfaceinstall32-section.md)

-   An *add-interface-section* that is referenced by an [**INF AddInterface Directive**](inf-addinterface-directive.md)

### Using the INF AddProperty Directive

To modify a property value, include an INF **AddProperty** directive in the section that installs a device instance, a device setup class, a device interface class, or a device interface. An **AddProperty** directive references one or more *add-property-sections* that include entries that specify the property, how to modify the property, and the value that is used to modify the property. The format of an **AddProperty** directive is as follows:

**AddProperty=**<em>add-property-section</em>\[**,**<em>add-property-section</em>\] ...

Each line in an add-property-section specifies one property. The following shows the two possible line formats that specify property information. The first line format shown specifies a property by its name. This format can be used only with the DEVPKEY_DrvPkg_*Xxx* properties. The second line format specifies a property by the property category and property identifier of the corresponding [property key](property-keys.md). This second format can be used to specify a system-defined property or a [custom device property](creating-custom-device-properties.md).

**\[**<em>add-property-section</em>**\]**
<em>property-name</em>**,,,\[**<em>flags</em>**\],**<em>value</em>
**{**<em>property-category-guid</em>**},**<em>property-pid</em>**,**<em>type</em>**,\[**<em>flags</em>**\],**<em>value</em>
The entry values supply the following:

<a href="" id="property-name"></a>*property-name*  
The name that identifies a DEVPKEY_DrvPkg_*Xxx* property. For example, **DeviceModel**, which represents the [**DEVPKEY_DrvPkg_Model**](https://msdn.microsoft.com/library/windows/hardware/ff543523) property, or **DeviceVendorWebSite**, which represents the [**DEVPKEY_DrvPkg_VendorWebSite**](https://msdn.microsoft.com/library/windows/hardware/ff543527) property.

<a href="" id="property-category-guid"></a>*property-category-guid*  
The GUID value of the property category to which the property belongs. For example, the system-defined [**DEVPKEY_Device_FriendlyName**](https://msdn.microsoft.com/library/windows/hardware/ff542502) property. The GUID value can also specify a custom device category.

<a href="" id="property-pid"></a>*property-pid*  
The property identifier that identifies a property within a property category. For example, the value of the property identifier for the DEVPKEY_Device_FriendlyName property is 14.

<a href="" id="flags"></a>*Flags*  
An optional flag that indicates how to modify the property value.

<a href="" id="type"></a>*Type*  
A [property-data-type identifier](property-data-type-identifiers.md) that specifies the data type.

<a href="" id="value"></a>*value*  
The value that is used to modify the property value.

The following example of an **AddProperty** directive includes two line entries. The first line includes the *property-name* entry value "DeviceModel" and the *value* entry value "Sample Device Model Name." This entry sets the DEVPKEY_DrvPkg_Model property. The second line entry sets a custom property in a custom property category. The *property-category-guid* entry value is "c22189e4-8bf3-4e6d-8467-8dc6d95e2a7e" and the *property-identifier* entry value is "2." The optional *Flags* entry value is not present and the *type* entry value is "18" (DEVPROP_TYPE_STRING). The *value* entry value is "String value for property 1."

```cpp
[Root_Install.NT]
AddProperty=Root_AddProperty

[Root_AddProperty]
DeviceModel,,,,"Sample Device Model Name"
{c22189e4-8bf3-4e6d-8467-8dc6d95e2a7e}, 2, 18,, "String value for property 1"
```

### Using the INF DelProperty Directive

To delete a property, include an INF **DelProperty** directive in the section that installs a device instance, a device setup class, a device interface class, or a device interface.

The main purpose of the [**INF DelProperty directive**](inf-delproperty-directive.md) is for use in an INF file that updates a device installation. In such a case, the **DelProperty** directive can be used to delete a property that was set by a previous installation, but is no longer required by the updated installation. Use the **DelProperty** directive with caution. **DelProperty** should not be used to delete a property that might be also set by a system component or by another INF file.

The **DelProperty** directive has the following format:

**DelProperty=**<em>del-property-section</em>\[**,**<em>del-property-section</em>\] ...

Each line in a *del-property-section* specifies one property. The following shows the two possible line formats that specify property information. The first line format shown specifies a property by its name. This format can be used only with the DEVPKEY_DrvPkg_*Xxx* properties. The second line format specifies a property by the property category and property identifier of the corresponding [property key](property-keys.md). The second format can be used to specify a system-defined property or a [custom device property](creating-custom-device-properties.md).

**\[**<em>del-property-section</em>**\]**
*property-name* \[**,,** *Flags* \[**,**<em>value</em>\]\]
**{**<em>property-category-guid</em>**},** *property-pid* \[**,** *Flags* \[**,**<em>value</em>\]\]
The entry values supply the following:

<a href="" id="property-name"></a>*property-name*  
The name that identifies a DEVPKEY_DrvPkg_*Xxx* property. For example, **DeviceModel**, which represents the [**DEVPKEY_DrvPkg_Model**](https://msdn.microsoft.com/library/windows/hardware/ff543523) property, or **DeviceVendorWebSite**, which represents the [**DEVPKEY_Device_FriendlyName**](https://msdn.microsoft.com/library/windows/hardware/ff542502) property.

<a href="" id="property-category-guid"></a>*property-category-guid*  
The GUID value of the property category to which the property belongs. For example, the system-defined [**DEVPKEY_Device_FriendlyName**](https://msdn.microsoft.com/library/windows/hardware/ff542502) property. The GUID value can also specify a custom device category.

<a href="" id="property-pid"></a>*property-pid*  
The property identifier that identifies a property within a property category. For example, the value of the property identifier for the DEVPKEY_Device_FriendlyName property is 14.

<a href="" id="flags"></a>*Flags*  
An optional flag that is valid for use only with a property whose data type is [**DEVPROP_TYPE_STRING_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff543614). If the flag is set, the delete operation deletes the string that is specified by *value* from the property string list.

<a href="" id="value"></a>*value*  
The string to delete from a property string list.

The following example of a *del-property-section* includes two line entries.

The first line includes the *property-name* entry value "DeviceModel", which deletes the DEVPKEY_DrvPkg_Model property. The second line entry deletes the string "DeleteThisString" from a custom device property value whose data type is DEVPROP_TYPE_STRING_LIST. In the second line, the *property-category-guid* entry value is "c22189e4-8bf3-4e6d-8467-8dc6d95e2a7e", the *property-identifier* entry value is "2", and the *Flags* entry value is "0x00000001."

```cpp
[SampleDelPropertySection]
DeviceModel
{c22189e4-8bf3-4e6d-8467-8dc6d95e2a7e}, 2, 0x00000001, "DeleteThisString"
```

 

 





