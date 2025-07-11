---
title: ACPI/BIOS Requirements for NVMe Dynamic Link Rate Management (DLRM)
description: ACPI and BIOS interface requirements for enabling Dynamic Link Rate Management on NVMe devices.
keywords: ACPI, DLRM, NVMe, PCIe, BIOS, power management
ms.date: 07/11/2025
ms.topic: reference
---

# ACPI/BIOS Requirements for NVMe Dynamic Link Rate Management (DLRM)

NVMe Dynamic Link Rate Management (DLRM) is a feature designed to optimize power efficiency in NVMe devices by dynamically adjusting the PCIe link speed based on I/O workload characteristics. This is increasingly important as newer PCIe generations offer higher bandwidth but also consume more power, impacting battery life in Windows devices.

DLRM enables the system to operate at the most efficient power state for the current workload, reducing unnecessary power consumption during typical scenarios such as productivity tasks, video playback, and online meetings.

## Prerequisites

To support DLRM, the following requirements must be met:

- **BIOS Support**: DLRM is opt-in and must be enabled by platform firmware. The enabling status is reported to the OS via ACPI.
- **OS Support**: DLRM is supported in Windows 24H2 build 26100.2894 and later.
- **Microsoft Inbox NVMe Driver**: The system must use the Microsoft inbox NVMe driver (`stornvme.sys`).
- **PCIe EQ Bypass Disabled**: Equalization Bypass must be disabled, as it restricts supported PCIe generations and conflicts with DLRM. Note: Generally, any PCIe feature that restricts PCIe generations should not be enabled as it will conflict with DLRM. 

## ACPI/BIOS Interface for DLRM

DLRM support is advertised to the OS via the ACPI `_DSM` method declared under the PCIe Root Port (RP) associated with the NVMe device. The _DSM method returns the DLRM enabling state. 

### _DSM Method UUID and Arguments

- **UUID**: `{C41F8AFB-4701-F0EB-1D26-0296648C30E4}`
- **Arguments**:
    - `Arg0`: UUID Unique function identifier
    - `Arg1`: Integer Revision Level (1)
    - `Arg2`: Integer Function Index
        - `0`: Query supported functions
        - `1`: Report DLRM enabling state (`0`: disabled, `1`: enabled)
    - `Arg3`: Package Parameters (None)

### Sample ASL Code

Sample ASL implementation of the `_DSM` method for DLRM support:

```ASL
Scope (\_SB.PC00.RP05.PXSX) { 
    Method (_DSM, 4, Serialized, 0, UnknownObj, {BuffObj, IntObj, IntObj, PkgObj}) { 
        If (LEqual (Arg0, ToUUID ("C41F8AFB-4701-F0EB-1D26-0296648C30E4"))) { 
            If (LEqual (1, ToInteger (Arg1))) { 
                Switch (ToInteger (Arg2)) { 
                    Case (0) { 
                        Return (Buffer () {0x03})  
                    } 
                    Case (1) { 
                        If (PNVM ()) { 
                            If (LAnd (CondRefOf (\DLRM), (LNotEqual (\DLRM, 0)))) {  
                                Return (1) 
                            } Else { 
                                Return (0) 
                            } 
                        } 
                    } 
                }  
            }   
        }  
        Return (Buffer () {0x00}) 
    }  
}
```

1. **UUID Check**: Verifies the UUID matches DLRM's unique identifier.
2. **Revision Check**: Ensures the revision level is 1.
3. **Function Index**:
    - `0`: Returns a buffer indicating supported functions.
    - `1`: Returns DLRM enablement state for storage devices (`1` if enabled, `0` otherwise).

> [!NOTE]
> - The `_DSM` method must be declared on the PCIe Root Port where the NVMe device is installed.
> - If no NVMe device is present, the method should return `0`.
> - The Root Port location may vary by platform design.
