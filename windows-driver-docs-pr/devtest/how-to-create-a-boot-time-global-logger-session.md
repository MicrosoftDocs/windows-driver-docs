---
title: How to Create a Boot-Time Global Logger Session
description: How to Create a Boot-Time Global Logger Session
ms.assetid: ddd9e1b1-d732-4ef1-a0e0-4d8e95660d7c
keywords:
- Global Logger trace session WDK , creating
- boot-time Global Logger trace session WDK , creating
- EnableKernelFlags WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to Create a Boot-Time Global Logger Session


The easiest way to create a Global Logger trace session that logs kernel events is to use [Tracelog](tracelog.md) to create a standard Global Logger trace session, and then add the **EnableKernelFlags** entry and its values. This topic describes the procedure.

1.  Use Tracelog to create a Global Logger trace session. The simplest command is as follows:

    ```
    tracelog -start GlobalLogger
    ```

    For instructions and more information, see [**Tracelog Command Syntax**](tracelog-command-syntax.md) and [Global Logger Trace Session](global-logger-trace-session.md). For an example, see [Example 13: Creating a Global Logger Session](example-13--creating-a-global-logger-session.md).

2.  Add a REG\_BINARY entry named **EnableKernelFlags** to the **HKLM\\System\\CurrentControlSet\\Control\\WMI\\GlobalLogger** subkey. Tracelog creates the **GlobalLogger** registry subkey when you use the **tracelog -start** command. The values that you can use for **EnableKernelFlags** are taken from the values of the **EnableFlags** member of the **EVENT\_TRACE\_PROPERTIES** structure. For a description of the **EnableFlags** values, see [**EVENT\_TRACE\_PROPERTIES**](https://msdn.microsoft.com/library/windows/desktop/aa363784).

3.  Restart the system.

4.  When your testing is complete, use the **tracelog -remove** GlobalLogger command to reinitialize the entries in the **GlobalLogger** subkey. Otherwise, the Global Logger trace session starts each time you start the system.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The presence of the **EnableKernelFlags** entry, with a valid value, converts the Global Logger trace session to an NT Kernel Logger trace session. The value of **EnableKernelFlags**, along with the other Global Logger registry entries, is used to configure the session. The trace session starts when you restart the system.

Registry entries are used to configure the Global Logger trace session, because the configuration values must be available before the system is fully operational.

You can configure a Global Logger trace session by editing the registry or by using [Tracelog](tracelog.md), a tool included in the Windows Driver Kit (WDK). For more information about the registry entries that configure the Global Logger trace session, see [Global Logger trace session](global-logger-trace-session.md).

After running this trace session, use the **tracelog -remove** command to set the value of the **Start** entry to 0 to delete the registry subkeys that you added. If you do not, the session will run each time you start the system and the log might grow very large.

For more information about the Tracelog commands, see [**Tracelog Command Syntax**](tracelog-command-syntax.md)

## <span id="related_topics"></span>Related topics


[**EVENT\_TRACE\_PROPERTIES**](https://msdn.microsoft.com/library/windows/desktop/aa363784)

[Example 13: Creating a Global Logger Session](example-13--creating-a-global-logger-session.md)

[Global Logger trace session](global-logger-trace-session.md)

[Tracelog](tracelog.md)

[**Tracelog Command Syntax**](tracelog-command-syntax.md)

 

 






