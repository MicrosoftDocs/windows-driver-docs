---
title: Converting a Windows NT 4.0 SCSI Miniport for Plug and Play
author: windows-driver-content
description: Converting a Windows NT 4.0 SCSI Miniport for Plug and Play
ms.assetid: 46e5eb41-ff41-4054-856b-cc32f286e543
keywords: ["SCSI miniport drivers WDK storage , PnP", "PnP WDK SCSI", "Plug and Play WDK SCSI", "converting SCSI miniport drivers"]
---

# Converting a Windows NT 4.0 SCSI Miniport for Plug and Play


## <span id="ddk_converting_a_windows_nt_4_0_scsi_miniport_for_plug_and_play_kg"></span><span id="DDK_CONVERTING_A_WINDOWS_NT_4_0_SCSI_MINIPORT_FOR_PLUG_AND_PLAY_KG"></span>


Even if a miniport driver has enabled Plug and Play in the registry, the driver will fault during initialization unless it honors certain restrictions in the use of the *HwContext* pointer and resources supplied by the port driver. A miniport driver might also fault during initialization if it depends on a predictable initialization order of drivers.

To run successfully under Plug and Play, a Microsoft Windows

NT 4.0 miniport driver's source code might need to be modified as described in the following sections.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Converting%20a%20Windows%20NT%204.0%20SCSI%20Miniport%20for%20Plug%20and%20Play%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


