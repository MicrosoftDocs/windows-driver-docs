---
title: KSMETHOD\_BDA\_CHECK\_CHANGES
description: Clients use KSMETHOD\_BDA\_CHECK\_CHANGES to determine whether a list of requested changes will work.
ms.assetid: 00a2d0ca-0ede-4ae5-ab2a-95d19143ea7c
keywords: ["KSMETHOD_BDA_CHECK_CHANGES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSMETHOD_BDA_CHECK_CHANGES
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSMETHOD\_BDA\_CHECK\_CHANGES


Clients use KSMETHOD\_BDA\_CHECK\_CHANGES to determine whether a list of requested changes will work.

## <span id="ddk_ksmethod_bda_check_changes_ks"></span><span id="DDK_KSMETHOD_BDA_CHECK_CHANGES_KS"></span>


### <span id="Specifying_This_Method"></span><span id="specifying_this_method"></span><span id="SPECIFYING_THIS_METHOD"></span>Specifying This Method

KSMETHOD with **Flags** member set to KSMETHOD\_TYPE\_NONE.

### <span id="Method_Data"></span><span id="method_data"></span><span id="METHOD_DATA"></span>Method Data

None

Remarks
-------

Before committing a list of changes, the network provider makes a KSMETHOD\_BDA\_CHECK\_CHANGES request to determine whether the requested changes will work. The minidriver may reserve resources when this request is made, to guarantee that the resources are available.

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


[**BdaCheckChanges**](https://msdn.microsoft.com/library/windows/hardware/ff556433)

[**KSMETHOD**](https://msdn.microsoft.com/library/windows/hardware/ff563398)

 

 






