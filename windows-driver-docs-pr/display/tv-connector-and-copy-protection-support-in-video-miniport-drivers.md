---
title: TV Connector and Copy Protection Support in Video Miniport Drivers
description: TV Connector and Copy Protection Support in Video Miniport Drivers
ms.assetid: 7d7d44b5-3248-4bee-bc4d-e02fd3c606a7
keywords:
- video miniport drivers WDK Windows 2000 , TV connector
- video miniport drivers WDK Windows 2000 , copy protection support
- TV connector WDK video miniport
- copy protection WDK video miniport
- IOCTL_VIDEO_HANDLE_VIDEOPARAMETERS
- copy protection WDK video miniport , about copy protection support
- hardware WDK copy protection
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# TV Connector and Copy Protection Support in Video Miniport Drivers


## <span id="ddk_tv_connector_and_copy_protection_support_in_video_miniport_drivers"></span><span id="DDK_TV_CONNECTOR_AND_COPY_PROTECTION_SUPPORT_IN_VIDEO_MINIPORT_DRIVERS"></span>


A video miniport driver for an adapter that has a TV connector must handle [**VRPs**](https://msdn.microsoft.com/library/windows/hardware/ff570547) with the [**IOCTL\_VIDEO\_HANDLE\_VIDEOPARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567805) I/O control code. This IOCTL is sent to the miniport driver to either query the capabilities and current settings of the TV connector and copy protection hardware or set the functionality of the TV connector and copy protection hardware. The miniport driver determines the action to be performed by checking the **dwCommand** field of the [**VIDEOPARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff570173) structure, which is passed in the VRP's **InputBuffer**. The system will not allow playback of Rovi (formerly Macrovision) protected DVDs if a miniport driver does not handle this VRP.

If **dwCommand** is set to VP\_COMMAND\_GET, and the device *does not* support TV output, then the miniport driver should return NO\_ERROR in the **Status** member of the VRP's **StatusBlock**. It should also set the **Information** member of the VRP's **StatusBlock** to the size, in bytes, of the VIDEOPARAMETERS structure. It should set **dwFlags** to zero, set **dwTVStandard** to VP\_TV\_STANDARD\_WIN\_VGA, and set **dwAvailableTVStandard** to VP\_TV\_STANDARD\_WIN\_VGA.

If **dwCommand** is set to VP\_COMMAND\_GET, and the device *does* support TV Out, the miniport driver should indicate this in the VIDEOPARAMETERS structure by setting the appropriate flags in the **dwFlags** member and by assigning values to the other structure members that correspond to the set flags.

The following sections provide implementation details for miniport drivers of devices that have a TV connector:

[Querying TV Connector and Copy Protection Hardware](querying-tv-connector-and-copy-protection-hardware.md)

[Setting Copy Protection Hardware](setting-copy-protection-hardware.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20TV%20Connector%20and%20Copy%20Protection%20Support%20in%20Video%20Miniport%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




