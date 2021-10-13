---
title: AVC_FUNCTION_PEER_DO_LIST
description: The AVC_FUNCTION_PEER_DO_LIST function code locates all nonvirtual avc.sys instances.
keywords: ["AVC_FUNCTION_PEER_DO_LIST Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVC_FUNCTION_PEER_DO_LIST
api_type:
- NA
ms.date: 07/27/2021
ms.localizationpriority: medium
---

# AVC_FUNCTION_PEER_DO_LIST

The AVC_FUNCTION_PEER_DO_LIST function code locates all nonvirtual *avc.sys* instances.

## I/O Status Block

If successful, the AV/C protocol driver sets **Irp-&gt;IoStatus.Status** to STATUS_SUCCESS.

Possible other return values include:

| Return value | Description |
|--|--|
| STATUS_INSUFFICIENT_RESOURCES | Could not obtain space for the list of device object references. |

## Comments

This function uses the **PeerList** member of the AVC_MULTIFUNC_IRB structure as shown below.

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

## Requirements

**Headers:** Declared in *avc.h*. Include *avc.h*.

### AVC_MULTIFUNC_IRB Input

**Common**  
The **Function** submember of this member must be set to **AVC_FUNCTION_PEER_DO_LIST** from the AVC_FUNCTION enumeration.

**PeerList**  
Specifies a list of all nonvirtual (peer) instances of *avc.sys*.

The caller may submit GUID_AVC_CLASS Device Interface requests through any of the objects returned in the object list. The caller must release the references to these objects (through **ObDereferenceObject**), and free the memory containing the list (through **ExFreePool**) when finished.

This function code may be called at IRQL >= DISPATCH_LEVEL.

## See also

[**AVC_MULTIFUNC_IRB**](/windows-hardware/drivers/ddi/avc/ns-avc-_avc_multifunc_irb)

[**AVC_PEER_DO_LIST**](/windows-hardware/drivers/ddi/avc/ns-avc-_avc_peer_do_list)

[**AVC_FUNCTION**](/windows-hardware/drivers/ddi/avc/ne-avc-_tagavc_function)

[**DEVICE_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_object)

[**ObDereferenceObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obdereferenceobject)

[**ExFreePool**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exfreepool)
