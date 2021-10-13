---
title: Device Specific Data (_DSD) for PCIe Root Ports
description: ACPI _DSD methods for supporting Modern Standby and PCI hot plug scenarios
ms:assetid: 44ad67da-f374-4a8e-80bd-d531853088a2
keywords: ACPI, ACPI \_DSD method
ms.date: 05/29/2020
ms.localizationpriority: medium
---

# ACPI Interface: Device Specific Data (\_DSD) for PCIe Root Ports

In Windows 10 (Version 1803), new ACPI \_DSD methods have been added to support Modern Standby and PCI hot plug scenarios.

## Directed Deepest Runtime Idle Platform State (DRIPS) support on PCIe Root Ports

 This ACPI object must be implemented in the ACPI scope of every PCIe Root Port/slot that is accessible to the user on Modern Standby-enabled systems that are capable of implementing the [Directed Power Management Framework (DFx)](../kernel/introduction-to-the-directed-power-management-framework.md).

```ASL
Name (_DSD, Package () {

          ToUUID("FDF06FAD-F744-4451-BB64-ECD792215B10"),

            Package () {

                Package (2) {"FundamentalDeviceResetTriggeredOnD3ToD0", 1},
            }
        }
)
```

## Identifying PCIe Root Ports supporting hot plug in D3

This ACPI object enables the operating system to identify and power manage PCIe Root ports that are capable of handling hot plug events while in D3 state. If this object is not implemented on the a PCIe hot plug capable port, then the system does not power manage this port if it has no children PCIe devices, causing the system to consume more power than necessary.

This object must be implemented on all PCIe Root Ports of Thunderbolt hierarchies, on Runtime D3 (RTD3) capable systems, in the Root Port ACPI device scope.

```ASL
Name (_DSD, Package () {  

        ToUUID("6211E2C0-58A3-4AF3-90E1-927A4E0C55A4"),  

        Package () {  

            Package (2) {"HotPlugSupportInD3", 1},  

                   }
        }
)
```

## Identifying externally exposed PCIe Root Ports

This ACPI object enables the operating system to identify externally exposed PCIe hierarchies, such as Thunderbolt. This object must be implemented in the Root Port ACPI device scope.

Note: On systems shipping with Windows 10, version 1803, this object should only be implemented on PCIe Root Ports of Thunderbolt hierarchies.

```ASL
Name (_DSD, Package () {  

ToUUID("EFCC06CC-73AC-4BC3-BFF0-76143807C389"),
Package () {
Package (2) {"ExternalFacingPort", 1}, // Property 1: This is an externally facing port/hierarchy
Package (2) {"UID", 0}, // Property 2: UID of the externally facing port on platform, range is: 0, 1, …, n-1
                   }
        }
)
```

## Identifying internal PCIe ports accessible to users and requiring DMA protection

This ACPI object enables the operating system to identify internal PCIe hierarchies that are easily accessible by users (such as, Laptop M.2 PCIe slots accessible by way of a latch) and require protection by the OS [Kernel DMA Protection](/windows/security/information-protection/kernel-dma-protection-for-thunderbolt) mechanism. This object must be implemented in the Root Port ACPI device scope.

Key items of note:

- Protecting PCI ports using this ACPI object is supported only in Windows 10, version 1903 and later.

- Kernel DMA Protection must be enabled in system BIOS/UEFI, in order for the OS to parse the \_DSD and apply necessary protections to the PCI port.

- Drivers of devices connected to this port MUST support [DMA remapping](./enabling-dma-remapping-for-device-drivers.md), otherwise Windows 10 may block these devices from operating until a user logs in or indefinitely, depending on [DMAGuard Policy](/windows/client-management/mdm/policy-csp-dmaguard).

```ASL
Name (_DSD, Package () {  

ToUUID("70D24161-6DD5-4C9E-8070-705531292865"),
Package () {
Package (2) {"DmaProperty", 1}, // Property 1: This port needs to be protected by the OS
Package (2) {"UID", 0}, // Property 2: UID of the PCIe port on platform, range is: 0, 1, …, n-1
                   }
        }
)
```

## Identifying PCIe ports supporting D3_COLD_AUX_POWER ECN Interface

This ACPI object enables the operating system to identify PCIe ports that support [D3_COLD_AUX_POWER ECN interface](/windows-hardware/drivers/ddi/wdm/ns-wdm-_d3cold_aux_power_and_timing_interface), which allows PCIe devices to request from the platform additional auxiliary power in D3, above the default 375mA @3.3V. Any PCI port or bridge defining this DSD *must* guarantee that when programming back the previously negotiated auxiliary power value, the operation succeeds.

```ASL
Name (_DSD, Package () {
            ToUUID("6B4AD420-8FD3-4364-ACF8-EB94876FD9EB"),
            Package () {
            }
        }
)

```

## Mapping native protocols (PCIe, DisplayPort) tunneled through USB4 to USB4 Host Routers

This ACPI object enables the operating system to map native protocols, such as PCIe and DisplayPort, tunneled through USB4 to the correct USB4 host router.

In the following sample, `Device (DSB0)` has a dependency on `\_SB.PCI0.NHI0`.

```ASL
Scope (\_SB.PCI0)
{
    Device (NHI0) { } //Host interface instance which has dependency on \_SB.PCI0.NHI0
    Device (DSB0) //Tunneled PCIe port instance
    {
        Name (_DSD, Package () {
            ToUUID("daffd814-6eba-4d8c-8a91-bc9bbf4aa301"), //Device Properties UUID 
            Package () {
                Package () { “usb4-host-interface", \_SB.PCI0.NHI0 },
                Package () { “usb4-port-number", PortInstance#},
            }
        })
    }
    Device (…) //Extend to DP and USB tunneled ports, as needed 
    {
        Name (_DSD, Package () {
            ToUUID("daffd814-6eba-4d8c-8a91-bc9bbf4aa301"), //Device Properties UUID 
            Package () {
                Package () { “usb4-host-interface", \_SB.PCI0.NHI0 },
                Package () { “usb4-port-number", PortInstance#},
            }
        })
    }
}
```

## See also

[Enabling PCI Express Native Control in Windows](enabling-pci-express-native-control.md)

[Kernel DMA Protection for Thunderbolt 3](/windows/security/information-protection/kernel-dma-protection-for-thunderbolt)

[Enabling DMA Remapping for device drivers](./enabling-dma-remapping-for-device-drivers.md)

[D3COLD_AUX_POWER_AND_TIMING_INTERFACE structure](/windows-hardware/drivers/ddi/wdm/ns-wdm-_d3cold_aux_power_and_timing_interface)
