---
title: MPEG2_A
description: MPEG2_A
keywords:
- MPEG2_A restricted profile WDK DirectX VA
ms.date: 04/20/2017
---

# MPEG2\_A


## <span id="ddk_mpeg2_a_gg"></span><span id="DDK_MPEG2_A_GG"></span>


The MPEG2\_A restricted profile contains a set of features required for support of MPEG-2 video Main Profile. Support of this profile is required for video accelerator drivers that provide hardware video acceleration capabilities.

The MPEG2\_A profile is defined by the following sets of restrictions:

### <span id="Restrictions_on_DXVA_ConnectMode"></span><span id="restrictions_on_dxva_connectmode"></span><span id="RESTRICTIONS_ON_DXVA_CONNECTMODE"></span>Restrictions on DXVA\_ConnectMode

The following restriction on the [**DXVA\_ConnectMode**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_connectmode) structure applies when the *bDXVA\_Func* variable defined in the **dwFunction** member of the [**DXVA\_ConfigPictureDecode**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_configpicturedecode) structure is equal to 1.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Structure Member</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>wRestrictedMode</strong></p></td>
<td align="left"><p>DXVA_RESTRICTED_MODE_MPEG2_A</p></td>
</tr>
</tbody>
</table>

 

### <span id="Restrictions_on_DXVA_PictureParameters"></span><span id="restrictions_on_dxva_pictureparameters"></span><span id="RESTRICTIONS_ON_DXVA_PICTUREPARAMETERS"></span>Restrictions on DXVA\_PictureParameters

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Structure Member</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>wRestrictedMode</strong></p></td>
<td align="left"><p>0x0A</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>BPP</em> variable (defined by adding 1 to <strong>bBPPminus1)</strong></p></td>
<td align="left"><p>8</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>MacroblockWidthMinus1</strong></p></td>
<td align="left"><p>15</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>MacroblockHeightMinus1</strong></p></td>
<td align="left"><p>15</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>bBlockWidthMinus1</strong></p></td>
<td align="left"><p>7</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>bBlockHeightMinus1</strong></p></td>
<td align="left"><p>7</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>bChromaFormat</strong> (4:2:0)</p></td>
<td align="left"><p>1</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>bRcontrol</strong></p></td>
<td align="left"><p>Zero</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>bBidirectionalAveragingMode</strong></p></td>
<td align="left"><p>Zero (MPEG-2 bidirectional averaging)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>bMVprecisionAndChromaRelation</strong></p></td>
<td align="left"><p>Zero (MPEG-2 half-sample motion)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>bPicExtrapolation</strong></p></td>
<td align="left"><p>Zero</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>bPicDeblocked</strong></p></td>
<td align="left"><p>Zero</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>bPic4MVallowed</strong></p></td>
<td align="left"><p>Zero</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>bPicOBMC</strong></p></td>
<td align="left"><p>Zero</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>bMV_RPS</strong></p></td>
<td align="left"><p>Zero</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>SpecificIDCT</strong></p></td>
<td align="left"><p>Zero</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>bPicScanFixed</strong></p></td>
<td align="left"><p>1</p></td>
</tr>
</tbody>
</table>

 

### <span id="Restrictions_on_DXVA_MBctrl_I_HostResidDiff_1__DXVA_MBctrl_I_OffHostIDCT_1__DXVA_MBctrl_P_HostResidDiff_1__and_DXVA_MBctrl_P_OffHostIDCT_1"></span><span id="restrictions_on_dxva_mbctrl_i_hostresiddiff_1__dxva_mbctrl_i_offhostidct_1__dxva_mbctrl_p_hostresiddiff_1__and_dxva_mbctrl_p_offhostidct_1"></span><span id="RESTRICTIONS_ON_DXVA_MBCTRL_I_HOSTRESIDDIFF_1__DXVA_MBCTRL_I_OFFHOSTIDCT_1__DXVA_MBCTRL_P_HOSTRESIDDIFF_1__AND_DXVA_MBCTRL_P_OFFHOSTIDCT_1"></span>Restrictions on DXVA\_MBctrl\_I\_HostResidDiff\_1, DXVA\_MBctrl\_I\_OffHostIDCT\_1, DXVA\_MBctrl\_P\_HostResidDiff\_1, and DXVA\_MBctrl\_P\_OffHostIDCT\_1

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">wMBtype Bits</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>MBscanMethod</em></p></td>
<td align="left"><p>May be a value of zero (zigzag) or a value of 1 (alternate vertical) if the <strong>ConfigHostInverseScan</strong> member of <a href="/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_configpicturedecode" data-raw-source="[&lt;strong&gt;DXVA_ConfigPictureDecode&lt;/strong&gt;](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_configpicturedecode)"><strong>DXVA_ConfigPictureDecode</strong></a> is equal to zero.</p></td>
</tr>
<tr class="even">
<td align="left"><p>H261LoopFilter</p></td>
<td align="left"><p>Zero</p></td>
</tr>
</tbody>
</table>

 

### <span id="Restrictions_on_Bitstream_Buffers"></span><span id="restrictions_on_bitstream_buffers"></span><span id="RESTRICTIONS_ON_BITSTREAM_BUFFERS"></span>Restrictions on Bitstream Buffers

The contents of any bitstream buffer must contain data in the MPEG-2 main profile video format.

The **bNewQmatrix** member of [**DXVA\_QmatrixData**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_qmatrixdata) equals zero, for i = 2 and 3 when inverse-quantization matrices are used.

