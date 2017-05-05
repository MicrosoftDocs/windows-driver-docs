---
title: Video Miniport Driver Header Files (Windows 2000 Model)
description: Video Miniport Driver Header Files (Windows 2000 Model)
ms.assetid: 7ce0df41-ce1e-4d76-b7e8-6d0a3576a58d
keywords:
- video miniport drivers WDK Windows 2000 , header files
- header files WDK video miniport
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>Contains the Win32 status constants that miniport drivers return to the video port driver, which are also returned to the miniport driver's corresponding kernel-mode display driver.</p></td>
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
<td align="left"><p>Contains the system-defined I/O control codes (IOCTLs) and corresponding structures that are sent in video request packets ([<em>VRPs</em>](https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-video-request-packet--vrp-)) to video miniport drivers.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>tvout.h</em></p></td>
<td align="left"><p>Contains the [<strong>VIDEOPARAMETERS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570173) structure used to implement TV connector and copy protection support and the constants used in this structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>video.h</em></p></td>
<td align="left"><p>Contains the <strong>VideoPort</strong><em>Xxx</em> and <em>SvgaHwIoPortXxx</em> video port function declarations, video-specific structures, such as the [<strong>VIDEO_REQUEST_PACKET</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570547), and the <em>HwVidXxx</em> video miniport function prototypes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>videoagp.h</em></p></td>
<td align="left"><p>Contains the AGP-specific structures, <em>AgpXxx</em> miniport driver function prototypes, and <strong>VideoPort</strong><em>Xxx</em> function declarations required to implement AGP support in a video miniport driver.</p></td>
</tr>
</tbody>
</table>

 

These headers are shipped with the Windows Driver Kit (WDK). For more detailed information about the functions, structures, system-defined I/O control codes, and constants in these header files, see [GDI Functions](https://msdn.microsoft.com/library/windows/hardware/ff566543).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Video%20Miniport%20Driver%20Header%20Files%20%28Windows%202000%20Model%29%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




