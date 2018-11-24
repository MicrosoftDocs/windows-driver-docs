---
title: AVC\_FUNCTION\_GET\_PIN\_COUNT
description: AVC\_FUNCTION\_GET\_PIN\_COUNT
ms.assetid: fb455843-c979-479c-ba7c-f84875a9ba6f
keywords: ["AVC_FUNCTION_GET_PIN_COUNT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVC_FUNCTION_GET_PIN_COUNT
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# AVC\_FUNCTION\_GET\_PIN\_COUNT


## <span id="ddk_avc_function_get_pin_count_ks"></span><span id="DDK_AVC_FUNCTION_GET_PIN_COUNT_KS"></span>


The **AVC\_FUNCTION\_GET\_PIN\_COUNT** function code obtains the number of pins supported by the underlying subunit device.

### I/O Status Block

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

 

### Comments

This function uses the **PinCount** member of the AVC\_MULTIFUNC\_IRB structure as shown below.

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

### Requirements

**Headers:** Declared in *avc.h*. Include *avc.h*.

### AVC\_MULTIFUNC\_IRB Input

**Common**  
The **Function** submember of this member must be set to **AVC\_FUNCTION\_GET\_PIN\_COUNT** from the AVC\_FUNCTION enumeration.

<span id="PinCount"></span><span id="pincount"></span><span id="PINCOUNT"></span>**PinCount**  
Specifies the number of pins on an AV/C device upon returning from the function.

This function code is not supported by virtual instances of *avc.sys*.

This must be called at IRQL = PASSIVE\_LEVEL.

### See Also

[**AVC\_MULTIFUNC\_IRB**](https://msdn.microsoft.com/library/windows/hardware/ff554177), [**AVC\_PIN\_COUNT**](https://msdn.microsoft.com/library/windows/hardware/ff554183), [**AVC\_FUNCTION**](https://msdn.microsoft.com/library/windows/hardware/ff554145)

 

 





