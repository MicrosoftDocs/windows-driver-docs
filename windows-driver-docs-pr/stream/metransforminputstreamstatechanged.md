---
title: METransformInputStreamStateChanged
description: The METransformInputStreamStateChanged event indicates that the input stream state or media type must be changed.
ms.assetid: 734080DD-8D96-4AF3-BB13-FDA8E0398C0B
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# METransformInputStreamStateChanged


The **METransformInputStreamStateChanged** event indicates that the input stream state or media type must be changed.

## <span id="When_sent"></span><span id="when_sent"></span><span id="WHEN_SENT"></span>When sent


When the Device MFT output is changed, the related input stream state may also need to be changed. When this condition occurs, Device MFT generates a **METransformInputStreamStateChanged** event.

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


| Parameter              | Description                                                                     |
|------------------------|---------------------------------------------------------------------------------|
| **Input stream index** | The input stream index must be set on the attribute store of the IMFMediaEvent. |

 

## Remarks


In response to this event, the device transform manager (DTM) will call [**GetInputStreamPreferredState**](https://msdn.microsoft.com/library/windows/hardware/mt797670) on the Device MFT with the specified input stream index. Device MFT will return the preferred state and mediatype.

DTM would set the requested mediatype on the devproxy output stream and then transition it to the requested streaming state. If this succeeds, then DTM will set the same mediatype on the Device MFT input stream and transition it to the requested state.

If there is an error during this process then the **SetInputStreamStatedwStatus** parameter will contain the error that occurred. Device MFT should propagate the error to the DTM as appropriate.

This event may be generated when the specified stream is in stopped or running state. If the stream is in stopped state, Device Transform Manager will query the preferred type for that Device MFT input stream and sets it to the output of Devproxy. If that is successful, then DTM will set the same preferred mediatype on the input of the Device MFT.

When Device MFT generates this event while streaming, further sample delivery will be stopped, and the preferred mediatype will be requested on the Device MFT input. This mediatype is set on the output of Devproxy and input of Device MFT. The stream will be automatically restarted on the Devproxy output stream and the samples will be delivered to the Device MFT input stream. When new samples arrive, Device MFT will deliver the samples to the related output streams.

 

 





