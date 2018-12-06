---
title: AVC\_FUNCTION\_PEER\_DO\_LIST
description: AVC\_FUNCTION\_PEER\_DO\_LIST
ms.assetid: 80ffd94e-788f-4874-b716-3eb66d90e4aa
keywords: ["AVC_FUNCTION_PEER_DO_LIST Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVC_FUNCTION_PEER_DO_LIST
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# AVC\_FUNCTION\_PEER\_DO\_LIST


## <span id="ddk_avc_function_peer_do_list_ks"></span><span id="DDK_AVC_FUNCTION_PEER_DO_LIST_KS"></span>


The **AVC\_FUNCTION\_PEER\_DO\_LIST** function code locates all nonvirtual *avc.sys* instances.

### I/O Status Block

If successful, the AV/C protocol driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS.

Possible other return values include:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>STATUS_INSUFFICIENT_RESOURCES</p></td>
<td><p>Could not obtain space for the list of device object references.</p></td>
</tr>
</tbody>
</table>

 

### Comments

This function uses the **PeerList** member of the AVC\_MULTIFUNC\_IRB structure as shown below.

```cpp
typedef struct _AVC_MULTIFUNC_IRB {
  AVC_IRB  Common;
  union {
    .
    .
    .
    AVC_PEER_DO_LIST PeerList;
 .
    .
    .
  };
} AVC_MULTIFUNC_IRB, *PAVC_MULTIFUNC_IRB;
```

### Requirements

**Headers:** Declared in *avc.h*. Include *avc.h*.

### AVC\_MULTIFUNC\_IRB Input

**Common**  
The **Function** submember of this member must be set to **AVC\_FUNCTION\_PEER\_DO\_LIST** from the AVC\_FUNCTION enumeration.

<span id="PeerList"></span><span id="peerlist"></span><span id="PEERLIST"></span>**PeerList**  
Specifies a list of all nonvirtual (peer) instances of *avc.sys*.

The caller may submit GUID\_AVC\_CLASS Device Interface requests through any of the objects returned in the object list. The caller must release the references to these objects (through **ObDereferenceObject**), and free the memory containing the list (through **ExFreePool**) when finished.

This function code may be called at IRQL &lt;= DISPATCH\_LEVEL.

### See Also

[**AVC\_MULTIFUNC\_IRB**](https://msdn.microsoft.com/library/windows/hardware/ff554177), [**AVC\_PEER\_DO\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff554179), [**AVC\_FUNCTION**](https://msdn.microsoft.com/library/windows/hardware/ff554145), [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147), [**ObDereferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff557724), [**ExFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff544590)

 

 





