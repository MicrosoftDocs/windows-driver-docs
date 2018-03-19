---
title: Integration testing
author: windows-driver-content
description: It is important to perform integration testing to ensure an optimal end-to-end user experience.
ms.assetid: 61C1AC15-498B-432B-8D26-0303425114FF
---

# Integration testing


It is important to perform integration testing to ensure an optimal end-to-end user experience

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
<td align="left"><p>[Indicator testing](indicator-testing.md)</p></td>
<td align="left"><p>This topic describes common indicator step procedures and examples.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Convertible testing](convertible-testing.md)</p></td>
<td align="left"><p>This topic describes tests for convertibles.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Touchscreen laptop system testing](touchscreen-laptop-system-testing.md)</p></td>
<td align="left"><p>This topic describes tests for touchscreen laptop systems.</p></td>
</tr>
</tbody>
</table>

 

Each system is unique in the way it implements the following:

-   Hardware buttons and their location
-   Various ways to switch between laptop and slate mode (for convertibles)

For more information about the scenarios described in this section, see [GPIO buttons and indicators implementation guide for Windows 8.1](gpio-buttons-and-indicators-implementation-guide-for-windows-8-1.md).

*Table 1 Indicator Combination Expected Behavior* shows the expected behavior for each indicator combination.

**Table 1 Indicator Combination Expected Behavior**

| Mode   | Dock     | Onscreen keyboard displayed | Auto-rotation enabled |
|--------|----------|-----------------------------|-----------------------|
| Laptop | Undocked | No                          | No                    |
| Laptop | Docked   | No                          | No                    |
| Slate  | Undocked | Yes                         | Yes                   |
| Slate  | Docked   | Yes                         | No                    |

 

This section describes a set of tests for various scenarios that involve docking and laptops/slate mode indicators. If any test fails, see [GPIO logging and investigations](gpio-logging-and-investigations.md).

 

 




