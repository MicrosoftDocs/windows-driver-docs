---
title: WdbgExts Input and Output
description: WdbgExts Input and Output
keywords: ["WdbgExts extensions, input", "WdbgExts extensions, output"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# WdbgExts Input and Output


This topic provides a brief overview of how input and output can be performed using the WdbgExts API. For an overview of the input and output streams in the [debugger engine](introduction.md#debugger-engine), see [Input and Output](input-and-output.md) in the [Debugger Engine Overview](debugger-engine-overview.md) section of this documentation.

The function [**dprintf**](/windows-hardware/drivers/ddi/wdbgexts/nc-wdbgexts-pwindbg_output_routine) works in a way similar to the standard C **printf** function and prints a formatted string to the Debugger Command window or, more precisely, the formatted string is sent to the [output callbacks](using-input-and-output.md#output-callbacks). To read a line of input from the debugger engine, use the function [**GetInputLine**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-getinputline).

To check for a user-initiated interrupt, use [**CheckControlC**](/windows-hardware/drivers/ddi/wdbgexts/nc-wdbgexts-pwindbg_check_control_c). This function should be used in loops to determine if the user has attempted to cancel execution of an extension.

For a more powerful input and output API, see [Using Input and Output](using-input-and-output.md) in the [Using the Debugger Engine API](using-the-debugger-engine-api.md) section of this documentation.

 

