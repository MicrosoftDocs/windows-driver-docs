---
title: AVC_FUNCTION_SET_CONNECTINFO
description: The AVC_FUNCTION_SET_CONNECT_INFO function code sets the AVCCONNECTINFO structure for each pin ID.
keywords: ["AVC_FUNCTION_SET_CONNECTINFO Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVC_FUNCTION_SET_CONNECTINFO
api_type:
- NA
ms.date: 07/27/2021
---

# AVC_FUNCTION_SET_CONNECTINFO

The AVC_FUNCTION_SET_CONNECT_INFO function code sets the **AVCCONNECTINFO** structure for each pin ID (offset from zero).

## I/O Status Block

If successful, the AV/C protocol driver sets **Irp->IoStatus.Status** to STATUS_SUCCESS.

Possible other return values include:

| Return value | Description |
|--|--|
| STATUS_TIMEOUT | The request was made, but no response was received before all time-out and retry processing was complete. |
| STATUS_REQUEST_ABORTED | Immediately abort when the IRP completion status is STATUS_REQUEST_ABORTED. This indicates that the device has been removed or is no longer available on the 1394 bus. |
| STATUS_* | Any other return code indicates that an error or warning occurred that was beyond the scope of the AV/C protocol. |

## Comments

This function uses the **SetConnectInfo** member of the **AVC_MULTIFUNC_IRB** structure as shown below.

```cpp
typedef struct _AVC_MULTIFUNC_IRB {
  AVC_IRB  Common;
  union {
    .
    .
    .
    AVC_SETCONNECT_INFO SetConnectInfo;
 .
    .
    .
  };
} AVC_MULTIFUNC_IRB, *PAVC_MULTIFUNC_IRB;
```

## Requirements

**Headers:** Declared in *avc.h* (Include *avc.h*)

### AVC_MULTIFUNC_IRB Input

**Common**  
The **Function** submember of this member must be set to **AVC_FUNCTION_SET_CONNECTINFO** from the AVC_FUNCTION enumeration.

**SetConnectInfo**  
Specifies the connection information for the AV/C device.

This function code is not supported by virtual instances of *avc.sys*.

A subunit driver must use this function if it provides an intersect handler. The AVCCONNECTINFO structure (contained inside the AVC_SET_CONNECTINFO structure) is derived from the AVCPRECONNECTINFO structures that are appended to the data ranges passed to the intersect handler.

After determining that the data ranges are compatible, the intersect handler generates an AVCCONNECTINFO structure. This structure is appended to the resulting data format, and also sent to *avc.sys*. It does not matter if the proposed data format is passed up for a better one later, because *avc.sys* only caches one AVCCONNECTINFO structure.

This must be called at IRQL = PASSIVE_LEVEL.

## See also

[**AVC_MULTIFUNC_IRB**](/windows-hardware/drivers/ddi/avc/ns-avc-_avc_multifunc_irb)

[**AVC_SETCONNECT_INFO**](/windows-hardware/drivers/ddi/avc/ns-avc-_avc_setconnect_info)

[**AVCCONNECTINFO**](/windows-hardware/drivers/ddi/avc/ns-avc-_avcconnectinfo)

[**AVC_FUNCTION**](/windows-hardware/drivers/ddi/avc/ne-avc-_tagavc_function)

[**AV/C Intersect Handler**](/windows-hardware/drivers/ddi/avc/nc-avc-pfnavcintersecthandler)
