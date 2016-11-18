---
title: Example 5 Enabling Trace Providers
description: Example 5 Enabling Trace Providers
ms.assetid: 405aea85-0248-4fd3-82eb-1beb76cc8a1b
keywords: ["Tracelog WDK , providers", "providers WDK software tracing", "tracing WDK , providers"]
---

# Example 5: Enabling Trace Providers


The following command enables a trace provider for a running trace session named "MyTrace":

```
tracelog -enable MyTrace -guid MyProvider.guid
```

In response, Tracelog enables the providers represented by the GUIDs in the MyProvider.guid file. The command does not change any other properties of the trace session.

You can start a trace session and then enable a provider, or you can enable the provider while starting the trace session. For example, the following commands start a trace session and then enable a provider:

```
tracelog -start MyTrace
tracelog -enable MyTrace -guid MyProvider.guid
```

In contrast, the following command starts the session and enables the providers in one command:

```
tracelog -start MyTrace -guid MyProvider.guid
```

Other than timing differences, the effect of these commands is the same.

Typically, **tracelog -enable** commands are used to change the flags and levels associated with a provider. Because flags and levels are properties of the provider, not properties of the trace session, you use a **tracelog -enable** command, not a **tracelog -update** command, to change them.

The following command changes the flags and level for the provider in the MyProvider.guid file. You must use the **-guid** parameter to specify the trace provider, even when that provider is the only provider enabled for the trace session.

```
tracelog -enable MyTrace -guid MyProvider.guid -flag 2 -level 2
```

You can also use the **tracelog -enable** command to add more providers to the trace session and to re-enable providers that you have disabled by using a **tracelog -disable** command.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Example%205:%20Enabling%20Trace%20Providers%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




