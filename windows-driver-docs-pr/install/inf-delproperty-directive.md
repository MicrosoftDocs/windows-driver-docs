---
title: INF DelProperty Directive
description: DelProperty references INF file sections that delete device properties for a device instance, a device setup class, a device interface class, or a device interface.
ms.assetid: fff227de-1664-4c9b-8709-1a8e1966bd79
keywords:
- INF DelProperty Directive Device and Driver Installation
topic_type:
- apiref
api_name:
- INF DelProperty Directive
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF DelProperty Directive


**Note**  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

A **DelProperty** directive references one or more INF file sections that delete [device properties](device-properties.md) for a device instance, a [device setup class](device-setup-classes.md), a [device interface class](device-interface-classes.md), or a device interface.

```cpp
[DDInstall] | 
[DDInstall.CoInstallers] | 
[ClassInstall32] | 
[ClassInstall32.ntx86] | 
[ClassInstall32.ntia64] |  (Windows XP and later versions of Windows)
[ClassInstall32.ntamd64] |  (Windows XP and later versions of Windows)
[interface-install-section] | 
[interface-install-section.nt] | 
[interface-install-section.ntx86] | 
[interface-install-section.ntia64] |  (Windows XP and later versions of Windows)
[interface-install-section.ntamd64] |  (Windows XP and later versions of Windows)
[add-interface-section] 
 
DelProperty=del-property-section[,del-property-section]...  (Windows Vista and later versions of Windows)
```

A **DelProperty** directive can be specified under any of the sections shown in the formal syntax statement above.

A *del-property-section* that is referenced by a **DelProperty** directive has the following format:

```cpp
[del-property-section]
(property-name [ ,, flags [, value]]) | ({property-category-guid}, property-pid [ , flags [, value]])
(property-name [ ,, flags [, value]]) | ({property-category-guid}, property-pid [ , flags [, value]])
...
```

A *del-property-section* can have any number of *property-name* entries or *property-guid* entries, each on a separate line.

## Entries


<a href="" id="property-name"></a>*property-name*  
One of the property names that represent the device instance [driver package](driver-packages.md) properties. The property names that are supported are the same as those that are described for the *property-name* entry of the [**INF AddProperty directive**](inf-addproperty-directive.md).

<a href="" id="property-category-guid"></a>*property-category-guid*  
A GUID value that identifies the property category. The GUID value can be a system-defined GUID that identifies a system-defined property category or a custom GUID that identifies a custom property category. The GUID values that are supported are the same as those that are described for the *property-category-guid* entry of the INF [**AddProperty**](inf-addproperty-directive.md) directive.

<a href="" id="property-pid"></a>*property-pid*  
A property identifier that indicates the specific property within the property category that is indicated by the *property-category-guid* value. For internal system reasons, a property identifier must be greater than or equal to two.

<a href="" id="flags"></a>*flags*  
An optional hexadecimal flag value that controls the delete operation. The only flag value supported is as follows:

<a href="" id="0x00000001--flg-delproperty-multi-sz-delstring-"></a>**0x00000001** (FLG_DELPROPERTY_MULTI_SZ_DELSTRING)  
If the property data type is [**DEVPROP_TYPE_STRING_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff543614), the operation deletes all the strings with the existing string list that match the string that is supplied by the value entry value. The case of a character is not considered in the comparison between the supplied string and an existing string in the string list.

<a href="" id="value"></a>*value*  
If the property data type is DEVPROP_TYPE_STRING_LIST and the flags entry is **0x00000001**, the *value* entry value supplies the string that the delete operation uses to search for matching strings in the existing string list and, if a matching string is found, the delete operation removes the matching string from the existing string list.

Remarks
-------

In general, an INF file should not be used to delete device properties that might be set by a system component or by another INF file. The primary purpose of the **DelProperty** directive is for use in an INF file that updates a previous device installation and a property that was set for a previous device installation is no longer required.

A *del-property-section* name must be unique within an INF file, but the section name can be referenced by more than one **DelProperty**directive in the same INF file. A section name must follow the general rules for defining section names that are described in [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

For more information about how to use the **DelProperty** directive, see [Using the INF AddProperty Directive and the INF DelProperty Directive](using-the-inf-addproperty-directive-and-the-inf-delproperty-directive.md).

Examples
--------

The following example of a delete property section includes two line entries: the first line entry includes a *property-name* entry value that deletes the **DeviceModel** property, and the second line entry deletes the string "DeleteThisString" from a custom device property value whose data type is DEVPROP_TYPE_STRING_LIST. In the second line, the *property-category-guid* entry value is "c22189e4-8bf3-4e6d-8467-8dc6d95e2a7e," the *property-identifier* entry value is "2," and the *flags* entry value is "0x00000001,"

```cpp
[SampleDelPropertySection]
DeviceModel
{c22189e4-8bf3-4e6d-8467-8dc6d95e2a7e}, 2, 0x00000001, "DeleteThisString"
```

## See also


[**AddProperty**](inf-addproperty-directive.md)

 

 






