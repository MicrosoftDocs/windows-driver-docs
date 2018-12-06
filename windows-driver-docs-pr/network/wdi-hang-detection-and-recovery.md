---
title: Hang detection and recovery
description: After a command is issued to the IHV component, the host starts a timer.
ms.assetid: 89133252-C08C-4ADC-A5EE-E46A91909337
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hang detection and recovery


After a command is issued to the IHV component, the host starts a timer. If the timer expires before the IHV component completes (Step 3 message in the figures in [Communication model, synchronization, and abort](wdi-communication-model.md)), the driver assumes that the IHV component is hung, resets the IHV component, and recovers if the precondition is correct.

The precondition is that the system will provide ACPI methods to reset the device, either at a bus or at the device level.

M1-M3 Hang Timeout is 10 seconds.

M3-M4 Task Hang Timeout is 30 seconds, or configurable based on task.

> [!NOTE]
> Some tasks may be expected to take longer than 30 seconds to complete (for example, Wi-Fi Direct Discover for the selected registrar bit in certain scenarios). In these cases, the host-initiated task timeout is adjusted accordingly to allow for 30 seconds longer than the maximum expected runtime of the task. 

These are maximum upper bounds for the commands and processing that takes longer than this time is considered an error. It is expected that under a normal mode of operation (no CPU stress), most tasks and properties finish significantly sooner than the timeouts specified above. These values are specified with each task/property. The adapter should ensure that it does not have waits that would cause those execution times to be exceeded.

## In this section

[UE hang detection and recovery flow](wdi-ue-hang-detection-and-recovery-flow.md)
[UE hang detection: steps 1-14](wdi-ue-hang-detection--step-1-to-step-14.md)
[Reset (surprise remove): steps 15-20](wdi-reset--surprise-remove---steps-15-20.md)
[Timings for diagnose call](wdi-timings-for-diagnose-call.md)
[LE hang detection](wdi-le-hang-detection.md)
[PLDR](wdi-pldr-and-fldr.md)
 

 





