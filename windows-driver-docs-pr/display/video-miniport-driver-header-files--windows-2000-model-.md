---
title: Video Miniport Driver Header Files (Windows 2000 Model)
description: Video Miniport Driver Header Files (Windows 2000 Model)
keywords:
- video miniport drivers WDK Windows 2000 , header files
- header files WDK video miniport
ms.date: 04/20/2017
---

# Video Miniport Driver Header Files (Windows 2000 Model)

Video miniport drivers in the Windows 2000 display driver model include the following header files:

| File Name | Contents |
| --------- | -------- |
| *dderror.h* | Contains the Win32 status constants that miniport drivers return to the video port driver, which are also returned to the miniport driver's corresponding kernel-mode display driver. |
| *devioctl.h* | Contains the macros and constants used to define I/O control codes. |
| *miniport.h* | Contains the basic types, constants, and structures for video (and SCSI) miniport drivers. |
| *ntddvdeo.h* | Contains the system-defined I/O control codes (IOCTLs) and corresponding structures that are sent in video request packets (VRPs) to video miniport drivers. |
| *tvout.h* | Contains the **VIDEOPARAMETERS** structure used to implement TV connector and copy protection support and the constants used in this structure. |
| *video.h* | Contains the **VideoPort***Xxx* and *SvgaHwIoPortXxx* video port function declarations, video-specific structures, such as the **VIDEO_REQUEST_PACKET**, and the *HwVidXxx* video miniport function prototypes. |
| *videoagp.h* | Contains the AGP-specific structures, *AgpXxx* miniport driver function prototypes, and **VideoPort***Xxx* function declarations required to implement AGP support in a video miniport driver. |

These headers are shipped with the Windows Driver Kit (WDK). For more detailed information about the functions, structures, system-defined I/O control codes, and constants in these header files, see [Using the Graphics DDI](using-the-graphics-ddi.md).
