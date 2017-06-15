---
title: Power States
author: windows-driver-content
description: Power States
MS-HAID:
- 'PwrMgmt\_15eab8cf-04e8-4086-b257-86f1ced3ecb4.xml'
- 'kernel.power\_states'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 33043903-9db6-4c51-b33c-921ade237ccf
keywords: ["power management WDK kernel , power states", "power states WDK kernel", "states WDK power management", "system power states WDK kernel", "device power states WDK kernel", "power consumption levels WDK kernel", "consumption levels WDK power management", "computing activity WDK power management", "physical device objects WDK power management", "PDOs WDK power management", "functional device objects WDK power management", "FDOs WDK power management", "filter DOs WDK power management"]
---

# Power States


## <a href="" id="ddk-power-states-kg"></a>


A power state indicates the level of power consumption—and thus the extent of computing activity—by the system or by a single device. The power manager sets the power state of the system as a whole. Device drivers set the power state of their individual devices.

The ACPI specification defines two sets of discrete power states: *system power states* and *device power states*. Each power state has a unique name.

[System power states](system-power-states.md) are named S*x*, where *x* is a state number between 0 and 5. [Device power states](device-power-states.md) are named D*x*, where *x* is a state number between 0 and 3. The state number is inversely related to power consumption: higher numbered states use less power. States S0 and D0 are the highest-powered, most functional, fully on states. States S5 and D3 are the lowest-powered states and have the longest wake-up latency.

These clearly defined power states allow many devices from various manufacturers to work together consistently and predictably. For example, when the power manager sets the system in state S3, it can rely upon drivers that support power management not only to put their devices in the corresponding device power state but also to return to the working state in a predictable fashion.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Power%20States%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


