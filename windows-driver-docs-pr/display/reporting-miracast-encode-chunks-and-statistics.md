---
title: Reporting Miracast encode chunks and statistics
description: Display hardware can process each video frame sent over a Miracast wireless display link by splitting the frame into multiple parts, or encode chunks.
ms.assetid: E1CE637F-42ED-4BEB-A2FF-04B4B88469DC
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting Miracast encode chunks and statistics


Display hardware can process each video frame sent over a Miracast wireless display link by splitting the frame into multiple parts, or *encode chunks*. Each chunk has a unique chunk ID that's generated from the frame number and the frame part (or slice) number. Each chunk that's related to the same desktop frame update must be assigned the same frame number.

## <span id="Reporting_chunk_processing"></span><span id="reporting_chunk_processing"></span><span id="REPORTING_CHUNK_PROCESSING"></span>Reporting chunk processing


A driver can encode a frame to be sent over a Miracast wireless link either in multiple processing steps—for example separating color conversion from encoding—or in a single step. Each processing step should be assigned a unique frame part number within the frame.

Either the Miracast user-mode driver or the display miniport driver must notify the operating system each time that the hardware has completed a processing step for a frame, and immediately before each part of the frame is sent to the network. The time of a particular reported processing step is assumed to be the time the event was reported to the operating system, so it's important to report the stages as rapidly as possible.

The operating system takes no action other than to log these events using the Event Tracing for Windows (ETW) kernel-level tracing facility. This info is nevertheless important for measuring and investigating performance issues.

These are the possible ways that a driver can provide the notification:

-   The Miracast user-mode driver calls the [**ReportStatistic**](https://msdn.microsoft.com/library/windows/hardware/dn265503) callback function to report details with the **MIRACAST\_STATISTIC\_TYPE\_CHUNK\_PROCESSING\_COMPLETE** type, or with **MIRACAST\_STATISTIC\_TYPE\_CHUNK\_SENT** to indicate the chunk is just about to be sent to the network stack for transmission.
-   The display miniport driver reports details of the chunk processing with the **DXGK\_INTERRUPT\_MICACAST\_CHUNK\_PROCESSING\_COMPLETE** interrupt type, although this report can only be made at interrupt time, and in a addition to logging the chunk info, a chunk packet is created and queued so that the Miracast user-mode driver can retrieve it by calling the [**GetNextChunkData**](https://msdn.microsoft.com/library/windows/hardware/dn265462) callback function.
-   The display miniport driver calls the [**DxgkCbReportChunkInfo**](https://msdn.microsoft.com/library/windows/hardware/dn344647) callback function at any IRQL level. This function logs only the chunk info and does not queue any chunk packets.

If the desktop image is not updated but the driver needs to encode the desktop image again to improve quality, the same frame number and part numbers should be used. The performance tools will trigger the second encode complete event for the same frame and part number, indicating that a second encode of the same frame was performed.

**Note**  The last slice of each frame must have a frame part number of zero. Doing this indicates to performance tools that this is the last slice of the frame.

 

To ensure correct synchronization of the primary surface, if the encoding is performed by the pixel pipeline, any requested flip operation at a VSync interval should not be reported before the encoding has finished accessing the primary surface. This prevents the presenter from rendering to the primary surface while the encode engine is reading from it.

The Miracast user-mode driver should inform the operating system at each of several stages of processing the frame:

<span id="Start_frame__chunk_type__MIRACAST_CHUNK_TYPE_FRAME_START_"></span><span id="start_frame__chunk_type__miracast_chunk_type_frame_start_"></span><span id="START_FRAME__CHUNK_TYPE__MIRACAST_CHUNK_TYPE_FRAME_START_"></span>Start frame, chunk type **MIRACAST\_CHUNK\_TYPE\_FRAME\_START**:  
Represents the point where the operating system asks the driver to display the new desktop frame. Although technically this could be reported from the Miracast user-mode driver, the start of processing new frame always involves the display miniport driver and should be reported by that driver.

<span id="Color_convert_complete__chunk_type_MIRACAST_CHUNK_TYPE_COLOR_CONVERT_COMPLETE_"></span><span id="color_convert_complete__chunk_type_miracast_chunk_type_color_convert_complete_"></span><span id="COLOR_CONVERT_COMPLETE__CHUNK_TYPE_MIRACAST_CHUNK_TYPE_COLOR_CONVERT_COMPLETE_"></span>Color convert complete, chunk type **MIRACAST\_CHUNK\_TYPE\_COLOR\_CONVERT\_COMPLETE**:  
Some solutions have separate color convert and encode stages. In such solutions the color convert complete processing event should be reported as soon as possible, and the driver should use the [**DXGK\_MIRACAST\_CHUNK\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn322056).**ProcessingTime** member to report the time it took for the hardware to perform the operation. If the entire frame is color converted all at once rather than in slices, then the part number should be zero.

<span id="Encode_complete__chunk_type_MIRACAST_CHUNK_TYPE_ENCODE_COMPLETE_"></span><span id="encode_complete__chunk_type_miracast_chunk_type_encode_complete_"></span><span id="ENCODE_COMPLETE__CHUNK_TYPE_MIRACAST_CHUNK_TYPE_ENCODE_COMPLETE_"></span>Encode complete, chunk type **MIRACAST\_CHUNK\_TYPE\_ENCODE\_COMPLETE**:  
Indicates that the H.264 encode has been completed. The **ProcessingTime** and **EncodeRate** members of the [**DXGK\_MIRACAST\_CHUNK\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn322056) structure should be completed.

<span id="Frame_send__calling_ReportStatistic_using_MIRACAST_STATISTIC_TYPE_CHUNK_SENT_"></span><span id="frame_send__calling_reportstatistic_using_miracast_statistic_type_chunk_sent_"></span><span id="FRAME_SEND__CALLING_REPORTSTATISTIC_USING_MIRACAST_STATISTIC_TYPE_CHUNK_SENT_"></span>Frame send, calling [**ReportStatistic**](https://msdn.microsoft.com/library/windows/hardware/dn265503) using **MIRACAST\_STATISTIC\_TYPE\_CHUNK\_SENT**:  
Indicates that the data packet for this frame/part number is just about to be sent to the networking API for transmission from the Miracast user-mode driver. If the data for this frame/part is sent using multiple calls to the networking API, then this should only be logged just before the first packet is sent. The call to indicate this should be made just before calling the network API. This is important because if the network API blocks calls, then we do not want that blocked time to count against processing of the frame in the graphics stack.

<span id="Dropped_frame__chunk_type__MIRACAST_CHUNK_TYPE_FRAME_DROPPED_"></span><span id="dropped_frame__chunk_type__miracast_chunk_type_frame_dropped_"></span><span id="DROPPED_FRAME__CHUNK_TYPE__MIRACAST_CHUNK_TYPE_FRAME_DROPPED_"></span>Dropped frame, chunk type **MIRACAST\_CHUNK\_TYPE\_FRAME\_DROPPED**:  
If at any time the driver decides that it won't complete the processing of the frame/part and send it to the sink, then it should report the dropped frame. In this context a frame is only considered dropped if the driver actually started processing it by logging **MIRACAST\_CHUNK\_TYPE\_FRAME\_START**. If a driver calculates that it's going to skip this frame without any processing, it can log **MIRACAST\_CHUNK\_TYPE\_FRAME\_DROPPED** without logging **MIRACAST\_CHUNK\_TYPE\_FRAME\_START**.

<span id="Driver_defined_chunk_type_MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_1_or__2_"></span><span id="driver_defined_chunk_type_miracast_chunk_type_encode_driver_defined_1_or__2_"></span><span id="DRIVER_DEFINED_CHUNK_TYPE_MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_1_OR__2_"></span>Driver defined chunk type **MIRACAST\_CHUNK\_TYPE\_ENCODE\_DRIVER\_DEFINED\_1** or **\_2**:  
These chunk types are available to help you understand the performance of a scenario. An example would be where the driver uses these types to indicate that an I-Frame was created for this frame. Another example would be where the driver logs an additional packet after the last slice of the frame has been sent to network APIs that contained the total size of the encoded frame.

Here are examples of how frame color is converted and then how the display miniport driver reports completion of the color conversion.

**Reporting a single frame without using slices:**

Value of [**MIRACAST\_CHUNK\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn265473) member:
**ChunkType** value
**ChunkId**.
**ChunkId**.
Stage of processing
MIRACAST\_ CHUNK\_TYPE\_
FrameNumber
PartNumber
ProcessingTime
EncodeRate
Start processing frame
**FRAME\_START**
101
0
0
0
Color conversion is complete
**COLOR\_CONVERT\_** **COMPLETE**
101
0
950
0
Encode is complete
**ENCODE\_** **COMPLETE**
101
0
1042
15000
Just before call to send data to network
[**ReportStatistic**](https://msdn.microsoft.com/library/windows/hardware/dn265503) call\*
101, value of **ChunkSent**. **ChunkId**. **FrameNumber**
0, value of **ChunkSent**. **ChunkId**. **PartNumber**
N/A
N/A
 

\*Called using **MIRACAST\_STATISTIC\_TYPE\_CHUNK\_SENT**.

**Reporting a single frame, processed using slices:**

Value of [**MIRACAST\_CHUNK\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn265473) member:
**ChunkType**
**ChunkId**.
**ChunkId**.
Stage of processing
MIRACAST\_ CHUNK\_TYPE\_
FrameNumber
PartNumber
ProcessingTime
EncodeRate
Start processing frame
**FRAME\_START**
101
0
0
0
Color conversion is complete
**COLOR\_CONVERT\_** **COMPLETE**
101
0
950
0
Encode of slice 1 is complete
**ENCODE\_** **COMPLETE**
101
1
1042
15000
Encode of slice 2 is complete
**ENCODE\_** **COMPLETE**
101
0
400
15000
Just before call to send slice 1 data to network
[**ReportStatistic**](https://msdn.microsoft.com/library/windows/hardware/dn265503) call\*
101, value of **ChunkSent**. **ChunkId**. **FrameNumber**
1, value of **ChunkSent**. **ChunkId**. **PartNumber**
N/A
N/A
Just before call to send slice 2 data to network
[**ReportStatistic**](https://msdn.microsoft.com/library/windows/hardware/dn265503) call\*
101, value of **ChunkSent**. **ChunkId**. **FrameNumber**
0, value of **ChunkSent**. **ChunkId**. **PartNumber** (See Note above.)
N/A
N/A
 

\*Called using **MIRACAST\_STATISTIC\_TYPE\_CHUNK\_SENT**.

**Reporting an original frame, processed and then re-encoded without using slices:**

Value of [**MIRACAST\_CHUNK\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn265473) member:
**ChunkType**
**ChunkId**.
**ChunkId**.
Stage of processing
MIRACAST\_ CHUNK\_TYPE\_
FrameNumber
PartNumber
ProcessingTime
EncodeRate
Start processing frame
**FRAME\_START**
101
0
0
0
Color conversion is complete
**COLOR\_CONVERT\_** **COMPLETE**
101
0
950
0
Encode is complete
**ENCODE\_** **COMPLETE**
101
0
1042
15000
Just before call to send data for original frame to network
[**ReportStatistic**](https://msdn.microsoft.com/library/windows/hardware/dn265503) call\*
101, value of **ChunkSent**. **ChunkId**. **FrameNumber**
0, value of **ChunkSent**. **ChunkId**. **PartNumber**
N/A
N/A
Re-encode is complete
**ENCODE\_** **COMPLETE**
101
0
500
15000
Just before call to send data for re-encoded frame to network
[**ReportStatistic**](https://msdn.microsoft.com/library/windows/hardware/dn265503) call\*
101, value of **ChunkSent**. **ChunkId**. **FrameNumber**
0, value of **ChunkSent**. **ChunkId**. **PartNumber**
N/A
N/A
 

\*Called using **MIRACAST\_STATISTIC\_TYPE\_CHUNK\_SENT**.

## <span id="Reporting_protocol_events"></span><span id="reporting_protocol_events"></span><span id="REPORTING_PROTOCOL_EVENTS"></span>Reporting protocol events


When the Miracast user-mode driver reports protocol events by calling the [**ReportStatistic**](https://msdn.microsoft.com/library/windows/hardware/dn265503) function with [**MIRACAST\_STATISTIC\_DATA**](https://msdn.microsoft.com/library/windows/hardware/dn265479).**StatisticType** set to **MIRACAST\_STATISTIC\_TYPE\_EVENT**, the operating system logs the event but takes no other action. These events are nevertheless valuable for diagnostics and performance investigation.

The [**MIRACAST\_PROTOCOL\_EVENT**](https://msdn.microsoft.com/library/windows/hardware/dn265477) enumeration includes possible protocol event types that can be reported.

## <span id="Reporting_protocol_errors"></span><span id="reporting_protocol_errors"></span><span id="REPORTING_PROTOCOL_ERRORS"></span>Reporting protocol errors


While a Miracast connected session is in progress, if a Miracast user-mode driver discovers an error, it should call the [**ReportSessionStatus**](https://msdn.microsoft.com/library/windows/hardware/dn265502) callback function with appropriate [**MIRACAST\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/dn265481) error status info in the *MiracastStatus* parameter. The operating session will always destroy the session when an error is reported.

Note that although the operating system merely logs the [**ReportSessionStatus**](https://msdn.microsoft.com/library/windows/hardware/dn265502)*Status* parameter for diagnostics and doesn't take any action based on its value. However, we recommend that the driver use this parameter to differentiate between different causes of the error.

 

 





