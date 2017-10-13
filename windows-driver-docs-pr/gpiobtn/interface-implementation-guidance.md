---
title: Interface implementation guidance
author: windows-driver-content
description: This section provides guidance for interface implementation.
ms.assetid: E97A880F-0422-432C-8567-444CA6FD2980
---

# Interface implementation guidance


This section provides guidance for interface implementation.

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
<td align="left"><p>[Available interfaces and related APIs](available-interfaces-and-related-apis.md)</p></td>
<td align="left"><p>There are three GPIO interfaces: one for each device. Each interface is referenced by a GUID.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Indicator implementation](indicator-implementation.md)</p></td>
<td align="left"><p>This topic describes indicator implementation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Button implementation](button-implementation.md)</p></td>
<td align="left"><p>We recommend that you use a physical GPIO resource for both the buttons and state indicators.</p></td>
</tr>
</tbody>
</table>

 

## <span id="System_state"></span><span id="system_state"></span><span id="SYSTEM_STATE"></span>System state


The default state for all buttons that are supported by the inbox driver on load is in the UP position.

The first indication by using the interface toggled the specified button (by index) to a state of DOWN.

The default state of the laptop/slate mode indicator is SLATE.

The default state of the docked mode indicator is UNDOCKED.

The first indication by using the interface toggled the indicator to the other state.

To query the state, you can use the GetSystemMetric API as follows:

``` syntax
int WINAPI GetSystemMetrics(
  _In_  int nIndex
);
```

Parameters that are available for indicators:

-   SM\_SYSTEMDOCKED for the docking state. The call returns 0 for Undocked Mode and non-zero otherwise.
-   SM\_CONVERTIBLESLATEMODE for the slate mode. The call returns 0 for Slate Mode and non-zero otherwise.

## <span id="Notifications"></span><span id="notifications"></span><span id="NOTIFICATIONS"></span>Notifications


When either system metric SM\_CONVERTIBLESLATEMODE or SM\_SYSTEMDOCKED changes, a broadcast message is sent by the system by using WM\_SETTINGCHANGE.

The LPARAM of the WM\_SETTINGCHANGE message indicates which system metric has changed by using a string of either “ConvertibleSlateMode” or “SystemDockMode”.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[gpiobtn\gpiobtn]:%20Interface%20implementation%20guidance%20%20RELEASE:%20%289/25/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


