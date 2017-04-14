---
title: Using Four Uncompressed Surfaces for Decoding
description: Using Four Uncompressed Surfaces for Decoding
ms.assetid: ceeea614-6793-4a75-8334-7dd062ac0b46
keywords: ["video decoding WDK DirectX VA , sequence requirements", "decoding video WDK DirectX VA , sequence requirements", "picture decoding WDK DirectX VA , sequence requirements", "sequence requirements WDK DirectX VA", "succession requirements WDK DirectX VA", "multiple uncompressed surfaces for decoding WDK DirectX VA", "uncompressed surfaces example for decoding WDK DirectX VA"]
---

# Using Four Uncompressed Surfaces for Decoding


## <span id="ddk_using_four_uncompressed_surfaces_for_decoding_gg"></span><span id="DDK_USING_FOUR_UNCOMPRESSED_SURFACES_FOR_DECODING_GG"></span>


The following table shows a hypothetical situation in which a video decoder requires one frame time to decode each picture. It decodes a bitstream consisting of a steadily increasing number of B pictures starting from zero B pictures after an initial I picture. The bitstream of B pictures occurs between pairs of P pictures. In this table, a letter shows the type of each picture (I, B, or P), a subscript shows the frame display index (the temporal display order of each picture), and a superscript shows the number of the buffer containing the picture.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Picture Decoded</th>
<th align="left">Picture Displayed</th>
<th align="left">Frames Decoded (at start of interval)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>I⁰₀</p></td>
<td align="left"></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>P¹₁</p></td>
<td align="left"></td>
<td align="left"><p>1</p></td>
</tr>
<tr class="odd">
<td align="left"><p>P²₃</p></td>
<td align="left"><p>I⁰₀</p></td>
<td align="left"><p>2</p></td>
</tr>
<tr class="even">
<td align="left"><p>B³₂</p></td>
<td align="left"><p>P¹₁</p></td>
<td align="left"><p>3</p></td>
</tr>
<tr class="odd">
<td align="left"><p>P⁰₆</p></td>
<td align="left"><p>B³₂</p></td>
<td align="left"><p>4</p></td>
</tr>
<tr class="even">
<td align="left"><p>B¹₄</p></td>
<td align="left"><p>P²₃</p></td>
<td align="left"><p>5</p></td>
</tr>
<tr class="odd">
<td align="left"><p>B³₅</p></td>
<td align="left"><p>B¹₄</p></td>
<td align="left"><p>6</p></td>
</tr>
<tr class="even">
<td align="left"><p>P²₁₀</p></td>
<td align="left"><p>B³₅</p></td>
<td align="left"><p>7</p></td>
</tr>
<tr class="odd">
<td align="left"><p>B¹₇</p></td>
<td align="left"><p>P⁰₆</p></td>
<td align="left"><p>8</p></td>
</tr>
<tr class="even">
<td align="left"><p>B³₈</p></td>
<td align="left"><p>B¹₇</p></td>
<td align="left"><p>9</p></td>
</tr>
<tr class="odd">
<td align="left"><p>B¹₉</p></td>
<td align="left"><p>B³₈</p></td>
<td align="left"><p>10</p></td>
</tr>
<tr class="even">
<td align="left"><p>P⁰₁₅</p></td>
<td align="left"><p>B¹₉</p></td>
<td align="left"><p>11</p></td>
</tr>
<tr class="odd">
<td align="left"><p>B³₁₁</p></td>
<td align="left"><p>P²₁₀</p></td>
<td align="left"><p>12</p></td>
</tr>
<tr class="even">
<td align="left"><p>B¹₁₂</p></td>
<td align="left"><p>B³₁₁</p></td>
<td align="left"><p>13</p></td>
</tr>
<tr class="odd">
<td align="left"><p>B³₁₃</p></td>
<td align="left"><p>B¹₁₂</p></td>
<td align="left"><p>14</p></td>
</tr>
<tr class="even">
<td align="left"><p>B¹₁₄</p></td>
<td align="left"><p>B³₁₃</p></td>
<td align="left"><p>15</p></td>
</tr>
<tr class="odd">
<td align="left"><p>P²₂₁</p></td>
<td align="left"><p>B¹₁₄</p></td>
<td align="left"><p>16</p></td>
</tr>
<tr class="even">
<td align="left"><p>B³₁₆</p></td>
<td align="left"><p>P²₂₁</p></td>
<td align="left"><p>17</p></td>
</tr>
<tr class="odd">
<td align="left"><p>B¹₁₇</p></td>
<td align="left"><p>B³₁₆</p></td>
<td align="left"><p>18</p></td>
</tr>
<tr class="even">
<td align="left"><p>B³₁₈</p></td>
<td align="left"><p>B¹₁₇</p></td>
<td align="left"><p>19</p></td>
</tr>
<tr class="odd">
<td align="left"><p>B¹₁₉</p></td>
<td align="left"><p>B³₁₈</p></td>
<td align="left"><p>20</p></td>
</tr>
<tr class="even">
<td align="left"><p>B³₂₀</p></td>
<td align="left"><p>B¹₁₉</p></td>
<td align="left"><p>21</p></td>
</tr>
<tr class="odd">
<td align="left"><p>P⁰₂₈</p></td>
<td align="left"><p>B³₂₀</p></td>
<td align="left"><p>22</p></td>
</tr>
</tbody>
</table>

 

Each B picture in the preceding table requires the decoding of two prior pictures in bitstream order before it can be decoded. As a consequence, the decoder cannot begin displaying pictures with their proper timing until after the second picture has been decoded (that is, until during the third time slice of decoding). Somewhere during this time slice, the display of pictures with their proper timing can begin.

The initiation of the display of a picture may not perfectly coincide with the picture that appears on the display. Instead, the display may continue to show a picture prior to the one that was sent for display until the proper time arrives to switch to the new picture. For optimal performance, surface 0 (which holds the first I picture) should not be overwritten for use by the B picture that arrives three frame times later, even though the I picture is not needed by that B picture for referencing. Instead, a fourth surface (surface 3) should be used to hold that B picture. This eliminates the need to check whether the display period of the first I picture has been completed before decoding the B picture.

The two rules described in [sequence requirements](sequence-requirements.md) for decoders require that each of the first three decoded pictures be placed in different surfaces, because none of them has been displayed until some time during the third period (period 2). Then, the fourth decoded picture should be placed in a fourth surface, because the display of the first displayed picture may not yet be over until some time during the fourth period (period 3).

A significant obstacle in the decoding process occurs as a result of having more than two B pictures in succession. This occurs in the preceding table upon encountering the tenth decoded picture (B¹₉). When the third or subsequent B picture in a contiguous series is encountered, the time lag tolerance between the display of one B picture and the use of a surface to hold the next decoded B picture is eliminated. The host decoder must check the display status of the B picture that was displayed in the previous period (B¹₇) to ensure that it has been removed from the display (waiting for this to happen if necessary), then it must immediately use the same surface for the next B picture to be decoded (surface 1 used for B¹₉). The decoder cannot decode the new B picture into either of the surfaces being used to hold its reference I or P pictures (in this case, surfaces 0 and 2 used for P⁰₆ and P²₁₀), and cannot decode the new B picture into the surface being displayed during the same interval of time (in this case, surface 3 used for B³₈). Thus, it must use the surface that was displayed in the immediately preceding period (in this case, surface 1).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Using%20Four%20Uncompressed%20Surfaces%20for%20Decoding%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




