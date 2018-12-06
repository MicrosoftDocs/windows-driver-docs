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
ms.date: 11/28/2017
ms.localizationpriority: medium
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

## See also


[**BDA\_CHANGE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff556518)

[**BdaGetChangeState**](https://msdn.microsoft.com/library/windows/hardware/ff556458)

[**KSMETHOD**](https://msdn.microsoft.com/library/windows/hardware/ff563398)

 

 






