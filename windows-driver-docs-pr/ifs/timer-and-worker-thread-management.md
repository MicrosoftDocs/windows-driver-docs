---
title: Timer and Worker Thread Management
description: Timer and Worker Thread Management
ms.assetid: b1feeb4a-0555-4ed6-a26c-ef2a5fc58280
keywords:
- RDBSS WDK file systems , worker thread management
- Redirected Drive Buffering Subsystem WDK file systems , worker thread management
- RDBSS WDK file systems , timers
- Redirected Drive Buffering Subsystem WDK file systems , timers
- timers WDK RDBSS
- worker threads WDK RDBSS
- one-shot notifications WDK RDBSS
- periodic triggers WDK RDBSS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Timer and Worker Thread Management


## <span id="ddk_timer_and_worker_thread_management_if"></span><span id="DDK_TIMER_AND_WORKER_THREAD_MANAGEMENT_IF"></span>


RDBSS provides several timer routines for worker thread management. These services are provided to all network mini-redirector drivers. The following types of timer routines are available:

-   A periodic trigger

-   A one-shot notification

A timer is associated with a device object and a worker thread routine. When a timer expires, a worker thread routine passed as an input parameter to the initial **RxPostOneShotTimerRequest** or **RxPostRecurrentTimerRequest** routine is called.

The following RDBSS timer routines are included.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Routine</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553395" data-raw-source="[&lt;strong&gt;RxCancelTimerRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553395)"><strong>RxCancelTimerRequest</strong></a></p></td>
<td align="left"><p>This routine cancels a timer request. The request to be canceled is identified by a pointer to the routine and a context parameter.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554612" data-raw-source="[&lt;strong&gt;RxPostOneShotTimerRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554612)"><strong>RxPostOneShotTimerRequest</strong></a></p></td>
<td align="left"><p>This routine is used by drivers to initialize a one-shot timer request. The worker thread routine passed to this routine is called once when the timer expires.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554615" data-raw-source="[&lt;strong&gt;RxPostRecurrentTimerRequest&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554615)"><strong>RxPostRecurrentTimerRequest</strong></a></p></td>
<td align="left"><p>This routine initializes a recurrent timer request. The worker thread routine passed to this routine is called at regular intervals when the recurrent timer fires based on the input parameters to this routine.</p></td>
</tr>
</tbody>
</table>

 

 

 




