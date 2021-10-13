---
title: Managing Memory Buffers During Audio Resource Rebalance and Surprise Removal Operations
description: PnP rebalancing is used in certain PCI scenarios where memory resources need to be reallocated. Memory Buffers need to be managed properly to avoid issues.
ms.date: 10/01/2020
ms.localizationpriority: medium
---

# Managing Memory Buffers During Audio Resource Rebalance and Surprise Removal Operations

## PnP Rebalance Overview

PnP rebalancing is used in certain PCI scenarios where memory resources need to be reallocated. PnP rebalancing is available in Windows 10, version 1511 and later versions of Windows. For general information on rebalancing, see [Implement PnP Rebalance for PortCls Audio Drivers](implement-pnp-rebalance-for-portcls-audio-drivers.md).

## PnP Surprise Removal Overview

PnP "Surprise Removal" (SR) occurs when a device been unexpectedly removed from the machine and is no longer available for I/O operations. For additional information, see [State Transitions for PnP Devices](../kernel/state-transitions-for-pnp-devices.md) and [Handling an IRP_MN_SURPRISE_REMOVAL Request](../kernel/handling-an-irp-mn-surprise-removal-request.md).

## Managing Memory Buffers During Audio Resource Rebalance and Surprise Removal Operations

This section describes how to manage memory buffers and the sequence of operations for memory buffer clean up during audio resource rebalance and PnP SR operations for HD Audio codec drivers.

Note that the operating system support for the buffer management approach described in this topic will be available in the next major feature release of Windows after the May 2019 Update.

If the allocation and deallocation of the supporting memory buffers is not done properly it can lead to memory corruption, soft hangs and failures, such as [Bug Check 0x9F: DRIVER_POWER_STATE_FAILURE](../debugger/bug-check-0x9f--driver-power-state-failure.md).


**Close Stream Handle Behavior**

When portcls receives the close stream handle, portcls invokes the functions below to set the stream state to stop and to free the buffer:

*set stream state* (If the stream is not already in the stop state.)

[IMiniportWaveRTStream::SetState](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertstream-setstate)

*release buffer*  

[IMiniportWaveRTStream::FreeAudioBuffer](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertstream-freeaudiobuffer) or [IMiniportWaveRTStreamNotification::FreeBufferWithNotification](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertstreamnotification-freebufferwithnotification)

Note that portcls miniport drivers should succeed the state transitions from higher value to lower values (RUN == 3, PAUSE==2, ACQUIRE==1, STOP==0) when the stream has been already stopped by the driver during a SR/STOP operation (i.e., when SR/STOP arrives before the close handle request).

**Buffer Handling**

When a stream is closed during normal operations, portcls invokes the Wave RT’s callbacks to let the driver stop its DMA operations and release its associated buffers:

[IMiniportWaveRTStream::SetState](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertstream-setstate) -> SetDmaEngineState (HD Audio Bus DDI). Takes action to start/pause DMA.

[IMiniportWaveRTStream::FreeAudioBuffer](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertstream-freeaudiobuffer) or [IMiniportWaveRTStreamNotification::FreeBufferWithNotification](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertstreamnotification-freebufferwithnotification)-> FreeDmaBuffer (HD Audio Bus DDI).

IMiniportWaveRTStream[Notification]’s destructor-> FreeDmaEngine (HD Audio Bus DDI). 

When a device is surprise removed, the miniport must release all its h/w resources without waiting for the open stream handles to close. This means that the miniport must stop, reset and free all its allocated DMA engines before forwarding the PnP request to PortCls with [PcDisptachIrp](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcdispatchirp) DDI. On the other hand, the miniport must not free the audio Wave RT buffers until the stream handles are closed and PortCls notifies the miniport with the FreeAudioBuffer/FreeBufferWithNotification callback.

When a device is stopped because it elected to support rebalance, the miniport must release all its hardware resources without waiting for the open stream handles to close. This means that the miniport must stop, reset and free all its allocated DMA engines in the PnP callback invoked by portcls. On the other hand, the miniport must not free the audio Wave RT buffers until the stream handles are closed and PortCls notifies the miniport with the FreeAudioBuffer/FreeBufferWithNotification callback.

Note that normal close stream operation can happen at the same time as SR/Stop operation, this means that the miniport must implement the proper synchronization between these threads.

Examples of operations assuming that the right serialization code exists between the SR/STOP and Close threads:


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
if (DmaEngineState != ResetState)
{
\\Set DMA Engine state to not running
SetDmaEngineState(context, StopState, 1, &dma);
SetDmaEngineState(context, ResetState, 1, &dma);
DmaEngineState = ResetState;
}
```


```
FREE_BUFFER:
\\Free DMA buffer
FreeDmaEBuffer(context, dma);
```


```
FREE_DMA_ENGINE:
if (DMAEngineAllocated==true)
{
\\Free DMA engine
FreeDmaEngine (context, dma);
DMAEngineAllocated=false
}
```

For more information, see:

[PSET_DMA_ENGINE_STATE callback function](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pset_dma_engine_state)

[HDAUDIO_STREAM_STATE Enumeration](/windows-hardware/drivers/ddi/hdaudio/ne-hdaudio-_hdaudio_stream_state)

[PFREE_DMA_ENGINE callback function](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pfree_dma_engine)

[PSET_DMA_ENGINE_STATE callback function](/windows-hardware/drivers/ddi/hdaudio/nc-hdaudio-pset_dma_engine_state)

[IMiniportWaveRTStreamNotification interface](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavertstreamnotification)

[IMiniportWaveRTStreamNotification::FreeBufferWithNotification method](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavertstreamnotification-freebufferwithnotification)

[PcDisptachIrp](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcdispatchirp)