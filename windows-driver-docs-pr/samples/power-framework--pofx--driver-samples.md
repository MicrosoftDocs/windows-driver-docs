---
title: Power framework (PoFx) driver samples
author: windows-driver-content
description: The driver samples in this directory provide a starting point for writing a custom driver for your device.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: BA2CC8F0-E337-4A5E-987F-1B40213F5983
---

# Power framework (PoFx) driver samples


The driver samples in this directory provide a starting point for writing a custom driver for your device.

## Power framework (PoFx)


| Sample Name       | Solution                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PEP ACPI Sample   | [pepsamples](http://go.microsoft.com/fwlink/p/?LinkId=620311) | Demonstrates an interface which allows a Power Engine Plugin (PEP) to implement ACPI runtime methods natively via a Windows driver rather than firmware.                                                                                                                                                                                                                                                                                               |
| UMDF2 PoFx Driver | [pofx](http://go.microsoft.com/fwlink/p/?LinkId=617936)       | The UMDF 2 SingleComp sample demonstrates how a UMDF2 driver can implement F-state-based power management for a device that has only a single component.                                                                                                                                                                                                                                                                                               |
| WDF PoFx Driver   | [pofx](http://go.microsoft.com/fwlink/p/?LinkId=617937)       | Contains two samples that demonstrate how a KMDF driver can implement F-state-based power management. The SingleComp sample demonstrates how a KMDF driver can implement F-state-based power management for a device that has only a single component. The MultiComp sample demonstrates how a KMDF driver can implement F-state-based power management for a device that has an arbitrary number of components that can be individually power-managed |

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdkappendix\wdkappendix%5D:%20Power%20framework%20%28PoFx%29%20driver%20samples%20%20RELEASE:%20%289/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


