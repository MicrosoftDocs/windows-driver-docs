---
title: KSMETHOD\_BDA\_START\_CHANGES
description: Clients use KSMETHOD\_BDA\_START\_CHANGES to reset a change list.
ms.assetid: 657fb89d-f216-4352-87d8-3d2d933cc8a5
keywords: ["KSMETHOD_BDA_START_CHANGES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSMETHOD_BDA_START_CHANGES
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSMETHOD\_BDA\_START\_CHANGES


Clients use KSMETHOD\_BDA\_START\_CHANGES to reset a change list.

## <span id="ddk_ksmethod_bda_start_changes_ks"></span><span id="DDK_KSMETHOD_BDA_START_CHANGES_KS"></span>


### <span id="Specifying_This_Method"></span><span id="specifying_this_method"></span><span id="SPECIFYING_THIS_METHOD"></span>Specifying This Method

KSMETHOD with **Flags** member set to KSMETHOD\_TYPE\_NONE.

### <span id="Method_Data"></span><span id="method_data"></span><span id="METHOD_DATA"></span>Method Data

None

Remarks
-------

Before the network provider begins to make changes, it makes a KSMETHOD\_BDA\_START\_CHANGES request, which causes any existing change list that has not been committed to be discarded and informs the filter's pins and nodes to start keeping track of a new set of changes. The network provider then calls the necessary interface methods on the filter or its pins, but the methods are not actually called yet. If at any point the network provider determines that the changes will not work, it can call this method to clear out the list.

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


[**BdaStartChanges**](https://msdn.microsoft.com/library/windows/hardware/ff556507)

[**KSMETHOD**](https://msdn.microsoft.com/library/windows/hardware/ff563398)

 

 






