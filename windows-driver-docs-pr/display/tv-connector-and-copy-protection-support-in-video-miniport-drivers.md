---
title: TV Connector and Copy Protection in Video Miniport Drivers
description: TV Connector and Copy Protection Support in Video Miniport Drivers
keywords:
- video miniport drivers WDK Windows 2000 , TV connector
- video miniport drivers WDK Windows 2000 , copy protection support
- TV connector WDK video miniport
- copy protection WDK video miniport
- IOCTL_VIDEO_HANDLE_VIDEOPARAMETERS
- copy protection WDK video miniport , about copy protection support
- hardware WDK copy protection
ms.date: 12/06/2018
ms.custom: seodec18
---

# TV Connector and Copy Protection Support in Video Miniport Drivers

A video miniport driver for an adapter that has a TV connector must handle [**VRPs**](/windows-hardware/drivers/ddi/video/ns-video-_video_request_packet) with the [**IOCTL\_VIDEO\_HANDLE\_VIDEOPARAMETERS**](/windows-hardware/drivers/ddi/ntddvdeo/ni-ntddvdeo-ioctl_video_handle_videoparameters) I/O control code. This IOCTL is sent to the miniport driver to either query the capabilities and current settings of the TV connector and copy protection hardware or set the functionality of the TV connector and copy protection hardware. The miniport driver determines the action to be performed by checking the **dwCommand** field of the [**VIDEOPARAMETERS**](/windows/win32/api/tvout/ns-tvout-videoparameters) structure, which is passed in the VRP's **InputBuffer**. The system will not allow playback of Rovi (formerly Macrovision) protected DVDs if a miniport driver does not handle this VRP.

If **dwCommand** is set to VP\_COMMAND\_GET, and the device *does not* support TV output, then the miniport driver should return NO\_ERROR in the **Status** member of the VRP's **StatusBlock**. It should also set the **Information** member of the VRP's **StatusBlock** to the size, in bytes, of the VIDEOPARAMETERS structure. It should set **dwFlags** to zero, set **dwTVStandard** to VP\_TV\_STANDARD\_WIN\_VGA, and set **dwAvailableTVStandard** to VP\_TV\_STANDARD\_WIN\_VGA.

If **dwCommand** is set to VP\_COMMAND\_GET, and the device *does* support TV Out, the miniport driver should indicate this in the VIDEOPARAMETERS structure by setting the appropriate flags in the **dwFlags** member and by assigning values to the other structure members that correspond to the set flags.

The following sections provide implementation details for miniport drivers of devices that have a TV connector:

[Querying TV Connector and Copy Protection Hardware](querying-tv-connector-and-copy-protection-hardware.md)

[Setting Copy Protection Hardware](setting-copy-protection-hardware.md)

 

