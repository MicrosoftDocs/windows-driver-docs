---
title: Standard Variable Expressions
description: Standard Variable Expressions
keywords:
- printer commands WDK Unidrv , strings
- command strings WDK Unidrv
- strings WDK Unidrv
- standard variable expressions WDK Unidrv
- max_repeat
ms.date: 01/31/2024
---

# Standard variable expressions

[!include[Print Support Apps](../includes/print-support-apps.md)]

When you specify arguments in a command string, you can specify the argument value as an expression. This expression can perform operations using the current values of the [standard variables](standard-variables.md). Each standard variable expression within a command string is delimited by braces ( {, } ).

A standard variable expression can consist of a combination of the following components:

- Zero, one, or more [standard variables](standard-variables.md)

- Integer [numeric values](numeric-values.md)

- Expression operators

A standard variable expression can't contain embedded macro references.

The expression operators are included in the following table.

| Operator | Definitions |
|--|--|
| *Val1*<b>+</b>*Val2* | Addition |
| *Val1*<b>-</b>*Val2* | Subtraction |
| *Val1*<b>/</b>*Val2* | Division |
| *Val1*<b>*</b>*Val2* | Multiplication |
| *Val1***MOD***Val2* | Modulus. Value is the remainder of dividing Val1 by Val2. |
| **max** ( *Val1* , *Val2* ) | Maximum. Value is the maximum of Val1 and Val2. |
| **max_repeat** ( *Val1* ) | See the **Using max_repeat** section. |
| **min** ( *Val1* , *Val2* ) | Minimum. Value is the minimum of *Val1* and *Val2*. |
| **( )** | Precedence operators. If not used, C language precedence is used. |

Standard variable expressions don't modify the values assigned to the standard variables. The calculated value is placed in the escape sequence, using the format specified by the [command string argument type](command-string-argument-types.md) specifier.

## Using max_repeat

The use of **max_repeat** is best explained with an example. Suppose a GPD file contains the following entry:

```GPD
*Command:CmdXMoveRelRight{*Cmd:"<1B>["%d[0,9600]{max_repeat((DestXRel/4))}"a"}
```

This command contains a single argument, of type **%d**. It also contains an argument range specification. Whenever Unidrv sends this command to the printer, it first calculates DestXRel/4 and determines if it is within the specified range. If the calculated value is greater than 9600, Unidrv sends the command repeatedly, with a maximum value of 9600, until the specified value is sent. Thus if DestXRel/4 equals 20,000, Unidrv sends the following commands:

```GPD
<1B>[9600
<1B>[9600
<1B>[800
```

The **max_repeat** operator can be used only if the following conditions are met:

- A command string includes only a single argument.

- The argument includes a range specification.
