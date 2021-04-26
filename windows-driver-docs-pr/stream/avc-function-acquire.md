---
title: AVC\_FUNCTION\_ACQUIRE
description: AVC\_FUNCTION\_ACQUIRE
keywords: ["AVC_FUNCTION_ACQUIRE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVC_FUNCTION_ACQUIRE
api_type:
- NA
ms.date: 09/11/2018
ms.localizationpriority: medium
---

# AVC\_FUNCTION\_ACQUIRE

The **AVC\_FUNCTION\_ACQUIRE** function code causes *avc.sys* to establish any connections suggested by cached AVCCONNECTINFO values.

## I/O Status Block

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
<td><p>STATUS_TIMEOUT</p></td>
<td><p>The request was made, but no response was received before all time-out and retry processing was complete.</p></td>
</tr>
<tr class="even">
<td><p>STATUS_REQUEST_ABORTED</p></td>
<td><p>Immediately abort when the IRP completion status is STATUS_REQUEST_ABORTED. This indicates that the device has been removed or is no longer available on the 1394 bus.</p></td>
</tr>
<tr class="odd">
<td><p>STATUS_*</p></td>
<td><p>Any other return code indicates that an error or warning occurred that was beyond the scope of the AV/C protocol.</p></td>
</tr>
</tbody>
</table>

## Comments

This function uses the **PinId** member of the AVC\_MULTIFUNC\_IRB structure as shown below.

```cpp
typedef struct _AVC_MULTIFUNC_IRB {
  AVC_IRB  Common;
  union {
    .
    .
    .
    AVC_PIN_ID PinId;
 .
    .
    .
  };
} AVC_MULTIFUNC_IRB, *PAVC_MULTIFUNC_IRB;
```

## Requirements

**Headers:** Declared in *avc.h*. Include *avc.h*.

## AVC\_MULTIFUNC\_IRB Input

**Common**  

The **Function** submember of this member must be set to **AVC\_FUNCTION\_ACQUIRE** from the AVC\_FUNCTION enumeration.

**PinId**  

Specifies the offset (or ID) of the pin for which a connection is to be acquired.

This function code is not supported by virtual instances of *avc.sys*.

A subunit driver must use this function when the pin becomes active.

This must be called at IRQL = PASSIVE\_LEVEL.

## See Also

[**AVC\_MULTIFUNC\_IRB**](/windows-hardware/drivers/ddi/avc/ns-avc-_avc_multifunc_irb)

[**AVC\_PIN\_ID**](/windows-hardware/drivers/ddi/avc/ns-avc-_avc_pin_id)

[**AVC\_FUNCTION**](/windows-hardware/drivers/ddi/avc/ne-avc-_tagavc_function)
