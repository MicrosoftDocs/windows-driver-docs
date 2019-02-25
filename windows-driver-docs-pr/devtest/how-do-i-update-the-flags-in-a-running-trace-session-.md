---
title: How do I update the flags in a running trace session
description: How do I update the flags in a running trace session
ms.assetid: 952cc60f-1877-49d5-b87c-493c1b90cfdf
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How do I update the flags in a running trace session?


To change the [trace flags](trace-flags.md) or [trace level](trace-level.md) in a running trace session, use the **tracelog -enable** command, not the **tracelog -update** command. For more information, see [**Tracelog Command Syntax**](tracelog-command-syntax.md).

Flags and levels are properties of a [trace provider](trace-provider.md), not of the [trace session](trace-session.md). Therefore, **tracelog -update**, the command to update the trace session, cannot be used to change the properties of a provider. Instead, use the **tracelog -enable** command to re-enable the provider with the new properties.

For information about the **tracelog -enable** command, see [**Tracelog Command Syntax**](tracelog-command-syntax.md). For an example of how to use this command, see [Example 5: Enabling Trace providers](example-5--enabling-trace-providers.md).

You can also use [TraceView](traceview.md) to change the flags or levels in a trace session that you started by using TraceView. The graphical user interface makes it easy to see what properties can be changed while the session runs, and to change them.

 

 





