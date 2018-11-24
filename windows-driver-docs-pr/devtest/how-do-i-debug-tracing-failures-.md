---
title: How do I debug tracing failures
description: How do I debug tracing failures
ms.assetid: 9f974482-e19d-4bcc-a884-4425741aa465
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How do I debug tracing failures?


To debug problems with your trace-instrumented driver, such as trace messages that are not showing up in trace log files, even when the provider is enabled, add a **WppDebug** macro definition to your source code.

**WppDebug** enables code designed to debug WPP. It traces actions such as registration and enable/disable activity.

Any **WppDebug** definition directive will work. For example:

```
#define WppDebug(a,b) printf b, printf("\n");
```

To call the routine, use the following format:

```
WppDebug(level,(format,...));
```

Do not confuse the **WppDebug** macro, which traces WPP actions, with the **WPP\_DEBUG** macro, which sends trace messages to a debugger.

 

 





