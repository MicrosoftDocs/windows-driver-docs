---
title: METransformHaveOutput
description: The METransformHaveOutput event indicates that a device transform has a sample ready on one of its output streams.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1CD11A3C-8181-4AF2-9AB3-10B04668CF1C
---

# METransformHaveOutput


The **METransformHaveOutput** event indicates that a device transform has a sample ready on one of its output streams.

## <span id="When_sent"></span><span id="when_sent"></span><span id="WHEN_SENT"></span>When sent


Devproxy or Device MFT raises this event when they have a sample ready on their output stream to be picked up by device transform manager (DTM).

When Devproxy raises METransformHaveOutput, DTM would call ProcessOutput on Devproxy. The resulting samples would be fed into the Device MFT’s corresponding input.

When Device MFT raises **METransformHaveOutput**, DTM would relay the event to Device Source. Device Source would call Process Output on Device Transform Manager which would be routed to the Device MFT. Thus the sample would be picked up by Device Source and would enter the media pipeline.

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


None.

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


Device MFT would receive the total output stream count of **MFT\_OUTPUT\_DATA\_BUFFER** structures in an array. It is expected to fill in the structure members with appropriate values. Before DTM calls back into the Device MFT to retrieve a sample, in response to a **METransformHaveOutput** message, if another sample becomes available for another stream, Device MFT would go ahead and send the sample in this ProcessOutput call. DTM would call ProcessOutput again, but at that time, Device MFT could just return the call with no samples if none is available.

For more information, see [**IMFDeviceTransform::ProcessOutput**](https://msdn.microsoft.com/library/windows/hardware/mt797682).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20METransformHaveOutput%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




