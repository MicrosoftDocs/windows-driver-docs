---
title: First Part of Macroblock Control Command Structure
description: First Part of Macroblock Control Command Structure
ms.assetid: b282adac-3bf3-4477-a817-371d37b174a5
keywords:
- macroblocks WDK DirectX VA , generic command structure
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# First Part of Macroblock Control Command Structure


## <span id="ddk_first_part_of_macroblock_control_command_structure_gg"></span><span id="DDK_FIRST_PART_OF_MACROBLOCK_CONTROL_COMMAND_STRUCTURE_GG"></span>


The first four members of a generic macroblock control command structure are always the same. The following table describes the members of the first part of this structure.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Member</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>wMBaddress</strong></p></td>
<td align="left"><p>Specifies the macroblock address of the macroblock currently being processed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>wMBtype</strong></p></td>
<td align="left"><p>Specifies the type of macroblock being processed. This member contains flags that indicate whether motion compensation is used to predict the value of the macroblock and what type of residual difference data is sent.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>dwMB_SNL</strong></p></td>
<td align="left"><p>Contains the two fields <em>MBskipsFollowing</em> (in the upper 8 bits) and <em>MBdataLocation</em> (in the lower 24 bits).</p>
<p><em>MBskipsFollowing</em> specifies the number of skipped macroblocks to be generated following the current macroblock.</p>
<p><em>MBdataLocation</em> is an index into the IDCT residual difference block data buffer, indicating the location of the residual difference data for the blocks of the current macroblock.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>wPatternCode</strong></p></td>
<td align="left"><p>Indicates whether residual difference data is sent for each block in the macroblock.</p></td>
</tr>
</tbody>
</table>

 

### <span id="wMBaddress"></span><span id="wmbaddress"></span><span id="WMBADDRESS"></span>wMBaddress

The **wMBaddress** structure member specifies the macroblock address of the current macroblock in raster scan order. The following table shows examples of macroblock addresses.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Macroblock</th>
<th align="left">Address</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>top-left</p></td>
<td align="left"><p>Zero</p></td>
</tr>
<tr class="even">
<td align="left"><p>top-right</p></td>
<td align="left"><p><strong>wPicWidthInMBminus1</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>lower-left</p></td>
<td align="left"><p><strong>wPicHeightInMBminus1</strong> x (<strong>wPicWidthInMBminus1</strong>+1)</p></td>
</tr>
<tr class="even">
<td align="left"><p>lower-right</p></td>
<td align="left"><p>(<strong>wPicHeightInMBminus1</strong>+1) x (<strong>wPicWidthInMBminus1</strong>+1) - 1</p></td>
</tr>
</tbody>
</table>

 

The **wPicWidthInMBminus1** and **wPicHeightInMBminus1** addresses are members of the [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) structure.

### <span id="wMBtype"></span><span id="wmbtype"></span><span id="WMBTYPE"></span>wMBtype

The **wMBtype** structure member specifies the type of macroblock being processed. This member contains a set of bits that define the way macroblocks and motion vectors are processed. The **bPic4MVallowed**, **bPicScanMethod**, **bPicBackwardPrediction**, **bPicStructure**, and **bPicScanFixed** addresses are members of the [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012)structure. The **bConfigHostInverseScan** address is a member of the [**DXVA\_ConfigPictureDecode**](https://msdn.microsoft.com/library/windows/hardware/ff563133) structure.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Bits</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>15 to 12</p></td>
<td align="left"><p><em>MvertFieldSel_3</em> (bit 15, the most significant) through <em>MvertFieldSel</em>_0 (bit 12)</p>
<p>Specifies vertical field selection for corresponding motion vectors sent later in the macroblock control command, as specified in the following tables. For frame-based motion with a frame picture structure (for example, for H.261 and H.263), these bits must all be zero. The bits in <em>MvertFieldSel_0, MvertFieldSel_1, MvertFieldSel_2,</em> and <em>MvertFieldSel_3</em> correspond to the motion_vertical_field_select[r][s] bits in Section 6.3.17.2 of MPEG-2.</p></td>
</tr>
<tr class="even">
<td align="left"><p>11</p></td>
<td align="left"><p>Reserved Bit. Must be zero.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>10</p></td>
<td align="left"><p><em>HostResidDiff</em></p>
<p>Specifies whether spatial-domain residual difference decoded blocks are sent, or whether transform coefficients are sent for off-host IDCT for the current macroblock. Must be zero if <strong>bConfigResidDiffHost</strong> is zero. Must be 1 if <strong>bConfigResidDiffAccelerator</strong> is zero.</p></td>
</tr>
<tr class="even">
<td align="left"><p>9 and 8</p></td>
<td align="left"><p><em>MotionType</em></p>
<p>Specifies the motion type in the picture. For example, for frame-based motion with a frame picture structure (as in H.261), bit 9 must be 1 and bit 8 must be zero.</p>
<p>The use of these bits corresponds directly to the use of the <em>frame_motion_type</em> or <em>field_motion_type</em> bits in Section 6.3.17.1 and Tables 6-17 and 6-18 of the MPEG-2 video standard when these bits are present in an MPEG-2 bitstream. The use of these bits is further explained following this table.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>7 and 6</p></td>
<td align="left"><p><em>MBscanMethod</em></p>
<p>Specifies the macroblock scan method. This must be equal to <strong>bPicScanMethod</strong> if <strong>bPicScanFixed</strong> is 1. If <em>HostResidDiff</em> is 1, this variable has no meaning and these bits should be set to zero.</p>
<p>If <strong>bConfigHostInverseScan</strong> is zero, <em>MBscanMethod</em> must be one of the following values:</p>
<ul>
<li><p>Bit 6 is zero and bit 7 is zero for zigzag scan (MPEG-2 Figure 7-2)</p></li>
<li><p>Bit 6 is 1 and bit 7 is zero for alternate-vertical scan (MPEG-2 Figure 7-3)</p></li>
<li><p>Bit 6 is zero and bit 7 is 1 for alternate-horizontal scan (H.263 Figure I.2 Part a)</p></li>
</ul>
<p>If <strong>bConfigHostInverseScan</strong> is 1, <em>MBscanMethod</em> must be equal to the following value:</p>
<ul>
<li><p>Bit 6 is 1 and bit 7 is 1 for arbitrary scan with absolute coefficient address.</p></li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p>5</p></td>
<td align="left"><p><em>FieldResidual</em></p>
<p>Indicates whether the residual difference blocks use a field IDCT structure as specified in MPEG-2.</p>
<p>This flag must be 1 if <strong>bPicStructure</strong> is 1 or 2. This flag must be zero when used for MPEG-2 if the <em>frame_pred_frame_DCT</em> flag in the MPEG-2 syntax is 1. This flag must be equal to the <em>dct_type</em> element of the MPEG-2 syntax when used for MPEG-2 if <em>dct_type</em> is present for the macroblock.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>4</p></td>
<td align="left"><p><em>H261LoopFilter</em></p>
<p>Specifies whether the H.261 loop filter (Section 3.2.3 of H.261) is active for the current macroblock prediction. The H.261 loop filter is a separable ¼, ½, ¼ filter applied both horizontally and vertically to all six blocks in an H.261 macroblock, except at block edges where one of the taps would fall outside the block. In such cases, the filter is changed to have coefficients 0, 1, 0. Full arithmetic precision is retained with rounding to 8-bit integers at the output of the 2-D filter process (half-integer or higher values being rounded up).</p></td>
</tr>
<tr class="even">
<td align="left"><p>3</p></td>
<td align="left"><p><em>Motion4MV</em></p>
<p>Indicates that forward motion uses a distinct motion vector for each of the four luminance blocks in the macroblock, as used in H.263 Annexes F and J. <em>Motion4MV</em> must be zero if <em>MotionForward</em> is zero or if <strong>bPic4MVallowed</strong> is zero.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>2</p></td>
<td align="left"><p><em>MotionBackward</em></p>
<p>This variable is used as specified for the corresponding <em>macroblock_motion_backward</em> parameter in MPEG-2. If the <strong>bPicBackwardPrediction</strong> member of the DXVA_PictureParameters structure is zero, <em>MotionBackward</em> must be zero.</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p><em>MotionForward</em></p>
<p>This variable is used as specified for the corresponding <em>macroblock_motion_forward</em> in MPEG-2. The use of this bit is further explained in the text following this table.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p><em>IntraMacroblock</em></p>
<p>Indicates that the macroblock is coded as intra and that no motion vectors are used for the current macroblock.</p>
<p>This variable corresponds to the <em>macroblock_intra</em> variable in MPEG-2. The use of this bit is further explained in the text following this table.</p></td>
</tr>
</tbody>
</table>

 

When macroblocks are predictively coded, they have associated motion vector values. The values are generated based on whether macroblocks are used for field-coded or frame-coded pictures. It is important for any implementation to properly account for every utilized macroblock type (especially for field-structured pictures or dual-prime motion).

The following two tables in this section indicate valid combinations of *IntraMacroblock*, *MotionForward*, *MotionBackward*, *MotionType*, *MvertFieldSel*, and **MVector** for frame-coded and field-coded pictures. **MVector** contains the horizontal and vertical components of a motion vector. The remaining variables and flags specify motion vector operation. This is determined according to the type of macroblock processed and whether macroblocks are being used for frame-coded or field-coded pictures.

The values shown in the following tables (in this section) occur for the following conditions:

-   *H261LoopFilter*, *Motion4MV*, and **bPicOBMC** are zero.

-   *PicCurrentField* flag is zero unless **bPicStructure** is 2 (bottom field). In this case, *PicCurrentField* is 1.

**MVector** is a member of the [**DXVA\_MBctrl\_P\_HostResidDiff\_1**](https://msdn.microsoft.com/library/windows/hardware/ff563993) and [**DXVA\_MBctrl\_P\_OffHostIDCT\_1**](https://msdn.microsoft.com/library/windows/hardware/ff563997) structures. The *IntraMacroblock*, *MotionForward*, *MotionBackward*, *MotionType*, *MvertFieldSel*, *H261LoopFilter*, and *Motion4MV* flags and variables are bitfields contained in the **wMBtype** member of the DXVA\_MBctrl\_P\_HostResidDiff\_1 and DXVA\_MBctrl\_P\_OffHostIDCT\_1 structures. **bPicOBMC** is a member of the [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) structure. The *PicCurrentField* flag is derived from the **bPicStructure** member of DXVA\_PictureParameters.

The following considerations apply when reviewing the following tables in this section:

-   In a number of places, the MPEG-2 variable name *PMV* is used to indicate the value of a motion vector. This notation is used to distinguish between the *PMV* variable as defined in MPEG-2, which is in frame coordinates, and a motion vector that may be in field coordinates (in other words, at half-vertical resolution). In all cases, *PMV* refers to the value of *PMV after* it has been updated by the current motion vector value (as specified in MPEG-2 video Section 7.6.3.1).

-   The definitions of vector'\[2\]\[0\] and vector'\[3\]\[0\] are found in MPEG-2 Section 7.6.3.6. The left**-**shift operation shown indicates that the vertical component is modified to frame coordinates.

-   In both "no motion" cases (0,0,0), the macroblock parameters emulate a forward prediction macroblock (0,1,0) with a zero-valued motion vector. (See also MPEG-2 Section 7.6.3.5.)

-   The values shown for *MotionType* in single quotes are binary representations (the first number is for bit 9 and the second is for bit 8).

-   The left-shift operator in the first table applies only to the second value shown.

### <span id="Frame-Structured_Pictures"></span><span id="frame-structured_pictures"></span><span id="FRAME-STRUCTURED_PICTURES"></span>Frame-Structured Pictures

The following table shows the valid combinations of element settings for frame-structured pictures (when the **bPicStructure** member of the [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) structure is equal to 3).

<table>
<colgroup>
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">IntraMacroblock, MotionForward, MotionBackward</th>
<th align="left">MotionType(meaning depends on picture type)</th>
<th align="left">MVector[0]MvertFieldSel_0 (1st, dir1)</th>
<th align="left">MVector[1]MvertFieldSel_1 (1st, dir2)</th>
<th align="left">MVector[2]MvertFieldSel_2 (2nd, dir1)</th>
<th align="left">MVector[3]MvertFieldSel_3 (2nd, dir2)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1,0,0 (intra)</p></td>
<td align="left"><p>&#39;00&#39; (intra)</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
</tr>
<tr class="even">
<td align="left"><p>0,0,0 (no motion)</p></td>
<td align="left"><p>&#39;10&#39; (no motion)</p></td>
<td align="left"><p>0</p>
<p>-</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0,1,0</p></td>
<td align="left"><p>&#39;10&#39; (frame MC)</p></td>
<td align="left"><p>PMV[0][0]</p>
<p>-</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
</tr>
<tr class="even">
<td align="left"><p>0,0,1</p></td>
<td align="left"><p>&#39;10&#39; (frame MC)</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>PMV[0][1]</p>
<p>-</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0,1,1</p></td>
<td align="left"><p>&#39;10&#39; (frame MC)</p></td>
<td align="left"><p>PMV[0][0]</p>
<p>-</p></td>
<td align="left"><p>PMV[0][1]</p>
<p>-</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
</tr>
<tr class="even">
<td align="left"><p>0,1,0</p></td>
<td align="left"><p>&#39;01&#39; (field MC)</p></td>
<td align="left"><p>PMV[0][0]</p>
<p>sel[0][0]</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>PMV[1][0]</p>
<p>sel[1][0]</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0,0,1</p></td>
<td align="left"><p>&#39;01&#39; (field MC)</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>PMV[0][1]</p>
<p>sel[0][1]</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>PMV[1][1]</p>
<p>sel[1][1]</p></td>
</tr>
<tr class="even">
<td align="left"><p>0,1,1</p></td>
<td align="left"><p>&#39;01&#39; (field MC)</p></td>
<td align="left"><p>PMV[0][0]</p>
<p>sel[0][0]</p></td>
<td align="left"><p>PMV[0][1]</p>
<p>sel[0][1]</p></td>
<td align="left"><p>PMV[1][0]</p>
<p>sel[1][0]</p></td>
<td align="left"><p>PMV[1][1]</p>
<p>sel[1][1]</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0,1,0</p></td>
<td align="left"><p>&#39;11&#39; (dual-prime)</p></td>
<td align="left"><p>PMV[0][0]</p>
<div>
 
</div>
<p>0 (top)</p></td>
<td align="left"><p>vector&#39;[2][0][0],</p>
<div>
 
</div>
vector&#39;[2][0][1]&lt;&lt;1
<p>1 (bottom)</p></td>
<td align="left"><p>PMV[0][0]</p>
<div>
 
</div>
<p>1</p></td>
<td align="left"><p>vector&#39;[3][0][0],</p>
<div>
 
</div>
vector&#39;[3][0][1]&lt;&lt;1
<p>0</p></td>
</tr>
</tbody>
</table>

 

### <span id="Field-Structured_Pictures"></span><span id="field-structured_pictures"></span><span id="FIELD-STRUCTURED_PICTURES"></span>Field-Structured Pictures

The following table shows the valid combinations of element settings for field-structured pictures (when the **bPicStructure** member of the [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) structure is equal to 1 or 2).

<table>
<colgroup>
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">IntraMacroblock, MotionForward, MotionBackward</th>
<th align="left">MotionType (meaning depends on picture type)</th>
<th align="left">MVector[0]MvertFieldSel_0 (1st, dir1)</th>
<th align="left">MVector[1]MvertFieldSel_1 (1st, dir2)</th>
<th align="left">MVector[2]MvertFieldSel_2 (2nd, dir1)</th>
<th align="left">MVector[3]MvertFieldSel_3(2nd, dir2)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1,0,0 (intra)</p></td>
<td align="left"><p>&#39;00&#39; (intra)</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
</tr>
<tr class="even">
<td align="left"><p>0,0,0 (no motion)</p></td>
<td align="left"><p>&#39;01&#39; (no motion)</p></td>
<td align="left"><p>0</p>
<p><em>PicCurrentField</em></p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0,1,0</p></td>
<td align="left"><p>&#39;01&#39; (field MC)</p></td>
<td align="left"><p>PMV[0][0]</p>
<p>sel[0][0]</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
</tr>
<tr class="even">
<td align="left"><p>0,0,1</p></td>
<td align="left"><p>&#39;01&#39; (field MC)</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>PMV[0][1]</p>
<p>sel[0][1]</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0,1,1</p></td>
<td align="left"><p>&#39;01&#39; (field MC)</p></td>
<td align="left"><p>PMV[0][0]</p>
<p>sel[0][0]</p></td>
<td align="left"><p>PMV[0][1]</p>
<p>sel[0][1]</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
</tr>
<tr class="even">
<td align="left"><p>0,1,0</p></td>
<td align="left"><p>&#39;10&#39; (16x8 MC)</p></td>
<td align="left"><p>PMV[0][0]</p>
<p>sel[0][0]</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>PMV[1][0]</p>
<p>sel[1][0]</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0,0,1</p></td>
<td align="left"><p>&#39;10&#39; (16x8 MC)</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>PMV[0][1]</p>
<p>sel[0][1]</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>PMV[1][1]</p>
<p>sel[1][1]</p></td>
</tr>
<tr class="even">
<td align="left"><p>0,1,1</p></td>
<td align="left"><p>&#39;10&#39; (16x8 MC)</p></td>
<td align="left"><p>PMV[0][0]</p>
<p>sel[0][0]</p></td>
<td align="left"><p>PMV[0][1]</p>
<p>sel[0][1]</p></td>
<td align="left"><p>PMV[1][0]</p>
<p>sel[1][0]</p></td>
<td align="left"><p>PMV[1][1]</p>
<p>sel[1][1]</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0,1,0</p></td>
<td align="left"><p>&#39;11&#39; (dual-prime)</p></td>
<td align="left"><p>PMV[0][0]</p>
<p><em>PicCurrentField</em></p></td>
<td align="left"><p>vector&#39;[2][0]</p>
<p><em>PicCurrentField</em></p></td>
<td align="left"><p>-</p>
<p>-</p></td>
<td align="left"><p>-</p>
<p>-</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Valid_Element_Settings_for_Field_and_Frame_Pictures"></span><span id="additional_valid_element_settings_for_field_and_frame_pictures"></span><span id="ADDITIONAL_VALID_ELEMENT_SETTINGS_FOR_FIELD_AND_FRAME_PICTURES"></span>Additional Valid Element Settings for Field and Frame Pictures

The remaining allowed cases for frame-structured and field-structured pictures are as follows.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Values</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>H261LoopFilter</em> = 1</p>
<p><strong>bPicOBMC</strong> = 0</p>
<p><em>Motion4MV</em> = 0</p></td>
<td align="left"><p>Indicates that one forward-motion vector is sent in <strong>MVector</strong>[0] and that the H.261 loop filter is active for the forward prediction in the macroblock.</p>
<p><em>MotionForward</em> must be 1 in this case, and <em>IntraMacroblock</em> and <em>MotionBackward</em> must both be zero.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>bPicOBMC</strong> = 0</p>
<p><em>Motion4MV</em> = 1</p></td>
<td align="left"><p>Indicates that four forward-motion vectors are sent in <strong>MVector</strong>[0] through <strong>MVector</strong>[3]. <em>MotionForward</em> must be 1 in this case, and <em>IntraMacroblock</em> must be zero.</p>
<p>If <em>MotionBackward</em> is 1, a fifth motion vector is sent for backward prediction in <strong>MVector</strong>[4].</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong><em>bPicOBMC</em></strong> = 1</p>
<p><em>Motion4MV</em> = 0</p></td>
<td align="left"><p>Indicates that 10 forward-motion vectors are sent in <strong>MVector</strong>[0] through <strong>MVector</strong>[9] for specification of OBMC motion, and that the values of the first four such motion vectors are all equal.</p>
<p>If <em>MotionBackward</em> is 1, an eleventh motion vector is sent for backward prediction in <strong>MVector</strong>[10].</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>bPicOBMC</strong> = 1</p>
<p><em>Motion4MV</em> = 1</p></td>
<td align="left"><p>Indicates that 10 forward-motion vectors are sent in <strong>MVector</strong>[0] through <strong>MVector</strong>[9] for specification of OBMC motion, and that the values of the first four such motion vectors may differ from each other.</p>
<p>If <em>MotionBackward</em> is 1, an eleventh motion vector is sent for backward prediction in <strong>MVector</strong>[10].</p></td>
</tr>
</tbody>
</table>

 

**Note**   The average operator is mathematically identical ((s1+s2+1)&gt;&gt;1) for MPEG-1, MPEG-2 half-sample prediction filtering, bidirectional averaging, and dual prime same-opposite parity combining. The H.263 bidirectional averaging operator does not add the offset of +1 prior to right-shifting. The **bBidirectionalAveragingMode** member of [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) determines which of these methods is used.

 

 

 





