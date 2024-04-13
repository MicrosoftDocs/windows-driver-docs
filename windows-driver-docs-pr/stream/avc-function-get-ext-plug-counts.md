---
title: AVC_FUNCTION_GET_EXT_PLUG_COUNTS
description: The AVC_FUNCTION_GET_EXT_PLUG_COUNTS function code obtains the external input and output plug counts.
keywords: ["AVC_FUNCTION_GET_EXT_PLUG_COUNTS Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- AVC_FUNCTION_GET_EXT_PLUG_COUNTS
api_type:
- NA
ms.date: 07/27/2021
---

# AVC_FUNCTION_GET_EXT_PLUG_COUNTS

The **AVC_FUNCTION_GET_EXT_PLUG_COUNTS** function code obtains the external input and output plug counts.

## I/O Status Block

If successful, the AV/C protocol driver sets **Irp-&gt;IoStatus.Status** to STATUS_SUCCESS.

Possible other return values include:

| Return value | Description |
|--|--|
| STATUS_TIMEOUT | The request was made, but no response was received before all time-out and retry processing was complete. |
| STATUS_REQUEST_ABORTED | Immediately abort when the IRP completion status is STATUS_REQUEST_ABORTED. This indicates that the device has been removed or is no longer available on the 1394 bus. |
| STATUS_* | Any other return code indicates that an error or warning occurred that was beyond the scope of the AV/C protocol. |

## Comments

This function uses the **ExtPlugCounts** member of the AVC_MULTIFUNC_IRB structure as shown below.

```cpp
typedef struct _AVC_MULTIFUNC_IRB {
  AVC_IRB  Common;
  union {
    .
    .
    .
    AVC_EXT_PLUG_COUNTS ExtPlugCounts;
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
The **Function** submember of this member must be set to **AVC_FUNCTION_GET_EXT_PLUG_COUNTS** from the AVC_FUNCTION enumeration.

**ExtPlugCounts**  
Specifies the count of external input and output plugs.

This function code is not supported by virtual instances of *avc.sys*.

Subunit drivers are responsible for determining the function, format, and use of external plugs. *Avc.sys* does, however, report any permanent connections between external plugs and subunit plugs as dedicated pins on the subunit (for more information, see [**AVC_FUNCTION_GET_CONNECTINFO**](avc-function-get-connectinfo.md)).

This must be called at IRQL = PASSIVE_LEVEL.

## See also

[**AVC_MULTIFUNC_IRB**](/windows-hardware/drivers/ddi/avc/ns-avc-_avc_multifunc_irb)

[**AVC_EXT_PLUG_COUNTS**](/windows-hardware/drivers/ddi/avc/ns-avc-_avc_ext_plug_counts)

[**AVC_FUNCTION**](/windows-hardware/drivers/ddi/avc/ne-avc-_tagavc_function)
