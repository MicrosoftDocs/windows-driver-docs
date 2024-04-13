---
title: Reporting Miracast Encode Chunks and Statistics on Windows 8.1
description: Display hardware can process each video frame sent over a Miracast wireless display link by splitting the frame into multiple parts, or encode chunks.
ms.date: 03/24/2023
---

# Reporting Miracast encode chunks and statistics on Windows 8.1

> [!NOTE]
> Starting in Windows 10 (WDDM 2.0), the operating system ships with a built-in Miracast stack that can work on any GPU. For information about the Microsoft Miracast stack and the requirements of drivers and hardware to support Miracast displays starting in Windows 10, see the following documentation:
>
> * [Building best-in-class Wireless projection solutions with Windows 10](/windows-hardware/design/device-experiences/wireless-projection)
>
> * The relevant [WHLK documentation](/windows-hardware/test/hlk/windows-hardware-lab-kit) at **Device.Graphics.WDDM13.DisplayRender.WirelessDisplay**
>
> Driver developers should no longer implement a custom Miracast stack. Microsoft might remove support for custom Miracast stacks in a future version of Windows.

On Windows 8.1, display hardware can process each video frame sent over a Miracast wireless display link by splitting the frame into multiple parts, or *encode chunks*. Each chunk has a unique chunk ID that's generated from the frame number and the frame part (or slice) number. Each chunk that's related to the same desktop frame update must be assigned the same frame number.

## Reporting chunk processing

A driver can encode a frame to be sent over a Miracast wireless link either in multiple processing steps—for example separating color conversion from encoding—or in a single step. Each processing step should be assigned a unique frame part number within the frame.

Either the Miracast user-mode driver or the display miniport driver must notify the operating system each time that:

* The hardware has completed a processing step for a frame.
* Immediately before each part of the frame is sent to the network.

The time of a particular reported processing step is assumed to be the time the event was reported to the operating system, so it's important to report the stages as rapidly as possible.

The operating system takes no action other than to log these events using the Event Tracing for Windows (ETW) kernel-level tracing facility. This info is nevertheless important for measuring and investigating performance issues.

A driver can provide the notification using one of the following possible ways:

* The Miracast user-mode driver calls the [**ReportStatistic**](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_report_statistic) callback function to report details with the **MIRACAST_STATISTIC_TYPE_CHUNK_PROCESSING_COMPLETE** type, or with **MIRACAST_STATISTIC_TYPE_CHUNK_SENT** to indicate the chunk is about to be sent to the network stack for transmission.
* The display miniport driver reports details of the chunk processing with the **DXGK_INTERRUPT_MICACAST_CHUNK_PROCESSING_COMPLETE** interrupt type, although this report can only be made at interrupt time. In addition to logging the chunk info, a chunk packet is created and queued so that the Miracast user-mode driver can retrieve it by calling the [**GetNextChunkData**](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_get_next_chunk_data) callback function.
* The display miniport driver calls the [**DxgkCbReportChunkInfo**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_miracast_report_chunk_info) callback function at any IRQL level. This function logs only the chunk info and doesn't queue any chunk packets.

The same frame number and part numbers should be used if the desktop image isn't updated but the driver needs to encode the desktop image again to improve quality. The performance tools trigger the second encode complete event for the same frame and part number, indicating that a second encode of the same frame was performed.

The last slice of each frame must have a frame part number of zero, which indicates the last slice of the frame to performance tools.

To ensure correct synchronization of the primary surface, if the pixel pipeline performs the encoding, any requested flip operation at a VSync interval shouldn't be reported before the encoding has finished accessing the primary surface. This behavior prevents the presenter from rendering to the primary surface while the encode engine is reading from it.

The Miracast user-mode driver should inform the operating system at each of several stages of processing the frame:

* Start frame, chunk type **MIRACAST_CHUNK_TYPE_FRAME_START**

  Represents the point where the operating system asks the driver to display the new desktop frame. Although technically the Miracast user-mode driver could report this stage, the start of processing a new frame always involves the display miniport driver, and therefore should be reported by that driver.

* Color conversion complete, chunk type **MIRACAST_CHUNK_TYPE_COLOR_CONVERT_COMPLETE**

  Some solutions have separate color convert and encode stages. In such solutions, the color convert complete processing event should be reported as soon as possible, and the driver should use the [**DXGK_MIRACAST_CHUNK_INFO**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-dxgk_miracast_chunk_info).**ProcessingTime** member to report the time it took for the hardware to perform the operation. If the entire frame is color converted all at once rather than in slices, then the part number should be zero.

* Encode complete, chunk type **MIRACAST_CHUNK_TYPE_ENCODE_COMPLETE**

  Indicates that the H.264 encode has been completed. The **ProcessingTime** and **EncodeRate** members of the [**DXGK_MIRACAST_CHUNK_INFO**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-dxgk_miracast_chunk_info) structure should be completed.

* Frame send, calling [**ReportStatistic**](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_report_statistic) using **MIRACAST_STATISTIC_TYPE_CHUNK_SENT**

  Indicates that the Miracast user-mode driver is about to send the data packet for this frame/part number to the networking API for transmission. If the data for this frame/part is sent using multiple calls to the networking API, then it should only be logged just before the first packet is sent. The call should be made just before calling the network API. This timing is important because if the network API blocks calls, we don't want that blocked time to count against processing of the frame in the graphics stack.

* Dropped frame, chunk type **MIRACAST_CHUNK_TYPE_FRAME_DROPPED**

  If at any time the driver decides that it won't complete the processing of the frame/part and send it to the sink, then it should report the dropped frame. In this context, a frame is only considered dropped if the driver actually started processing it by logging **MIRACAST_CHUNK_TYPE_FRAME_START**. If a driver calculates that it's going to skip this frame without any processing, it can log **MIRACAST_CHUNK_TYPE_FRAME_DROPPED** without logging **MIRACAST_CHUNK_TYPE_FRAME_START**.

* Driver defined chunk type **MIRACAST_CHUNK_TYPE_ENCODE_DRIVER_DEFINED_1** or **_2**

  These chunk types are available to help you understand the performance of a scenario. Some examples include:

  * The driver uses these types to indicate that an I-Frame was created for this frame.
  * The driver logs another packet after the last slice of the frame has been sent to network APIs that contained the total size of the encoded frame.

## Examples of frame color conversion

The following examples show how frame color is converted and how the display miniport driver reports completion of the color conversion.

Table references to the members of the [**MIRACAST_CHUNK_INFO**](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-miracast_chunk_info) structure are:

* **ChunkType** is a [MIRACAST_CHUNK_TYPE_*XXX*](/windows-hardware/drivers/ddi/netdispumdddi/ne-netdispumdddi-miracast_chunk_type) value.

* **FrameNumber** and **PartNumber** are members of the [**ChunkId**](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-miracast_chunk_id) union.

* **ProcessingTime** is the time in microseconds.

* **EncodeRate** is in kilobits per second.

**MIRACAST_STATISTIC_TYPE_CHUNK_SENT** is used in processing stages involving calls to [**ReportStatistic**](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_report_statistic).

### Reporting a single frame without using slices

| Processing stage | ChunkType | FrameNumber | PartNumber | ProcessingTime | EncodeRate |
| ---------------- | --------- | ----------- | ---------- | -------------- | ---------- |
| Start processing frame       | **FRAME_START** | 101 | 0 | 0 | 0 |
| Color conversion is complete | **COLOR_CONVERT_COMPLETE** | 101 | 0 | 950 | 0 |
| Encode is complete           | **ENCODE_COMPLETE** | 101 | 0 | 1042 | 15000 |
| Just before call to send data to network **ReportStatistic** call | n/a | 101 (value of **ChunkSent.ChunkId.FrameNumber**) | 0 (value of **ChunkSent.ChunkId.PartNumber**) | n/a | n/a |

### Reporting a single frame, processed using slices

| Processing stage | ChunkType | FrameNumber | PartNumber | ProcessingTime | EncodeRate |
| ---------------- | --------- | ----------- | ---------- | -------------- | ---------- |
| Start processing frame        | **FRAME_START** | 101 | 0 | 0 | 0 |
| Color conversion is complete  | **COLOR_CONVERT_COMPLETE** | 101 | 0 | 950 | 0 |
| Encode of slice 1 is complete | **ENCODE_COMPLETE** | 101 | 1 | 1042 | 15000 |
| Encode of slice 2 is complete | **ENCODE_COMPLETE** | 101 | 0 | 400 | 15000 |
| Just before call to send slice 1 data to network **ReportStatistic** call | n/a | 101 (value of **ChunkSent.ChunkId.FrameNumber** for slice 1) | 1 (value of **ChunkSent.ChunkId.PartNumber** for slice 1) | n/a | n/a |
| Just before call to send slice 2 data to network **ReportStatistic** call | n/a | 101 (value of **ChunkSent.ChunkId.FrameNumber** for slice 2) | 0 (value of **ChunkSent.ChunkId.FrameNumber** for slice 2) | n/a | n/a |

### Reporting an original frame, processed and then re-encoded without using slices

| Processing stage | ChunkType | FrameNumber | PartNumber | ProcessingTime | EncodeRate |
| ---------------- | --------- | ----------- | ---------- | -------------- | ---------- |
| Start processing frame        | **FRAME_START** | 101 | 0 | 0 | 0 |
| Color conversion is complete  | **COLOR_CONVERT_COMPLETE** | 101 | 0 | 950 | 0 |
| Encode is complete            | **ENCODE_COMPLETE** | 101 | 0 | 1042 | 15000 |
| Just before call to send data for the original frame to network **ReportStatistic** call | n/a | 101 (value of **ChunkSent.ChunkId.FrameNumber**) | 0 (value of **ChunkSent.ChunkId.PartNumber**) | n/a | n/a |
| Re-encode is complete         | **ENCODE_COMPLETE** | 101 | 0 | 500 | 15000 |
| Just before call to send data for re-encoded frame to network **ReportStatistic** | n/a | 101 (value of **ChunkSent.ChunkId.FrameNumber**) | 0 (value of **ChunkSent.ChunkId.PartNumber**) | n/a | n/a |

## Reporting protocol events

When the Miracast user-mode driver reports protocol events by calling the [**ReportStatistic**](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_report_statistic) function with [**MIRACAST_STATISTIC_DATA**](/windows-hardware/drivers/ddi/netdispumdddi/ns-netdispumdddi-miracast_statistic_data)**.StatisticType** set to **MIRACAST_STATISTIC_TYPE_EVENT**, the operating system logs the event but takes no other action. These events are nevertheless valuable for diagnostics and performance investigation.

The [**MIRACAST_PROTOCOL_EVENT**](/windows-hardware/drivers/ddi/netdispumdddi/ne-netdispumdddi-miracast_protocol_event) enumeration includes possible protocol event types that can be reported.

## Reporting protocol errors

While a Miracast connected session is in progress, if a Miracast user-mode driver discovers an error, it should call the [**ReportSessionStatus**](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_report_session_status) callback function with appropriate [**MIRACAST_STATUS**](/windows-hardware/drivers/ddi/netdispumdddi/ne-netdispumdddi-miracast_status) error status info in the *MiracastStatus* parameter. The operating session always destroys the session when an error is reported.

Although the operating system merely logs the [**ReportSessionStatus**](/windows-hardware/drivers/ddi/netdispumdddi/nc-netdispumdddi-pfn_report_session_status) **Status** parameter for diagnostics and doesn't take any action based on its value, the driver should use this parameter to differentiate between different causes of the error.
