---
title: How to Log to the Global Logger Session
description: How to Log to the Global Logger Session
ms.assetid: b5efea00-39cd-4df3-aac4-ade9126f69ed
keywords:
- Global Logger trace session WDK , logging
- boot-time Global Logger trace session WDK , logging
- logs WDK tracing during boot
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to Log to the Global Logger Session


Use the following procedure to configure a driver to log to the Global Logger trace session:

1. Add the following definition to the driver code. Insert the definition between the [WPP\_CONTROL\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186) macro definition and the include statement for the [trace message header file](trace-message-header-file.md).
   ```
   #define WPP_GLOBALLOGGER
   ```

2. Use [Tracelog](tracelog.md) to configure a Global Logger trace session. The simplest command is as follows:

   ```
   tracelog -start GlobalLogger
   ```

   For complete instructions, including parameters for configuring the Global Logger trace session, see [**Tracelog Command Syntax**](tracelog-command-syntax.md) and [Global Logger Trace Session](global-logger-trace-session.md).

   For an example, see [Example 13: Creating a Global Logger Session](example-13--creating-a-global-logger-session.md).

   This command creates and configures the trace session, but the session does not start until you restart the system (step 5).

3. Under the **HKLM\\System\\CurrentControlSet\\Control\\WMI\\GlobalLogger** subkey, add a subkey named for the [control GUID](control-guid.md) of the trace provider. In Windows Vista and later versions of Windows, the control GUID must be enclosed in braces ( {} ).

   The **tracelog -start GlobalLogger** command adds the **GlobalLogger** subkey to the registry. The **ControlGUID** subkey establishes the driver as a [trace provider](trace-provider.md) for the Global Logger trace session.

   For example, to configure the Tracedrv sample driver to log to the Global Logger trace session on a computer running Windows XP, add a subkey named for the Tracedrv control GUID, d58c126f-b309-11d1-969e-0000f875a5bc: **HKLM\\SYSTEM\\CurrentControlSet\\Control\\WMI\\GlobalLogger\\d58c126f-b309-11d1-969e-0000f875a5bc**.

   [TraceDrv](http://go.microsoft.com/fwlink/p/?LinkId=617726), a sample driver that was designed for software tracing, is available in the [Windows driver samples](http://go.microsoft.com/fwlink/p/?LinkId=616507 ) repository on GitHub.

4. To configure the trace provider, add the following registry entries to the **ControlGUID** subkey. These entries are optional and their values are defined by the driver.

   <table>
   <colgroup>
   <col width="33%" />
   <col width="33%" />
   <col width="33%" />
   </colgroup>
   <thead>
   <tr class="header">
   <th align="left">Entry name</th>
   <th align="left">Data type</th>
   <th align="left">Description</th>
   </tr>
   </thead>
   <tbody>
   <tr class="odd">
   <td align="left"><p><strong>Flags</strong></p></td>
   <td align="left"><p>REG_DWORD</p></td>
   <td align="left"><p>Specifies the <a href="trace-flags.md" data-raw-source="[trace flags](trace-flags.md)">trace flags</a> for the provider.</p>
   <p>The meaning of the flags is defined independently by each trace provider. Typically, flags represent increasingly detailed reporting levels.</p></td>
   </tr>
   <tr class="even">
   <td align="left"><p><strong>Level</strong></p></td>
   <td align="left"><p>REG_DWORD</p></td>
   <td align="left"><p>Specifies the <a href="trace-level.md" data-raw-source="[trace level](trace-level.md)">trace level</a> for the provider.</p>
   <p>The meaning of the <strong>Level</strong> value is defined independently by each trace provider. Typically, the trace level represents the severity of the event (information, warning, or error).</p></td>
   </tr>
   </tbody>
   </table>




Note that the name of the **Flags** entry is plural and the name of the **Level** entry is singular.


5.  Restart the system. This starts the Global Logger trace session.

After your testing is complete, delete the **ControlGUID** subkey or set the value of the **Start** entry in the **GlobalLogger** subkey to 0. If you do not, the Global Logger session runs, and the driver logs to it, every time you restart the system.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

When WPP\_GLOBALLOGGER is present, WPP adds code that reads the registry and determines whether the Global Logger session is running and whether the driver is enabled for tracing to the Global Logger session. This code takes the place of the enable notification that the driver would receive from a standard trace session.

Also, because the Global Logger session does not provide callback notification, Windows assumes that a callback has occurred, and proceeds accordingly.

The WPP definitions generate only a small amount of code, so there is no need to remove them from the code after testing.









