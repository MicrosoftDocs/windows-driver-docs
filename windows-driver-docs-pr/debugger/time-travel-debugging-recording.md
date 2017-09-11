---
title: Time Travel Debugging - Recording 
description: This section describes how to record time travel traces.
ms.author: windowsdriverdev
ms.date: 09/11/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>

# ![Small logo on windbg preview](images/windbgx-preview-logo.png) Time Travel Debugging - Recording 

This section describes how to record time travel traces.

To record a TTD trace, follow these steps.

1. In WinDbg Preview, select **File** > **Launch executable (advanced)**.

2. Fill in the path to the user mode executable that you wish to trace. For information about working with the Launch Executable menu in WinDbg Preview, see [WinDbg Preview - Start a user-mode session](windbg-user-mode-preview.md).

![Screen shot of WinDbg Preview showing start recording checkbox](images/ttd-start-recording.png)

> [!NOTE]
> The UI shown here is preliminary and will likely change. Updated information will be provided in a later release of the documentation. 
>

3. Check the **Record Process** box to create a trace when the executable is launched. 

4. Click **OK** to launch the executable and start tracing. 

5. The recording dialog appears indicating the trace is being recorded.

![TTD recording popup showing stop and debug as well as cancel options](images/ttd-recording-pop-up.png)

6. When the recording dialog box is being displayed you can:

- Stop tracing and debug your program. 
- Cancel the tracing. This option does not TBD.

    Here is where you work to cause the activity that you wish to analyze to occur. You may open a problematic file or click on a specific button in the app to cause the event of interest to occur. 

    TBD - Need to test focus of UI and console apps to better clarify the intended experience.

    Using breakpoints is a common approach to pause code execution at the event of interest.

    TBD - Need to add example / walkthrough topic showing breakpoint usage.

7. Once complete, close your app or hit “Stop and debug” – This will kill your process.

8. When the application terminates, the trace file will be closed and written out to disk. This is the case if your program crashes as well.

```
Time Travel Position: 6D1:0
ntdll!ZwTerminateProcess+0x12:
00007ffc`61f75922 0f05            syscall
||0:0:000> !index
Successfully created the index in 0ms.
```

9. When the trace file is closed, indexing will happen automatically as shown in the output below. Indexing allows for complete and faster memory value look ups. This indexing process will take longer for larger trace files.

```
Time Travel Position: 10:0
ntdll!ZwTestAlert+0x14:
00007ffc`61f789d4 c3              ret
0:000> !index
Indexed 1/1 keyframes
Successfully created the index in 96ms.
```

10. At this point you are at the end/beginning (TBD) of the trace file.

11. Now that you have a recorded a TTD trace, you can play the trace back or work with the trace file, for example sharing it with a co-worker. For more information see:

- [Time Travel Debugging - Playback](time-travel-debugging-playback.md)
- [Time Travel Debugging - Working with trace files](time-travel-debugging-trace-files.md)
- [Time Travel Debugging - Troubleshooting](time-travel-debugging-troubleshooting.md)

---

## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




