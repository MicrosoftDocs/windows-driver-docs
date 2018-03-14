---
title: UWP device apps for cameras
description: This section introduces UWP device apps for cameras.
ms.assetid: 6CF13679-BCF3-443C-A864-4BBC54B8DA1C
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# UWP device apps for cameras


This section introduces UWP device apps for cameras. Device apps can highlight the special features of cameras through customized camera settings and special camera effects.

## <span id="in_this_section"></span>In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[How to customize camera options](how-to-customize-camera-options.md)</p></td>
<td align="left"><p>In Windows 8.1, UWP device apps let device manufacturers customize the flyout that displays more camera options in some camera apps. This topic introduces the <strong>More options</strong> flyout that's displayed by the CameraCatureUI API, and shows how the C# version of the [UWP device app for camera](http://go.microsoft.com/fwlink/p/?LinkID=227865) sample replaces the default flyout with a custom flyout.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Creating a camera driver MFT](creating-a-camera-driver-mft.md)</p></td>
<td align="left"><p>In Windows 8.1, UWP device apps let device manufacturers apply custom settings and special effects on the camera's video stream with a camera driver MFT (media foundation transform). This topic introduces driver MFTs and uses the [Driver MFT](http://go.microsoft.com/fwlink/p/?LinkID=251566) sample to show how to create one.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Considerations for driver MFTs on multi-pin cameras](driver-mfts-on-multi-pin-cameras.md)</p></td>
<td align="left"><p>Some cameras provide separate pins for preview, capture, and stills. These multi-pin cameras pose unique challenges to developers. This topic covers some points to consider when developing a camera driver MFT on a multi-pin camera.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Identifying the location of internal cameras](identifying-the-location-of-internal-cameras.md)</p></td>
<td align="left"><p>This topic provides info about supporting internal cameras on systems in Windows 8.1. It describes how to identify the physical location of built-in cameras so that they work correctly with UWP apps. It also describes how to set the Model ID so that the camera works with UWP device apps.</p></td>
</tr>
</tbody>
</table>

 

## <span id="windows_8.1_samples"></span><span id="WINDOWS_8.1_SAMPLES"></span>Windows 8.1 samples


-   The [UWP device app for camera](http://go.microsoft.com/fwlink/p/?LinkID=227865) sample provides a UWP device app that controls the effect implemented by the driver MFT.

-   The [driver MFT](http://go.microsoft.com/fwlink/p/?LinkID=251566) sample provides a driver MFT for use with a camera's UWP device app. A driver MFT is a Media Foundation Transform that's used with a specific camera when capturing video. The driver MFT is also known as MFT0 because it is the first MFT applied to the video stream captured from the camera. This MFT can provide a video effect or other processing when capturing photos or video from the camera. It can be distributed along with the driver package for a camera.

-   The [Camera Capture UI](http://go.microsoft.com/fwlink/p/?linkid=228589) sample demonstrates how to use the [Windows.Media.Capture.CameraCaptureUI](http://msdn.microsoft.com/library/windows/apps/br241030) API, which displays a full-screen UI for capturing photos or videos. The Camera Capture UI provides controls for switching from photo to video, a timer for taking time-delayed photos, and a Camera options control for adjusting camera settings.

    You can use this sample to invoke the [UWP device app for camera](http://go.microsoft.com/fwlink/p/?LinkID=227865) sample.

-   The [Camera Options UI](http://go.microsoft.com/fwlink/p/?linkid=228588) sample demonstrates how to use camera options in a UWP device app.

 

 





