---
title: "!storagekd.storloglist"
description: "The !storagekd.storloglist extension displays the Storport adapter’s internal log entries."
keywords: ["!storagekd.storloglist Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- storagekd.storloglist
api_type:
- NA
---

# !storagekd.storloglist

The **!storagekd.storloglist** extension displays the Storport adapter’s internal log entries.

```dbgcmd
!storagekd.storloglist <Address> [<starting_entry> [<ending_entry>]] [L <count>] 
```

## Parameters

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of a Storport adapter device extension or device object.

<span id="_______starting_entry______"></span><span id="_______STARTING_ENTRY______"></span> *starting\_entry*   
The beginning entry in the range to display. If not specified, the last *count* entries will be displayed.

<span id="_______ending_entry______"></span><span id="_______ENDING_ENTRY______"></span> *ending\_entry*   
The ending entry in the range to display. If not specified, *count* entries will be displayed, beginning with the item specified by *starting\_entry*.

<span id="_______count______"></span><span id="_______COUNT______"></span> *count*   
Count of entries to be displayed. If not specified, a value of 50 is used.

## DLL

Storagekd.dll

## Remarks

Here is an example of **!storagekd.storloglist** display:

**0: kd&gt; !storagekd.storloglist ffffe0010f5e01a0**

```dbgcmd
Storport RaidLogList
    Circular buffer location:  0xffffe0010f5e1720
    Total logs written: 8
    Displaying entries 0 through 7
    ---------------------------------------------------------------------
    [0]_[23:04:20.521] ResumeDevice.......... Caller: storport!RaidUnitPauseTimerDpcRoutine+0x28 (fffff800`fb4d0b28), P/P/T/L: 0/0/0/0, Pause count: 0, Resumed: True
    [1]_[23:04:20.646] ResumeDevice.......... Caller: storport!RaidUnitPauseTimerDpcRoutine+0x28 (fffff800`fb4d0b28), P/P/T/L: 0/0/0/0, Pause count: 0, Resumed: True
    [2]_[23:04:20.646] SpPauseDevice......... Caller: iaStorAV!RpiPauseDevice+0x67 (fffff800`fb70554f), P/T/L: 3/0/0, Timeout: 180, Adapter: 0xffffe0010f5e01a0
    [3]_[23:04:20.646] PauseDevice........... Caller: storport!StorPortPauseDevice+0x2f6 (fffff800`fb4b52d6), P/P/T/L: 0/3/0/0, Pause count: 1
    [4]_[23:04:20.646] SpResumeDevice........ Caller: iaStorAV!RpiResumeDevice+0x5f (fffff800`fb7055fb), P/T/L: 3/0/0, Adapter: 0xffffe0010f5e01a0
    [5]_[23:04:20.646] ResumeDevice.......... Caller: storport!StorPortResumeDevice+0x19 (fffff800`fb4aa23f), P/P/T/L: 0/3/0/0, Pause count: 0, Resumed: True
    [6]_[23:04:20.646] SpPauseDevice......... Caller: iaStorAV!RpiPauseDevice+0x67 (fffff800`fb70554f), P/T/L: 3/0/0, Timeout: 180, Adapter: 0xffffe0010f5e01a0
    [7]_[23:04:20.646] PauseDevice........... Caller: storport!StorPortPauseDevice+0x2f6 (fffff800`fb4b52d6), P/P/T/L: 0/3/0/0, Pause count: 1
```
