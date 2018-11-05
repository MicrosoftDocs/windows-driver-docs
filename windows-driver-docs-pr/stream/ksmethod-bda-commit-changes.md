---
title: KSMETHOD\_BDA\_COMMIT\_CHANGES
description: Clients use KSMETHOD\_BDA\_COMMIT\_CHANGES to commit a list of requested changes.
ms.assetid: f6572a4e-2328-4157-80f7-110e0fe58a4f
keywords: ["KSMETHOD_BDA_COMMIT_CHANGES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSMETHOD_BDA_COMMIT_CHANGES
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSMETHOD\_BDA\_COMMIT\_CHANGES


Clients use KSMETHOD\_BDA\_COMMIT\_CHANGES to commit a list of requested changes.

## <span id="ddk_ksmethod_bda_commit_changes_ks"></span><span id="DDK_KSMETHOD_BDA_COMMIT_CHANGES_KS"></span>


### <span id="Specifying_This_Method"></span><span id="specifying_this_method"></span><span id="SPECIFYING_THIS_METHOD"></span>Specifying This Method

KSMETHOD with **Flags** member set to KSMETHOD\_TYPE\_NONE.

### <span id="Method_Data"></span><span id="method_data"></span><span id="METHOD_DATA"></span>Method Data

None

Remarks
-------

When the network provider makes a KSMETHOD\_BDA\_COMMIT\_CHANGES request, the list of changes are committed on the underlying filter, at which point the filter resets its state and a new cycle can begin.

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


[**BdaCommitChanges**](https://msdn.microsoft.com/library/windows/hardware/ff556435)

[**KSMETHOD**](https://msdn.microsoft.com/library/windows/hardware/ff563398)

 

 






