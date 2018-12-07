---
title: Example 5 Enabling Trace Providers
description: Example 5 Enabling Trace Providers
ms.assetid: 405aea85-0248-4fd3-82eb-1beb76cc8a1b
keywords:
- Tracelog WDK , providers
- providers WDK software tracing
- tracing WDK , providers
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





