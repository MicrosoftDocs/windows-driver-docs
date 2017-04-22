---
title: Forced Versus Connected Targets
description: Forced Versus Connected Targets
ms.assetid: 690e585b-3c90-4373-844d-42afe033b59b
keywords:
- connecting displays WDK Windows 7 display , CCD concepts, forced versus connected targets
- connecting displays WDK Windows Server 2008 R2 display , CCD concepts, forced versus connected targets
- configuring displays WDK Windows 7 display , CCD concepts, forced versus connected targets
- configuring displays WDK Windows Server 2008 R2 display , CCD concepts, forced versus connected targets
- CCD concepts WDK Windows 7 display , forced versus connected targets
- CCD concepts WDK Windows Server 2008 R2 display , forced versus connected targets
- forced versus connected targets WDK Windows 7 display
- forced versus connected targets WDK Windows Server 2008 R2 display
- connected versus forced targets WDK Windows 7 display
- connected versus forced targets WDK Windows Server 2008 R2 display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Forced Versus Connected Targets


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The CCD APIs introduce the concepts of connected monitors and forceable targets. A monitor is connected to a target if the GPU can detect the presence of the monitor, which is a physical attribute of the monitor and target. A target is forceable if the GPU can send a display signal out of the target even if the GPU cannot detect a connected monitor. All analog target types are considered forceable, and all digital targets are not considered forceable. The following table describes the combination of connected and forced states when the path is active and not active.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Path-active state</th>
<th align="left">Path-forced state</th>
<th align="left">Monitor-connection state</th>
<th align="left">Result</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Active</p></td>
<td align="left"><p>Forced</p></td>
<td align="left"><p>Connected</p></td>
<td align="left"><p>Target output is enabled because a monitor is connected and is active.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Active</p></td>
<td align="left"><p>Forced</p></td>
<td align="left"><p>Not connected</p></td>
<td align="left"><p>Target output is enabled as the path is being forced and is active.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Active</p></td>
<td align="left"><p>Not forced</p></td>
<td align="left"><p>Connected</p></td>
<td align="left"><p>Target output is enabled because a monitor is connected and is active.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Active</p></td>
<td align="left"><p>Not forced</p></td>
<td align="left"><p>Not connected</p></td>
<td align="left"><p>The path cannot be set because it is not being forced and the monitor is not connected.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Not active</p></td>
<td align="left"><p>Forced</p></td>
<td align="left"><p>Connected</p></td>
<td align="left"><p>Target output can be enabled because it is being forced and a monitor is connected.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Not active</p></td>
<td align="left"><p>Forced</p></td>
<td align="left"><p>Not connected</p></td>
<td align="left"><p>Target output can be enabled because it is being forced.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Not active</p></td>
<td align="left"><p>Not forced</p></td>
<td align="left"><p>Connected</p></td>
<td align="left"><p>Target output can be enabled because a monitor is connected.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Not active</p></td>
<td align="left"><p>Not forced</p></td>
<td align="left"><p>Not connected</p></td>
<td align="left"><p>Target output cannot be enabled because a monitor is not connected and the path is not being forced.</p></td>
</tr>
</tbody>
</table>

 

The following table describes several types of possible forced state for each path.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Forced state</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Normal force</p></td>
<td align="left"><p>This forced state is lost after power transitions, reboots, or forced state is turned off.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Path-persistent</p></td>
<td align="left"><p>This forced state is lost after reboot. The Microsoft Win32 <strong>ChangeDisplaySettingsEx</strong> function always destroys all path-persisted monitors even if those monitors in their paths are the target of the <strong>ChangeDisplaySettingsEx</strong> call. If a caller calls the [<strong>SetDisplayConfig</strong>](https://msdn.microsoft.com/library/windows/hardware/ff569533) CCD function with the SDC_USE_SUPPLIED_DISPLAY_CONFIG or SDC_TOPOLOGY_SUPPLIED flag set in the <em>Flags</em> parameter, <strong>SetDisplayConfig</strong> removes the path-persisted monitor if the new topology does not include the path that the monitor is in. For all other SDC_TOPOLOGY_XXX flags that the caller specifies in the <em>Flags</em> parameter, <strong>SetDisplayConfig</strong> removes the path-persisted monitor unless the caller also specifies the SDC_PATH_PERSIST_IF_REQUIRED flag and the path is active in the new topology.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Boot persistent</p></td>
<td align="left"><p>This forced state is only lost when it is turned off. This state is persistent across system reboots.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Forced%20Versus%20Connected%20Targets%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




