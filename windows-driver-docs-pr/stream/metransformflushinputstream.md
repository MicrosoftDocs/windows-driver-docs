---
title: METransformFlushInputStream Event
description: The METransformFlushInputStream event informs the Device Transform Manager to flush the output stream of devproxy that is connected to the input of Device MFT.
ms.date: 11/28/2017
---

# METransformFlushInputStream event


The **METransformFlushInputStream** event informs the Device Transform Manager to flush the output stream of devproxy that is connected to the input of Device MFT.

This is needed when a specific output of Device MFT gets flushed, the corresponding input of Device MFT and the connected devproxy stream need to be flushed.

## <span id="When_sent"></span><span id="when_sent"></span><span id="WHEN_SENT"></span>When sent


When Device MFT’s output is changed or flushed, the related input streams may need a flush. When this condition arises, Device MFT generates this event.

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


| Parameter              | Description                                                                     |
|------------------------|---------------------------------------------------------------------------------|
| **Input stream index** | The input stream index must be set on the attribute store of the IMFMediaEvent. |

 

## Remarks


When Device MFT’s input stream’s connected stream needs to be flushed, it generates this event. In response to this event, DTM would call [**FlushOutputStream**](/windows/win32/api/mftransform/nf-mftransform-imfdevicetransform-flushoutputstream) on the connected stream of the Devproxy and it will call [**FlushInputStream**](/windows/win32/api/mftransform/nf-mftransform-imfdevicetransform-flushinputstream) on the Device MFT. Device MFT would flush its input stream and the flush operation is considered complete.

In general, this event would be called when the stream itself is in running state or about to be stopped.

 

