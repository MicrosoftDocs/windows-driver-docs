---
title: WMI Generic Property Page Provider
description: WMI Generic Property Page Provider
ms.assetid: 44cfafdf-c8e2-4175-95e5-3c5d03dc206d
keywords: ["WMI WDK kernel , property sheets", "property sheets WDK WMI", "generic property page providers WDK WMI", "property pages WDK WMI", "property qualifiers WDK WMI", "device property sheets WDK WMI"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# WMI Generic Property Page Provider





On Windows XP and later operating systems, drivers can expose their WMI classes through the WMI generic property page provider. The provider uses each class declaration to create a simple property page for the class properties.

### How Property Qualifiers Determine the Property Page

The WMI generic property page provider uses a control appropriate for the data type of each property in the class. The following property qualifiers modify the type of control used:

-   **Write**

    A property with the **write** qualifier can be changed through the property page. Otherwise the property is read-only.

-   **Values** and **ValuesMap**

    The generic property page provider uses a list box to represent the possible values.

-   **Range**

    The generic property page provider validates that the data entered conforms to the specified range.

-   **DisplayName**

    The generic property page provider uses the value of this property qualifier as the label for the property.

-   **DisplayInHex**

    If present, the property value is displayed in hexadecimal.

Driver writers should localize property qualifiers that are strings. See [Localizing MOF Files](localizing-mof-files.md) for details.

### Enabling the Generic Property Page Provider

Each device that exposes classes to be used by Wmiprop.dll must enable Wmiprop.dll as a co-installer. To do this, make the following addition to the co-installer *add-registry-section*: add a value entry for the class GUID under the **HKLM\\System\\CurrentControlSet\\Control\\CoDeviceInstallers** registry key. The value for the value entry is "WmiProp.dll, WmiPropCoInstaller".

For example:

```cpp
; This section is defined in the Co-installer section, as follows.
; [Co-installer]
; AddReg = CoInstaller_AddReg

[CoInstaller_AddReg] 
HKLM, System\CurrentControlSet\Control\CoDeviceInstallers, ClassGUID,
    0x00010000, "WmiProp.dll, WmiPropCoInstaller"
```

*ClassGUID* is the GUID for the WMI class. See [Registering a Class Co-installer](https://msdn.microsoft.com/library/windows/hardware/ff549801) for details.

You must also specify the particular WMI classes to be exposed through the generic property provider. To do this, set the **WmiConfigClasses** value-entry to be a comma-separated list of the WMI classes in the *add-registry-section* of the device class or device hardware instance.

```cpp
; the device class AddReg section.
[device_class_AddReg]
HKR,,"WmiConfigClasses",0x00000000,"class1,class2"

; the device hardware instance AddReg section.
[device_hw_inst_AddReg]
HKR,,"WmiConfigClasses",0x00000000,"class3"
```

See [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320) for a description of an *add-registry-section* in INF files.

Wmiprop.dll assumes only one instance of each class. Each class is represented by a tab on the property sheet. Use the **DisplayName** property qualifier to set the title text of the tab. A property page for a class only appears if there is currently an instance of the class. Therefore, if the device is removed or not started, the pages do not appear.

 

 




