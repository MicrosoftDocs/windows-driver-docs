---
title: Video Miniport Driver Header Files (Windows 2000 Model)
description: Video Miniport Driver Header Files (Windows 2000 Model)
ms.assetid: 7ce0df41-ce1e-4d76-b7e8-6d0a3576a58d
keywords:
- video miniport drivers WDK Windows 2000 , header files
- header files WDK video miniport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Video Miniport Driver Header Files (Windows 2000 Model)


## <span id="ddk_video_miniport_driver_header_files_windows_2000_model__gg"></span><span id="DDK_VIDEO_MINIPORT_DRIVER_HEADER_FILES_WINDOWS_2000_MODEL__GG"></span>


Video miniport drivers in the Windows 2000 display driver model include the following header files:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">File Name</th>
<th align="left">Contents</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>dderror.h</em></p></td>
<td align="left"><p>Contains the Win32 status constants that miniport drivers return to the video port driver, which are also returned to the miniport driver&#39;s corresponding kernel-mode display driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>devioctl.h</em></p></td>
<td align="left"><p>Contains the macros and constants used to define I/O control codes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>miniport.h</em></p></td>
<td align="left"><p>Contains the basic types, constants, and structures for video (and SCSI) miniport drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>ntddvdeo.h</em></p></td>
<td align="left"><p>Contains the system-defined I/O control codes (IOCTLs) and corresponding structures that are sent in video request packets (<a href="https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-video-request-packet--vrp-" data-raw-source="[&lt;em&gt;VRPs&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-video-request-packet--vrp-)"><em>VRPs</em></a>) to video miniport drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>tvout.h</em></p></td>
<td align="left"><p>Contains the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570173" data-raw-source="[&lt;strong&gt;VIDEOPARAMETERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570173)"><strong>VIDEOPARAMETERS</strong></a> structure used to implement TV connector and copy protection support and the constants used in this structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>video.h</em></p></td>
<td align="left"><p>Contains the <strong>VideoPort</strong><em>Xxx</em> and <em>SvgaHwIoPortXxx</em> video port function declarations, video-specific structures, such as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570547" data-raw-source="[&lt;strong&gt;VIDEO_REQUEST_PACKET&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570547)"><strong>VIDEO_REQUEST_PACKET</strong></a>, and the <em>HwVidXxx</em> video miniport function prototypes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>videoagp.h</em></p></td>
<td align="left"><p>Contains the AGP-specific structures, <em>AgpXxx</em> miniport driver function prototypes, and <strong>VideoPort</strong><em>Xxx</em> function declarations required to implement AGP support in a video miniport driver.</p></td>
</tr>
</tbody>
</table>

 

These headers are shipped with the Windows Driver Kit (WDK). For more detailed information about the functions, structures, system-defined I/O control codes, and constants in these header files, see [GDI Functions](https://msdn.microsoft.com/library/windows/hardware/ff566543).

 

 





