---
title: Command String Argument Types
description: Command String Argument Types
ms.assetid: c7540c3f-265a-4fee-aca9-b8cc10b6be8f
keywords: ["printer commands WDK Unidrv , strings", "command strings WDK Unidrv", "strings WDK Unidrv"]
---

# Command String Argument Types


## <a href="" id="ddk-command-string-argument-types-gg"></a>


When you include arguments in command strings, you must specify each argument's type. Each argument type specification is a single letter, preceded by a percent sign.

The following table lists all the argument type specifiers.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Argument Type Specifier</th>
<th align="left">Description of resulting value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>%&lt;<em>Digits</em>&gt;d</p></td>
<td align="left"><p>ASCII string representing a decimal value, including a minus sign if negative. <em>&lt;Digits&gt;</em> is an optional number indicating the string length.</p></td>
</tr>
<tr class="even">
<td align="left"><p>%&lt;<em>Digits</em>&gt;D</p></td>
<td align="left"><p>ASCII string representing decimal value, including a plus or minus sign. <em>&lt;Digits&gt;</em> is an optional number indicating the string length.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%c</p></td>
<td align="left"><p>Binary byte.</p></td>
</tr>
<tr class="even">
<td align="left"><p>%C</p></td>
<td align="left"><p>Binary byte added to ASCII &quot;0&quot;.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%f</p></td>
<td align="left"><p>Unsigned ASCII string representing a decimal value, with a decimal point inserted as the third character from the right, as in &quot;12.25&quot;.</p></td>
</tr>
<tr class="even">
<td align="left"><p>%g</p></td>
<td align="left"><p>2 * ABS(<em>Parameter</em>) + IS_NEGATIVE(<em>Parameter</em>) as a base-64 number, least significant digit to most significant digit. The most significant digit (0-63) is represented by bytes 191 through 254. All other digits are represented by bytes 63 through 126. &quot;IS_NEGATIVE(<em>Parameter</em>)&quot; is 1 if <em>Parameter</em> is negative, and zero otherwise.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%l</p></td>
<td align="left"><p>Binary word, least significant byte first.</p></td>
</tr>
<tr class="even">
<td align="left"><p>%m</p></td>
<td align="left"><p>Binary word, most significant byte first.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%n</p></td>
<td align="left"><p>Canon integer encoding. Binary value encoded from most significant byte to least significant byte. The 4 least significant bits are encoded as 001<em>sbbbb</em>, where <em>s</em> represents the sign (0 is negative, 1 is positive), and <em>b</em> represents a significant bit of the integer. The next most significant 6 bits are encoded as 01<em>bbbbbb</em>. For example, 254 (11111110) is represented as (01001111 00111110).</p></td>
</tr>
<tr class="even">
<td align="left"><p>%q</p></td>
<td align="left"><p>ASCII string representing a QUME hexadecimal number. For Toshiba/Qume devices.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>%v</p></td>
<td align="left"><p>NEC VFU (Vertical Format Unit) encoding. The specified variable's value is divided by 1/6 inch. The result is the number of times VFU data is sent to the printer.</p></td>
</tr>
</tbody>
</table>

 

You can specify a range of acceptable values for any argument. To do so, include the argument's minimum and maximum values by placing them inside a set of square brackets ( \[, \] ), immediately following the argument type specifier, and separating the values by a comma. For example, the following command specifies 0 through 255 as an acceptable range for the value of LinefeedSpacing/2:

```
*Command:CmdSetLineSpacing{*Cmd:"<1B>3"%c[0,255]{(LinefeedSpacing/2)}}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Command%20String%20Argument%20Types%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




