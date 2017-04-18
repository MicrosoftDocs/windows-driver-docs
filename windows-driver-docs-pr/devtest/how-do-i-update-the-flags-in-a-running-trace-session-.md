---
title: How do I update the flags in a running trace session
description: How do I update the flags in a running trace session
ms.assetid: 952cc60f-1877-49d5-b87c-493c1b90cfdf
---

# How do I update the flags in a running trace session?


To change the [trace flags](trace-flags.md) or [trace level](trace-level.md) in a running trace session, use the **tracelog -enable** command, not the **tracelog -update** command. For more information, see [**Tracelog Command Syntax**](tracelog-command-syntax.md).

Flags and levels are properties of a [trace provider](trace-provider.md), not of the [trace session](trace-session.md). Therefore, **tracelog -update**, the command to update the trace session, cannot be used to change the properties of a provider. Instead, use the **tracelog -enable** command to re-enable the provider with the new properties.

For information about the **tracelog -enable** command, see [**Tracelog Command Syntax**](tracelog-command-syntax.md). For an example of how to use this command, see [Example 5: Enabling Trace providers](example-5--enabling-trace-providers.md).

You can also use [TraceView](traceview.md) to change the flags or levels in a trace session that you started by using TraceView. The graphical user interface makes it easy to see what properties can be changed while the session runs, and to change them.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20How%20do%20I%20update%20the%20flags%20in%20a%20running%20trace%20session?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




