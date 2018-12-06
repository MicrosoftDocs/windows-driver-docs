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
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p>This forced state is lost after reboot. The Microsoft Win32 <strong>ChangeDisplaySettingsEx</strong> function always destroys all path-persisted monitors even if those monitors in their paths are the target of the <strong>ChangeDisplaySettingsEx</strong> call. If a caller calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff569533" data-raw-source="[&lt;strong&gt;SetDisplayConfig&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff569533)"><strong>SetDisplayConfig</strong></a> CCD function with the SDC_USE_SUPPLIED_DISPLAY_CONFIG or SDC_TOPOLOGY_SUPPLIED flag set in the <em>Flags</em> parameter, <strong>SetDisplayConfig</strong> removes the path-persisted monitor if the new topology does not include the path that the monitor is in. For all other SDC_TOPOLOGY_XXX flags that the caller specifies in the <em>Flags</em> parameter, <strong>SetDisplayConfig</strong> removes the path-persisted monitor unless the caller also specifies the SDC_PATH_PERSIST_IF_REQUIRED flag and the path is active in the new topology.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Boot persistent</p></td>
<td align="left"><p>This forced state is only lost when it is turned off. This state is persistent across system reboots.</p></td>
</tr>
</tbody>
</table>

 

 

 





