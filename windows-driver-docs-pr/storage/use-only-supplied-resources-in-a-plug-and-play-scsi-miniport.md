---
title: Use Only Supplied Resources in a Plug and Play SCSI Miniport
description: Use Only Supplied Resources in a Plug and Play SCSI Miniport
ms.assetid: 26c688dc-b6af-4a0c-8401-d53e653d90b3
keywords: ["SCSI miniport drivers WDK storage , PnP", "PnP WDK SCSI", "Plug and Play WDK SCSI", "converting SCSI miniport drivers", "resource restrictions WDK SCSI"]
---

# Use Only Supplied Resources in a Plug and Play SCSI Miniport


## <span id="ddk_use_only_supplied_resources_in_a_plug_and_play_scsi_miniport_kg"></span><span id="DDK_USE_ONLY_SUPPLIED_RESOURCES_IN_A_PLUG_AND_PLAY_SCSI_MINIPORT_KG"></span>


One of the goals for a Plug and Play system is to reduce or eliminate the number of drivers that detect their devices by accessing known memory locations. This includes drivers that determine their resources by reading the configuration space for their HBA.

In Plug and Play, devices on enumerable buses are detected by the driver for the bus. This allows the bus driver to handle any resource conflicts, provide special-case fixes for broken bus and bridge parts, and so forth.

Consequently, a SCSI miniport driver must use only the resources provided by the port driver (if any) in Microsoft Windows 2000 and later systems. The miniport driver is allowed to scan the bus for an HBA only if the port driver passes in zero-value access ranges. If the miniport driver attempts to use resources that are not assigned to it, the [**ScsiPortGetDeviceBase**](https://msdn.microsoft.com/library/windows/hardware/ff564629) call will fail. Calls to read and write device registers or ports that have not been properly mapped also might fail.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Use%20Only%20Supplied%20Resources%20in%20a%20Plug%20and%20Play%20SCSI%20Miniport%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




