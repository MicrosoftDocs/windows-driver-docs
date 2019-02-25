---
title: Interface implementation guidance
description: This section provides guidance for interface implementation.
ms.assetid: E97A880F-0422-432C-8567-444CA6FD2980
ms.localizationpriority: medium
ms.date: 10/17/2018
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
<td align="left"><p><a href="available-interfaces-and-related-apis.md" data-raw-source="[Available interfaces and related APIs](available-interfaces-and-related-apis.md)">Available interfaces and related APIs</a></p></td>
<td align="left"><p>There are three GPIO interfaces: one for each device. Each interface is referenced by a GUID.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="indicator-implementation.md" data-raw-source="[Indicator implementation](indicator-implementation.md)">Indicator implementation</a></p></td>
<td align="left"><p>This topic describes indicator implementation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="button-implementation.md" data-raw-source="[Button implementation](button-implementation.md)">Button implementation</a></p></td>
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

 

 




