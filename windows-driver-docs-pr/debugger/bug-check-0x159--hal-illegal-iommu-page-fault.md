---
title: Bug Check 0X159 HAL_ILLEGAL_IOMMU_PAGE_FAULT
description: The HAL_ILLEGAL_IOMMU_PAGE_FAULT bug check has a value of 0x00000159.
keywords: ["Bug Check 0x159 HAL_ILLEGAL_IOMMU_PAGE_FAULT", "HAL_ILLEGAL_IOMMU_PAGE_FAULT"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- HAL_ILLEGAL_IOMMU_PAGE_FAULT
api_type:
- NA
---

# Bug Check 0x159: HAL\_ILLEGAL\_IOMMU\_PAGE\_FAULT


The HAL\_ILLEGAL\_IOMMU\_PAGE\_FAULT bug check has a value of 0x00000159. This indicates that the IOMMU has delivered a page fault against an ASID that was in the process of being freed. The driver was responsible for completing any inflight requests before this point in time and this bugcheck indicates a driver in the system did not do so.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## HAL\_ILLEGAL\_IOMMU\_PAGE\_FAULT Parameters


| Parameter | Description                       |
|-----------|-----------------------------------|
| 1         | IOMMU Vendor disambiguation       |
| 2         | Pointer to fault packet           |
| 3         | Vendor specific fault packet data |
| 4         | Vendor specific fault packet data |

 

| Parameter | Description                           |
|-----------|---------------------------------------|
| 1         | IOMMU Vendor disambiguation = 0x3xxx. |
| 2         | Status                                |
| 3         | PASID                                 |
| 4         | DirectoryBase                         |

 

 

 




