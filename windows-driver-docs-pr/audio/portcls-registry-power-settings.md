---
title: PortCls Registry Power Settings
description: This topic explains the PortCls registry power settings for Windows 8.
ms.assetid: 148D044E-B736-4526-BDC5-2C180A590C21
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20PortCls%20Registry%20Power%20Settings%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


