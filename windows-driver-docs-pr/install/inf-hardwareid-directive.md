---
title: INF HardwareId Directive
description: The Found New Hardware Wizard and Hardware Update Wizard support INF HardwareId directives in the [DeviceInstall] section of an Autorun.inf file.
ms.assetid: aceb4db2-ae00-47f3-994a-49541437e260
keywords:
- INF HardwareId Directive Device and Driver Installation
topic_type:
- apiref
api_name:
- INF HardwareId Directive
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF HardwareId Directive


**Note**  The **HardwareId** directive is only supported within an *Autorun.inf* file. This directive must not be used within the INF files that are used for PnP device installations.

 

Starting with Windows Vista, the Found New Hardware Wizard and Hardware Update Wizard support INF **HardwareId** directives in the **\[DeviceInstall\]** section of an *Autorun.inf* file. The author of *Autorun.inf* can use these **HardwareId** directives to specify Plug and Play (PnP) hardware identifiers (IDs) of the devices for which the AutoRun-enabled application provides and installs drivers.

```cpp
[DeviceInstall] 
 
HardwareId="pnp-hardware-id"
...
```

## Entries


<a href="" id="-pnp-hardware-id-"></a>"*pnp-hardware-id*"  
This value specifies a PnP device hardware ID. The hardware ID must be enclosed in double quotation marks (").

The hardware ID can be fairly generic, such as PCI\\VEN_1234&DEV_1234, or very specific, such as PCI\\VEN_1234&DEV_1234&SUBSYS_12345678&REV_01.

Only one PnP hardware ID can be specified per HardwareId directive. To specify multiple hardware IDs, use multiple HardwareId directives, one per line.

Remarks
-------

During a [hardware-first installation](hardware-first-installation.md), the user installs a hardware device before installing the drivers for that device. In this case, the Found New Hardware Wizard prompts the user for the distribution medium.

If the distribution medium has an AutoRun-enabled [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application), the wizard parses the *Autorun.inf* file to look for a **HardwareId** directive entry that matches the device that is being installed. If the wizard finds a **HardwareId** directive that matches the device, the wizard invokes the AutoRun-enabled application, which installs the driver and device-specific applications instead of the wizard.

The Found New Hardware Wizard does not determine whether the application installed a driver for the device. In this case, the application must install a driver for the device. If the *Autorun.inf* file does not include a **HardwareId** directive that identifies the device that is being installed, the wizard does not start the application and continues with device installation.

Although there may be multiple **HardwareId** directives within the **\[DeviceInstall\]** section of an *Autorun.inf* file, each directive should specify a unique PnP hardware ID.

 

 





