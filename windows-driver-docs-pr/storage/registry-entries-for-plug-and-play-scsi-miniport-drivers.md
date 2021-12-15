---
title: Registry Entries for Plug and Play SCSI Miniport Drivers
description: Registry Entries for Plug and Play SCSI Miniport Drivers
keywords:
- SCSI miniport drivers WDK storage , PnP
- PnP WDK SCSI
- Plug and Play WDK SCSI
- PnPInterface
- registry WDK SCSI
ms.date: 10/27/2021
---

# Registry Entries for Plug and Play SCSI Miniport Drivers

To support Plug and Play, a SCSI miniport driver must:

- Be installed as a service for the host bus adapter (HBA).

- Have a **PnPInterface** entry in the registry that indicates the interfaces for that the miniport driver supports Plug and Play.

Installing a miniport driver as a service for a SCSI HBA is customarily done by providing an setup information (INF) file that matches the Plug and Play hardware ID for a given HBA to the correct driver to control that device. For details about setting up an INF file, see [Plug and Play](../kernel/introduction-to-plug-and-play.md)*.*

Unless a miniport driver is installed as a service for an HBA, the **PnPInterface** registry entry will *prevent* the miniport driver from initializing. The specified interfaces are initialized only when Plug and Play locates an appropriate HBA. If no service is properly assigned to the HBA, Plug and Play will never determine which driver to notify when it detects the device. This behavior is by design and a miniport driver should not attempt to circumvent it.

The **PnPInterface** registry entry should be made under the **Services** key for the miniport driver. For example, the following registry entry enables Plug and Play for a fictitious miniport driver called Twiddle.

```cpp
HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services
    \Twiddle
        \Parameters
            \PnpInterface
                5 : REG_DWORD : 1
                1 : REG_DWORD : 1
                2 : REG_DWORD : 1
                8 : REG_DWORD : 1
```

The values preceding REG_DWORD correspond to the INTERFACE_TYPE enumerated type declared in *miniport.h*. The values in this example indicate that the Twiddle miniport driver supports Plug and Play for the following interfaces: **PCIBus** (5), **Isa** (1), **Eisa** (2) and **PCMCIABus** (8). The value following REG_DWORD is a flag that indicates Plug and Play support for the interface. This flag can be any value but must be present.

After the **PnPInterface** values are set in the registry and the system is restarted, the miniport driver can be initialized as a Plug and Play driver. During initialization, the SCSI port driver checks the registry to determine whether the miniport driver should be run as a Plug and Play or legacy driver. The SCSI port driver checks the registry for each interface type that the miniport driver supports (for example, PCI and ISA). This is intended primarily to simplify debugging for writers of multiple-interface miniport drivers. The miniport driver writer should make sure that a miniport driver is capable of being run as a Plug and Play driver for all interfaces that driver supports.
