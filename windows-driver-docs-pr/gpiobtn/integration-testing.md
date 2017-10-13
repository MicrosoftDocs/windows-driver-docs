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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[gpiobtn\gpiobtn]:%20Integration%20testing%20%20RELEASE:%20%289/25/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


