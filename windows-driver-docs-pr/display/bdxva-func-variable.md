---
title: bDXVA_Func Variable
description: bDXVA_Func Variable
keywords:
- video decoding WDK DirectX VA , formats
- decoding video WDK DirectX VA , formats
- picture decoding WDK DirectX VA , formats
- formats WDK DirectX VA
- bDXVA_Func variable WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# bDXVA\_Func Variable


## <span id="ddk_bdxva_func_variable_gg"></span><span id="DDK_BDXVA_FUNC_VARIABLE_GG"></span>


The **bDXVA\_Func** variable is an 8-bit value that is associated with DirectX VA operations as follows.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">bDXVA_Func Value</th>
<th align="left">Operation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>Compressed picture decoding</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Alpha-blend data loading</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Alpha-blend combination</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Picture resampling</p></td>
</tr>
</tbody>
</table>

 

The **bDXVA\_Func** variable is used to perform the following tasks:

-   Probe and lock a configuration for a specific DirectX VA function. This is done by including **bDXVA\_Func** in a **DXVA\_ConfigQueryOrReplyFlag** variable and in a **DXVA\_ConfigQueryOrReplyFlag** variable when these variables are sent in the **dwFunction** member of a [**DD\_RENDERMOCOMPDATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_rendermocompdata) structure in a call to [*DdMoCompRender*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_mocompcb_render).

-   Specify the function associated with a configuration structure passed with a probe or lock command by inclusion with a **DXVA\_ConfigQueryOrReplyFlag** variable in a **DXVA\_ConfigQueryOrReplyFlag** variable sent in the **dwFunction** member of the following structures:
    [**DXVA\_ConfigPictureDecode**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_configpicturedecode) for compressed picture decoding
    [**DXVA\_ConfigAlphaLoad**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_configalphaload) for alpha-blending data loading
    [**DXVA\_ConfigAlphaCombine**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_configalphacombine) for alpha-blending combination
-   Initialize an encryption protocol for a specific DirectX VA function by inclusion in a **DXVA\_EncryptProtocolFunc** variable sent in the **dwFunction** member of a [**DD\_RENDERMOCOMPDATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_rendermocompdata) structure in a call to [*DdMoCompRender*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_mocompcb_render).

-   Specify the function associated with an encryption protocol by inclusion in the **dwFunction** member of the [**DXVA\_EncryptProtocolHeader**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_encryptprotocolheader) structure.

-   Signal an operation to be performed by inclusion in a series of **bDXVA\_Func** byte values in the **dwFunction** member of a [**DD\_RENDERMOCOMPDATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_rendermocompdata) structure in a call to [*DdMoCompRender*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_mocompcb_render). The first **bDXVA\_Func** operation is specified in the most significant byte, the next operation is specified in the next most significant byte, and so on. Remaining bytes in **dwFunction** not used to signal an operation are set to zero.

 

