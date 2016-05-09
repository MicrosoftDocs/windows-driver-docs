---
title: Supporting Plug and Play in a SCSI Miniport Driver
author: windows-driver-content
description: Supporting Plug and Play in a SCSI Miniport Driver
ms.assetid: c8b148ac-b1ab-4870-8818-5ef1c2d68599
keywords: ["SCSI miniport drivers WDK storage , PnP", "PnP WDK SCSI", "Plug and Play WDK SCSI"]
---

# Supporting Plug and Play in a SCSI Miniport Driver


## <span id="ddk_supporting_plug_and_play_in_a_scsi_miniport_driver_kg"></span><span id="DDK_SUPPORTING_PLUG_AND_PLAY_IN_A_SCSI_MINIPORT_DRIVER_KG"></span>


Although Microsoft Windows 2000 and later operating systems are Plug and Play operating systems, by default SCSI miniport drivers are run as legacy drivers. The HBA for a legacy miniport driver cannot be removed from the system while it is running, nor are legacy miniport drivers automatically detected when added to a running system. These limitations might be acceptable for certain HBAs, but SCSI miniport drivers for PC Card/CardBus HBAs and HBAs in laptops should support Plug and Play.

A Plug and Play miniport driver must implement an *HwScsiAdapterControl* routine to stop and manage power to the HBA. No additional routines are required of a Plug and Play miniport driver to accommodate changes in driver initialization.

The SCSI port driver creates PDOs for target devices and the FDO for the miniport driver, and handles requests to add, start or unload the device on behalf of the miniport driver. For general information about Plug and Play drivers, see [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Supporting%20Plug%20and%20Play%20in%20a%20SCSI%20Miniport%20Driver%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


