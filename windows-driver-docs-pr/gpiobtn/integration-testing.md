---
title: Integration testing
description: It is important to perform integration testing to ensure an optimal end-to-end user experience.
ms.assetid: 61C1AC15-498B-432B-8D26-0303425114FF
ms.localizationpriority: medium
ms.date: 10/17/2018
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
<td align="left"><p><a href="indicator-testing.md" data-raw-source="[Indicator testing](indicator-testing.md)">Indicator testing</a></p></td>
<td align="left"><p>This topic describes common indicator step procedures and examples.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="convertible-testing.md" data-raw-source="[Convertible testing](convertible-testing.md)">Convertible testing</a></p></td>
<td align="left"><p>This topic describes tests for convertibles.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="touchscreen-laptop-system-testing.md" data-raw-source="[Touchscreen laptop system testing](touchscreen-laptop-system-testing.md)">Touchscreen laptop system testing</a></p></td>
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

 

 




