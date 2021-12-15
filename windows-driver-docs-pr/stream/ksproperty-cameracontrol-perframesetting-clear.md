---
title: KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_CLEAR
description: The KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_CLEAR property ID that is defined in KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_PROPERTY is used to clear the per-frame settings in the driver.
keywords: ["KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_CLEAR Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_PERFRAMESETTING_CLEAR
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 09/11/2018
---

# KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_CLEAR

The **KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_CLEAR** property ID that is defined in **KSPROPERTY\_CAMERACONTROL\_PERFRAMESETTING\_PROPERTY** is used to clear the per-frame settings in the driver. This is a SET only control and there is no payload for this. This is usually used while finishing (unpreparing) a photo sequence.

## Photo sequence usage summary


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

## Requirements

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
