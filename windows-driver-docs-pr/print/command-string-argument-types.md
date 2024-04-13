---
title: Command String Argument Types
description: Command String Argument Types
keywords:
- printer commands WDK Unidrv , strings
- command strings WDK Unidrv
- strings WDK Unidrv
ms.date: 01/26/2023
---

# Command String Argument Types

[!include[Print Support Apps](../includes/print-support-apps.md)]

When you include arguments in command strings, you must specify each argument's type. Each argument type specification is a single letter, preceded by a percent sign.

The following table lists all the argument type specifiers:

| Argument type specifier | Description of resulting value |
|---|---|
| %\<*Digits*\>d | ASCII string representing a decimal value, including a minus sign if negative. *\<Digits\>* is an optional number indicating the string length. |
| %\<*Digits*\>D | ASCII string representing decimal value, including a plus or minus sign. *\<Digits\>* is an optional number indicating the string length. |
| %c | Binary byte. |
| %C | Binary byte added to ASCII "0". |
| %f | Unsigned ASCII string representing a decimal value, with a decimal point inserted as the third character from the right, as in "12.25". |
| %g | 2 \* ABS(*Parameter*) + IS_NEGATIVE(*Parameter*) as a base-64 number, least significant digit to most significant digit. The most significant digit (0-63) is represented by bytes 191 through 254. All other digits are represented by bytes 63 through 126. "IS_NEGATIVE(*Parameter*)" is 1 if *Parameter* is negative, and zero otherwise. |
| %l | Binary word, least significant byte first. |
| %m | Binary word, most significant byte first. |
| %n | Canon integer encoding. Binary value encoded from most significant byte to least significant byte. The 4 least significant bits are encoded as 001*sbbbb*, where *s* represents the sign (0 is negative, 1 is positive), and *b* represents a significant bit of the integer. The next most significant 6 bits are encoded as 01*bbbbbb*. For example, 254 (11111110) is represented as (01001111 00111110). |
| %q | ASCII string representing a QUME hexadecimal number. For Toshiba/Qume devices. |
| %v | NEC VFU (Vertical Format Unit) encoding. The specified variable's value is divided by 1/6 inch. The result is the number of times VFU data is sent to the printer. |

You can specify a range of acceptable values for any argument. To do so, include the argument's minimum and maximum values by placing them inside a set of square brackets ( \[, \] ), immediately following the argument type specifier, and separating the values by a comma. For example, the following command specifies 0 through 255 as an acceptable range for the value of LinefeedSpacing/2:

```cpp
*Command:CmdSetLineSpacing{*Cmd:"<1B>3"%c[0,255]{(LinefeedSpacing/2)}}
```
