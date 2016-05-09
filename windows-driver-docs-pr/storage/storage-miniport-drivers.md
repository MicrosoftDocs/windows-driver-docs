---
title: Storage Miniport Drivers
description: Storage Miniport Drivers
ms.assetid: 374d8370-02a9-43ab-ab47-27fa9f4051ea
keywords: ["storage miniport drivers WDK", "miniport drivers WDK storage", "storage drivers WDK , miniport drivers"]
---

# Storage Miniport Drivers


## <span id="ddk_storage_miniport_drivers_kg"></span><span id="DDK_STORAGE_MINIPORT_DRIVERS_KG"></span>


This section contains the following topics:

[SCSI Miniport Drivers](scsi-miniport-drivers.md)

[Storport Miniport Drivers](storport-miniport-drivers.md)

[IDE Controller Minidrivers](ide-controller-minidrivers.md)

[ATA Miniport Drivers](ata-miniport-drivers.md)

The best practice for storage miniport drivers is to avoid calling operating system routines other than the routines that the port driver support libraries provide. For example, storage miniport drivers should not call [**KeQuerySystemTime**](https://msdn.microsoft.com/library/windows/hardware/ff553068). Instead, miniport drivers should call routines like [**ScsiPortQuerySystemTime**](https://msdn.microsoft.com/library/windows/hardware/ff564708) or [**StorPortQuerySystemTime**](https://msdn.microsoft.com/library/windows/hardware/ff567465). Storage miniport drivers should not call [**MmGetPhysicalAddress**](https://msdn.microsoft.com/library/windows/hardware/ff554547). Instead, miniport drivers should call routines like [**ScsiPortGetPhysicalAddress**](https://msdn.microsoft.com/library/windows/hardware/ff564636) and [**StorPortGetPhysicalAddress**](https://msdn.microsoft.com/library/windows/hardware/ff567095).

Do not use [Hardware Abstraction Layer Routines](https://msdn.microsoft.com/library/windows/hardware/ff546644) in miniport drivers.

The following list indicates the port driver support library that each type of storage miniport driver should use:

-   SCSI Port miniport drivers: [SCSI Port Library Routines](https://msdn.microsoft.com/library/windows/hardware/ff565375)

-   Storport miniport drivers: [Storport Driver Support Routines](https://msdn.microsoft.com/library/windows/hardware/ff567548)

-   IDE miniport drivers: [PciIdeX Library Routines](https://msdn.microsoft.com/library/windows/hardware/ff563803)

-   ATA Port miniport drivers: [ATA Port Library Routines](https://msdn.microsoft.com/library/windows/hardware/ff551343)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storage%20Miniport%20Drivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




