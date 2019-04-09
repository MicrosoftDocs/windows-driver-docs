---
title: Managing Memory Buffers During Audio Resource Rebalance and Surprise Removal Operations
description: PnP rebalancing is used in certain PCI scenarios where memory resources need to be reallocated. Memory Buffers need to be managed properly to avoid issues.
ms.date: 04/09/2019
ms.localizationpriority: medium
---

# Managing Memory Buffers During Audio Resource Rebalance and Surprise Removal Operations

## PnP Rebalance Overview

PnP rebalancing is used in certain PCI scenarios where memory resources need to be reallocated. PnP rebalancing is available in Windows 10, version 1511 and later versions of Windows. For general information on rebalancing, see [Implement PnP Rebalance for PortCls Audio Drivers](implement-pnp-rebalance-for-portcls-audio-drivers.md).

## PnP Surprise Removal Overview

PnP "surprise removal" occurs when a device been unexpectedly removed from the machine and is no longer available for I/O operations. For additional information, see [State Transitions for PnP Devices](https://docs.microsoft.com/windows-hardware/drivers/kernel/state-transitions-for-pnp-devices) and [Handling an IRP_MN_SURPRISE_REMOVAL Request](https://docs.microsoft.com/windows-hardware/drivers/kernel/handling-an-irp-mn-surprise-removal-request).

## Managing Memory Buffers During Audio Resource Rebalance and Surprise Removal Operations

This section describes how to manage memory buffers and the sequence of operations for memory buffer clean up during audio resource rebalance and PnP surprise removal operations

If the allocation and deallocation of the supporting memory buffers is not done properly it can lead to memory corruption, soft hangs and failures, such as [Bug Check 0x9F: DRIVER_POWER_STATE_FAILURE](https://docs.microsoft.com/windows-hardware/drivers/debugger/bug-check-0x9f--driver-power-state-failure).


**Close Stream Handle Behavior**

When portcls receives the close stream handle, portcls will invoke the functions below to set the stream state to stop and to free the buffer:

*set stream state*

[IMiniportWaveRTStream::SetState](https://msdn.microsoft.com/en-us/library/windows/hardware/ff536756(v=vs.85).aspx)

*release buffer*  

[IMiniportWaveRTStream::FreeAudioBuffer](https://msdn.microsoft.com/library/windows/hardware/ff536745) or [IMiniportWaveRTStreamNotification::FreeBufferWithNotification](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/portcls/nf-portcls-iminiportwavertstreamnotification-freebufferwithnotification)

Note that portcls miniport drivers should succeed the state transitions from higher value to lower values (RUN == 3, PAUSE==2, ACQUIRE==1, STOP==0) when the stream has been already stopped by a Surprise Removal(SR)/STOP operation (i.e., when SR/STOP arrives before the close handle request).

**Suggested Buffer Handling**

Assuming that the right serialization code exists between the SR/STOP and Close threads the flow will be similar to the following:

On Close:

```
STOP_DMA

FREE_BUFFER

FREE_DMA_ENGINE
```

On SR/Stop:

```
STOP_DMA

FREE_DMA_ENGINE
```

This is the definition for these operations in pseudocode.

```
STOP_DMA:
If (DMA is running)
{
\\Set DMA Engine state to not running
SetDmaEngineState(context, StopState, 1, &dma);
SetDmaEngineState(context, ResetState, 1, &dma);
}
```


```
FREE_BUFFER
\\Free DMA buffer
FreeDmaEBuffer(context, dma);
```


```
FREE_DMA_ENGINE
If (DMA engine is allocated)
{
\\Free DMA engine
FreeDmaEngine (context, dma);
\\Set DMA engine is now freed - bool freeDma=false
}
```

For more information, see:

 [PSET_DMA_ENGINE_STATE callback function](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/hdaudio/nc-hdaudio-pset_dma_engine_state)

[HDAUDIO_STREAM_STATE Enumeration](https://docs.microsoft.com/en-us/windows-hardware/drivers/ddi/content/hdaudio/ne-hdaudio-_hdaudio_stream_state)

[PFREE_DMA_ENGINE callback function](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/hdaudio/nc-hdaudio-pfree_dma_engine)

[PSET_DMA_ENGINE_STATE callback function](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/hdaudio/nc-hdaudio-pset_dma_engine_state)