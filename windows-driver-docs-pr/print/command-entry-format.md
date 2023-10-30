---
title: Command entry format
description: Command entry format
keywords:
- printer commands WDK Unidrv , entry format
- formats WDK printer commands
ms.date: 06/16/2023
---

# Command entry format

[!include[Print Support Apps](../includes/print-support-apps.md)]

To specify a printer command entry in a GPD file, use the following format:

**\*Command**: *CommandName* {*CommandAttributes*}

where *CommandName* is one of the predefined [command names](command-names.md), and *CommandAttributes* is a set of [command attributes](command-attributes.md).

For example, a GPD file might contain the following specification of the CmdStartPage command, which initializes a page for printing.

```GPD
*Command: CmdStartPage
{
    *Order: PAGE_SETUP.100
    *Cmd: "<0D>"
}
```

If, for a particular *CommandName* value, you only need to specify the \*Cmd attribute, you can use a shortened version of the command entry format, as follows:

**\*Command**: *CommandName*: *CommandString*

where *CommandString* is a text string representing a printer command escape sequence. For more information about specifying escape sequences, see [Command String Format](command-string-format.md).

For example, a GPD file might contain the following specification of the CmdBoldOn command, which turns on bold text:

```GPD
*Command: CmdBoldOn: "<1B>(s3B"
```
