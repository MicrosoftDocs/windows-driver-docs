---
title: bDXVA\_Func Variable
description: bDXVA\_Func Variable
ms.assetid: 6db9fa71-7bc2-4eb6-afcb-b16df48f7e8b
keywords:
- video decoding WDK DirectX VA , formats
- decoding video WDK DirectX VA , formats
- picture decoding WDK DirectX VA , formats
- formats WDK DirectX VA
- bDXVA_Func variable WDK DirectX VA
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

-   Probe and lock a configuration for a specific DirectX VA function. This is done by including **bDXVA\_Func** in a **DXVA\_ConfigQueryOrReplyFlag** variable and in a **DXVA\_ConfigQueryOrReplyFlag** variable when these variables are sent in the **dwFunction** member of a [**DD\_RENDERMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551693) structure in a call to [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248).

-   Specify the function associated with a configuration structure passed with a probe or lock command by inclusion with a **DXVA\_ConfigQueryOrReplyFlag** variable in a **DXVA\_ConfigQueryOrReplyFlag** variable sent in the **dwFunction** member of the following structures:
    [**DXVA\_ConfigPictureDecode**](https://msdn.microsoft.com/library/windows/hardware/ff563133) for compressed picture decoding
    [**DXVA\_ConfigAlphaLoad**](https://msdn.microsoft.com/library/windows/hardware/ff563129) for alpha-blending data loading
    [**DXVA\_ConfigAlphaCombine**](https://msdn.microsoft.com/library/windows/hardware/ff563126) for alpha-blending combination
-   Initialize an encryption protocol for a specific DirectX VA function by inclusion in a **DXVA\_EncryptProtocolFunc** variable sent in the **dwFunction** member of a [**DD\_RENDERMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551693) structure in a call to [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248).

-   Specify the function associated with an encryption protocol by inclusion in the **dwFunction** member of the [**DXVA\_EncryptProtocolHeader**](https://msdn.microsoft.com/library/windows/hardware/ff563965) structure.

-   Signal an operation to be performed by inclusion in a series of **bDXVA\_Func** byte values in the **dwFunction** member of a [**DD\_RENDERMOCOMPDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551693) structure in a call to [*DdMoCompRender*](https://msdn.microsoft.com/library/windows/hardware/ff550248). The first **bDXVA\_Func** operation is specified in the most significant byte, the next operation is specified in the next most significant byte, and so on. Remaining bytes in **dwFunction** not used to signal an operation are set to zero.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20bDXVA_Func%20Variable%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




