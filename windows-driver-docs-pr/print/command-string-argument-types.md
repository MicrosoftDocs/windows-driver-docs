---
title: Command String Argument Types
description: Command String Argument Types
ms.assetid: c7540c3f-265a-4fee-aca9-b8cc10b6be8f
keywords:
- printer commands WDK Unidrv , strings
- command strings WDK Unidrv
- strings WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Command String Argument Types





When you include arguments in command strings, you must specify each argument's type. Each argument type specification is a single letter, preceded by a percent sign.

The following table lists all the argument type specifiers.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Argument Type Specifier</th>
<th>Description of resulting value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>%&lt;<em>Digits</em>&gt;d</p></td>
<td><p>ASCII string representing a decimal value, including a minus sign if negative. <em>&lt;Digits&gt;</em> is an optional number indicating the string length.</p></td>
</tr>
<tr class="even">
<td><p>%&lt;<em>Digits</em>&gt;D</p></td>
<td><p>ASCII string representing decimal value, including a plus or minus sign. <em>&lt;Digits&gt;</em> is an optional number indicating the string length.</p></td>
</tr>
<tr class="odd">
<td><p>%c</p></td>
<td><p>Binary byte.</p></td>
</tr>
<tr class="even">
<td><p>%C</p></td>
<td><p>Binary byte added to ASCII &quot;0&quot;.</p></td>
</tr>
<tr class="odd">
<td><p>%f</p></td>
<td><p>Unsigned ASCII string representing a decimal value, with a decimal point inserted as the third character from the right, as in &quot;12.25&quot;.</p></td>
</tr>
<tr class="even">
<td><p>%g</p></td>
<td><p>2 * ABS(<em>Parameter</em>) + IS_NEGATIVE(<em>Parameter</em>) as a base-64 number, least significant digit to most significant digit. The most significant digit (0-63) is represented by bytes 191 through 254. All other digits are represented by bytes 63 through 126. &quot;IS_NEGATIVE(<em>Parameter</em>)&quot; is 1 if <em>Parameter</em> is negative, and zero otherwise.</p></td>
</tr>
<tr class="odd">
<td><p>%l</p></td>
<td><p>Binary word, least significant byte first.</p></td>
</tr>
<tr class="even">
<td><p>%m</p></td>
<td><p>Binary word, most significant byte first.</p></td>
</tr>
<tr class="odd">
<td><p>%n</p></td>
<td><p>Canon integer encoding. Binary value encoded from most significant byte to least significant byte. The 4 least significant bits are encoded as 001<em>sbbbb</em>, where <em>s</em> represents the sign (0 is negative, 1 is positive), and <em>b</em> represents a significant bit of the integer. The next most significant 6 bits are encoded as 01<em>bbbbbb</em>. For example, 254 (11111110) is represented as (01001111 00111110).</p></td>
</tr>
<tr class="even">
<td><p>%q</p></td>
<td><p>ASCII string representing a QUME hexadecimal number. For Toshiba/Qume devices.</p></td>
</tr>
<tr class="odd">
<td><p>%v</p></td>
<td><p>NEC VFU (Vertical Format Unit) encoding. The specified variable&#39;s value is divided by 1/6 inch. The result is the number of times VFU data is sent to the printer.</p></td>
</tr>
</tbody>
</table>

 

You can specify a range of acceptable values for any argument. To do so, include the argument's minimum and maximum values by placing them inside a set of square brackets ( \[, \] ), immediately following the argument type specifier, and separating the values by a comma. For example, the following command specifies 0 through 255 as an acceptable range for the value of LinefeedSpacing/2:

```cpp
*Command:CmdSetLineSpacing{*Cmd:"<1B>3"%c[0,255]{(LinefeedSpacing/2)}}
```

 

 




