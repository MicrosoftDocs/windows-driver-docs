---
title: AVC\_FUNCTION\_GET\_CONNECTINFO
description: AVC\_FUNCTION\_GET\_CONNECTINFO
ms.assetid: d4230024-a765-47f0-9958-9f71761f7b85
keywords: ["AVC_FUNCTION_GET_CONNECTINFO Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVC_FUNCTION_GET_CONNECTINFO
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# AVC\_FUNCTION\_GET\_CONNECTINFO


## <span id="ddk_avc_function_get_connectinfo_ks"></span><span id="DDK_AVC_FUNCTION_GET_CONNECTINFO_KS"></span>


The AVC\_FUNCTION\_GET\_CONNECT\_INFO function code obtains the AVCPRECONNECTINFO structure for each pin ID (offset from zero).

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

This function uses the **PreConnectInfo** member of the AVC\_MULTIFUNC\_IRB structure as shown below.

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

The members of the AVC\_PRECONNECT\_INFO structure are shown below:

```cpp
typedef struct _AVC_PRECONNECT_INFO {
    IN ULONG PinId
    OUT AVCPRECONNECTINFO ConnectInfo;
} AVC_PRECONNECT_INFO, *PAVC_PRECONNECT_INFO;
```

### Requirements

**Headers:** Declared in *avc.h*. Include *avc.h*.

### AVC\_MULTIFUNC\_IRB Input

**Common**  
The **Function** submember of this member must be set to **AVC\_FUNCTION\_GET\_CONNECTINFO** from the AVC\_FUNCTION enumeration.

<span id="ConnectInfo"></span><span id="connectinfo"></span><span id="CONNECTINFO"></span>**ConnectInfo**  
Specifies the connection information for the AV/C device.

This function code is not supported by virtual instances of *avc.sys*.

A subunit driver must use this function if it is responsible for creating the data ranges included in the KSPIN\_DESCRIPTOR structure. The AVCPRECONNECTINFO structure is appended to the **DataRanges** member for connections external to the PC.

This must be called at IRQL = PASSIVE\_LEVEL.

### See Also

[**AVC\_MULTIFUNC\_IRB**](https://msdn.microsoft.com/library/windows/hardware/ff554177), [**AVC\_PRECONNECT\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff554190), [**AVCPRECONNECTINFO**](https://msdn.microsoft.com/library/windows/hardware/ff554103), [**AVC\_FUNCTION**](https://msdn.microsoft.com/library/windows/hardware/ff554145)

 

 





