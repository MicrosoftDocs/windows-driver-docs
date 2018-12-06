---
title: AVC\_FUNCTION\_GET\_UNIQUE\_ID
description: AVC\_FUNCTION\_GET\_UNIQUE\_ID
ms.assetid: 51b35686-03a9-45b3-8bdc-14cbd24714dc
keywords: ["AVC_FUNCTION_GET_UNIQUE_ID Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVC_FUNCTION_GET_UNIQUE_ID
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# AVC\_FUNCTION\_GET\_UNIQUE\_ID


## <span id="ddk_avc_function_get_unique_id_ks"></span><span id="DDK_AVC_FUNCTION_GET_UNIQUE_ID_KS"></span>


The **AVC\_FUNCTION\_GET\_UNIQUE\_ID** function code obtains the unique ID of the AV/C unit.

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

This function uses the **UniqueID** member of the AVC\_MULTIFUNC\_IRB structure as shown below.

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

The members of the AVC\_UNIQUE\_ID structure are shown below:

```cpp
typedef struct _AVC_UNIQUE_ID {
    OUT GUID DeviceID;
} AVC_UNIQUE_ID, *PAVC_UNIQUE_ID;
```

### Requirements

**Headers:** Declared in *avc.h*. Include *avc.h*.

### AVC\_MULTIFUNC\_IRB Input

**Common**  
The **Function** submember of this member must be set to **AVC\_FUNCTION\_GET\_UNIQUE\_ID** from the AVC\_FUNCTION enumeration.

<span id="UniqueID"></span><span id="uniqueid"></span><span id="UNIQUEID"></span>**UniqueID**  
Specifies a GUID representing the unit as a whole. All subunits within the same unit share the same GUID. No two units share the same GUID.

This function code is not supported by virtual instances of *avc.sys*.

The subunit driver uses this function if it must report the device GUID to a controlling application (an application that must know which of the many subunit driver instances belong in the same unit), or if it is building its own AVCPRECONNECTINFO structures for external plugs.

This must be called at IRQL = PASSIVE\_LEVEL.

### See Also

[**AVC\_MULTIFUNC\_IRB**](https://msdn.microsoft.com/library/windows/hardware/ff554177), [**AVC\_UNIQUE\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff554200), [**AVCPRECONNECTINFO**](https://msdn.microsoft.com/library/windows/hardware/ff554103), [**AVC\_FUNCTION**](https://msdn.microsoft.com/library/windows/hardware/ff554145)

 

 





