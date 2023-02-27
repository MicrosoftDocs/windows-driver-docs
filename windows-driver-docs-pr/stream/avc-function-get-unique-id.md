---
title: AVC_FUNCTION_GET_UNIQUE_ID
description: The AVC_FUNCTION_GET_UNIQUE_ID function code obtains the unique ID of the AV/C unit.
keywords: ["AVC_FUNCTION_GET_UNIQUE_ID Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- AVC_FUNCTION_GET_UNIQUE_ID
api_type:
- NA
ms.date: 07/27/2021
---

# AVC_FUNCTION_GET_UNIQUE_ID

The AVC_FUNCTION_GET_UNIQUE_ID function code obtains the unique ID of the AV/C unit.

## I/O Status Block

If successful, the AV/C protocol driver sets **Irp->IoStatus.Status** to STATUS_SUCCESS.

Possible other return values include:

| Return value | Description |
|--|--|
| STATUS_TIMEOUT | The request was made, but no response was received before all time-out and retry processing was complete. |
| STATUS_REQUEST_ABORTED | Immediately abort when the IRP completion status is STATUS_REQUEST_ABORTED. This indicates that the device has been removed or is no longer available on the 1394 bus. |
| STATUS_* | Any other return code indicates that an error or warning occurred that was beyond the scope of the AV/C protocol. |

## Comments

This function uses the **UniqueID** member of the AVC_MULTIFUNC_IRB structure as shown below.

```cpp
typedef struct _AVC_MULTIFUNC_IRB {
  AVC_IRB  Common;
  union {
    .
    .
    .
    AVC_UNIQUE_ID UniqueID;
 .
    .
    .
  };
} AVC_MULTIFUNC_IRB, *PAVC_MULTIFUNC_IRB;
```

The members of the AVC_UNIQUE_ID structure are shown below:

```cpp
typedef struct _AVC_UNIQUE_ID {
    OUT GUID DeviceID;
} AVC_UNIQUE_ID, *PAVC_UNIQUE_ID;
```

## Requirements

**Headers:** Declared in *avc.h*. Include *avc.h*.

### AVC_MULTIFUNC_IRB Input

**Common**  
The **Function** submember of this member must be set to **AVC_FUNCTION_GET_UNIQUE_ID** from the AVC_FUNCTION enumeration.

**UniqueID**  
Specifies a GUID representing the unit as a whole. All subunits within the same unit share the same GUID. No two units share the same GUID.

This function code is not supported by virtual instances of *avc.sys*.

The subunit driver uses this function if it must report the device GUID to a controlling application (an application that must know which of the many subunit driver instances belong in the same unit), or if it is building its own AVCPRECONNECTINFO structures for external plugs.

This must be called at IRQL = PASSIVE_LEVEL.

## See also

[**AVC_MULTIFUNC_IRB**](/windows-hardware/drivers/ddi/avc/ns-avc-_avc_multifunc_irb)

[**AVC_UNIQUE_ID**](/windows-hardware/drivers/ddi/avc/ns-avc-_avc_unique_id)

[**AVCPRECONNECTINFO**](/windows-hardware/drivers/ddi/avc/ns-avc-_avcpreconnectinfo)

[**AVC_FUNCTION**](/windows-hardware/drivers/ddi/avc/ne-avc-_tagavc_function)
