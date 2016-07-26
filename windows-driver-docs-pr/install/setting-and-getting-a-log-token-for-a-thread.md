---
title: Setting and Getting a Log Token for a Thread
description: Setting and Getting a Log Token for a Thread
ms.assetid: 6c701b91-ae0a-48ba-a1e0-711fc21eaf60
keywords: ["text logs WDK SetupAPI , log context", "log context WDK SetupAPI", "SetupGetThreadLogToken", "SetupAPI logging WDK Windows Vista , log context", "log tokens WDK SetupAPI", "thread log tokens WDK SetupAPI", "SetupSetThreadLogToken"]
---

# Setting and Getting a Log Token for a Thread


[SetupAPI logging](setupapi-logging--windows-vista-and-later-.md) supports a mechanism that establishes a log context for a thread. This context is established by setting a [log token](log-tokens.md) for the thread. SetupAPI provides this mechanism so that code that is called by a thread can write log entries to the log context of the calling thread.

For example, a thread can set a log token for its log context before it calls a class installer or co-installer. The installer, in turn, can retrieve the calling thread's log token and use that token to write log entries in the text log and section that is associated with the calling thread's log context.

### <a href="" id="setting-a-log-token-for-a-thread"></a> Setting a log token for a thread

The [**SetupSetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552216) function sets a log token for the thread from which this function was called. The log token can either be a system-defined log token or a log token that was retrieved by calling [**SetupGetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552211).

The following are examples of how a log context can be established for a thread:

-   An installation application can call **SetupSetThreadLogToken** to establish a log context for other installation code that runs within the same thread. When it is establishing the log context for the thread, the application should use a system-defined [log token](log-tokens.md), such as LOGTOKEN\_SETUPAPI\_APPLOG, in the call to **SetupSetThreadLogToken**.

    **Note**  If the log context is set by using a system-defined [log token](log-tokens.md), subsequent calls to a [SetupAPI logging function](https://msdn.microsoft.com/library/windows/hardware/ff550878) that are made from that log context, write log entries to the installation text log, which are not part of a [text log section](format-of-a-text-log-section.md).

     

-   If a class installer or co-installer starts a new thread, the installer can set the log context for that thread to be the same as the parent thread. This is done in the following way:
    1.  Before the parent thread starts the new thread, it acquires the current log token by calling [**SetupGetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552211).
    2.  The parent thread starts the new thread and passes the current log token through an implementation-specific method, such as saving the token in a global variable.
    3.  The new thread calls [**SetupSetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552216) with the current log token. As a result, the new thread "inherits" the log context of the parent thread.

    **Note**  If a thread of a class installer or co-installer sets the log context by using this method, subsequent calls to a [SetupAPI logging function](https://msdn.microsoft.com/library/windows/hardware/ff550878) that are made from that log context write log entries to the installation text log that may be part of a [text log section](format-of-a-text-log-section.md). This only happens if a text log section was established by the SetupAPI installation operation that called the installer.

     

The following is an example of a call to **SetupSetThreadLogToken** that sets the log context of the current thread to the device installation text log (*SetupAPI.app.log)* by specifying the system-defined log token of LOGTOKEN\_SETUPAPI\_APPLOG. A subsequent call to a [SetupAPI logging function](https://msdn.microsoft.com/library/windows/hardware/ff550878) that uses this log context would write the log entry to the device installation text log, but not as part of a [text log section](format-of-a-text-log-section.md).

```
SP_LOG_TOKEN LogToken = LOGTOKEN_SETUPAPI_APPLOG;
SetupSetThreadLogToken(LogToken);
```

### <a href="" id="getting-a-log-token-for-a-thread"></a> Getting a log token for a thread

The [**SetupGetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552211) function retrieves a log token for the thread from which this function was called.

For example, a class installer can call **SetupGetThreadLogToken** to retrieve the log token that applies to the SetupAPI operation that called the class installer. The class installer can then use this retrieved log token to log entries in the text log that applies to the corresponding SetupAPI operation.

**Note**  If the log context of a thread was not previously set by a call to [**SetupSetThreadLogToken**](https://msdn.microsoft.com/library/windows/hardware/ff552216), a call to **SetupGetThreadLogToken** returns a log token with a value of LOGTOKEN\_UNSPECIFIED.

 

The following is an example of a call to **SetupGetThreadLogToken** that retrieves the log token for the current thread.

```
SP_LOG_TOKEN LogToken = SetupGetThreadLogToken();
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Setting%20and%20Getting%20a%20Log%20Token%20for%20a%20Thread%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




