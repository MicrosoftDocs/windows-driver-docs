---
title: METransformFlushInputStream event
description: The METransformFlushInputStream event informs the Device Transform Manager to flush the output stream of devproxy that is connected to the input of Device MFT.
ms.assetid: 400FB4BE-90F2-4FF2-A709-7E213D99DCC8
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# METransformFlushInputStream event


The **METransformFlushInputStream** event informs the Device Transform Manager to flush the output stream of devproxy that is connected to the input of Device MFT.

This is needed when a specific output of Device MFT gets flushed, the corresponding input of Device MFT and the connected devproxy stream need to be flushed.

## <span id="When_sent"></span><span id="when_sent"></span><span id="WHEN_SENT"></span>When sent


When Device MFT’s output is changed or flushed, the related input streams may need a flush. When this condition arises, Device MFT generates this event.

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


| Parameter              | Description                                                                     |
|------------------------|---------------------------------------------------------------------------------|
| **Input stream index** | The input stream index must be set on the attribute store of the IMFMediaEvent. |

 

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


When Device MFT’s input stream’s connected stream needs to be flushed, it generates this event. In response to this event, DTM would call [**FlushOutputStream**](https://msdn.microsoft.com/library/windows/hardware/mt797665) on the connected stream of the Devproxy and it will call [**FlushInputStream**](https://msdn.microsoft.com/library/windows/hardware/mt797664) on the Device MFT. Device MFT would flush its input stream and the flush operation is considered complete.

In general, this event would be called when the stream itself is in running state or about to be stopped.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20METransformFlushInputStream%20event%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




