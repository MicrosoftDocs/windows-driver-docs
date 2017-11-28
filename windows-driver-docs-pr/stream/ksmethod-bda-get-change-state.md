---
title: KSMETHOD\_BDA\_GET\_CHANGE\_STATE
description: Clients use KSMETHOD\_BDA\_GET\_CHANGE\_STATE to determine the current change state for a filter.
ms.assetid: bb635b88-6d51-4d0c-9134-2fc6287a4146
keywords: ["KSMETHOD_BDA_GET_CHANGE_STATE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSMETHOD_BDA_GET_CHANGE_STATE
api_location:
- Bdamedia.h
api_type:
- HeaderDef
---

# KSMETHOD\_BDA\_GET\_CHANGE\_STATE


Clients use KSMETHOD\_BDA\_GET\_CHANGE\_STATE to determine the current change state for a filter.

## <span id="ddk_ksmethod_bda_get_change_state_ks"></span><span id="DDK_KSMETHOD_BDA_GET_CHANGE_STATE_KS"></span>


### <span id="Specifying_This_Method"></span><span id="specifying_this_method"></span><span id="SPECIFYING_THIS_METHOD"></span>Specifying This Method

KSMETHOD with **Flags** member set to KSMETHOD\_TYPE\_READ.

### <span id="Method_Data"></span><span id="method_data"></span><span id="METHOD_DATA"></span>Method Data

Value from the BDA\_CHANGE\_STATE enumerated type that identifies the current change state for the filter.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Bdamedia.h (include Bdamedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**BDA\_CHANGE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff556518)

[**BdaGetChangeState**](https://msdn.microsoft.com/library/windows/hardware/ff556458)

[**KSMETHOD**](https://msdn.microsoft.com/library/windows/hardware/ff563398)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSMETHOD_BDA_GET_CHANGE_STATE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





