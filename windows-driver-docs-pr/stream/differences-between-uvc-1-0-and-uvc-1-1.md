---
title: Differences between UVC 1.0 and UVC 1.1
description: Differences between UVC 1.0 and UVC 1.1
ms.assetid: 5199fc4f-7bc2-4edb-bb52-cd2028756f64
keywords:
- USB Video Class drivers WDK AVStream , version differences
- USB Video Class drivers WDK AVStream , differences between UVC 1.0 and UVC 1.1
- Video Class drivers WDK USB , differences between UVC 1.0 and UVC 1.1
- UVC drivers WDK AVStream , differences between UVC 1.0 and UVC 1.1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Differences between UVC 1.0 and UVC 1.1


When you design UVC-compliant hardware to work with Windows 7 or earlier version of Windows, you must decide between supporting UVC 1.0 and 1.1.

A device that is compliant with UVC 1.1 should set the **bcdUVC** flag in the Class-Specific VC Interface to 0x110. In addition, if the optional Processing Unit descriptor exists, a 1.1-compliant device should do the following:

1.  Add a **bmVideoStandards** field to the Processing Unit descriptor.

2.  Update the **bLength** field in the Processing Unit.

3.  Update **wTotalLength** to reflect the larger PU size of the Processing Unit.

The following table summarizes the differences between UVC 1.0 and 1.1.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Status</th>
<th>Descriptor/Request/Control</th>
<th>Field</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>change</p></td>
<td><p>Class-Specific VC Interface</p></td>
<td><p><strong>bcdUVC</strong></p></td>
<td><p>0x110 for 1.1, 0x100 for 1.0</p></td>
</tr>
<tr class="even">
<td><p>obsolete</p></td>
<td><p>Class-Specific VC Interface</p></td>
<td><p><strong>dwClockFrequency</strong></p></td>
<td><p>Unused for 1.1</p></td>
</tr>
<tr class="odd">
<td><p>change</p></td>
<td><p>Processing Unit</p></td>
<td><p><strong>bLength</strong></p></td>
<td><p>10+n for 1.1, 9+n for 1.0</p></td>
</tr>
<tr class="even">
<td><p>new</p></td>
<td><p>Processing Unit</p></td>
<td><p><strong>bmVideoStandards</strong></p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>change</p></td>
<td><p>Class-Specific VS Interface Input Header</p></td>
<td><p><strong>bmaControls(n)</strong></p></td>
<td><p>1.1 uses some of these bits differently in &quot;Probe and Commit&quot;</p></td>
</tr>
<tr class="even">
<td><p>change</p></td>
<td><p>Class-Specific VS Interface Output Header</p></td>
<td><p><strong>bLength</strong></p></td>
<td><p>9+(p*n) for 1.1, 8 for 1.0</p></td>
</tr>
<tr class="odd">
<td><p>new</p></td>
<td><p>Class-Specific VS Interface Output Header</p></td>
<td><p><strong>bControlSize</strong></p></td>
<td></td>
</tr>
<tr class="even">
<td><p>new</p></td>
<td><p>Class-Specific VS Interface Output Header</p></td>
<td><p><strong>bmaControls(n)</strong></p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>obsolete</p></td>
<td><p>Interface Control</p></td>
<td><p><strong>VC_REQUEST_INDICATE_HOST_CLOCK_CONTROL</strong></p></td>
<td><p>Mandatory for 1.0 devices supporting host to device payloads that use SCR/PTS</p></td>
</tr>
<tr class="even">
<td><p>new</p></td>
<td><p>Interface Control</p></td>
<td><p><strong>GET_INFO</strong></p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>new</p></td>
<td><p>Processing Unit</p></td>
<td><p><strong>PU_DIGITAL_MULTIPLIER_CONTROL</strong></p></td>
<td></td>
</tr>
<tr class="even">
<td><p>new</p></td>
<td><p>Processing Unit</p></td>
<td><p><strong>PU_ANALOG_VIDEO_STANDARD_CONTROL</strong></p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>new</p></td>
<td><p>Processing Unit</p></td>
<td><p><strong>PU_ANALOG_LOCK_STATUS_CONTROL</strong></p></td>
<td></td>
</tr>
<tr class="even">
<td><p>change</p></td>
<td><p>Video Probe and Commit Control</p></td>
<td><p><strong>wLength</strong></p></td>
<td><p>34 for 1.1, 26 for 1.0</p></td>
</tr>
<tr class="odd">
<td><p>new</p></td>
<td><p>Video Probe and Commit Control</p></td>
<td><p><strong>dwClockFrequency</strong></p></td>
<td></td>
</tr>
<tr class="even">
<td><p>new</p></td>
<td><p>Video Probe and Commit Control</p></td>
<td><p><strong>bmFramingInfo</strong></p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>new</p></td>
<td><p>Video Probe and Commit Control</p></td>
<td><p><strong>bPreferredVersion</strong></p></td>
<td></td>
</tr>
<tr class="even">
<td><p>new</p></td>
<td><p>Video Probe and Commit Control</p></td>
<td><p><strong>bMinVersion</strong></p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>new</p></td>
<td><p>Video Probe and Commit Control</p></td>
<td><p><strong>bMaxVersion</strong></p></td>
<td></td>
</tr>
<tr class="even">
<td><p>new</p></td>
<td><p>Video Probe and Commit Control</p></td>
<td><p><strong>GET_INFO</strong> for VS_PROBE_CONTROL</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>new</p></td>
<td><p>Video Probe and Commit Control</p></td>
<td><p><strong>GET_INFO</strong> for VS_COMMIT_CONTROL</p></td>
<td></td>
</tr>
<tr class="even">
<td><p>obsolete</p></td>
<td><p>Class-Specific VS Interface</p></td>
<td><p><strong>VS_FORMAT_MPEG1</strong></p></td>
<td><p>Not supported by any Windows operating system</p></td>
</tr>
<tr class="odd">
<td><p>obsolete</p></td>
<td><p>Class-Specific VS Interface</p></td>
<td><p><strong>VS_FORMAT_MPEG2PS</strong></p></td>
<td><p>Not supported by any Windows operating system</p></td>
</tr>
<tr class="even">
<td><p>obsolete</p></td>
<td><p>Class-Specific VS Interface</p></td>
<td><p><strong>VS_FORMAT_MPEG4SL</strong></p></td>
<td><p>Not supported by any Windows operating system</p></td>
</tr>
<tr class="odd">
<td><p>obsolete</p></td>
<td><p>Class-Specific VS Interface</p></td>
<td><p><strong>VS_FORMAT_VENDOR</strong></p></td>
<td><p>Not supported by any Windows operating system</p></td>
</tr>
<tr class="even">
<td><p>obsolete</p></td>
<td><p>Class-Specific VS Interface</p></td>
<td><p><strong>VS_FRAME_VENDOR</strong></p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>new</p></td>
<td><p>Class-Specific VS Interface</p></td>
<td><p><strong>VS_FORMAT_FRAME_BASED</strong></p></td>
<td></td>
</tr>
<tr class="even">
<td><p>new</p></td>
<td><p>Class-Specific VS Interface</p></td>
<td><p><strong>VS_FRAME_FRAME_BASED</strong></p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>new</p></td>
<td><p>Class-Specific VS Interface</p></td>
<td><p><strong>VS_FORMAT_STREAM_BASED</strong></p></td>
<td></td>
</tr>
</tbody>
</table>

 

For UVC 1.0 devices, the length of the MPEG2TS format descriptor is 7. Because UVC 1.1 includes a new 16 byte GUID field, the length of the MPEG2TS format descriptor is 23.

Accordingly, if you update the MPEG2TS descriptor to 23 bytes, you must also set the **bcdUVC** flag in the Class-Specific VC Interface to 0x110.

 

 




