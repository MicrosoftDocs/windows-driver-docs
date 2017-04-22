---
title: Stream Changes
author: windows-driver-content
description: Stream Changes
ms.assetid: 3bd6a511-c602-4159-87b4-7e1e55c03b2e
keywords:
- stream changes WDK DVD decoder
- formats WDK DVD decoder
- headers WDK DVD decoder
- stream formats WDK DVD decoder
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Stream Changes


## <a href="" id="ddk-stream-changes-ksg"></a>


The format of a DVD stream may change at anytime. For example, the audio stream format can change between AC3 and LPCM during playback.

Each data sample in the stream contains a [**KSSTREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567138) structure appended to it. This structure contains an **OptionsFlags** member.

The data sample associated with a header that contains one of the following flags may or may not contain a null data packet or valid data.

The following values of the KSSTREAM\_HEADER **OptionsFlags** member are important to DVD playback:

<a href="" id="ksstream-header-optionsf-datadiscontinuity"></a>**KSSTREAM\_HEADER\_OPTIONSF\_DATADISCONTINUITY**  
The KSSTREAM\_HEADER\_OPTIONSF\_DATADISCONTINUITY bit indicates that the sample immediately following it belongs to a different source (or location/position) of data than the previous sample. This indicates that whatever processing was in progress using the previous sample must be completed. This bit often comes in the middle of a previous frame, thus indicating that the decoder should discard the previous frame and begin processing with the new data.

<a href="" id="ksstream-header-optionsf-timediscontinuity"></a>**KSSTREAM\_HEADER\_OPTIONSF\_TIMEDISCONTINUITY**  
The KSSTREAM\_HEADER\_OPTIONSF\_TIMEDISCONTINUITY bit indicates that there will be a time gap in data immediately following this sample. For example, if the DVD stream contains a still frame encoded as a single I frame, the decoder receives all of the data for the I frame, with the last sample containing the KSSTREAM\_HEADER\_OPTIONSF\_TIMEDISCONTINUITY flag. This indicates that the decoder should immediately decode the I frame and not wait for B frame data.

<a href="" id="ksstream-header-optionsf-typechanged"></a>**KSSTREAM\_HEADER\_OPTIONSF\_TYPECHANGED**  
The KSSTREAM\_HEADER\_OPTIONSF\_TYPECHANGED bit indicates that the sample connected with the header will be a new [**KSDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff561656) block for the stream. This allows for changing of data types dynamically. An example would be the changing of video from 4x3 to 16x9, or the changing of audio from AC3 to PCM. The decoder should make all necessary changes for the new format block only when all data prior to the packet with the new format block has been processed.

When a stream format change occurs, the minidriver receives a data packet with the KSSTREAM\_HEADER\_OPTIONSF\_TYPECHANGED bit set in the **OptionsFlags** member of the KSSTREAM\_HEADER structure of the data packet.

The minidriver may never see the KSSTREAM\_HEADER\_OPTIONSF\_TYPECHANGED flag if it does not correctly expose the data formats supported by its audio stream.

**Correctly exposing the data formats supported by a stream involves two steps:**

1.  The SRB\_GET\_STREAM\_INFO handler for the stream must set the **StreamFormatsArray** pointer to point to an array of **NumberOfFormatArrayEntries** pointers, each of which points to a valid format block.

2.  The SRB\_GET\_DATA\_INTERSECTION handler must copy the format block corresponding to the proposed format into the supplied buffer.

A video format change must also signal KSSTREAM events to the video port connection to indicate that the video format has changed. A minidriver should use [**StreamClassStreamNotification**](https://msdn.microsoft.com/library/windows/hardware/ff568266)(SignalMultipleStreamEvents, pMyHwDevExt-&gt;pMyStreamObject, &MY\_KSEVENTSETID\_VPNOTIFY, KSEVENT\_VPNOTIFY\_FORMATCHANGE) for this purpose.

When some parameter of the video format changes, such as pixel aspect ratio, the decoder receives a format block. The decoder should signal the video port to renegotiate the video port connection. The decoder calls [**StreamClassStreamNotification**](https://msdn.microsoft.com/library/windows/hardware/ff568266) with the parameter *SignalMultipleStreamEvents*.

The DVD decoder minidriver must indicate that support is provided for this event in the [**HW\_STREAM\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff559692) entry for the VideoPort stream. The event set ID for the video port event is [KSEVENTSETID\_VPNotify](https://msdn.microsoft.com/library/windows/hardware/ff561780) and the event ID is [**KSEVENT\_VPNOTIFY\_FORMATCHANGE**](https://msdn.microsoft.com/library/windows/hardware/ff561933).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Stream%20Changes%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


