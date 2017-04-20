---
title: Obtaining Additional Monitor Target Modes
description: Obtaining Additional Monitor Target Modes
ms.assetid: fc0e2d43-8fc2-4757-ba77-f72a01e04343
keywords:
- monitor target modes WDK display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Obtaining Additional Monitor Target Modes


Beginning with Windows 7, a new monitor interface is available, [**DXGK\_MONITOR\_INTERFACE\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff561968). It provides two additional functions that are not in the original [**DXGK\_MONITOR\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff561949) interface:

[**pfnGetAdditionalMonitorModeSet**](https://msdn.microsoft.com/library/windows/hardware/ff561970)

[**pfnReleaseAdditionalMonitorModeSet**](https://msdn.microsoft.com/library/windows/hardware/ff561977)

These functions provide a dynamic and scalable way for a display miniport driver to add target modes to the VidPN target. In comparison, the DXGK\_MONITOR\_INTERFACE interface provides only a static list of target modes. Using these functions, the driver can query the operating system for a list of additional modes that it should enumerate. The driver can validate the requested modes and reject those that the monitor does not support.

When the display miniport driver receives a call to the driver-implemented [**DxgkDdiEnumVidPnCofuncModality**](https://msdn.microsoft.com/library/windows/hardware/ff559649) function to enumerate target modes,

it should use the following procedure to add compatible timing information to the target mode set:

1.  Return the filtered additional target modes that it obtains when it calls [**pfnGetAdditionalMonitorModeSet**](https://msdn.microsoft.com/library/windows/hardware/ff561970). It should also return the regular target modes, as described in [Enumerating Cofunctional VidPN Source and Target Modes](enumerating-cofunctional-vidpn-source-and-target-modes.md).

2.  The **pfnGetAdditionalMonitorModeSet** function will return the following:
    -   *ppAdditionalModesSet*, a list of additional timing modes in [**DXGK\_TARGETMODE\_DETAIL\_TIMING**](https://msdn.microsoft.com/library/windows/hardware/ff562060) format.
    -   *pNumberModes,* the number of timing modes.

3.  Iterate through all of these timing modes.

4.  Filter out all incompatible timing modes and any regular modes that were already supplied during the call to *DxgkDdiEnumVidPnCofuncModality*.

5.  Convert the remaining timing modes to [**D3DKMDT\_VIDPN\_TARGET\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff546729) type.

6.  Add all of the remaining timing modes to the VidPN target mode set.

7.  Call [**pfnReleaseAdditionalMonitorModeSet**](https://msdn.microsoft.com/library/windows/hardware/ff561977) to release the additional timing mode list that was returned from **pfnGetAdditionalMonitorModeSet**.

The display miniport driver should add all additional timing modes that are supported by the hardware to the VidPN source mode set and the target mode set. When the display mode manager (DMM) generates a mode list, all display modes, including additional timing modes, that are not supported by the monitor are indicated as not being supported by the monitor and appear only in the raw mode list. Regardless of whether a monitor is connected or not, the miniport driver should report all VidPN source and target mode sets that are supported by the monitor. A driver that reports only monitor-supported modes must also report the additional modes that are not supported by the currently connected monitor.

### <span id="crt_monitors"></span><span id="CRT_MONITORS"></span>**CRT Monitors**

For CRT monitors, DMM adds as an additional target mode the 640 x 480 x 60Hz standard monitor timing that is defined in the Video Electronics Standards Association (VESA) specification, *VESA and Industry Standards and Guidelines for Computer Display Monitor Timing version 1.0*.

### <span id="dtv_and_hdtv_monitors"></span><span id="DTV_AND_HDTV_MONITORS"></span>**DTV and HDTV Monitors**

For Digital Television (DTV) and High-Definition Television (HDTV) monitors, DMM adds as additional target modes all the standard DTV modes that are required by the [WHCK]( http://go.microsoft.com/fwlink/p/?linkid=258342) Automated Test GRAPHICS-0043, as shown in the following tables. A display miniport driver should prune all modes that are not supported by the display hardware.

**59.95Hz DTV System:**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">DTV Format</th>
<th align="left">HDTV Format</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>640 x 480p x 59.94Hz, Aspect Ratio 4:3</p></td>
<td align="left"><p>640 x 480p x 59.94Hz, Aspect Ratio 4:3</p></td>
</tr>
<tr class="even">
<td align="left"><p>720(1440) x 480i x 59.94Hz, Aspect Ratio 4:3</p></td>
<td align="left"><p>720(1440) x 480i x 59.94Hz, Aspect Ratio 4:3</p></td>
</tr>
<tr class="odd">
<td align="left"><p>720(1440) x 480i x 59.94Hz , Aspect Ratio 16:9</p></td>
<td align="left"><p>720(1440) x 480i x 59.94Hz , Aspect Ratio 16:9</p></td>
</tr>
<tr class="even">
<td align="left"><p>720 x 480p x 59.94Hz, Aspect Ratio 4:3</p></td>
<td align="left"><p>720 x 480p x 59.94Hz, Aspect Ratio 4:3</p></td>
</tr>
<tr class="odd">
<td align="left"><p>720 x 480p x 59.94Hz, Aspect Ratio 16:9</p></td>
<td align="left"><p>720 x 480p x 59.94Hz, Aspect Ratio 16:9</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>1280 x 720p x 59.94Hz, Aspect Ratio 16:9</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"><p>1920 x1080i x 59.94Hz, Aspect Ratio 16:9</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>1920 x 1080p x 59.94Hz, Aspect Ratio 16:9</p></td>
</tr>
</tbody>
</table>

 

**50Hz DTV System:**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">DTV Format</th>
<th align="left">HDTV Format</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>640 x 480p x 59.94Hz, Aspect Ratio 4:3</p></td>
<td align="left"><p>640 x 480p x 59.94Hz, Aspect Ratio 4:3</p></td>
</tr>
<tr class="even">
<td align="left"><p>720(1440) x 576i x 50Hz, Aspect Ratio 4:3</p></td>
<td align="left"><p>720(1440) x 576i x 50Hz, Aspect Ratio 4:3</p></td>
</tr>
<tr class="odd">
<td align="left"><p>720(1440) x 576i x 50Hz, Aspect Ratio 16:9</p></td>
<td align="left"><p>720(1440) x 576i x 50Hz, Aspect Ratio 16:9</p></td>
</tr>
<tr class="even">
<td align="left"><p>720 x 576p x 50Hz, Aspect Ratio 4:3</p></td>
<td align="left"><p>720x 576p x 50Hz, Aspect Ratio 4:3</p></td>
</tr>
<tr class="odd">
<td align="left"><p>720 x 576p x 50Hz, Aspect Ratio 16:9</p></td>
<td align="left"><p>720x 576p x 50Hz, Aspect Ratio 16:9</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>1280 x 720p x 50Hz, Aspect Ratio 16:9</p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"><p>1920 x 1080i x 50Hz, Aspect Ratio 16:9</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>1920 x 1080p x 50Hz, Aspect Ratio 16:9</p></td>
</tr>
</tbody>
</table>

 

Miniport drivers written for Windows Vista should continue to conform with the [WHCK]( http://go.microsoft.com/fwlink/p/?linkid=258342) Automated Test GRAPHICS-0043 and add the additional DTV modes specified in these tables. Drivers written for Windows 7 only have to support the new **pfnGetAdditionalMonitorModeSet** and **pfnReleaseAdditionalMonitorModeSet** functions.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Obtaining%20Additional%20Monitor%20Target%20Modes%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




