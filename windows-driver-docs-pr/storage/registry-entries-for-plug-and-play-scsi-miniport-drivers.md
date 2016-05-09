---
title: Registry Entries for Plug and Play SCSI Miniport Drivers
author: windows-driver-content
description: Registry Entries for Plug and Play SCSI Miniport Drivers
ms.assetid: d4c7c8ee-9d04-4fd4-9b70-2630d2ce6401
keywords: ["SCSI miniport drivers WDK storage , PnP", "PnP WDK SCSI", "Plug and Play WDK SCSI", "PnPInterface", "registry WDK SCSI"]
---

# Registry Entries for Plug and Play SCSI Miniport Drivers


## <span id="ddk_registry_entries_for_plug_and_play_scsi_miniport_drivers_kg"></span><span id="DDK_REGISTRY_ENTRIES_FOR_PLUG_AND_PLAY_SCSI_MINIPORT_DRIVERS_KG"></span>


To support Plug and Play, a SCSI miniport driver must:

-   Be installed as a service for the HBA.

-   Have a **PnPInterface** entry in the registry that indicates the interfaces for that the miniport driver supports Plug and Play.

Installing a miniport driver as a service for a SCSI HBA is customarily done by providing an setup information (INF) file that matches the Plug and Play hardware ID for a given HBA to the correct driver to control that device. For details about setting up an INF file, see [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125)*.*

Unless a miniport driver is installed as a service for an HBA, the **PnPInterface** registry entry will *prevent* the miniport driver from initializing. The specified interfaces are initialized only when Plug and Play locates an appropriate HBA. If no service is properly assigned to the HBA, Plug and Play will never determine which driver to notify when it detects the device. This behavior is by design and a miniport driver should not attempt to circumvent it.

The **PnPInterface** registry entry should be made under the **Services** key for the miniport driver. For example, the following registry entry enables Plug and Play for a fictitious miniport driver called Twiddle.

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Registry%20Entries%20for%20Plug%20and%20Play%20SCSI%20Miniport%20Drivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


