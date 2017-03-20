---
title: Macroblock Prediction
description: Macroblock Prediction
ms.assetid: 95e779ab-b110-4636-9475-6881dba89649
keywords: ["MCP WDK DirectX VA", "motion compensation WDK DirectX VA", "DirectX Video Acceleration WDK Windows 2000 display , video decoding", "Video Acceleration WDK DirectX , video decoding", "VA WDK DirectX , video decoding", "decoding video WDK DirectX VA , macroblock prediction", "video decoding WDK DirectX VA , macroblock prediction", "macroblocks WDK DirectX VA , prediction"]
---

# Macroblock Prediction


## <span id="ddk_macroblock_prediction_gg"></span><span id="DDK_MACROBLOCK_PREDICTION_GG"></span>


The formation of a macroblock prediction through motion-compensated prediction (MCP) must be done as a series of discrete stages as shown in the following figure and steps:

![diagram illustrating creating a macroblock prediction through motion-compensated prediction (mcp)](images/preddata.png)

The following four steps are involved in creating a macroblock prediction:

1.  Form the reference frame

    A reference frame is an uncompressed surface that was previously created by the decoding of a previous picture, or by writing directly into a video accelerator uncompressed surface.

2.  Extract the reference block

    A reference block is not necessarily the same as a prediction block. It most likely consists of extra samples that are needed in the prediction filtering stages. Unless half-sample filtering is executed in the memory unit, the reference block for a 16x16 half-sample filtered macroblock has a 17x17 matrix of blocks with each block consisting of an 8 row by 8 column of pixel element data. The size of the reference block is both a function of the prediction block dimensions and filter attributes of the prediction block. A reference block must refer to a block of data extracted from a reference frame buffer for use in [motion-compensated prediction](motion-compensated-prediction.md) (MCP).

    **Note**   The reference block is not defined for DirectX VA because it may have properties that reflect implementation-specific means of maintaining picture buffers.

     

3.  Filter the reference block to form a prediction block

    The reference block may be filtered in a third stage to produce a prediction block.

4.  Combine prediction blocks to form macroblock prediction

    One or more prediction blocks are combined to form the final prediction of the macroblock samples. Blocks are combined by averaging the pixel values between corresponding blocks in one or more prediction planes and rounding each up to the nearest integer (when fractional data is 0.5 or higher). P picture blocks are combined with the temporally closest previous I or P picture blocks. B picture blocks are combined with the closest previous and future I or P picture blocks.

The following figure shows the additional steps in the video decoding process that occur when creating a macroblock prediction. (The blocks with solid lines depict the motion compensation process, while the blocks with dotted lines depict other aspects of video decoding.)

![diagram illustrating signal flow of motion-compensation prediction blocks](images/sigflowmo3.png)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Macroblock%20Prediction%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




