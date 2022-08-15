---
title: Power framework (PoFx) driver samples
description: The driver samples in this directory provide a starting point for writing a custom PoFx driver for your device.
ms.date: 11/19/2019
---

# Power framework (PoFx) driver samples

The driver samples in this directory provide a starting point for writing a custom PoFx driver for your device.

| Sample | Description |
| --- | --- |
| [PEP ACPI Sample](/samples/microsoft/windows-driver-samples/pep-acpi-sample) | Demonstrates an interface which allows a Power Engine Plugin (PEP) to implement ACPI runtime methods natively via a Windows driver rather than firmware. |
| [UMDF2 PoFx Driver](/samples/microsoft/windows-driver-samples/power-framework-pofx-sample-umdf-version-2) | The UMDF 2 SingleComp sample demonstrates how a UMDF2 driver can implement F-state-based power management for a device that has only a single component. |
| [WDF PoFx Driver](/samples/microsoft/windows-driver-samples/kmdf-power-framework-pofx-sample) | Contains two samples that demonstrate how a KMDF driver can implement F-state-based power management. The SingleComp sample demonstrates how a KMDF driver can implement F-state-based power management for a device that has only a single component. The MultiComp sample demonstrates how a KMDF driver can implement F-state-based power management for a device that has an arbitrary number of components that can be individually power-managed |
