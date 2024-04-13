---
title: Obtaining Additional Monitor Target Modes
description: Obtaining Additional Monitor Target Modes
keywords:
- monitor target modes WDK display
ms.date: 04/20/2017
---

# Obtaining Additional Monitor Target Modes


Beginning with Windows 7, a new monitor interface is available, [**DXGK\_MONITOR\_INTERFACE\_V2**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_monitor_interface_v2). It provides two additional functions that are not in the original [**DXGK\_MONITOR\_INTERFACE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_monitor_interface) interface:

[**pfnGetAdditionalMonitorModeSet**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_monitor_getadditionalmonitormodeset)

[**pfnReleaseAdditionalMonitorModeSet**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_monitor_releaseadditionalmonitormodeset)

These functions provide a dynamic and scalable way for a display miniport driver to add target modes to the VidPN target. In comparison, the DXGK\_MONITOR\_INTERFACE interface provides only a static list of target modes. Using these functions, the driver can query the operating system for a list of additional modes that it should enumerate. The driver can validate the requested modes and reject those that the monitor does not support.

When the display miniport driver receives a call to the driver-implemented [**DxgkDdiEnumVidPnCofuncModality**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_enumvidpncofuncmodality) function to enumerate target modes,

it should use the following procedure to add compatible timing information to the target mode set:

1.  Return the filtered additional target modes that it obtains when it calls [**pfnGetAdditionalMonitorModeSet**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_monitor_getadditionalmonitormodeset). It should also return the regular target modes, as described in [Enumerating Cofunctional VidPN Source and Target Modes](enumerating-cofunctional-vidpn-source-and-target-modes.md).

2.  The **pfnGetAdditionalMonitorModeSet** function will return the following:
    -   *ppAdditionalModesSet*, a list of additional timing modes in [**DXGK\_TARGETMODE\_DETAIL\_TIMING**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_dxgk_targetmode_detail_timing) format.
    -   *pNumberModes,* the number of timing modes.

3.  Iterate through all of these timing modes.

4.  Filter out all incompatible timing modes and any regular modes that were already supplied during the call to *DxgkDdiEnumVidPnCofuncModality*.

5.  Convert the remaining timing modes to [**D3DKMDT\_VIDPN\_TARGET\_MODE**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_target_mode) type.

6.  Add all of the remaining timing modes to the VidPN target mode set.

7.  Call [**pfnReleaseAdditionalMonitorModeSet**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_monitor_releaseadditionalmonitormodeset) to release the additional timing mode list that was returned from **pfnGetAdditionalMonitorModeSet**.

The display miniport driver should add all additional timing modes that are supported by the hardware to the VidPN source mode set and the target mode set. When the display mode manager (DMM) generates a mode list, all display modes, including additional timing modes, that are not supported by the monitor are indicated as not being supported by the monitor and appear only in the raw mode list. Regardless of whether a monitor is connected or not, the miniport driver should report all VidPN source and target mode sets that are supported by the monitor. A driver that reports only monitor-supported modes must also report the additional modes that are not supported by the currently connected monitor.

## CRT Monitors

For CRT monitors, DMM adds as an additional target mode the 640 x 480 x 60Hz standard monitor timing that is defined in the Video Electronics Standards Association (VESA) specification, *VESA and Industry Standards and Guidelines for Computer Display Monitor Timing version 1.0*.

## DTV and HDTV Monitors

For Digital Television (DTV) and High-Definition Television (HDTV) monitors, DMM adds as additional target modes all the standard DTV modes that are required by the [WHCK](/windows-hardware/test/hlk/windows-hardware-lab-kit) Automated Test GRAPHICS-0043, as shown in the following tables. A display miniport driver should prune all modes that are not supported by the display hardware.

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

 

Miniport drivers written for Windows Vista should continue to conform with the [WHCK](/windows-hardware/test/hlk/windows-hardware-lab-kit) Automated Test GRAPHICS-0043 and add the additional DTV modes specified in these tables. Drivers written for Windows 7 only have to support the new **pfnGetAdditionalMonitorModeSet** and **pfnReleaseAdditionalMonitorModeSet** functions.


 
## See also

[Determining Whether a VidPN is Supported on a Display Adapter](determining-whether-a-vidpn-is-supported-on-a-display-adapter.md)

[Enumerating Cofunctional VidPN Source and Target Modes](enumerating-cofunctional-vidpn-source-and-target-modes.md)

[Video Present Network Terminology](video-present-network-terminology.md)

[VidPN Objects and Interfaces](vidpn-objects-and-interfaces.md)
