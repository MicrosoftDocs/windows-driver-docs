---
title: DXVA_ConfigQueryOrReplyFlag and DXVA_ConfigQueryorReplyFunc Variables
description: DXVA_ConfigQueryOrReplyFlag and DXVA_ConfigQueryorReplyFunc Variables
ms.assetid: bfb1a98e-b9f0-4baa-b486-b2ff33a8bac5
keywords:
- video decoding WDK DirectX VA , formats
- decoding video WDK DirectX VA , formats
- picture decoding WDK DirectX VA , formats
- formats WDK DirectX VA
- bDXVA_Func variable WDK DirectX VA
- DXVA_ConfigQueryOrReplyFlag
- DXVA_ConfigQueryorReplyFunc
- video decoding WDK DirectX VA , configuration probing and locking
- decoding video WDK DirectX VA , configuration probing and locking
- picture decoding WDK DirectX VA , configuration probing and locking
- minimal interoperability configuration set WDK DirectX VA
- locking configurations WDK DirectX VA
- probing configurations WDK DirectX VA
- configuration probing and locking WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DXVA\_ConfigQueryOrReplyFlag and DXVA\_ConfigQueryorReplyFunc Variables


## <span id="ddk_dxva_configqueryorreplyflag_and_dxva_configqueryorreplyfunc_variab"></span><span id="DDK_DXVA_CONFIGQUERYORREPLYFLAG_AND_DXVA_CONFIGQUERYORREPLYFUNC_VARIAB"></span>


The *DXVA\_ConfigQueryOrReplyFlag* variable indicates the type of query or response when using probing and locking commands. The most significant 24 bits of the **dwFunction** member of the following structures contains the *DXVA\_ConfigQueryOrReplyFlag* variable.

[**DXVA\_ConfigPictureDecode**](https://msdn.microsoft.com/library/windows/hardware/ff563133) for compressed picture decoding.

[**DXVA\_ConfigAlphaLoad**](https://msdn.microsoft.com/library/windows/hardware/ff563129) for alpha-blending data loading.

[**DXVA\_ConfigAlphaCombine**](https://msdn.microsoft.com/library/windows/hardware/ff563126) for alpha-blending combination.

The most significant 20 bits of the *DXVA\_ConfigQueryOrReplyFlag* variable specify the following queries and responses.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0xFFFF1</p></td>
<td align="left"><p>Sent by the host decoder as a probing command.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xFFFF5</p></td>
<td align="left"><p>Sent by the host decoder as a locking command.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xFFFF8</p></td>
<td align="left"><p>Sent by the accelerator with an S_OK response to a probing command, with a copy of the probed configuration.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xFFFF9</p></td>
<td align="left"><p>Sent by the accelerator with an S_OK response to a probing command, with a suggested alternative configuration.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xFFFFC</p></td>
<td align="left"><p>Sent by the accelerator with an S_OK response to a locking command, with a copy of the locked configuration.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xFFFFB</p></td>
<td align="left"><p>Sent by the accelerator with an S_FALSE response to a probing command, with a suggested alternative configuration.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xFFFFF</p></td>
<td align="left"><p>Sent by the accelerator with an S_FALSE response to a locking command, with a suggested alternative configuration.</p></td>
</tr>
</tbody>
</table>

 

The least significant 4 bits of the *DXVA\_ConfigQueryOrReplyFlag* variable specify the following status indicators for queries and responses.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Bit</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>This is zero when sent by the host decoder, and 1 when sent by the accelerator.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>This is zero when associated with a probe, and 1 when associated with a lock.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>This is zero for success, and 1 for failure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0</p></td>
<td align="left"><p>This is zero when it is a duplicate configuration structure, and 1 when it is a new configuration structure.</p></td>
</tr>
</tbody>
</table>

 

The least significant 8 bits of the **dwFunction** member is the is the *bDXVA\_Func* variable. The *bDXVA\_Func* variable, when used with *DXVA\_ConfigQueryorReplyFunc*, indicates probing and locking operations and specifies an associated configuration function.

### <span id="Probing_and_Locking"></span><span id="probing_and_locking"></span><span id="PROBING_AND_LOCKING"></span>Probing and Locking

When *bDXVA\_Func* is used to probe and lock a configuration for a specific DirectX VA function, *bDXVA\_Func* is placed in the 8 least significant bits of the *DXVA*\_*ConfigQueryorReplyFunc* variable. *DXVA*\_*ConfigQueryorReplyFunc* is conveyed to the accelerator as specified in the Microsoft Windows SDK.

### <span id="Specifying_a_Configuration_To_Be_Probed_or_Locked"></span><span id="specifying_a_configuration_to_be_probed_or_locked"></span><span id="SPECIFYING_A_CONFIGURATION_TO_BE_PROBED_OR_LOCKED"></span>Specifying a Configuration To Be Probed or Locked

When *bDXVA\_Func* is used to specify the function associated with a configuration structure that is passed with a probe or lock command, *bDXVA\_Func* is placed in the 8 least significant bits of the *DXVA\_ConfigQueryorReplyFunc* variable in the **dwFunction** member of one of the following configuration structures:

[**DXVA\_ConfigPictureDecode**](https://msdn.microsoft.com/library/windows/hardware/ff563133) for compressed picture decoding.

[**DXVA\_ConfigAlphaLoad**](https://msdn.microsoft.com/library/windows/hardware/ff563129) for alpha-blending data loading.

[**DXVA\_ConfigAlphaCombine**](https://msdn.microsoft.com/library/windows/hardware/ff563126) for alpha-blending combination.

### <span id="DXVA_EncryptProtocolFunc"></span><span id="dxva_encryptprotocolfunc"></span><span id="DXVA_ENCRYPTPROTOCOLFUNC"></span>DXVA\_EncryptProtocolFunc

The most significant 24 bits of the *DXVA\_EncryptProtocolFunc* DWORD variable are set as follows:

-   0xFFFF00 when sent by the host software decoder in the **dwFunction** member of the [**DD\_RENDERMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551693) structure in a call to [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248).

-   0xFFFF08 when sent by the video accelerator in the **dwFunction** member of the [**DXVA\_EncryptProtocolHeader**](https://msdn.microsoft.com/library/windows/hardware/ff563965) structure.

The least significant 8 bits of the *DXVA\_EncryptProtocolFunc* DWORD variable contain the value of *bDXVA\_Func* associated with the encryption protocol. The only value supported for this use is *bDXVA\_Func* = 1 (compressed picture decoding).

### <span id="Specifying_an_Operation_to_be_Performed_by_DdMoCompRender"></span><span id="specifying_an_operation_to_be_performed_by_ddmocomprender"></span><span id="SPECIFYING_AN_OPERATION_TO_BE_PERFORMED_BY_DDMOCOMPRENDER"></span>Specifying an Operation to be Performed by DdMoCompRender

When *bDXVA\_Func* is used to signal an actual operation to be performed (compressed picture decoding, alpha-blend data loading, alpha-blend combination, or picture resampling), *bDXVA\_Func* is conveyed to the accelerator by inclusion in a series of *bDXVA\_Func* byte values in the **dwFunction** member of a [**DD\_RENDERMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551693) structure in a call to [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248). The first *bDXVA\_Func* operation is specified in the most significant byte, the next operation is specified in the next most significant byte, and so on. Any remaining bytes of **dwFunction** are set to zero.

 

 





