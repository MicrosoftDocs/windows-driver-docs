---
title: AVC\_FUNCTION\_GET\_SUBUNIT\_INFO
description: AVC\_FUNCTION\_GET\_SUBUNIT\_INFO
ms.assetid: 1793df9d-b186-425f-a3dd-3054cb9b74bf
keywords: ["AVC_FUNCTION_GET_SUBUNIT_INFO Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVC_FUNCTION_GET_SUBUNIT_INFO
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# AVC\_FUNCTION\_GET\_SUBUNIT\_INFO


## <span id="ddk_avc_function_get_subunit_info_ks"></span><span id="DDK_AVC_FUNCTION_GET_SUBUNIT_INFO_KS"></span>


The **AVC\_FUNCTION\_GET\_SUBUNIT\_INFO** function code obtains the subunit information of the target device.

### I/O Status Block

This function always sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS.

### Comments

This function uses the **Subunits** member of the AVC\_MULTIFUNC\_IRB structure as shown below.

```cpp
typedef struct _AVC_MULTIFUNC_IRB {
  AVC_IRB  Common;
  union {
    .
    .
    .
    AVC_SUBUNIT_INFO_BLOCK Subunits;
 };
} AVC_MULTIFUNC_IRB, *PAVC_MULTIFUNC_IRB;
```

### Requirements

**Headers:** Declared in *avc.h*. Include *avc.h*.

### AVC\_MULTIFUNC\_IRB Input

**Common**  
The **Function** submember of this member must be set to **AVC\_FUNCTION\_GET\_SUBUNIT\_INFO** from the AVC\_FUNCTION enumeration.

<span id="Subunits"></span><span id="subunits"></span><span id="SUBUNITS"></span>**Subunits**  
Specifies a description of an AV/C subunit's information.

This function is satisfied locally, so no commands are sent to the target.

This function code may be called at IRQL &lt;= DISPATCH\_LEVEL.

### See Also

[**AVC\_MULTIFUNC\_IRB**](https://msdn.microsoft.com/library/windows/hardware/ff554177), [**AVC\_SUBUNIT\_INFO\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff554199), [**AVC\_FUNCTION**](https://msdn.microsoft.com/library/windows/hardware/ff554145)

 

 





