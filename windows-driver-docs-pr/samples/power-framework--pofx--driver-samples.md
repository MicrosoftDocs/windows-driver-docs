---
title: Power framework (PoFx) driver samples
description: The driver samples in this directory provide a starting point for writing a custom PoFx driver for your device.
ms.assetid: BA2CC8F0-E337-4A5E-987F-1B40213F5983
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Power framework (PoFx) driver samples


The driver samples in this directory provide a starting point for writing a custom PoFx driver for your device.

## Power framework (PoFx)


| Sample Name       | Solution                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PEP ACPI Sample   | [pepsamples](http://go.microsoft.com/fwlink/p/?LinkId=620311) | Demonstrates an interface which allows a Power Engine Plugin (PEP) to implement ACPI runtime methods natively via a Windows driver rather than firmware.                                                                                                                                                                                                                                                                                               |
| UMDF2 PoFx Driver | [pofx](http://go.microsoft.com/fwlink/p/?LinkId=617936)       | The UMDF 2 SingleComp sample demonstrates how a UMDF2 driver can implement F-state-based power management for a device that has only a single component.                                                                                                                                                                                                                                                                                               |
| WDF PoFx Driver   | [pofx](http://go.microsoft.com/fwlink/p/?LinkId=617937)       | Contains two samples that demonstrate how a KMDF driver can implement F-state-based power management. The SingleComp sample demonstrates how a KMDF driver can implement F-state-based power management for a device that has only a single component. The MultiComp sample demonstrates how a KMDF driver can implement F-state-based power management for a device that has an arbitrary number of components that can be individually power-managed |

 

 

 




