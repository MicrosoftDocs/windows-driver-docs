---
title: Capturing Video
author: windows-driver-content
description: Capturing Video
ms.assetid: 0adea8fe-1669-4daf-a858-05e014f00a72
keywords:
- video capture WDK AVStream , capturing process
- capturing video WDK AVStream , capturing process
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Capturing Video


Once the stream is in the **KSSTATE\_RUN** state, the capture process begins. Based on the frame interval specified by the **AvgTimePerFrame** member of the [**KS\_VIDEOINFOHEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567700) structure passed when the stream is opened, the stream transfers images into buffers passed through SRB\_READ\_DATA. Additional information about the image captured is returned in the [**KS\_FRAME\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567645) structure that is appended to the end of the [**KSSTREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567138) structure.

The following example code obtains the appended KS\_FRAME\_INFO structure:

```
PKSSTREAM_HEADER pDataPacket = pSrb->CommandData.DataBufferArray;
PKS_FRAME_INFO pFrameInfo = (PKS_FRAME_INFO) (pDataPacket + 1); 
```

A minidriver should set additional information fields about the data captured, such as frames captured, frames dropped, and field polarity. The frame information is generally stored in a member of the driver-writer defined stream extension.

```
*pFrameInfo = pStrmEx->FrameInfo; // Get the frame info from the minidriver-defined stream extension
```

It is optimal to update the **PictureNumber** or **DropCount** members of [**KS\_FRAME\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567645), [**KS\_VBI\_FRAME\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567694), or [**KSPROPERTY\_DROPPEDFRAMES\_CURRENT\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565138) at transition into the **KSSTATE\_ACQUIRE** state.

It is acceptable to update these members on transition from the **KSSTATE\_ACQUIRE** state into the **KSSTATE\_PAUSE** state.

Do not update **PictureNumber** or **DropCount** on transition from the **KSSTATE\_PAUSE** state to the **KSSTATE\_RUN** state or the **KSSTATE\_RUN** state to the **KSSTATE\_PAUSE** state.

If frames have been previously dropped, the minidriver should set the discontinuity flag and then reset its internal flag. The following code demonstrates setting the data discontinuity flag:

```
if (pStrmEx->fDiscontinuity) {
    pDataPacket->OptionsFlags |= KSSTREAM_HEADER_OPTIONSF_DATADISCONTINUITY;
    pStrmEx->fDiscontinuity = FALSE;
}
```

Finally, the minidriver should relinquish control of the SRB, completing the frame capture.

```
CompleteStreamSRB (pSrb);
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Capturing%20Video%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


