---
title: Registry Entries for Plug and Play SCSI Miniport Drivers
description: Registry Entries for Plug and Play SCSI Miniport Drivers
ms.assetid: d4c7c8ee-9d04-4fd4-9b70-2630d2ce6401
keywords:
- SCSI miniport drivers WDK storage , PnP
- PnP WDK SCSI
- Plug and Play WDK SCSI
- PnPInterface
- registry WDK SCSI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registry Entries for Plug and Play SCSI Miniport Drivers


## <span id="ddk_registry_entries_for_plug_and_play_scsi_miniport_drivers_kg"></span><span id="DDK_REGISTRY_ENTRIES_FOR_PLUG_AND_PLAY_SCSI_MINIPORT_DRIVERS_KG"></span>


To support Plug and Play, a SCSI miniport driver must:

-   Be installed as a service for the HBA.

-   Have a **PnPInterface** entry in the registry that indicates the interfaces for that the miniport driver supports Plug and Play.

Installing a miniport driver as a service for a SCSI HBA is customarily done by providing an setup information (INF) file that matches the Plug and Play hardware ID for a given HBA to the correct driver to control that device. For details about setting up an INF file, see [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125)*.*

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

The values preceding REG\_DWORD correspond to the INTERFACE\_TYPE enumerated type declared in *miniport.h*. The values in this example indicate that the Twiddle miniport driver supports Plug and Play for the following interfaces: **PCIBus** (5), **Isa** (1), **Eisa** (2) and **PCMCIABus** (8). The value following REG\_DWORD is a flag that indicates Plug and Play support for the interface. (Currently, this flag can be any value but must be present. In the future, the flag may be optional.)

After the **PnPInterface** values are set in the registry and the system is restarted, the miniport driver can be initialized as a Plug and Play driver. During initialization, the SCSI port driver checks the registry to determine whether the miniport driver should be run as a Plug and Play or legacy driver. The SCSI port driver checks the registry for each interface type that the miniport driver supports (for example, PCI and ISA). This is intended primarily to simplify debugging for writers of multiple-interface miniport drivers. The miniport driver writer should make sure that a miniport driver is capable of being run as a Plug and Play driver for all interfaces that driver supports.

 

 




