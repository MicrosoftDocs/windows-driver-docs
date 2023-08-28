---
title: Summary of ACPI support in Windows
description: This article summarizes the subset of ACPI 5.0 features that are required to support Windows on SoC-based platforms.
ms.date: 03/23/2023
---

# Summary of ACPI support in Windows

This article summarizes the subset of Advanced Configuration and Power Interface (ACPI) 5.0 features that are required to support Windows on SoC-based platforms.

| Feature | Section of ACPI 5.0 specification | Notes |
|--|--|--|
| System description tables | 5.2.5 | Root System Description Pointer (RSDP) |
|  | 5.2.7, 5.2.8 | Either of Root (RSDT) or Extended (XSDT) System Description Tables |
|  | 5.2.9 | Fixed ACPI Description Table (FADT) |
|  | 5.2.12 | Multiple APIC Description Table (MADT) |
|  | 5.2.24 | Generic Timer Description Table (GTDT) |
|  | 5.2.6 | Core System Resources Table (CSRT) Specification |
|  | 5.2.6 | Debug Port Table 2 (DBG2) [Specification](/previous-versions/windows/hardware/design/dn639131(v=vs.85)) |
|  | 5.2.11.1 | Differentiated System Description Table (DSDT) |
|  | 5.2.11.2 | Secondary System Description Table (SSDT) |
| Device management | 6.1 | Device Identification Objects |
|  | 6.2 | Device Configuration Objects |
| GPIO | 5.6.5.1 | GPIO controller devices |
|  | 5.6.5 | GPIO-signaled ACPI events |
|  | 6.4.3.8.1, 19.5.53, 19.5.54 | GPIO resource descriptors and macros |
|  | 5.5.2.4.4 | GeneralPurposeIO OpRegions |
| Simple peripheral bus (SPB) | 6.4.3.8.2, 19.5.55, 19.5.118, 19.5.134 | SPB resource descriptors and macros |
|  |  | GenericSerialBus OpRegions |
| Device power management | 3.3 |  |
|  | 7.1 | Power Resources |
|  | 7.2 | Device Power Management Objects |
| ACPI-defined devices | 9.0, 10 |  |
|  | 9.5 | Control Method Power Button |
|  | 9.4 | Control Method Lid Device |
|  | 10.2 | Control Method Battery device |
|  | 9.18 | Control Method Time and Alarm device |
|  | 11 | Thermal Zones |
| Device-specific support | 8.4 | Processors |
|  | Appendix B | Displays |
|  | 6.1.8, 9.13 | USB |
|  |  | SD bus |
|  |  | Cameras |
|  |  | HID-over-I<sup>2</sup>C devices |
|  | 3.2.1, 4.8.2.2.1.2, 4.8.2.2.1.3 | Buttons |
|  |  | Dock and convertible PC sensors |
