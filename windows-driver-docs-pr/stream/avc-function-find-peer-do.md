---
title: AVC_FUNCTION_FIND_PEER_DO
description: The AVC_FUNCTION_FIND_PEER_DO function code locates a nonvirtual avc.sys instance.
keywords: ["AVC_FUNCTION_FIND_PEER_DO Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVC_FUNCTION_FIND_PEER_DO
api_type:
- NA
ms.date: 07/27/2021
ms.localizationpriority: medium
---

# AVC_FUNCTION_FIND_PEER_DO

The AVC_FUNCTION_FIND_PEER_DO function code locates a nonvirtual *avc.sys* instance.

## I/O Status Block

If successful, the AV/C protocol driver sets **Irp-&gt;IoStatus.Status** to STATUS_SUCCESS.

Possible other return values include:

| Return value | Description |
|--|--|
| STATUS_UNSUCCESSFUL | A nonvirtual instance of *avc.sys* was not found |
| STATUS_INVALID_GENERATION | A bus reset occurred before the Device Object reference could be found. Obtain a new NodeAddress and try again. |

## Comments

This function uses the **PeerLocator** member of the AVC_MULTIFUNC_IRB structure as shown below.

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

## Requirements

**Headers:** Declared in *avc.h*. Include *avc.h*.

### AVC_MULTIFUNC_IRB Input

**Common**  
The **Function** submember of this member must be set to **AVC_FUNCTION_FIND_PEER_DO** from the AVC_FUNCTION enumeration.

**PeerLocator**  
Specifies the nonvirtual (peer) instances of *avc.sys*.

This function locates a nonvirtual *avc.sys* instance according to the node address of the device it represents. If an instance is not found, the IRP completes with a status of STATUS_UNSUCCESSFUL. Once an instance is located, the caller may submit any GUID_AVC_CLASS Device Interface requests through the object. The caller must release the reference to this object (through **ObDereferenceObject**) when finished with it.

This function code may be called at IRQL <= DISPATCH_LEVEL.

## See also

[**AVC_MULTIFUNC_IRB**](/windows-hardware/drivers/ddi/avc/ns-avc-_avc_multifunc_irb)

[**AVC_PEER_DO_LOCATOR**](/windows-hardware/drivers/ddi/avc/ns-avc-_avc_peer_do_locator)

[**AVC_FUNCTION**](/windows-hardware/drivers/ddi/avc/ne-avc-_tagavc_function)

[**ObDereferenceObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obdereferenceobject)
