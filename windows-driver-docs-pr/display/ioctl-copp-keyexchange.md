---
title: IOCTL\_COPP\_KeyExchange control code
description: Returns the digital certificate used by the graphics hardware.
ms.assetid: edb0d4db-cf7e-4e13-a25b-8fce0e9f2ec0
keywords: ["IOCTL_COPP_KeyExchange control code Display Devices"]
topic_type:
- apiref
api_name:
- IOCTL_COPP_KeyExchange
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# IOCTL\_COPP\_KeyExchange control code


Returns the digital certificate used by the graphics hardware.

## <span id="ddk_ioctl_copp_keyexchange_gg"></span><span id="DDK_IOCTL_COPP_KEYEXCHANGE_GG"></span>


### <span id="Input_Parameters"></span><span id="input_parameters"></span><span id="INPUT_PARAMETERS"></span>Input Parameters

The [**VIDEO\_REQUEST\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff570547) (VRP) **InputBuffer** contains information passed from the display driver. For example, the display driver can pass a pointer to a COPP\_IO\_InputBuffer structure defined as follows:

```
typedef struct {
    PVOID* ppThis;
    PVOID InputBuffer;
    HRESULT phr;
} COPP_IO_InputBuffer;
```

The **ppThis** member points to a pointer to the COPP DirectX VA device object that is used to retrieve the hardware digital certificate. The **InputBuffer** member is not required. The **phr** member should be set to the value returned from the [*COPPKeyExchange*](https://msdn.microsoft.com/library/windows/hardware/ff539646) function.

### <span id="Output_Parameters"></span><span id="output_parameters"></span><span id="OUTPUT_PARAMETERS"></span>Output Parameters

The miniport driver returns an array of bytes in the VRP **OutputBuffer**. The array contains the digital certificate.

### <span id="I_O_Status_Block"></span><span id="i_o_status_block"></span><span id="I_O_STATUS_BLOCK"></span>I/O Status Block

The miniport driver sets the **Information** member of the [**STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff569732) structure to the value in the **OutputBufferLength** member of the VRP.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.</p></td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[*COPPKeyExchange*](https://msdn.microsoft.com/library/windows/hardware/ff539646)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20IOCTL_COPP_KeyExchange%20control%20code%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





