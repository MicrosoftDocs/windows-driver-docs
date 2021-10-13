---
title: Capturing Video
description: Capturing Video
keywords:
- video capture WDK AVStream , capturing process
- capturing video WDK AVStream , capturing process
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Capturing Video


Once the stream is in the **KSSTATE\_RUN** state, the capture process begins. Based on the frame interval specified by the **AvgTimePerFrame** member of the [**KS\_VIDEOINFOHEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_videoinfoheader) structure passed when the stream is opened, the stream transfers images into buffers passed through SRB\_READ\_DATA. Additional information about the image captured is returned in the [**KS\_FRAME\_INFO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_frame_info) structure that is appended to the end of the [**KSSTREAM\_HEADER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksstream_header) structure.

The following example code obtains the appended KS\_FRAME\_INFO structure:

```cpp
PKSSTREAM_HEADER pDataPacket = pSrb->CommandData.DataBufferArray;
PKS_FRAME_INFO pFrameInfo = (PKS_FRAME_INFO) (pDataPacket + 1); 
```

A minidriver should set additional information fields about the data captured, such as frames captured, frames dropped, and field polarity. The frame information is generally stored in a member of the driver-writer defined stream extension.

```cpp
*pFrameInfo = pStrmEx->FrameInfo; // Get the frame info from the minidriver-defined stream extension
```

It is optimal to update the **PictureNumber** or **DropCount** members of [**KS\_FRAME\_INFO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_frame_info), [**KS\_VBI\_FRAME\_INFO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_vbi_frame_info), or [**KSPROPERTY\_DROPPEDFRAMES\_CURRENT\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_droppedframes_current_s) at transition into the **KSSTATE\_ACQUIRE** state.

It is acceptable to update these members on transition from the **KSSTATE\_ACQUIRE** state into the **KSSTATE\_PAUSE** state.

Do not update **PictureNumber** or **DropCount** on transition from the **KSSTATE\_PAUSE** state to the **KSSTATE\_RUN** state or the **KSSTATE\_RUN** state to the **KSSTATE\_PAUSE** state.

If frames have been previously dropped, the minidriver should set the discontinuity flag and then reset its internal flag. The following code demonstrates setting the data discontinuity flag:

```cpp
if (pStrmEx->fDiscontinuity) {
    pDataPacket->OptionsFlags |= KSSTREAM_HEADER_OPTIONSF_DATADISCONTINUITY;
    pStrmEx->fDiscontinuity = FALSE;
}
```

Finally, the minidriver should relinquish control of the SRB, completing the frame capture.

```cpp
CompleteStreamSRB (pSrb);
```
