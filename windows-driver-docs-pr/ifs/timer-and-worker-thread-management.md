---
title: Timer and Worker Thread Management
author: windows-driver-content
description: Timer and Worker Thread Management
ms.assetid: b1feeb4a-0555-4ed6-a26c-ef2a5fc58280
keywords: ["RDBSS WDK file systems , worker thread management", "Redirected Drive Buffering Subsystem WDK file systems , worker thread management", "RDBSS WDK file systems , timers", "Redirected Drive Buffering Subsystem WDK file systems , timers", "timers WDK RDBSS", "worker threads WDK RDBSS", "one-shot notifications WDK RDBSS", "periodic triggers WDK RDBSS"]
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
<td align="left"><p>[<strong>RxCancelTimerRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553395)</p></td>
<td align="left"><p>This routine cancels a timer request. The request to be canceled is identified by a pointer to the routine and a context parameter.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>RxPostOneShotTimerRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554612)</p></td>
<td align="left"><p>This routine is used by drivers to initialize a one-shot timer request. The worker thread routine passed to this routine is called once when the timer expires.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>RxPostRecurrentTimerRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554615)</p></td>
<td align="left"><p>This routine initializes a recurrent timer request. The worker thread routine passed to this routine is called at regular intervals when the recurrent timer fires based on the input parameters to this routine.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Timer%20and%20Worker%20Thread%20Management%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


