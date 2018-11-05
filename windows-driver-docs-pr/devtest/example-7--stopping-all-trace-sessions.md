---
title: Example 7 Stopping All Trace Sessions
description: Example 7 Stopping All Trace Sessions
ms.assetid: a832bf9a-ab7e-4ec0-823b-52bc6016e791
keywords:
- trace sessions WDK , stopping
- stopping trace sessions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example 7: Stopping All Trace Sessions


## <span id="ddk_stopping_all_trace_sessions_tools"></span><span id="DDK_STOPPING_ALL_TRACE_SESSIONS_TOOLS"></span>


The following command stops all trace sessions on the computer:

```
tracelog -x
```

In response, Tracelog lists each trace session running on the computer and asks if you want to stop the session. For example:

```
Do you want to stop the "My Trace" session (Y or N)?
```

To stop the session, type **Y**. Tracelog then lists the properties of the session along with the following message:

```
The "MyTrace" session has been stopped
```

 

 





