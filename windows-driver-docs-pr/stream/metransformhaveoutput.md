---
title: METransformHaveOutput
description: The METransformHaveOutput event indicates that a device transform has a sample ready on one of its output streams.
ms.assetid: 1CD11A3C-8181-4AF2-9AB3-10B04668CF1C
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# METransformHaveOutput


The **METransformHaveOutput** event indicates that a device transform has a sample ready on one of its output streams.

## <span id="When_sent"></span><span id="when_sent"></span><span id="WHEN_SENT"></span>When sent


Devproxy or Device MFT raises this event when they have a sample ready on their output stream to be picked up by device transform manager (DTM).

When Devproxy raises METransformHaveOutput, DTM would call ProcessOutput on Devproxy. The resulting samples would be fed into the Device MFT’s corresponding input.

When Device MFT raises **METransformHaveOutput**, DTM would relay the event to Device Source. Device Source would call Process Output on Device Transform Manager which would be routed to the Device MFT. Thus the sample would be picked up by Device Source and would enter the media pipeline.

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


None.

## Remarks


Device MFT would receive the total output stream count of **MFT\_OUTPUT\_DATA\_BUFFER** structures in an array. It is expected to fill in the structure members with appropriate values. Before DTM calls back into the Device MFT to retrieve a sample, in response to a **METransformHaveOutput** message, if another sample becomes available for another stream, Device MFT would go ahead and send the sample in this ProcessOutput call. DTM would call ProcessOutput again, but at that time, Device MFT could just return the call with no samples if none is available.

For more information, see [**IMFDeviceTransform::ProcessOutput**](https://msdn.microsoft.com/library/windows/hardware/mt797682).

 

 





