---
title: What are PRE / POST macros
description: What are PRE / POST macros
ms.assetid: f5acb047-def3-443a-b220-77543f9a71e3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# What are PRE / POST macros?


PRE-logging and POST-logging macros define WPP\_LEVEL\_PRE(*level*) and WPP\_LEVEL\_POST(*level*) macros. The latter are user code that becomes part of the tracing function's expansion. PRE- and POST-logging macros can be used for any in-process setup or for cleanup around trace points.

By default they are set to do nothing. However, you can define them to add some pre-logging and post-logging logic.

```
PRE macro // If defined
If (WPP_CHECK_INIT && (Level,Flag) is enabled) {
....Call TraceMessage;
}
POST macro // If defined
```

For an example about how to define the PRE/POST macros, see [How are Trace-If expressions used?](how-are-trace-if-expressions-used-.md).

 

 





