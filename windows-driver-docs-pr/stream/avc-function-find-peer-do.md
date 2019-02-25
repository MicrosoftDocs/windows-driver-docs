---
title: AVC\_FUNCTION\_FIND\_PEER\_DO
description: AVC\_FUNCTION\_FIND\_PEER\_DO
ms.assetid: a21dde69-f005-4782-97d9-095a57b2b1a5
keywords: ["AVC_FUNCTION_FIND_PEER_DO Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVC_FUNCTION_FIND_PEER_DO
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# AVC\_FUNCTION\_FIND\_PEER\_DO


## <span id="ddk_avc_function_find_peer_do_ks"></span><span id="DDK_AVC_FUNCTION_FIND_PEER_DO_KS"></span>


The **AVC\_FUNCTION\_FIND\_PEER\_DO** function code locates a nonvirtual *avc.sys* instance.

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
<td><p>STATUS_UNSUCCESSFUL</p></td>
<td><p>A nonvirtual instance of <em>avc.sys</em> was not found</p></td>
</tr>
<tr class="even">
<td><p>STATUS_INVALID_GENERATION</p></td>
<td><p>A bus reset occurred before the Device Object reference could be found. Obtain a new NodeAddress and try again.</p></td>
</tr>
</tbody>
</table>

 

### Comments

This function uses the **PeerLocator** member of the AVC\_MULTIFUNC\_IRB structure as shown below.

```cpp
typedef struct _AVC_MULTIFUNC_IRB {
  AVC_IRB  Common;
  union {
    .
    .
    .
    AVC_PEER_DO_LOCATOR PeerLocator;
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
The **Function** submember of this member must be set to **AVC\_FUNCTION\_FIND\_PEER\_DO** from the AVC\_FUNCTION enumeration.

<span id="PeerLocator"></span><span id="peerlocator"></span><span id="PEERLOCATOR"></span>**PeerLocator**  
Specifies the nonvirtual (peer) instances of *avc.sys*.

This function locates a nonvirtual *avc.sys* instance according to the node address of the device it represents. If an instance is not found, the IRP completes with a status of STATUS\_UNSUCCESSFUL. Once an instance is located, the caller may submit any GUID\_AVC\_CLASS Device Interface requests through the object. The caller must release the reference to this object (through **ObDereferenceObject**) when finished with it.

This function code may be called at IRQL &lt;= DISPATCH\_LEVEL.

### See Also

[**AVC\_MULTIFUNC\_IRB**](https://msdn.microsoft.com/library/windows/hardware/ff554177), [**AVC\_PEER\_DO\_LOCATOR**](https://msdn.microsoft.com/library/windows/hardware/ff554180), [**AVC\_FUNCTION**](https://msdn.microsoft.com/library/windows/hardware/ff554145), [**ObDereferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff557724)

 

 





