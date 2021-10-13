---
title: AVC_FUNCTION_GET_CONNECTINFO
description: The AVC_FUNCTION_GET_CONNECT_INFO function code obtains the AVCPRECONNECTINFO structure for each pin ID.
keywords: ["AVC_FUNCTION_GET_CONNECTINFO Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVC_FUNCTION_GET_CONNECTINFO
api_type:
- NA
ms.date: 07/27/2021
ms.localizationpriority: medium
---

# AVC_FUNCTION_GET_CONNECTINFO

The AVC_FUNCTION_GET_CONNECT_INFO function code obtains the **AVCPRECONNECTINFO** structure for each pin ID (offset from zero).

## I/O Status Block

If successful, the AV/C protocol driver sets **Irp-&gt;IoStatus.Status** to STATUS_SUCCESS.

Possible other return values include:

| Return value | Description |
|--|--|
| STATUS_TIMEOUT | The request was made, but no response was received before all time-out and retry processing was complete. |
| STATUS_REQUEST_ABORTED | Immediately abort when the IRP completion status is STATUS_REQUEST_ABORTED. This indicates that the device has been removed or is no longer available on the 1394 bus. |
| STATUS_* | Any other return code indicates that an error or warning occurred that was beyond the scope of the AV/C protocol. |

## Comments

This function uses the **PreConnectInfo** member of the AVC_MULTIFUNC_IRB structure as shown below.

```cpp
typedef struct _AVC_MULTIFUNC_IRB {
  AVC_IRB  Common;
  union {
    .
    .
    .
    AVC_PRECONNECT_INFO PreConnectInfo;
 .
    .
    .
  };
} AVC_MULTIFUNC_IRB, *PAVC_MULTIFUNC_IRB;
```

The members of the AVC_PRECONNECT_INFO structure are shown below:

```cpp
typedef struct _AVC_PRECONNECT_INFO {
    IN ULONG PinId
    OUT AVCPRECONNECTINFO ConnectInfo;
} AVC_PRECONNECT_INFO, *PAVC_PRECONNECT_INFO;
```

## Requirements

**Headers:** Declared in *avc.h*. Include *avc.h*.

### AVC_MULTIFUNC_IRB Input

**Common**  
The **Function** submember of this member must be set to **AVC_FUNCTION_GET_CONNECTINFO** from the AVC_FUNCTION enumeration.

**ConnectInfo**  
Specifies the connection information for the AV/C device.

This function code is not supported by virtual instances of *avc.sys*.

A subunit driver must use this function if it is responsible for creating the data ranges included in the KSPIN_DESCRIPTOR structure. The AVCPRECONNECTINFO structure is appended to the **DataRanges** member for connections external to the PC.

This must be called at IRQL = PASSIVE_LEVEL.

## See also

[**AVC_MULTIFUNC_IRB**](/windows-hardware/drivers/ddi/avc/ns-avc-_avc_multifunc_irb)

[**AVC_PRECONNECT_INFO**](/windows-hardware/drivers/ddi/avc/ns-avc-_avc_preconnect_info)

[**AVCPRECONNECTINFO**](/windows-hardware/drivers/ddi/avc/ns-avc-_avcpreconnectinfo)

[**AVC_FUNCTION**](/windows-hardware/drivers/ddi/avc/ne-avc-_tagavc_function)
