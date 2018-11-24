---
title: Removing a Trace Provider
description: Removing a Trace Provider
ms.assetid: 3ea38137-9196-46a6-8cb5-04722cd43086
keywords:
- trace providers WDK
- providers WDK software tracing
- trace sessions WDK , providers
- removing trace providers
- disabling trace providers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Removing a Trace Provider


You cannot use the TraceView window to remove or disable a trace provider from a running trace session. However, you can remove a provider while you are creating the trace session and before TraceView has started it.

While you are creating a trace session, use the following procedure to remove a trace provider:

1.  On the **File** menu, click **Create New Log Session**.

2.  In the **Name** list, click the provider you want to remove.

3.  Click **Remove Provider**.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

You can also disable a trace provider in a session that TraceView started by typing the following command in a Command Prompt window.

```
traceview -disable SessionName -guid {#GUID | GUIDFile}
```

However, this command causes TraceView to stop the trace session. To continue, use a **traceview -start***SessionName* command to restart the trace session. For more information, see [**TraceView Control Commands**](traceview-control-commands.md).

 

 





