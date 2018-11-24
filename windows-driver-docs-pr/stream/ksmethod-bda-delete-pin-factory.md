---
title: KSMETHOD\_BDA\_DELETE\_PIN\_FACTORY
description: Clients use KSMETHOD\_BDA\_DELETE\_PIN\_FACTORY to delete a pin factory for a filter.
ms.assetid: b9e9306a-5b0e-47d0-9194-eb60d793bebc
keywords: ["KSMETHOD_BDA_DELETE_PIN_FACTORY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSMETHOD_BDA_DELETE_PIN_FACTORY
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSMETHOD\_BDA\_DELETE\_PIN\_FACTORY


Clients use KSMETHOD\_BDA\_DELETE\_PIN\_FACTORY to delete a pin factory for a filter.

## <span id="ddk_ksmethod_bda_delete_pin_factory_ks"></span><span id="DDK_KSMETHOD_BDA_DELETE_PIN_FACTORY_KS"></span>


### <span id="Specifying_This_Method"></span><span id="specifying_this_method"></span><span id="SPECIFYING_THIS_METHOD"></span>Specifying This Method

KSM\_PIN with the **Flags** member of the **Method** member set to KSMETHOD\_TYPE\_NONE.

### <span id="Method_Data"></span><span id="method_data"></span><span id="METHOD_DATA"></span>Method Data

None

Remarks
-------

Specifies the pin factory to delete in the **PinId** member of the KSM\_PIN structure.

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


[**BdaMethodDeletePin**](https://msdn.microsoft.com/library/windows/hardware/ff556474)

[**KSM\_PIN**](https://msdn.microsoft.com/library/windows/hardware/ff563453)

 

 






