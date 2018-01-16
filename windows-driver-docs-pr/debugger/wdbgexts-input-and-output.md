---
title: WdbgExts Input and Output
description: WdbgExts Input and Output
ms.assetid: 5648b509-7bdd-4d2a-947f-db55a8c69100
keywords: ["WdbgExts extensions, input", "WdbgExts extensions, output"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WdbgExts Input and Output


This topic provides a brief overview of how input and output can be performed using the WdbgExts API. For an overview of the input and output streams in the [debugger engine](introduction.md#debugger-engine), see [Input and Output](input-and-output.md) in the [Debugger Engine Overview](debugger-engine-overview.md) section of this documentation.

The function [**dprintf**](https://msdn.microsoft.com/library/windows/hardware/ff542750) works in a way similar to the standard C **printf** function and prints a formatted string to the Debugger Command window or, more precisely, the formatted string is sent to the [output callbacks](using-input-and-output.md#output-callbacks). To read a line of input from the debugger engine, use the function [**GetInputLine**](https://msdn.microsoft.com/library/windows/hardware/ff546905).

To check for a user-initiated interrupt, use [**CheckControlC**](https://msdn.microsoft.com/library/windows/hardware/ff539072). This function should be used in loops to determine if the user has attempted to cancel execution of an extension.

For a more powerful input and output API, see [Using Input and Output](using-input-and-output.md) in the [Using the Debugger Engine API](using-the-debugger-engine-api.md) section of this documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20WdbgExts%20Input%20and%20Output%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




