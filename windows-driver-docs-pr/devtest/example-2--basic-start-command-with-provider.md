---
title: Example 2 Basic Start Command with Provider
description: Example 2 Basic Start Command with Provider
ms.assetid: 86730943-107e-441a-a860-4df540bc0426
keywords:
- trace sessions WDK , starting
- start command
- -start command
- guid parameter
- -guid parameter
- starting trace sessions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example 2: Basic Start Command with Provider


The following start command is identical to the command in Example 1, except that it uses the **-guid** parameter to enable a provider for the trace session:

```
tracelog -start MyTrace -guid #d58c126f-b309-11d1-969e-0000f875a5bc
```

The command starts a trace session named "My Trace". It uses the **-guid** parameter to specify the control GUID of the trace provider. The GUID is preceded by a number sign (**\#**) to indicate that it is a GUID and not a GUID file name.

In response, Tracelog starts the MyTrace trace log session and enables the provider specified by the GUID. It uses the default values for other properties of the session, including creating a log file in C:\\LogFile.etl.

If you do not specify the name of the trace session (in this case, "MyTrace"), Tracelog starts an NT Kernel Logger trace session, which is the default.

If you do not specify flags or levels, some providers might not generate trace messages, even when they are enabled.

 

 





