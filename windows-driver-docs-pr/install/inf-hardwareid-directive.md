---
title: INF HardwareId Directive
description: Starting with Windows Vista, the Found New Hardware Wizard and Hardware Update Wizard support INF HardwareId directives in the \ DeviceInstall\ section of an Autorun.inf file.
ms.assetid: aceb4db2-ae00-47f3-994a-49541437e260
keywords: ["INF HardwareId Directive Device and Driver Installation"]
topic_type:
- apiref
api_name:
- INF HardwareId Directive
api_type:
- NA
---

# INF HardwareId Directive


**Note**  The **HardwareId** directive is only supported within an *Autorun.inf* file. This directive must not be used within the INF files that are used for PnP device installations.

 

Starting with Windows Vista, the Found New Hardware Wizard and Hardware Update Wizard support INF **HardwareId** directives in the **\[DeviceInstall\]** section of an *Autorun.inf* file. The author of *Autorun.inf* can use these **HardwareId** directives to specify Plug and Play (PnP) hardware identifiers (IDs) of the devices for which the AutoRun-enabled application provides and installs drivers.

``` syntax
[DeviceInstall] 
 
HardwareId="pnp-hardware-id"
...
```

## Entries


<a href="" id="-pnp-hardware-id-"></a>"*pnp-hardware-id*"  
This value specifies a PnP device hardware ID. The hardware ID must be enclosed in double quotation marks (").

The hardware ID can be fairly generic, such as PCI\\VEN\_1234&DEV\_1234, or very specific, such as PCI\\VEN\_1234&DEV\_1234&SUBSYS\_12345678&REV\_01.

Only one PnP hardware ID can be specified per HardwareId directive. To specify multiple hardware IDs, use multiple HardwareId directives, one per line.

Remarks
-------

During a [hardware-first installation](hardware-first-installation.md), the user installs a hardware device before installing the drivers for that device. In this case, the Found New Hardware Wizard prompts the user for the distribution medium.

If the distribution medium has an AutoRun-enabled [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application), the wizard parses the *Autorun.inf* file to look for a **HardwareId** directive entry that matches the device that is being installed. If the wizard finds a **HardwareId** directive that matches the device, the wizard invokes the AutoRun-enabled application, which installs the driver and device-specific applications instead of the wizard.

The Found New Hardware Wizard does not determine whether the application installed a driver for the device. In this case, the application must install a driver for the device. If the *Autorun.inf* file does not include a **HardwareId** directive that identifies the device that is being installed, the wizard does not start the application and continues with device installation.

Although there may be multiple **HardwareId** directives within the **\[DeviceInstall\]** section of an *Autorun.inf* file, each directive should specify a unique PnP hardware ID.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20INF%20HardwareId%20Directive%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




