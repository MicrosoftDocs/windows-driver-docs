---
title: Device Specific Data (_DSD) for PCIe Root Ports
description: ACPI _DSD methods for supporting Modern Standby and PCI hot plug scenarios
ms:assetid: 44ad67da-f374-4a8e-80bd-d531853088a2
keywords: ACPI, ACPI \_DSD method
ms.date: 04/10/2018
ms.localizationpriority: medium
---

# ACPI Interface: Device Specific Data (_DSD) for PCIe Root Ports

In Windows 10 (Version 1803), new ACPI _DSD methods have been added to support Modern Standby and PCI hot plug scenarios:
## Directed Deepest Runtime Idle Platform State (DRIPS) support on PCIe Root Ports 

 This ACPI object must be implemented in the ACPI scope of every PCIe Root Port/slot that is accessible to the user on Modern Standby-enabled desktop systems. 

```cpp
Name (_DSD, Package () {

          ToUUID("FDF06FAD-F744-4451-BB64-ECD792215B10"),

            Package () {

                Package (2) {"FundamentalDeviceResetTriggeredOnD3ToD0", 1},
            }
        }
) 
```

## Identifying PCIe Root Ports supporting hot plug in D3

This ACPI object allows the operating system to identify and power manage PCIe Root ports that are capable of handling hot plug events while in D3 state. If this object is not implemented on the a PCIe hot plug capable port, then the system does not power manage this port if it has no children PCIe devices, causing the system to consume more power than necessary.

This object must be implemented on all PCIe Root Ports of Thunderbolt™ hierarchies, on Runtime D3 (RTD3) capable systems, in the Root Port ACPI device scope.

```cpp
Name (_DSD, Package () {  

        ToUUID("6211E2C0-58A3-4AF3-90E1-927A4E0C55A4"),  

        Package () {  

            Package (2) {"HotPlugSupportInD3", 1},  

                   }
        }
)
```

## Identifying externally exposed PCIe Root Ports

This ACPI object allows the operating system to identify externally exposed PCIe hierarchies (e.g. Thunderbolt™). This object must be implemented in the Root Port ACPI device scope.

Note: On systems shipping with Windows 10 1803, this should only be implemented on PCIe Root Ports of Thunderbolt™ hierarchies.

```cpp
Name (_DSD, Package () {  

ToUUID("EFCC06CC-73AC-4BC3-BFF0-76143807C389"),
Package () {
Package (2) {"ExternalFacingPort", 1}, // Property 1: This is an externally facing port/hierarchy
Package (2) {"UID", 0}, // Property 2: UID of the externally facing port on platform, range is: 0, 1, …, n-1
                   }
        }
)
```
## See Also

[Enabling PCI Express Native Control in Windows](enabling-pci-express-native-control.md)
