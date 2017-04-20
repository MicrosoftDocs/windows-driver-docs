---
title: Motion-Compensated Prediction
description: Motion-Compensated Prediction
ms.assetid: 02706369-2d99-4ac9-8dad-9e431acff42f
keywords:
- MCP WDK DirectX VA
- motion compensation WDK DirectX VA
- DirectX Video Acceleration WDK Windows 2000 display , video decoding
- Video Acceleration WDK DirectX , video decoding
- VA WDK DirectX , video decoding
- decoding video WDK DirectX VA , motion compensation prediction
- video decoding WDK DirectX VA , motion compensation prediction
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Motion-Compensated Prediction


## <span id="ddk_motion_compensated_prediction_gg"></span><span id="DDK_MOTION_COMPENSATED_PREDICTION_GG"></span>


Block motion-compensated prediction (MCP) is the type of prediction implemented by DirectX VA. This prediction type is what gives the MPEG and H.26x family of codecs the advantage over pure still-frame coding methods, such as JPEG. Types of motion-compensated prediction other than block-based prediction are not implemented by DirectX VA.

In motion-compensated prediction, previously transmitted and decoded data serves as the prediction for current data. The difference between the prediction and the actual current data values is the prediction error. The coded prediction error is added to the prediction to obtain the final representation of the input data. After the coded prediction error is added to the MCP, the final decoded picture is used in the MCP to generate subsequent coded pictures.

This recursive loop occasionally is broken by various types of resets that are specific to the element being predicted. The resets are described by the semantics of the decoding process. (For example, motion vectors and coefficient predictions are reset at slice boundaries, while the whole temporal frame prediction chain is reset by an intra-refresh frame.)

The following figure shows the signal flow for motion-compensated prediction.

![diagram illustrating motion-compensated prediction signal flow](images/sigflow.png)

The steps required for motion-compensated prediction coding of pictures are as follows:

1.  Reference blocks are extracted from previously decoded frames and modified as specified by encoded mode selection and the motion vectors and other prediction commands to form the prediction of each image block.

2.  The transformed difference between the current input data block and the prediction is approximated as closely as possible within the available bit rate by the encoder, and the result is sent as the coded prediction error.

3.  The prediction and inverse-transformed prediction error are summed to form a reconstructed picture block.

4.  The reconstructed picture block is stored in a reference frame buffer to be used for the prediction of subsequent pictures.

5.  This process continues again at step 1.

Motion vectors, DCT coefficients, and other data that is not directly part of the MCP process also employ prediction to make the transmitted form of the data more compact. These instances of prediction are executed on the [*host CPU*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-host-cpu) processor or bitstream parser/variable-length-decoding unit.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Motion-Compensated%20Prediction%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




