---
title: PortCls Registry Power Settings
description: This topic explains the PortCls registry power settings for Windows.
ms.date: 09/29/2022
---

# PortCls Registry Power Settings


This topic explains the PortCls registry power settings.

In Windows, (PortCls) miniport drivers can use registry values in the driver’s registry key to do the following:

- Determine whether or not PortCls enables idle power management

- Determine the idle timeout values for battery conservation mode, versus high performance mode

By default, Windows has power settings that PortCls uses to determine whether to register for "device idle" detection with the power manager, when the runtime power framework indicates that power is no longer required. The parameters that are used to describe the power setting profile are defined as follows.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Registry value</th>
<th align="left">Data type</th>
<th align="left">Default value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">ConservationIdleTime</td>
<td align="left">REG_BINARY</td>
<td align="left">0</td>
<td align="left">Idle timeout for the device, when the system is on battery power.</td>
</tr>
<tr class="even">
<td align="left">IdlePowerState</td>
<td align="left">REG_BINARY</td>
<td align="left">3 (D3)
<p>Valid values:</p>
1 - D1
2 - D2
3 - D3</td>
<td align="left">Specifies the power state that the device will enter, when power is no longer needed.</td>
</tr>
<tr class="odd">
<td align="left">PerformanceIdleTime</td>
<td align="left">REG_BINARY</td>
<td align="left">0</td>
<td align="left">Idle timeout for the device, when the system is on AC power.</td>
</tr>
</tbody>
</table>

 

The following Windows registry fragment shows the syntax that is used for providing the power setting information.

```inf
[MyAudioDevice.AddReg]
HKR,PowerSettings,ConservationIdleTime,%REG_BINARY%, 0x1e, 0x00, 0x00, 0x00
HKR,PowerSettings,PerformanceIdleTime,%REG_BINARY%, 0x00, 0x00, 0x00, 0x00
HKR,PowerSettings,IdlePowerState,%REG_BINARY%, 0x03, 0x00, 0x00, 0x00
```

The preceding fragment shows a hexadecimal (hex) value of "1e" for the *ConservationIdleTime*, and this equates to a 30-second idle timeout. The hex value of "0" shown for *PerformanceIdleTime* means that idle management has been disabled. And the value of "03" shown for the *IdlePowerState* means that when power is no longer needed, the device associated with this power setting profile will enter the D3 power state.



