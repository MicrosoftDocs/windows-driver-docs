---
title: AVC_FUNCTION_GET_SUBUNIT_INFO
description: The AVC_FUNCTION_GET_SUBUNIT_INFO function code obtains the subunit information of the target device.
keywords: ["AVC_FUNCTION_GET_SUBUNIT_INFO Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- AVC_FUNCTION_GET_SUBUNIT_INFO
api_type:
- NA
ms.date: 11/28/2017
---

# AVC_FUNCTION_GET_SUBUNIT_INFO

The AVC_FUNCTION_GET_SUBUNIT_INFO function code obtains the subunit information of the target device.

## I/O Status Block

This function always sets **Irp->IoStatus.Status** to STATUS_SUCCESS.

## Comments

This function uses the **Subunits** member of the AVC_MULTIFUNC_IRB structure as shown below.

```cpp
typedef struct _AVC_MULTIFUNC_IRB {
  AVC_IRB  Common;
  union {
    .
    .
    .
    AVC_SUBUNIT_INFO_BLOCK Subunits;
 };
} AVC_MULTIFUNC_IRB, *PAVC_MULTIFUNC_IRB;
```

## Requirements

**Headers:** Declared in *avc.h*. Include *avc.h*.

### AVC_MULTIFUNC_IRB Input

**Common**  
The **Function** submember of this member must be set to **AVC_FUNCTION_GET_SUBUNIT_INFO** from the AVC_FUNCTION enumeration.

**Subunits**  
Specifies a description of an AV/C subunit's information.

This function is satisfied locally, so no commands are sent to the target.

This function code may be called at IRQL &lt;= DISPATCH_LEVEL.

## See also

[**AVC_MULTIFUNC_IRB**](/windows-hardware/drivers/ddi/avc/ns-avc-_avc_multifunc_irb)

[**AVC_SUBUNIT_INFO_BLOCK**](/windows-hardware/drivers/ddi/avc/ns-avc-_avc_subunit_info_block)

[**AVC_FUNCTION**](/windows-hardware/drivers/ddi/avc/ne-avc-_tagavc_function)
