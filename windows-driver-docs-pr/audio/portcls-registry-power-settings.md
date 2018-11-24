---
title: PortCls Registry Power Settings
description: This topic explains the PortCls registry power settings for Windows 8.
ms.assetid: 148D044E-B736-4526-BDC5-2C180A590C21
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PortCls Registry Power Settings


This topic explains the PortCls registry power settings for Windows 8.

In Windows 8, (PortCls) miniport drivers can use registry values in the driver’s registry key to do the following:

-   Determine whether or not PortCls enables idle power management

-   Determine the idle timeout values for battery conservation mode, versus high performance mode

By default, Windows 8 has power settings that PortCls uses to determine whether to register for "device idle" detection with the power manager, when the runtime power framework indicates that power is no longer required. The parameters that are used to describe the power setting profile are defined as follows.

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
<td align="left">0-second timeout.</td>
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
<td align="left">0-second timeout.</td>
</tr>
</tbody>
</table>

 

The following Windows registry fragment shows the syntax that is used for providing the power setting information.

``` syntax
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4D36E96C-E325-11CE-BFC1-08002BE10318}\0000\PowerSettings]
"ConservationIdleTime"=hex:1e,00,00,00
"PerformanceIdleTime"=hex:00,00,00,00
“IdlePowerState”=hex:03,00,00,00
```

The preceding fragment shows a hexadecimal (hex) value of "1e" for the *ConservationIdleTime*, and this equates to a 30-second idle timeout. The hex value of "0" shown for *PerformanceIdleTime* means that idle management has been disabled. And the value of "03" shown for the *IdlePowerState* means that when power is no longer needed, the device associated with this power setting profile will enter the D3 power state.

 

 




