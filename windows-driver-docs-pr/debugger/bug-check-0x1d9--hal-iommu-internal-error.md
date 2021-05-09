---
title: Bug Check 0x1D9 HAL_IOMMU_INTERNAL_ERROR
description: The HAL_IOMMU_INTERNAL_ERROR bug check has a value of 0x000001D9. It indicates that that the UcmUcsi driver has encountered an error.
keywords: ["Bug Check 0x1D9 HAL_IOMMU_INTERNAL_ERROR", "HAL_IOMMU_INTERNAL_ERROR"]
ms.date: 01/14/2019
topic_type:
- apiref
api_name:
- HAL_IOMMU_INTERNAL_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1D9: HAL\_IOMMU\_INTERNAL\_ERROR

The HAL\_IOMMU\_INTERNAL\_ERROR bug check has a value of 0x000001D9. It indicates that an internal error was detected in the HAL IOMMU library.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

 
## HAL\_IOMMU\_INTERNAL\_ERROR Parameters

|Parameter|Description|
|-------- |---------- |
|1| Indicates the failed operation. See values below.|
|2| See values below. |
|3| See values below. |
|4| See values below. |

**Failed Operation Values**

```text
0x00 : Failed to delete IOMMU domain
     Parameter 2 - Status
     Parameter 3 - Pointer to the IOMMU domain object

0x01 : Failed to unmap pages from IOMMU domain
     Parameter 2 - Status
     Parameter 3 - Pointer to the IOMMU domain object
     Parameter 4 - Logical address

0x02 : Failed to leave IOMMU domain
     Parameter 2 - Status
     Parameter 3 - Pointer to the IOMMU domain object
```

## ## Cause

An internal error was detected in the HAL IOMMU library.

## ## See Also-

[Bug Check Code Reference](bug-check-code-reference2.md)
