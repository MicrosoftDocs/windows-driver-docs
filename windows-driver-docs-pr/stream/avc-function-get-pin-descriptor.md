---
title: AVC_FUNCTION_GET_PIN_DESCRIPTOR
description: The AVC_FUNCTION_GET_PIN_DESCRIPTOR function code obtains the pin descriptor for each pin ID.
keywords: ["AVC_FUNCTION_GET_PIN_DESCRIPTOR Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVC_FUNCTION_GET_PIN_DESCRIPTOR
api_type:
- NA
ms.date: 07/27/2021
---

# AVC_FUNCTION_GET_PIN_DESCRIPTOR

The **AVC_FUNCTION_GET_PIN_DESCRIPTOR** function code obtains the pin descriptor for each pin ID (offset from zero).

## I/O Status Block

If successful, the AV/C protocol driver sets **Irp-&gt;IoStatus.Status** to STATUS_SUCCESS.

Possible other return values include:

| Return value | Description |
|--|--|
| STATUS_TIMEOUT | The request was made, but no response was received before all time-out and retry processing was complete. |
| STATUS_REQUEST_ABORTED | Immediately abort when the IRP completion status is STATUS_REQUEST_ABORTED. This indicates that the device has been removed or is no longer available on the 1394 bus. |
| STATUS_* | Any other return code indicates that an error or warning occurred that was beyond the scope of the AV/C protocol. |

## Comments

This function uses the **PinDescriptor** member of the AVC_MULTIFUNC_IRB structure as shown below.

```cpp
typedef struct _AVC_MULTIFUNC_IRB {
  AVC_IRB  Common;
  union {
    .
    .
    .
    AVC_PIN_DESCRIPTOR PinDescriptor;
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
The **Function** submember of this member must be set to **AVC_FUNCTION_GET_PIN_DESCRIPTOR** from the AVC_FUNCTION enumeration.

**PinDescriptor**  
Specifies the description of a pin on an AV/C subunit device.

This function code is not supported by virtual instances of *avc.sys*.

In addition to the pin descriptor, this function may also return the address of an intersect handler and an opaque context value associated with the intersect handler. If the intersect handler member is **NULL**, the subunit driver must provide an intersect handler. If the intersect handler member is not **NULL**, an intersect handler is provided and the driver may use it.

*Avc.sys* never provides a data intersection, but a filter driver (for example, *avcstrm.sys*) fills it in as the request is being completed back up through the stack.

This must be called at IRQL = PASSIVE_LEVEL.

### See also

[**AVC_MULTIFUNC_IRB**](/windows-hardware/drivers/ddi/avc/ns-avc-_avc_multifunc_irb)

[**AVC_PIN_DESCRIPTOR**](/windows-hardware/drivers/ddi/avc/ns-avc-_avc_pin_descriptor)

[**AVC_FUNCTION**](/windows-hardware/drivers/ddi/avc/ne-avc-_tagavc_function)

[**KSPIN_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-kspin_descriptor)

[**AV/C Intersect Handler**](/windows-hardware/drivers/ddi/avc/nc-avc-pfnavcintersecthandler)
