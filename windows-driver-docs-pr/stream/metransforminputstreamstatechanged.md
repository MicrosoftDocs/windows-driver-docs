---
title: METransformInputStreamStateChanged
description: The METransformInputStreamStateChanged event indicates that the input stream state or media type must be changed.
ms.assetid: 734080DD-8D96-4AF3-BB13-FDA8E0398C0B
---

# METransformInputStreamStateChanged


The **METransformInputStreamStateChanged** event indicates that the input stream state or media type must be changed.

## <span id="When_sent"></span><span id="when_sent"></span><span id="WHEN_SENT"></span>When sent


When the Device MFT output is changed, the related input stream state may also need to be changed. When this condition occurs, Device MFT generates a **METransformInputStreamStateChanged** event.

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


| Parameter              | Description                                                                     |
|------------------------|---------------------------------------------------------------------------------|
| **Input stream index** | The input stream index must be set on the attribute store of the IMFMediaEvent. |

 

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


In response to this event, the device transform manager (DTM) will call [**GetInputStreamPreferredState**](https://msdn.microsoft.com/library/windows/hardware/mt797670) on the Device MFT with the specified input stream index. Device MFT will return the preferred state and mediatype.

DTM would set the requested mediatype on the devproxy output stream and then transition it to the requested streaming state. If this succeeds, then DTM will set the same mediatype on the Device MFT input stream and transition it to the requested state.

If there is an error during this process then the **SetInputStreamStatedwStatus** parameter will contain the error that occurred. Device MFT should propagate the error to the DTM as appropriate.

This event may be generated when the specified stream is in stopped or running state. If the stream is in stopped state, Device Transform Manager will query the preferred type for that Device MFT input stream and sets it to the output of Devproxy. If that is successful, then DTM will set the same preferred mediatype on the input of the Device MFT.

When Device MFT generates this event while streaming, further sample delivery will be stopped, and the preferred mediatype will be requested on the Device MFT input. This mediatype is set on the output of Devproxy and input of Device MFT. The stream will be automatically restarted on the Devproxy output stream and the samples will be delivered to the Device MFT input stream. When new samples arrive, Device MFT will deliver the samples to the related output streams.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20METransformInputStreamStateChanged%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




