---
title: INF AddProperty Directive
description: An AddProperty directive references one or more INF file sections that modify the device properties that are set for a device instance, a device setup class, a device interface class, or a device interface.
ms.assetid: 8fcb1355-f13d-4d96-aa73-62a094a52267
keywords:
- INF AddProperty Directive Device and Driver Installation
topic_type:
- apiref
api_name:
- INF AddProperty Directive
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF AddProperty Directive


An **AddProperty** directive references one or more INF file sections that modify the [device properties](device-properties.md) that are set for a device instance, a [device setup class](device-setup-classes.md), a [device interface class](device-interface-classes.md), or a device interface.

```cpp
[DDInstall] |
[DDInstall.nt] |
[DDInstall.ntx86] |
[DDInstall.ntia64] |
[DDInstall.ntamd64]
[ClassInstall32] | 
[ClassInstall32.nt] | 
[ClassInstall32.ntx86] |
[ClassInstall32.ntia64] |  (Windows XP and later versions of Windows)
[ClassInstall32.ntamd64]  |  (Windows XP and later versions of Windows)
[interface-install-section] | 
[interface-install-section.nt] | 
[interface-install-section.ntx86] | 
[interface-install-section.ntia64] |  (Windows XP and later versions of Windows)
[interface-install-section.ntamd64]  (Windows XP and later versions of Windows)
[add-interface-section]

AddProperty=add-property-section[,add-property-section]...  (Windows Vista and later versions of Windows)
...
```

Each *add-property-section* can have entries to do the following:

-   Add a device property and initialize the value of the property.
-   Modify the value of an existing device property.

An *add-property-section* that is referenced by an **AddProperty** directive has the following format:

```cpp
[add-property-section]
(property-name, , , [flags], value]) | 
({property-category-guid}, property-pid, type, [flags], value)
...
```

An add property section can have any number of *property-name* entries or *property-guid* entries, each on a separate line.

## Entries


<a href="" id="property-name"></a>*property-name*  
One of the following property names that represent the device instance [driver package](driver-packages.md) properties:

-   **DeviceModel**
-   **DeviceVendorWebsite**
-   **DeviceDetailedDescription**
-   **DeviceDocumentationLink**
-   **DeviceIcon**
-   **DeviceBrandingIcon**

<a href="" id="property-category-guid"></a>*property-category-guid*  
A GUID value that identifies the property category. The GUID value can be a system-defined GUID that identifies one of the property categories for a device instance, a [device setup class](device-setup-classes.md), a [device interface class](device-interface-classes.md), or a device interface. All properties that have the same GUID value are members of the same category. These property categories are defined in *Devpkey.h*.

The GUID value can also be a custom GUID value that identifies a custom property category.

<a href="" id="property-pid"></a>*property-pid*  
The property identifier that indicates the specific property within the property category that is indicated by the *property-category-guid* value. For internal system reasons, a property identifier must be greater than or equal to two.

<a href="" id="type"></a>type  
The numeric value, in decimal or hexadecimal format, of the [property-data-type identifier](https://msdn.microsoft.com/library/windows/hardware/ff541476) for the property that is specified by the *property-category-guid* value and the *property-pid* value. Only the following [**base data types**](https://msdn.microsoft.com/library/windows/hardware/ff537793) are supported:

-   DEVPROP_TYPE_STRING
-   DEVPROP_TYPE_STRING_LIST
-   DEVPROP_TYPE_BINARY
-   DEVPROP_TYPE_BOOLEAN
-   DEVPROP_TYPE_UINT32

For example, the decimal value of the DEVPROP_TYPE_STRING data type is 18 (0x00000012) and the decimal value of the DEVPROP_TYPE_STRING_LIST data type is 2066 (0x00002012).

<a href="" id="flags"></a>*flags*  
An optional hexadecimal value that is a bitwise OR of the following flags that control the add operation:

<a href="" id="0x00000001--flg-addproperty-noclobber--"></a>**0x00000001** (FLG_ADDPROPERTY_NOCLOBBER)   
A flag that prevents the value entry value from replacing the existing property value. If a driver writer wants to make a property able to be overridden through **Include** and **Needs** directives, the writer must specify this flag for that property. This is because Windows processes the INF sections that are referenced by **Include** and **Needs** directives after Windows processes all other directives within the INF section that included the **Include** and **Needs** directives.

<a href="" id="0x00000002--flg-addproperty-overwriteonly--"></a>**0x00000002** (FLG_ADDPROPERTY_OVERWRITEONLY)   
A flag that sets the property value to the value entry value only if the specified property already exists.

<a href="" id="0x00000004--flg-addproperty-append--"></a>**0x00000004** (FLG_ADDPROPERTY_APPEND)   
A flag that appends the value entry value to that of an existing property string value. This flag is valid only if the property data type is DEVPROP_TYPE_STRING_LIST. The supplied string is not appended to an existing property string value if the supplied string is already present in the existing string value.

<a href="" id="0x00000008--flg-addproperty-or-"></a>**0x00000008** (FLG_ADDPROPERTY_OR)  
A flag that performs a bitwise OR of the value entry value to that of the existing property value. This flag is valid only if the property data type is DEVPROP_TYPE_UINT32.

<a href="" id="0x00000010--flg-addproperty-and-"></a>**0x00000010** (FLG_ADDPROPERTY_AND)  
A flag that performs a bitwise AND of the value entry value to that of the existing property value. This flag is valid only if the property data type is DEVPROP_TYPE_UINT32.

<a href="" id="value"></a>*value*  
The value that the add operation uses to modify a property value, depending on the property data type and the value of the *flags* entry.

Remarks
-------

The **AddProperty** directive can be used to modify a system-defined device property or a custom device property. This directive can be specified under any of the sections shown in the formal syntax statement above.

Each *add-property-section* name must be unique within an INF file, but the section can be referenced by more than one **AddProperty** directive in the same INF file. Each section name must follow the general rules for defining section names that are described in [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

For more information about how to use the INF **AddProperty** directive, see [Using the INF AddProperty Directive and the INF DelProperty Directive](using-the-inf-addproperty-directive-and-the-inf-delproperty-directive.md).

Examples
--------

The following example of an add property section includes two line entries: the first line entry sets the **DeviceModel** property by name, and the second line entry sets a custom device property by specifying a custom property key GUID.

The first line includes the *property-name* entry value "DeviceModel" and the *value* entry value "Sample Device Model Name."

The second line entry sets a custom property in a custom property category. The property-category-guid entry value is "c22189e4-8bf3-4e6d-8467-8dc6d95e2a7e" and the property-identifier entry value is "2".

The optional *flags* entry value is not present, and the type entry value is "18" (DEVPROP_TYPE_STRING). The value entry value is "String value for property 1."

```cpp
[SampleAddPropertySection]
DeviceModel,,,,"Sample Device Model Name"
{c22189e4-8bf3-4e6d-8467-8dc6d95e2a7e}, 2, 18,, "String value for property 1"
```

## See also


[**DelProperty**](inf-delproperty-directive.md)

 

 






