---
title: AVC\_FUNCTION\_SET\_CONNECTINFO
description: AVC\_FUNCTION\_SET\_CONNECTINFO
ms.assetid: e97b525a-2236-44a9-9d49-dc0df760f21e
keywords: ["AVC_FUNCTION_SET_CONNECTINFO Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVC_FUNCTION_SET_CONNECTINFO
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# AVC\_FUNCTION\_SET\_CONNECTINFO


## <span id="ddk_avc_function_set_connectinfo_ks"></span><span id="DDK_AVC_FUNCTION_SET_CONNECTINFO_KS"></span>


The AVC\_FUNCTION\_SET\_CONNECT\_INFO function code sets the AVCCONNECTINFO structure for each pin ID (offset from zero).

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

This function uses the **SetConnectInfo** member of the AVC\_MULTIFUNC\_IRB structure as shown below.

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

### Requirements

**Headers:** Declared in *avc.h*. Include *avc.h*.

### AVC\_MULTIFUNC\_IRB Input

**Common**  
The **Function** submember of this member must be set to **AVC\_FUNCTION\_SET\_CONNECTINFO** from the AVC\_FUNCTION enumeration.

<span id="SetConnectInfo"></span><span id="setconnectinfo"></span><span id="SETCONNECTINFO"></span>**SetConnectInfo**  
Specifies the connection information for the AV/C device.

This function code is not supported by virtual instances of *avc.sys*.

A subunit driver must use this function if it provides an intersect handler. The AVCCONNECTINFO structure (contained inside the AVC\_SET\_CONNECTINFO structure) is derived from the AVCPRECONNECTINFO structures that are appended to the data ranges passed to the intersect handler.

After determining that the data ranges are compatible, the intersect handler generates an AVCCONNECTINFO structure. This structure is appended to the resulting data format, and also sent to *avc.sys*. It does not matter if the proposed data format is passed up for a better one later, because *avc.sys* only caches one AVCCONNECTINFO structure.

This must be called at IRQL = PASSIVE\_LEVEL.

### See Also

[**AVC\_MULTIFUNC\_IRB**](https://msdn.microsoft.com/library/windows/hardware/ff554177), [**AVC\_SETCONNECT\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff554192), [**AVCCONNECTINFO**](https://msdn.microsoft.com/library/windows/hardware/ff554101), [**AVC\_FUNCTION**](https://msdn.microsoft.com/library/windows/hardware/ff554145), [**AV/C Intersect Handler**](https://msdn.microsoft.com/library/windows/hardware/ff556379)

 

 





