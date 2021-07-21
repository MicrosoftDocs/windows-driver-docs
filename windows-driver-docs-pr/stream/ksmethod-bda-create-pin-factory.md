---
title: KSMETHOD\_BDA\_CREATE\_PIN\_FACTORY
description: Clients use KSMETHOD\_BDA\_CREATE\_PIN\_FACTORY to create a pin factory for a filter.
keywords: ["KSMETHOD_BDA_CREATE_PIN_FACTORY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSMETHOD_BDA_CREATE_PIN_FACTORY
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSMETHOD\_BDA\_CREATE\_PIN\_FACTORY


Clients use KSMETHOD\_BDA\_CREATE\_PIN\_FACTORY to create a pin factory for a filter.

## <span id="ddk_ksmethod_bda_create_pin_factory_ks"></span><span id="DDK_KSMETHOD_BDA_CREATE_PIN_FACTORY_KS"></span>


### <span id="Specifying_This_Method"></span><span id="specifying_this_method"></span><span id="SPECIFYING_THIS_METHOD"></span>Specifying This Method

KSM\_PIN with the **Flags** member of the **Method** member set to KSMETHOD\_TYPE\_READ.

### <span id="Method_Data"></span><span id="method_data"></span><span id="METHOD_DATA"></span>Method Data

ULONG, representing the identifier of the pin factory.

## Requirements

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


[**BdaMethodCreatePin**](/windows-hardware/drivers/ddi/bdasup/nf-bdasup-bdamethodcreatepin)

[**KSM\_PIN**](/windows-hardware/drivers/ddi/bdasup/ns-bdasup-_ksm_pin)

 

