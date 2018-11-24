---
title: AVC\_FUNCTION\_GET\_EXT\_PLUG\_COUNTS
description: AVC\_FUNCTION\_GET\_EXT\_PLUG\_COUNTS
ms.assetid: dced18ac-dc26-4c47-bc92-a3f3daec505b
keywords: ["AVC_FUNCTION_GET_EXT_PLUG_COUNTS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVC_FUNCTION_GET_EXT_PLUG_COUNTS
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# AVC\_FUNCTION\_GET\_EXT\_PLUG\_COUNTS


## <span id="ddk_avc_function_get_ext_plug_counts_ks"></span><span id="DDK_AVC_FUNCTION_GET_EXT_PLUG_COUNTS_KS"></span>


The **AVC\_FUNCTION\_GET\_EXT\_PLUG\_COUNTS** function code obtains the external input and output plug counts.

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

This function uses the **ExtPlugCounts** member of the AVC\_MULTIFUNC\_IRB structure as shown below.

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

### Requirements

**Headers:** Declared in *avc.h*. Include *avc.h*.

### AVC\_MULTIFUNC\_IRB Input

**Common**  
The **Function** submember of this member must be set to **AVC\_FUNCTION\_GET\_EXT\_PLUG\_COUNTS** from the AVC\_FUNCTION enumeration.

<span id="ExtPlugCounts"></span><span id="extplugcounts"></span><span id="EXTPLUGCOUNTS"></span>**ExtPlugCounts**  
Specifies the count of external input and output plugs.

This function code is not supported by virtual instances of *avc.sys*.

Subunit drivers are responsible for determining the function, format, and use of external plugs. *Avc.sys* does, however, report any permanent connections between external plugs and subunit plugs as dedicated pins on the subunit (for more information, see [**AVC\_FUNCTION\_GET\_CONNECTINFO**](avc-function-get-connectinfo.md)).

This must be called at IRQL = PASSIVE\_LEVEL.

### See Also

[**AVC\_MULTIFUNC\_IRB**](https://msdn.microsoft.com/library/windows/hardware/ff554177), [**AVC\_EXT\_PLUG\_COUNTS**](https://msdn.microsoft.com/library/windows/hardware/ff554143), [**AVC\_FUNCTION**](https://msdn.microsoft.com/library/windows/hardware/ff554145)

 

 





