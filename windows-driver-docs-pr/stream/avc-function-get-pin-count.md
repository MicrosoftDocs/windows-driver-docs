---
title: AVC_FUNCTION_GET_PIN_COUNT
description: The AVC_FUNCTION_GET_PIN_COUNT function code obtains the number of pins supported by the underlying subunit device.
keywords: ["AVC_FUNCTION_GET_PIN_COUNT Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- AVC_FUNCTION_GET_PIN_COUNT
api_type:
- NA
ms.date: 07/27/2021
---

# AVC_FUNCTION_GET_PIN_COUNT

The AVC_FUNCTION_GET_PIN_COUNT function code obtains the number of pins supported by the underlying subunit device.

## I/O Status Block

If successful, the AV/C protocol driver sets **Irp-&gt;IoStatus.Status** to STATUS_SUCCESS.

Possible other return values include:

| Return value | Description |
|--|--|
| STATUS_TIMEOUT | The request was made, but no response was received before all time-out and retry processing was complete. |
| STATUS_REQUEST_ABORTED | Immediately abort when the IRP completion status is STATUS_REQUEST_ABORTED. This indicates that the device has been removed or is no longer available on the 1394 bus. |
| STATUS_* | Any other return code indicates that an error or warning occurred that was beyond the scope of the AV/C protocol. |

## Comments

This function uses the **PinCount** member of the AVC_MULTIFUNC_IRB structure as shown below.

```cpp
typedef struct _AVC_MULTIFUNC_IRB {
  AVC_IRB  Common;
  union {
    AVC_PIN_COUNT PinCount;
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
The **Function** submember of this member must be set to **AVC_FUNCTION_GET_PIN_COUNT** from the AVC_FUNCTION enumeration.

**PinCount**  
Specifies the number of pins on an AV/C device upon returning from the function.

This function code is not supported by virtual instances of *avc.sys*.

This must be called at IRQL = PASSIVE_LEVEL.

## See also

[**AVC_MULTIFUNC_IRB**](/windows-hardware/drivers/ddi/avc/ns-avc-_avc_multifunc_irb)

[**AVC_PIN_COUNT**](/windows-hardware/drivers/ddi/avc/ns-avc-_avc_pin_count)

[**AVC_FUNCTION**](/windows-hardware/drivers/ddi/avc/ne-avc-_tagavc_function)
