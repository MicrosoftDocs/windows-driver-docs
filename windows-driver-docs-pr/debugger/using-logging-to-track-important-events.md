---
title: Using Logging to Track Important Events
description: Using Logging to Track Important Events
ms.assetid: 297336c2-85fb-4235-a7ab-0bbf571b8b98
keywords: ["kernel streaming debugging, video stream stall, logging"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using Logging to Track Important Events


In general, data is moved downstream only by triggering events, the minidriver's processing, and buffer completions. To isolate the cause of a hang or stall:

- Check for mismatched **KsGate*Xxx*** calls.

- Check for omitted **Ks*Xxx*AttemptProcessing** calls.

- Look for problems in code related to triggering events, including code that either references the pin flags for the problem stream or that calls **KsPinAttemptProcessing**.

- Look for problems in the code related to the processing dispatch, in particular where it queues to hardware and where clone pointers are created.

- Look for problems in the code related to the driver's deferred procedure call (DPC), especially where buffers are completed or any calls are made to [KsStreamPointerDelete](https://go.microsoft.com/fwlink/p/?linkid=56550).

- Look for problems in the startup code for the stream.

The most effective way to collect this information is by logging everything in the affected region, including processing, buffer acquisition (such as cloning and programming hardware), buffer release (such as deleting clones), and any gate manipulations. Most of this information is highly timing dependent and requires memory-based logging or ETW.

To maintain a rolling memory-based log, use the following code:

```cpp
typedef struct _LOGENTRY {
    ULONG Tag;
    ULONG Arg[3];
} LOGENTRY, *PLOGENTRY;
#define LOGSIZE 2048
LONG g_LogCount;
LOGENTRY g_Log [LOGSIZE];
#define LOG(tag,arg1,arg2,arg3) do { \
    LONG i = InterlockedIncrement (&g_LogCount) % LOGSIZE; \
    g_Log [i].Tag = tag; \
    g_Log [i].Arg [0] = (ULONG)(arg1); \
    g_Log [i].Arg [1] = (ULONG)(arg2); \
    g_Log [i].Arg [2] = (ULONG)(arg3); \
} while (0)
```dbgcmd

Then, use a simple "dc g\_Log" to view the contents of the **g\_Log** array in the debugger.

The following example uses the above memory-based scheme to determine the cause of a processing stall. Output is from an AVStream streaming scenario in graphedt. The following minidriver events were logged:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Abbreviation</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>Strt</em></p></td>
<td align="left"><p>This event occurs when the minidriver first queues buffers for the device from within the minidriver's <em>Start</em> dispatch.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>Prc&lt;</em></p></td>
<td align="left"><p>This event occurs at the start of the minidriver's <em>Process</em> dispatch.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>AddB</em></p></td>
<td align="left"><p>This event occurs when the minidriver queues buffers to the device from within its <em>Process</em> dispatch.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>DPC&lt;</em></p></td>
<td align="left"><p>This event occurs at the start of the minidriver's <em>CallOnDPC</em>. It indicates buffer completion.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>Atmp</em></p></td>
<td align="left"><p>This event occurs when the minidriver calls from within the DPC to <strong>KsPinAttemptProcessing</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>Dele</em></p></td>
<td align="left"><p>This event occurs when the minidriver calls from within the DPC to delete a clone stream pointer.</p></td>
</tr>
</tbody>
</table>

 

Log excerpts are as follows:

```text
f9494b80  3c435044 816e2c90 00000000 00000000  DPC<.,n.........
f9494b90  656c6544 816e2c90 81750260 00000000  Dele.,n.`.u.....
f9494ba0  706d7441 816e2c90 ffa4d418 00000000  Atmp.,n.........
f9494bb0  3c637250 819c1f00 00000000 00000000  Prc<............
f9494bc0  42646441 819c1f00 ffa2eb08 00000000  AddB............
f9494bd0  3c435044 816e2c90 00000000 00000000  DPC<.,n.........
f9494be0  656c6544 816e2c90 ffa80348 00000000  Dele.,n.H.......
f9494bf0  706d7441 816e2c90 ffa4d418 00000000  Atmp.,n.........
f9494c00  3c637250 819c1f00 00000000 00000000  Prc<............
f9494c10  42646441 819c1f00 ffa3d9b8 00000000  AddB............
```

This first log excerpt is representative of the normal streaming state. In the first line, the minidriver's *CallOnDPC* is called to complete a buffer (*DPC&lt;*). The buffer is deleted (*Dele*), and **KsPinAttemptProcessing** is called to move the leading edge forward, if there are any unprocessed buffers in the queue (*Atmp*). In this case, there were, as can be seen by the call to the process dispatch (*Prc&lt;*). More buffers are added to the queue (*AddB*), and the whole scenario repeats.

This next excerpt includes the last entries in the log right before the stall occurred.

```text
f949b430  3c435044 816e2c90 00000000 00000000  DPC<.,n.........
f949b440  656c6544 816e2c90 ffac4de8 00000000  Dele.,n..M......
f949b450  706d7441 816e2c90 ffa4d418 00000000  Atmp.,n.........
f949b460  3c435044 816e2c90 00000000 00000000  DPC<.,n.........
f949b470  656c6544 816e2c90 816ffc80 00000000  Dele.,n...o.....
f949b480  706d7441 816e2c90 ffa4d418 00000000  Atmp.,n.........
f949b490  3c435044 816e2c90 00000000 00000000  DPC<.,n.........
f949b4a0  656c6544 816e2c90 ffa80348 00000000  Dele.,n.H.......
f949b4b0  706d7441 816e2c90 ffa4d418 00000000  Atmp.,n.........
f949b4c0  3c435044 816e2c90 00000000 00000000  DPC<.,n.........
f949b4d0  656c6544 816e2c90 8174e1c0 00000000  Dele.,n...t.....
f949b4e0  706d7441 816e2c90 ffa4d418 00000000  Atmp.,n.........
```

In this example, several buffers are being completed (indicated by the repeated instances of *DPC&lt;*), but there are no unprocessed buffers in the queue, so the process dispatch is not being called (indicated by the absence of *Prc&lt;*). In fact, all of the processed buffers in the queue have been completed, apparently before any new unprocessed buffers could be added. Because the application is already running (so that *Start* will not be called) and no calls are being made to *CallOnDPC* (because there are no processed buffers ready to be completed), any new buffers are apparently accumulating ahead of the leading edge, waiting to be processed, with nothing initiating processing.

The problem is that the KSPIN\_FLAG\_DO\_NOT\_INITIATE\_PROCESSING flag has been set. When this flag is set, processing occurs only through a call to *Start* or *CallOnDPC*. If this flag is not set, processing will be initiated whenever new buffers are added to the queue.

 

 





