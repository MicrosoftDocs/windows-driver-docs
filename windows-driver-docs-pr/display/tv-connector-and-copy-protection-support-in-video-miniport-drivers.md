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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# TV Connector and Copy Protection Support in Video Miniport Drivers


## <span id="ddk_tv_connector_and_copy_protection_support_in_video_miniport_drivers"></span><span id="DDK_TV_CONNECTOR_AND_COPY_PROTECTION_SUPPORT_IN_VIDEO_MINIPORT_DRIVERS"></span>


A video miniport driver for an adapter that has a TV connector must handle [**VRPs**](https://msdn.microsoft.com/library/windows/hardware/ff570547) with the [**IOCTL\_VIDEO\_HANDLE\_VIDEOPARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567805) I/O control code. This IOCTL is sent to the miniport driver to either query the capabilities and current settings of the TV connector and copy protection hardware or set the functionality of the TV connector and copy protection hardware. The miniport driver determines the action to be performed by checking the **dwCommand** field of the [**VIDEOPARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff570173) structure, which is passed in the VRP's **InputBuffer**. The system will not allow playback of Rovi (formerly Macrovision) protected DVDs if a miniport driver does not handle this VRP.

If **dwCommand** is set to VP\_COMMAND\_GET, and the device *does not* support TV output, then the miniport driver should return NO\_ERROR in the **Status** member of the VRP's **StatusBlock**. It should also set the **Information** member of the VRP's **StatusBlock** to the size, in bytes, of the VIDEOPARAMETERS structure. It should set **dwFlags** to zero, set **dwTVStandard** to VP\_TV\_STANDARD\_WIN\_VGA, and set **dwAvailableTVStandard** to VP\_TV\_STANDARD\_WIN\_VGA.

If **dwCommand** is set to VP\_COMMAND\_GET, and the device *does* support TV Out, the miniport driver should indicate this in the VIDEOPARAMETERS structure by setting the appropriate flags in the **dwFlags** member and by assigning values to the other structure members that correspond to the set flags.

The following sections provide implementation details for miniport drivers of devices that have a TV connector:

[Querying TV Connector and Copy Protection Hardware](querying-tv-connector-and-copy-protection-hardware.md)

[Setting Copy Protection Hardware](setting-copy-protection-hardware.md)

 

 





