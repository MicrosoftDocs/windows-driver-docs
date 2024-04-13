---
title: Command String Format
description: Command String Format
keywords:
- printer commands WDK Unidrv , strings
- command strings WDK Unidrv
- strings WDK Unidrv
ms.date: 01/26/2023
---

# Command String Format

[!include[Print Support Apps](../includes/print-support-apps.md)]

Command strings are used to specify the escape sequences that Unidrv must send to printer hardware. Command strings can be made up of the following elements:

- Quoted text strings, which have the following format:

    "*TextString*"

- Command arguments, which have the following format:

    %*ArgumentType*{*StandardVariableExpression*}

Unidrv supports a maximum of 14 quoted text strings and command arguments in a command string.

As an example, a printer's command to set a rectangle's gray fill percentage might be specified as follows:

```cpp
*Command: CmdRectGrayFill: "<1B>*c" %d{GrayPercentage} "g2P"
```

To send a percent sign (**%**) to a printer, include two percent sign characters (**%%**) in the command string. If the percent sign is at the end of the command string, you must use the hexadecimal equivalent, as in:

**"**_string_ **&lt;25 25&gt;"**.
