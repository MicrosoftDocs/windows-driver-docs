---
title: METransformNeedInput
description: The METransformNeedInput event indicates that a device transform needs an input.
ms.assetid: AACD80F6-90A1-4338-AE5B-4A9248747949
---

# METransformNeedInput


The **METransformNeedInput** event indicates that a device transform needs an input.

## <span id="When_sent"></span><span id="when_sent"></span><span id="WHEN_SENT"></span>When sent


This event is sent when a device transform needs input to generate output. Typically, async MFTs use this message to get input samples for processing and producing an output sample.

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


| Parameter              | Description                                                                                                   |
|------------------------|---------------------------------------------------------------------------------------------------------------|
| **Input stream index** | The input stream index is sent in the IMFMediaEvent attribute store as **MF\_EVENT\_MFT\_INPUT\_STREAM\_ID**. |

 

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


This event will not be handled by device transform manager (DTM) for the following reasons:

-   Devproxy does not have any input pins
-   Even though Device MFT has input pins, it is automatically fed samples when they are available on the output of Devproxy. Therefore, there is no need for Device MFT to request for samples. This request would be ignored by DTM.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20METransformNeedInput%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




