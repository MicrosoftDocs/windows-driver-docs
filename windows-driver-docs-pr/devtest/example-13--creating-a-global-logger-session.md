---
title: Example 13 Creating a Global Logger Session
description: Example 13 Creating a Global Logger Session
ms.assetid: 11574df3-817e-4bf3-a849-dd5ac723fb1d
keywords: ["trace sessions WDK , Global Logger", "Global Logger trace session WDK , examples"]
---

# Example 13: Creating a Global Logger Session


## <span id="ddk_controlling_a_global_logger_session_tools"></span><span id="DDK_CONTROLLING_A_GLOBAL_LOGGER_SESSION_TOOLS"></span>


A [Global Logger trace session](global-logger-trace-session.md) differs from other trace sessions in that it reads its configuration parameters from registry entries. Because Tracelog handles these differences for you, the commands that you use to start and stop Global Logger trace sessions do not differ much from those for other sessions. However, you cannot update a Global Logger session and, after stopping the session, you must use a **tracelog -remove** command to reset the registry entries created for the session.

Also, the **tracelog -start** command does not start the trace session; it just creates and configures it. The session starts when you reboot the system.

The following command is the simplest command that configures a Global Logger session. It uses the **tracelog -start** command with the reserved **GlobalLogger** name. Tracelog uses the default values for all other parameters.

```
tracelog -start GlobalLogger
```

In response, Tracelog creates a **GlobalLogger** subkey in **HKLM\\SYSTEM\\CurrentControlSet\\Control\\WMI** with a registry entry for each parameter. It creates a **Start** entry in the subkey and sets its value to \`1.

Because the command did not include the **-f** parameter, the trace log for this session is stored in the default location for Global Logger trace sessions, %SystemRoot%\\System32\\LogFiles\\WMI\\trace.log. To view the log, use [Tracefmt](tracefmt.md) or [TraceView](traceview.md) with the System.tmf[trace message format file](trace-message-format-file.md).

After the session is configured, reboot the system to start the trace session.

The following command stops the trace session, but it does not affect the registry entries.

```
tracelog -stop GlobalLogger
```

Then, to reset the registry entries, use the following command.

```
tracelog -remove GlobalLogger
```

This command deletes any registry entries for optional parameters (none, in this case). It leaves the **GlobalLogger** subkey and the **Start** entry, but it sets the value of **Start** to 0 (do not start).

The **tracelog -remove** command is not required. You can leave the entries in the registry and use them the next time you run a Global Logger trace session. If you start the session with different parameters, Tracelog replaces the values of the registry entries with the values specified in the **tracelog -start** command.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Example%2013:%20Creating%20a%20Global%20Logger%20Session%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




