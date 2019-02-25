---
title: KSMETHOD\_BDA\_CREATE\_TOPOLOGY
description: Clients use KSMETHOD\_BDA\_CREATE\_TOPOLOGY to create a topology structure in Ring 3 that reflects the known connections in a filter.
ms.assetid: 3f34c7cc-d711-478b-a017-ad2c46545a9b
keywords: ["KSMETHOD_BDA_CREATE_TOPOLOGY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSMETHOD_BDA_CREATE_TOPOLOGY
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSMETHOD\_BDA\_CREATE\_TOPOLOGY


Clients use KSMETHOD\_BDA\_CREATE\_TOPOLOGY to create a topology structure in Ring 3 that reflects the known connections in a filter.

## <span id="ddk_ksmethod_bda_create_topology_ks"></span><span id="DDK_KSMETHOD_BDA_CREATE_TOPOLOGY_KS"></span>


### <span id="Specifying_This_Method"></span><span id="specifying_this_method"></span><span id="SPECIFYING_THIS_METHOD"></span>Specifying This Method

KSMETHOD with the **Flags** member set to KSMETHOD\_TYPE\_WRITE.

### <span id="Method_Data"></span><span id="method_data"></span><span id="METHOD_DATA"></span>Method Data

A KSMULTIPLE\_ITEM structure, which is the header for a list of topology information.

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


[**BdaMethodCreateTopology**](https://msdn.microsoft.com/library/windows/hardware/ff556471)

[**KSMETHOD**](https://msdn.microsoft.com/library/windows/hardware/ff563398)

[**KSMULTIPLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff563441)

 

 






