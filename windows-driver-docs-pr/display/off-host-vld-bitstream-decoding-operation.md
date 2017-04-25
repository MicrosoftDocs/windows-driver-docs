---
title: Off-Host VLD Bitstream Decoding Operation
description: Off-Host VLD Bitstream Decoding Operation
ms.assetid: fd339d5f-2d63-4b2f-a5dc-7ab7a6799a6d
keywords:
- off-host VLD bitstream processing WDK DirectX VA
- bitstream VLD processing WDK DirectX VA
- inverse-quantization matrix buffers WDK DirectX VA
- slice-control buffers WDK DirectX VA
- bitstream buffers WDK DirectX VA
- compressed picture decoding WDK DirectX VA , macroblock-oriented picture decoding
- picture decoding WDK DirectX VA , compressed
- video decoding WDK DirectX VA , compressed pictures
- decoding video WDK DirectX VA , compressed pictures
- video decoding WDK DirectX VA , off-host VLD bitstream processing
- decoding video WDK DirectX VA , off-host VLD bitstream processing
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Off-Host VLD Bitstream Decoding Operation


## <span id="ddk_off_host_vld_bitstream_decoding_operation_gg"></span><span id="DDK_OFF_HOST_VLD_BITSTREAM_DECODING_OPERATION_GG"></span>


When variable-length decoding of raw bitstream data is performed on the accelerator, the data sent by the host for the decoding of the picture is divided into the following buffer types.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Buffer Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Inverse-quantization matrix</p></td>
<td align="left"><p>Provides information about how to perform inverse-quantization of the bitstream data.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Slice control</p></td>
<td align="left"><p>Provides information about the location of start codes and data within a corresponding bitstream data buffer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Bitstream</p></td>
<td align="left"><p>Contains raw streams of data encoded according to a particular video coding specification.</p></td>
</tr>
</tbody>
</table>

 

### <span id="Inverse-Quantization_Matrix_Buffers"></span><span id="inverse-quantization_matrix_buffers"></span><span id="INVERSE-QUANTIZATION_MATRIX_BUFFERS"></span>Inverse-Quantization Matrix Buffers

An inverse-quantization matrix buffer is sent to initialize inverse-quantization matrices for off-host bitstream decoding. Inverse-quantization matrix buffers provide information about how to decode all current and subsequent video in the bitstream, until a new inverse-quantization matrix buffer is provided. (Thus, inverse-quantization matrices are persistent.) No more than one inverse-quantization matrix buffer can be sent from the host to the accelerator at a time. The [**DXVA\_QmatrixData**](https://msdn.microsoft.com/library/windows/hardware/ff564034) structure loads quantization matrix data for compressed video-picture decoding.

### <span id="Slice-Control_Buffers"></span><span id="slice-control_buffers"></span><span id="SLICE-CONTROL_BUFFERS"></span>Slice-Control Buffers

Slice-control buffers guide the operation of off-host VLD bitstream processing. The host software decoder determines the location of slice-level resynchronization points in the bitstream. A slice is defined to be a multimacroblock layer that includes a resynchronization point in the bitstream data. In H.261 bitstreams, an H.261 Group Of Blocks (GOB) is considered a slice. In H.263 bitstreams, a sequence of one or more H.263 GOBs starting with a GOB start code and containing no additional GOB start codes is considered a slice. The slice-control buffer contains an array of [**DXVA\_SliceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff564049) slice-control structures, which apply to the contents of a corresponding bitstream data buffer.

### <span id="Bitstream_Buffers"></span><span id="bitstream_buffers"></span><span id="BITSTREAM_BUFFERS"></span>Bitstream Buffers

If a bitstream buffer is used, the buffer simply contains raw bytes from a video bitstream. This type of buffer is used for off-host decoding, including low-level bitstream parsing with variable-length decoding.

Certain restrictions are imposed on the contents of bitstream buffers, in order that the data received by accelerators is in a recognizable and efficient form.

1.  Except for MPEG-1 and MPEG-2, the first bitstream buffer for each picture must start with all data, if any, following the end of all data for any prior picture that precedes the first slice for the current picture in the bitstream (for example, the sequence header or picture header).

2.  For MPEG-1 and MPEG-2, the first bitstream buffer for each picture must start with the slice start code of the first slice of the picture (for example, no sequence header or picture header), because all relevant data is provided in other parameters.

3.  If the start of a slice of bitstream data is located within a particular bitstream buffer, the end of that slice must also be located within that same buffer unless the buffer that contains the start of the slice has reached its allocated size.

The decoder should manage the filling of the bitstream buffers to avoid placing the data for one slice into more than one buffer.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Off-Host%20VLD%20Bitstream%20Decoding%20Operation%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




