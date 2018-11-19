---
title: Command String Format
description: Command String Format
ms.assetid: 3b33b261-08c7-4441-94f5-6c9de53ae349
keywords:
- printer commands WDK Unidrv , strings
- command strings WDK Unidrv
- strings WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Command String Format





Command strings are used to specify the escape sequences that Unidrv must send to printer hardware. Command strings can be made up of the following elements:

-   Quoted text strings, which have the following format:

    "*TextString*"

-   Command arguments, which have the following format:

    %*ArgumentType*{*StandardVariableExpression*}

Unidrv supports a maximum of 14 quoted text strings and command arguments in a command string.

As an example, a printer's command to set a rectangle's gray fill percentage might be specified as follows:

```cpp
*Command: CmdRectGrayFill: "<1B>*c" %d{GrayPercentage} "g2P"
```

To send a percent sign (**%**) to a printer, include two percent sign characters (**%%**) in the command string. If the percent sign is at the end of the command string, you must use the hexadecimal equivalent, as in:

**"**<em>string</em> **&lt;25 25&gt;"**.

 

 




