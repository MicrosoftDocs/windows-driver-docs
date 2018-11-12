---
title: Debugging a Processing Stall
description: Debugging a Processing Stall
ms.assetid: 9dff37ed-4843-4e85-8ab3-6a0a37a58c23
keywords: ["kernel streaming debugging, video stream stall, processing stall"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debugging a Processing Stall


Begin by finding the relevant pin. In a hypothetical case, the relevant video capture pin has address **8160DDE0**, so we use the [**!ks.dump**](-ks-dump.md) extension command on this address to get more details:

```dbgcmd
kd> !ks.dump 8160DDE0 7
Pin object 8160DDE0 [CKsPin = 8160DD50]
    DeviceState    KSSTATE_RUN
    ClientState    KSSTATE_RUN
    CKsPin object 8160DD50 [KSPIN = 8160DDE0]
        State                    KSSTATE_RUN
        Processing Mutex         8160DFD0 is not held
        And Gate &               8160DF88
        And Gate Count           1
```

First, determine if the pin is in the appropriate state and whether the processing mutex is being held by another thread. In this case, the pin state is **KSSTATE\_RUN**, as it should be, and the processing mutex is not being held, so we next use the [**!ks.dumpqueue**](-ks-dumpqueue.md) extension to determine if there are frames available:

```dbgcmd
kd> !ks.dumpqueue 8160DDE0 7
Queue 8172D5D8:
 Frames Received  : 763
    Frames Waiting   : 5
...<this part of display not shown>...
Queue 8172D5D8:
 Frame Header 81B77E60:
        Irp = 816EE008
        Refcount = 1
    Frame Header 81A568D0:
        Irp = 816DE008
        Refcount = 0
    Frame Header 81844ED8:
        Irp = FFA0F650
        Refcount = 0
    Frame Header 8174B0B0:
        Irp = FFABB460
        Refcount = 0
    Leading Edge:
        Stream Pointer 8183EA58 [Public 8183EA90]:
            Frame Header = 81B77E60
...<this part of display not shown>...
```

In the above partial display of the **!ks.dumpqueue** output, we see that there are five frames waiting, or available. Are these frames ahead of or behind the leading edge? In the **!ks.dumpqueue** display, the frames are always listed from oldest to newest. The frame header of the leading edge matches that of the first frame listed, the oldest frame. Thus all of the available frames are ahead of the leading edge.

If this were not the case, and instead all of the frames were behind the leading edge, and they had a reference count due to clone pointers, the problems most likely originate with either the hardware or the driver's programming of hardware. Make sure that the hardware is signaling buffer completions (check interrupts and DPCs) and determine that the driver is responding appropriately to those notifications (by deleting clones upon buffer completion, for example).

If, as in our example, all of the frames are ahead of the leading edge, the problem is almost certainly a software issue. Further information can be obtained by looking at the pin's And gate.

### <span id="interpreting_the_and_gate"></span><span id="INTERPRETING_THE_AND_GATE"></span>Interpreting the And Gate

The pin's And gate controls processing. If the gate count is one, processing can occur. Obtain the current status of the And gate by using the **!ks.dump** extension:

```dbgcmd
kd> !ks.dump 8160DDE0 7
Pin object 8160DDE0 [CKsPin = 8160DD50]
    DeviceState    KSSTATE_RUN
    ClientState    KSSTATE_RUN
    CKsPin object 8160DD50 [KSPIN = 8160DDE0]
        State                    KSSTATE_RUN
        Processing Mutex         8160DFD0 is not held
        And Gate &               8160DF88
        And Gate Count           1
```

Because the gate count is one, the And gate is open. In this case, investigate the following potential causes for the processing stall:

-   The process dispatch incorrectly returned STATUS\_PENDING.

-   The data availability case is missing a [KsPinAttemptProcessing](https://go.microsoft.com/fwlink/p/?linkid=56545) call.

 

 





