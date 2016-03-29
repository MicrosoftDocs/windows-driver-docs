---
title: Standard Variable Expressions
description: Standard Variable Expressions
ms.assetid: b77c6b88-9ef2-4485-b77c-50acb21e13b9
keywords: ["printer commands WDK Unidrv , strings", "command strings WDK Unidrv", "strings WDK Unidrv", "standard variable expressions WDK Unidrv", "max_repeat"]
---

# Standard Variable Expressions


## <a href="" id="ddk-standard-variable-expressions-gg"></a>


When you specify arguments in a command string, you can specify the argument value as an expression. This expression can perform operations using the current values of the [standard variables](standard-variables.md). Each standard variable expression within a command string is delimited by braces ( {, } ).

A standard variable expression can consist of a combination of the following components:

-   Zero, one, or more [standard variables](standard-variables.md)

-   Integer [numeric values](numeric-values.md)

-   Expression operators

A standard variable expression cannot contain embedded macro references.

The expression operators are included in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Operator</th>
<th align="left">Definitions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>Val1</em><strong>+</strong><em>Val2</em></p></td>
<td align="left"><p>Addition.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>Val1</em><strong>-</strong><em>Val2</em></p></td>
<td align="left"><p>Subtraction.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>Val1</em><strong>/</strong><em>Val2</em></p></td>
<td align="left"><p>Division.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>Val1</em><strong>*</strong><em>Val2</em></p></td>
<td align="left"><p>Multiplication.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>Val1</em><strong>MOD</strong><em>Val2</em></p></td>
<td align="left"><p>Modulus. Value is the remainder of dividing <em>Val1</em> by <em>Val2</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>max</strong> ( <em>Val1</em> , <em>Val2</em> )</p></td>
<td align="left"><p>Maximum. Value is the maximum of <em>Val1</em> and <em>Val2</em>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>max_repeat</strong> ( <em>Val1</em> )</p></td>
<td align="left"><p>See the <strong>Using max_repeat</strong> section.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>min</strong> ( <em>Val1</em> , <em>Val2</em> )</p></td>
<td align="left"><p>Minimum. Value is the minimum of <em>Val1</em> and <em>Val2</em>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>( )</strong></p></td>
<td align="left"><p>Precedence operators. If not used, C-language precedence is used.</p></td>
</tr>
</tbody>
</table>

 

Standard variable expressions do not modify the values assigned to the standard variables. The calculated value is placed in the escape sequence, using the format specified by the [command string argument type](command-string-argument-types.md) specifier.

### <a href="" id="ddk-using-max-repeat-gg"></a>Using max\_repeat

The use of **max\_repeat** is best explained with an example. Suppose a GPD file contains the following entry:

```
*Command:CmdXMoveRelRight{*Cmd:"<1B>["%d[0,9600]{max_repeat((DestXRel/4))}"a"}
```

This command contains a single argument, of type **%d**. It also contains an argument range specification. Whenever Unidrv sends this command to the printer, it first calculates DestXRel/4 and determines if it is within the specified range. If the calculated value is greater than 9600, Unidrv sends the command repeatedly, with a maximum value of 9600, until the specified value has been sent. Thus if DestXRel/4 equals 20,000, Unidrv sends the following commands:

```
<1B>[9600
<1B>[9600
<1B>[800
```

The **max\_repeat** operator can be used only if the following conditions are met:

-   A command string includes only a single argument.

-   The argument includes a range specification.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Standard%20Variable%20Expressions%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




