---
title: Time Travel Debugging - Troubleshooting
description: This section describes how to troubleshoot time travel traces.
ms.author: windowsdriverdev
ms.date: 09/18/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>


# ![Small logo on windbg preview](images/windbgx-preview-logo.png) Time Travel Debugging - Troubleshooting

This section describes how to troubleshoot time travel traces.

## Issues attempting to record a process

### I get an error message that says "WinDbg must be run elevated to support Time Travel Debugging"

As it says, running the debugger elevated is a requirement. In order to run the debugger elevated, right-click on its icon in the start menu and then select "More --> Run as Administrator".

### I can't launch and record a Windows Store application

This is not supported at this time, but you may attach to and record an already-running Windows Store application.

### I can't record a <insert esoteric process type - running in another session, security context, credentials...> process

At this time, TTD only record regular processes that you can be normally launched from a command console or by clicking on an executable or shortcut in Windows Explorer.

> [!NOTE]
> JCAB: the wording of this will require some finagling. I don't even know what could fail, really. Elevation might enable crazy scenarios. I think Jordi mentioned recording LSASS, of all things, from WinDbg.
> But we should put something here, catch-all, to address recoding failures like these.
>

### I cannot successfully record my application in this computer

If recording of your application fails, we suggest verifying whether you can record a simple Windows process. "ping.exe" or "cmd.exe" are two examples of simple processes.

If that fails...

### I cannot successfully record anything at all in my computer

TTD recording is an invasive technology, which can interfere with other invasive technologies like application virtualization frameworks, information management products, security software or antivirus products.

See "Things to look out for" in [Time Travel Debugging - Overview](time-travel-debugging-overview.md) for information on known TTD incompatibilities.

## Issues with .IDX index files

Debugging a trace file without an index file, or with a corrupted or incomplete index file, is possible, but is not recommended.
The index file is needed to ensure that memory values read from the debugged process are most accurate, and to increase the efficiency of all other debugging operations.

Use the ```!index -status``` command to examine the state of the .IDX index file associated with the .RUN trace file.

If it you may try recreating the index file by running ```!index -force```.

### Recreating the .IDX index file

If you suspect and issue with the index file, or ```!index -status``` says anything other than "Index file loaded", recreate it.
To do this you may run ```!index -force```. If that fails:

1. Close the debugger.
2. Delete the existing IDX file, it will have the same name as the .RUN trace file and be located in the same directory that the .RUN file is.
3. Open the trace .RUN file in WinDbg Preview. This will run the ```!index``` command to re-create the index.
5. Use the ```!index -status``` command to confirm that the trace index is functional.

Please, ensure that there's enough space for the index file in the same location where the trace file resides.
Depending on the contents of the recording, the index file may be significantly larger than the trace file.

## Issues with Trace .RUN Files

When there are issues with the trace .RUN file, you may receive error messages such as these.

```
Replay and log are out of sync at fallback data. Packet type is incorrect "Packet Type"
Replay and log are out of sync at opaque data. Log had already reached the end
Replay exit thread event does not match up with logged event
Logged debug write values are out of sync with replay
```
In most cases all of the failure messages indicate that the .RUN trace file is not usable and must be re-recorded.

??? TBD 
Would any (or all?) failures be related to a troublesome INDEX file? Do we want to share which messages indicate that?

Do we want to talk about disabling CPU features as mentioned on the wiki? 

32 vs. 64 bit?

??? TBD - I need some help with this topic as I think the related Wikis are not targeted towards external release and may be out of date:

https://osgwiki.com/wiki/Trace_file_derailment

https://osgwiki.com/wiki/Debugging_a_Time_Travel_Trace

??? TBD - Please add any additional information and correct anything below.

??? TBD - It would be great to use any product telemetry to look at the 3-5 top failures and offer guidance for those in the docs.


### Re-recording the user mode app

If there is a specific issue with recording a user mode app, you may want to try recording a different app on the same PC, or try the same app on a different PC. You may want to try and record a different use of the app to see if there is a specific issue with recording certain parts of the app.


> Additional Content Pending

??? TBD - What additional information can we provide to help our users troubleshoot the most common issues with TTD?


## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




