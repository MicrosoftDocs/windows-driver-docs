---
title: Macroblock Control Commands
description: Macroblock Control Commands
ms.assetid: be70ec8f-1821-4075-b5e3-b7574fbe4e27
keywords:
- macroblocks WDK DirectX VA , commands
- DXVA_MBctrl_I_HostResidDiff_1
- DXVA_MBctrl_I_OffHostIDCT_1
- DXVA_MBctrl_P_HostResidDiff_1
- DXVA_MBctrl_P_OffHostIDCT_1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Macroblock Control Commands


## <span id="ddk_macroblock_control_commands_gg"></span><span id="DDK_MACROBLOCK_CONTROL_COMMANDS_GG"></span>


The generation of each decoded macroblock during compressed picture decoding is governed by a macroblock control command structure. There are four macroblock control command structures defined in the *dxva.h* header file:

[**DXVA\_MBctrl\_I\_HostResidDiff\_1**](https://msdn.microsoft.com/library/windows/hardware/ff563983)

[**DXVA\_MBctrl\_I\_OffHostIDCT\_1**](https://msdn.microsoft.com/library/windows/hardware/ff563989)

[**DXVA\_MBctrl\_P\_HostResidDiff\_1**](https://msdn.microsoft.com/library/windows/hardware/ff563993)

[**DXVA\_MBctrl\_P\_OffHostIDCT\_1**](https://msdn.microsoft.com/library/windows/hardware/ff563997)

The structures explicitly defined in *dxva.h* are special cases of a generic design used for macroblock control commands in DirectX VA. For a description of this generic design, see [Generic Form of Macroblock Control Command Structures](generic-form-of-macroblock-control-command-structures.md).

The selection of which macroblock control command structure to use is based on the type of picture to be decoded and on how it will be decoded. The following structure members and flags determine picture type, decoding options, and which of the four DirectX VA macroblock control structures will be used:

-   The **bPicIntra**, **bChromaFormat**, **bPicOBMC**, **bPicBinPB**, **bPic4MVallowed** and **bMV\_RPS** members of the [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) structure.

-   The **bConfigResidDiffHost** member of the [**DXVA\_ConfigPictureDecode**](https://msdn.microsoft.com/library/windows/hardware/ff563133) structure.

-   The *HostResidDiff* flag (bit 10 in the **wMBtype** member of each macroblock control structure).

The values for these structure members and flags are shown in the following sections.

### <span id="DXVA_MBctrl_I_HostResidDiff_1"></span><span id="dxva_mbctrl_i_hostresiddiff_1"></span><span id="DXVA_MBCTRL_I_HOSTRESIDDIFF_1"></span>DXVA\_MBctrl\_I\_HostResidDiff\_1

The [**DXVA\_MBctrl\_I\_HostResidDiff\_1**](https://msdn.microsoft.com/library/windows/hardware/ff563983) structure is used for intra pictures with host-based [*residual difference decoding*](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-residual-difference-decoding). The following structure members and flags must equal the indicated values:

-   **bPicIntra** must equal 1 (intra pictures).

-   **bChromaFormat** must equal 1 (4:2:0 sampling).

-   *HostResidDiff* must equal 1 (host-based IDCT).

-   **bConfigResidDiffHost** must equal 1 (host-based residual difference decoding).

### <span id="DXVA_MBctrl_I_OffHostIDCT_1"></span><span id="dxva_mbctrl_i_offhostidct_1"></span><span id="DXVA_MBCTRL_I_OFFHOSTIDCT_1"></span>DXVA\_MBctrl\_I\_OffHostIDCT\_1

The [**DXVA\_MBctrl\_I\_OffHostIDCT\_1**](https://msdn.microsoft.com/library/windows/hardware/ff563989) structure is used for intra pictures with 4:2:0 sampling with off-host residual difference decoding. The following structure members and flags must equal the indicated values:

-   **bPicIntra** must equal 1 (intra pictures).

-   **bChromaFormat** must equal 1 (4:2:0 sampling).

-   *HostResidDiff* must equal zero (off-host IDCT).

-   **bConfigResidDiffHost** must equal zero (off-host residual difference decoding).

### <span id="DXVA_MBctrl_P_HostResidDiff_1"></span><span id="dxva_mbctrl_p_hostresiddiff_1"></span><span id="DXVA_MBCTRL_P_HOSTRESIDDIFF_1"></span>DXVA\_MBctrl\_P\_HostResidDiff\_1

The [**DXVA\_MBctrl\_P\_HostResidDiff\_1**](https://msdn.microsoft.com/library/windows/hardware/ff563993) structure is used for P and B pictures with host-based residual difference decoding. The following macroblock control processes are not used: OBMC, use of four motion vectors per macroblock for the B part of a PB picture, and use of motion vector reference picture selection.

The following structure members and flags must equal the indicated values:

-   **bPicIntra** must equal zero (decoding for [*P picture*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-predictive-coded-picture--p-picture-) and [*B picture*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-b-picture) or concealment motion vectors in [*I picture*](https://msdn.microsoft.com/library/windows/hardware/ff556290#wdkgloss-i-picture)).

-   **bChromaFormat** must equal 1 (4:2:0 sampling).

-   *HostResidDiff* must equal 1 (host-based IDCT).

-   **bPicOBMC** must equal zero (OBMC not used).

-   **bMV\_RPS** must equal zero (motion vector reference picture selection not used).

-   At least one of **bPicBinPB** (B-picture in PB-frame motion compensation not used) and **bPic4MVallowed** (four forward-reference motion vectors per macroblock not used) must equal zero.

-   **bConfigResidDiffHost** must equal 1 (host-based residual difference decoding).

### <span id="DXVA_MBctrl_P_OffHostIDCT_1"></span><span id="dxva_mbctrl_p_offhostidct_1"></span><span id="DXVA_MBCTRL_P_OFFHOSTIDCT_1"></span>DXVA\_MBctrl\_P\_OffHostIDCT\_1

The [**DXVA\_MBctrl\_P\_OffHostIDCT\_1**](https://msdn.microsoft.com/library/windows/hardware/ff563997) structure is used for P and B pictures with 4:2:0 sampling with off-host residual difference decoding. The following macroblock control processes are not used: OBMC, use of four motion vectors per macroblock for the B part of a PB picture, and use of motion vector reference picture selection.

The following structure members and flags must equal the indicated values:

-   **bPicIntra** member of the [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) structure must equal zero (decoding for P and [*B pictures*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-b-picture) or concealment motion vectors in [*I pictures*](https://msdn.microsoft.com/library/windows/hardware/ff556290#wdkgloss-i-picture)).

-   **bChromaFormat** must equal 1 (4:2:0 sampling).

-   *HostResidDiff* must equal zero (off-host IDCT).

-   **bPicOBMC** must equal zero (OBMC not used).

-   **bMV\_RPS** must equal zero (motion vector reference picture selection not used).

-   At least one of **bPicBinPB** (B-picture in PB-frame motion compensation not used) and **bPic4MVallowed** (four forward-reference motion vectors per macroblock not used) must equal zero.

-   **bConfigResidDiffHost** must equal zero (off-host residual difference decoding).

 

 





