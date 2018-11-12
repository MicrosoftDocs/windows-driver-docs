---
title: Setting and Getting a Log Token for a Thread
description: Setting and Getting a Log Token for a Thread
ms.assetid: 6c701b91-ae0a-48ba-a1e0-711fc21eaf60
keywords:
- text logs WDK SetupAPI , log context
- log context WDK SetupAPI
- SetupGetThreadLogToken
- SetupAPI logging WDK Windows Vista , log context
- log tokens WDK SetupAPI
- thread log tokens WDK SetupAPI
- SetupSetThreadLogToken
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting and Getting a Log Token for a Thread


[SetupAPI logging](setupapi-logging--windows-vista-and-later-.md) supports a mechanism that establishes a log context for a thread. This context is established by setting a [log token](log-tokens.md) for the thread. SetupAPI provides this mechanism so that code that is called by a thread can write log entries to the log context of the calling thread.

For example, a thread can set a log token for its log context before it calls a class installer or co-installer. The installer, in turn, can retrieve the calling thread's log token and use that token to write log entries in the text log and section that is associated with the calling thread's log context.

### <a href="" id="setting-a-log-token-for-a-thread"></a> Setting a log token for a thread

The [**SetupSetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552216) function sets a log token for the thread from which this function was called. The log token can either be a system-defined log token or a log token that was retrieved by calling [**SetupGetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552211).

The following are examples of how a log context can be established for a thread:

-   An installation application can call **SetupSetThreadLogToken** to establish a log context for other installation code that runs within the same thread. When it is establishing the log context for the thread, the application should use a system-defined [log token](log-tokens.md), such as LOGTOKEN_SETUPAPI_APPLOG, in the call to **SetupSetThreadLogToken**.

    **Note**  If the log context is set by using a system-defined [log token](log-tokens.md), subsequent calls to a [SetupAPI logging function](https://msdn.microsoft.com/library/windows/hardware/ff550878) that are made from that log context, write log entries to the installation text log, which are not part of a [text log section](format-of-a-text-log-section.md).

     

-   If a class installer or co-installer starts a new thread, the installer can set the log context for that thread to be the same as the parent thread. This is done in the following way:
    1.  Before the parent thread starts the new thread, it acquires the current log token by calling [**SetupGetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552211).
    2.  The parent thread starts the new thread and passes the current log token through an implementation-specific method, such as saving the token in a global variable.
    3.  The new thread calls [**SetupSetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552216) with the current log token. As a result, the new thread "inherits" the log context of the parent thread.

    **Note**  If a thread of a class installer or co-installer sets the log context by using this method, subsequent calls to a [SetupAPI logging function](https://msdn.microsoft.com/library/windows/hardware/ff550878) that are made from that log context write log entries to the installation text log that may be part of a [text log section](format-of-a-text-log-section.md). This only happens if a text log section was established by the SetupAPI installation operation that called the installer.

     

The following is an example of a call to **SetupSetThreadLogToken** that sets the log context of the current thread to the device installation text log (*SetupAPI.app.log)* by specifying the system-defined log token of LOGTOKEN_SETUPAPI_APPLOG. A subsequent call to a [SetupAPI logging function](https://msdn.microsoft.com/library/windows/hardware/ff550878) that uses this log context would write the log entry to the device installation text log, but not as part of a [text log section](format-of-a-text-log-section.md).

```cpp
SP_LOG_TOKEN LogToken = LOGTOKEN_SETUPAPI_APPLOG;
SetupSetThreadLogToken(LogToken);
```

### <a href="" id="getting-a-log-token-for-a-thread"></a> Getting a log token for a thread

The [**SetupGetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552211) function retrieves a log token for the thread from which this function was called.

For example, a class installer can call **SetupGetThreadLogToken** to retrieve the log token that applies to the SetupAPI operation that called the class installer. The class installer can then use this retrieved log token to log entries in the text log that applies to the corresponding SetupAPI operation.

**Note**  If the log context of a thread was not previously set by a call to [**SetupSetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552216), a call to **SetupGetThreadLogToken** returns a log token with a value of LOGTOKEN_UNSPECIFIED.

 

The following is an example of a call to **SetupGetThreadLogToken** that retrieves the log token for the current thread.

```cpp
SP_LOG_TOKEN LogToken = SetupGetThreadLogToken();
```

 

 





