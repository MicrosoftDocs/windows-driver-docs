---
title: Time Travel Debugging - Troubleshooting
description: This section describes how to troubleshoot time travel traces.
ms.date: 10/18/2017
ms.localizationpriority: medium
---

# Time Travel Debugging - Troubleshooting

![Small time travel logo showing clock.](images/ttd-time-travel-debugging-logo.png) 

This section describes how to troubleshoot time travel traces.

## Issues attempting to record a process

### I get an error message that says "WinDbg must be run elevated to support Time Travel Debugging"

As the message indicates, running the debugger elevated is a requirement. In order to run the debugger elevated, right-click on the **WinDbg Preview** icon in the start menu and then select **More** > **Run as Administrator**.

### I installed WinDbg Preview with an account that does not have administrator privileges and I get an error message that says "WinDbg must be run elevated to support Time Travel Debugging"

Re-install WinDbg Preview using an account that has administrator privileges and use that account when recording in the debugger.

### I can't launch and record a UWP application

This is not supported at this time, but you may attach to and record an already-running UWP application.

### I can't record a <insert name of unusual process type - running in another session, security context, credentials...> process

At this time, TTD only record regular processes that you can be normally launched from a command console or by clicking on an executable or shortcut in Windows Explorer.

### I cannot successfully record my application on my computer

If recording of your application fails, verify that you can record a simple Windows process.  For example, "ping.exe" or "cmd.exe" are simple processes that can normally be recorded.

### I cannot successfully record anything at all on my computer

TTD recording is an invasive technology, which can interfere with other invasive technologies like application virtualization frameworks, information management products, security software or antivirus products.

See "Things to look out for" in [Time Travel Debugging - Overview](time-travel-debugging-overview.md) for information on known TTD incompatibilities.

### I’m tracing an application and running AppVerifier at the same time, and the performance when replaying the trace is slow.

Because of the way AppVerifier uses memory to check the application, the experience later when replaying the trace can be noticeably worse than without AppVerifier. To improve performance, disable AppVerifier when recording the app. If this is not possible, you may need to close the callstack window in WinDbg in order to improve performance.


## Issues with .IDX index files

Debugging a trace file without an index file, or with a corrupted or incomplete index file, is possible, but is not recommended.
The index file is needed to ensure that memory values read from the debugged process are most accurate, and to increase the efficiency of all other debugging operations.

Use the `!index -status` command to examine the state of the .IDX index file associated with the .RUN trace file.

If it you may try recreating the index file by running `!index -force`.

### Recreating the .IDX index file

If you suspect and issue with the index file, or `!index -status` says anything other than "Index file loaded", recreate it.
To do this you may run `!index -force`. If that fails:

1. Close the debugger.
2. Delete the existing IDX file, it will have the same name as the .RUN trace file and be located in the same directory that the .RUN file is.
3. Open the trace .RUN file in WinDbg Preview. This will run the `!index` command to re-create the index.
4. Use the `!index -status` command to confirm that the trace index is functional.

Ensure that there's enough space for the index file in the same location where the trace file resides.
Depending on the contents of the recording, the index file may be significantly larger than the trace file, typically on the order of twice as large.

## Issues with Trace .RUN Files

When there are issues with the trace .RUN file, you may receive error messages such as these.

```dbgcmd
Replay and log are out of sync at fallback data. Packet type is incorrect "Packet Type"
Replay and log are out of sync at opaque data. Log had already reached the end
Replay exit thread event does not match up with logged event
Logged debug write values are out of sync with replay
```

In most cases all of the failure messages indicate that the .RUN trace file is not usable and must be re-recorded.


### Re-recording the user mode app

If there is a specific issue with recording a user mode app, you may want to try recording a different app on the same PC, or try the same app on a different PC. You may want to try and record a different use of the app to see if there is a specific issue with recording certain parts of the app.


### When debugging or creating the index, I see messages about “Derailment events”.

It is possible that you may see messages like this one:

```dbgcmd
Derailment event MissingDataDerailment(7) on UTID 2, position 2A550B:108 with PC 0x7FFE5EEB4448 Request address: 0x600020, size: 32
```

TTD works by running an emulator inside of the debugger, which executes the instructions of the debugged process in order to replicate the state of that process at every position in the recording. Derailments happen when this emulator observes some sort of discrepancy between the resulting state and information found in the trace file. The error quoted above, for instance, refers to an instruction found on location 0x7FFE5EEB4448, at position 2A550B:108 in the trace, which attempted to read some memory around location 0x600020, which doesn’t exist in the recording.

Derailments are often caused by some error in the recorder, or sometimes in the emulator, at some recorded instruction further back in the trace. 

In most cases this failure message indicates that the .RUN trace file will have a gap in the thread that derailed, starting at the point that it derailed, for some indeterminate number of instructions. If the event of interest you are trying to debug didn’t happen during that gap, the trace may be usable. If the event of interest occurred during that gap, the trace will need to be re-recorded.


## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---






