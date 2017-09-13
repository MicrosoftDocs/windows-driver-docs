---
title: Time Travel Debugging - Troubleshooting
description: This section describes how to troubleshoot time travel traces.
ms.author: windowsdriverdev
ms.date: 09/06/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>


# ![Small logo on windbg preview](images/windbgx-preview-logo.png) Time Travel Debugging - Troubleshooting

This section describes how to troubleshoot time travel traces.

??? TBD - I need some help with this topic as I think the related Wikis are not targeted towards external relase and may be out of date:

https://osgwiki.com/wiki/Trace_file_derailment

https://osgwiki.com/wiki/Debugging_a_Time_Travel_Trace

P??? TBD - Please add any additional information and correct anything below.

P??? TBD - It would be great to use any product telemetry to look at the 3-5 top failures and offer guidance for those in the docs.


## Issues with .IDX index files

Use the ```!tt.index status``` command to examine the state of the .IDX index file associated with the .RUN trace file.

### Recreating the .IDX index file

If you suspect and issue with the index file, recreate it. To to this:

1. Delete the existing IDX file, it will have the same name as the .RUN trace file and be located in the same directory that the .RUN file is.
2. Open the trace .RUN file in WinDbg Preview.
3. Run the ```!tt.index``` command.
4. Use the ```!tt.index status``` command to confirm that the trace index is functional.


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
Do we want to talk about disabling CPU features as mentioned on the wiki? 32 vs. 64 bit?


### Re-recording the user mode app

If there is a specific issue with recording a user mode app, you may want to try recording a different app on the same PC, or try the same app on a different PC. You may want to try and record a different use of the app to see if there is a specific issue with recording certain parts of the app.

## TTD Incompatibilities

See "Things to look out for" in [Time Travel Debugging - Overview](time-travel-debugging-overview.md) for information on TTD incompatibilities.


> Additional Content Pending

??? TBD - What additional information can we provide to help our users troubleshoot the most common issues with TTD?


## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




