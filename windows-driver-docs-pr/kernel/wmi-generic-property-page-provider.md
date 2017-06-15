---
title: WMI Generic Property Page Provider
author: windows-driver-content
description: WMI Generic Property Page Provider
MS-HAID:
- 'WMI\_84c1d77e-0d39-4bca-a148-2e661a0a879b.xml'
- 'kernel.wmi\_generic\_property\_page\_provider'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 44cfafdf-c8e2-4175-95e5-3c5d03dc206d
keywords: ["WMI WDK kernel , property sheets", "property sheets WDK WMI", "generic property page providers WDK WMI", "property pages WDK WMI", "property qualifiers WDK WMI", "device property sheets WDK WMI"]
---

# WMI Generic Property Page Provider


## <a href="" id="ddk-wmi-generic-property-page-provider-kg"></a>


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

```
; This section is defined in the Co-installer section, as follows.
; [Co-installer]
; AddReg = CoInstaller_AddReg

[CoInstaller_AddReg] 
HKLM, System\CurrentControlSet\Control\CoDeviceInstallers, ClassGUID,
    0x00010000, "WmiProp.dll, WmiPropCoInstaller"
```

*ClassGUID* is the GUID for the WMI class. See [Registering a Class Co-installer](https://msdn.microsoft.com/library/windows/hardware/ff549801) for details.

You must also specify the particular WMI classes to be exposed through the generic property provider. To do this, set the **WmiConfigClasses** value-entry to be a comma-separated list of the WMI classes in the *add-registry-section* of the device class or device hardware instance.

```
; the device class AddReg section.
[device_class_AddReg]
HKR,,"WmiConfigClasses",0x00000000,"class1,class2"

; the device hardware instance AddReg section.
[device_hw_inst_AddReg]
HKR,,"WmiConfigClasses",0x00000000,"class3"
```

See [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320) for a description of an *add-registry-section* in INF files.

Wmiprop.dll assumes only one instance of each class. Each class is represented by a tab on the property sheet. Use the **DisplayName** property qualifier to set the title text of the tab. A property page for a class only appears if there is currently an instance of the class. Therefore, if the device is removed or not started, the pages do not appear.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20WMI%20Generic%20Property%20Page%20Provider%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


