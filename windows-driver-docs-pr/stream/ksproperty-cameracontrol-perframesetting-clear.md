---
title: KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_CLEAR
description: The KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_CLEAR property ID that is defined in KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_PROPERTY is used to clear the per-frame settings in the driver.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: CCFB4226-36A7-4A5A-8A65-F8E9F281AAA4
keywords: ["KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_CLEAR Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_CLEAR
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_CLEAR


The **KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_CLEAR** property ID that is defined in **KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_PROPERTY** is used to clear the per-frame settings in the driver. This is a SET only control and there is no payload for this. This is usually used while finishing (unpreparing) a photo sequence.

## <span id="Photo_sequence_usage_summary"></span><span id="photo_sequence_usage_summary"></span><span id="PHOTO_SEQUENCE_USAGE_SUMMARY"></span>Photo sequence usage summary


**Infinite photo sequence**

The photo sequence enters the prepare state when a prepare photo sequence command is issued by the app client. The driver pin may be created or has already been created depending on the warm start state and whether it is the first time the photo sequence is prepared. After the prepare state is completed, the driver pin will be transited to the running state and the photo sequence transits to the ready state. The driver will then start filling its internal history buffers.

After a photo sequence start trigger KS\_VideoControlFlag\_StartPhotoSequenceCapture is received, the photo sequence will transit to the capture state and the driver pin remains in the running state. Upon entering this state, the driver will start to fill the future frames and deliver all available history frames along with any future frames.

After a photo sequence stop trigger KS\_VideoControlFlag\_StopPhotoSequenceCapture is received, the photo sequence transits to the ready state and the driver pin remains in the running state. Upon entering this state, the driver will stop delivering frames back to the pipeline and start filling its internal history buffers instead.

The photo sequence enters the unprepare state when a finish command is issued by the app client. The driver pin will be transited from the running state to the paused or stopped state by the pipeline depending on whether the warm state is enabled.

**Finite photo sequence**

The photo sequence enters the prepare state when a prepare photo sequence command is issued by the app client. The driver pin may be created or has already been created depending on the warm start state and whether it is the first time the photo sequence is prepared. After the prepare state is completed, the driver pin will be transited to the running state and the photo sequence transits to the ready state. The driver will then start filling its internal history buffers.

After a photo sequence start trigger KS\_VideoControlFlag\_StartPhotoSequenceCapture is received, the photo sequence will transit to the capture state and the driver pin remains in the running state. Upon entering this state, the driver will start to fill the future frames and deliver all available history frames along with any future frames.

After the last frame specified in the photo sequence has been marked with KSSTREAM\_HEADER\_OPTIONSF\_ENDOFPHOTOSEQUENCE and delivered, the photo sequence transits to the wait state and the driver pin remains in the running state. Upon entering this state, the driver shall stop delivering any frames back to the pipeline. The driver may choose to not generate any frames or to start filling its internal history buffers. The exact behavior is up to OEM.

After a photo sequence stop trigger KS\_VideoControlFlag\_StopPhotoSequenceCapture is received, the photo sequence transits to the ready state and the driver pin remains in the running state. Upon entering this state, driver starts filling its internal history buffers with no frames delivered to pipeline.

The photo sequence enters the unprepare state when a finish command is issued by the app client. The driver pin will be transited from the running state to the paused or stopped state by the pipeline depending on whether the warm state is enabled or not.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ksmedia.h</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_CLEAR%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




