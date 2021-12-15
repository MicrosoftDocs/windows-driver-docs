---
title: Bug Check 0x158 ILLEGAL_IOMMU_PAGE_FAULT
description: The ILLEGAL_IOMMU_PAGE_FAULT bug check has a value of 0x00000158. This indicates that the IOMMU has delivered a page fault packet for an invalid ASID. 
keywords: ["Bug Check 0x158 ILLEGAL_IOMMU_PAGE_FAULT", "ILLEGAL_IOMMU_PAGE_FAULT"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ILLEGAL_IOMMU_PAGE_FAULT
api_type:
- NA
---

# Bug Check 0x158: ILLEGAL\_IOMMU\_PAGE\_FAULT


The ILLEGAL\_IOMMU\_PAGE\_FAULT bug check has a value of 0x00000158. This indicates that the IOMMU has delivered a page fault packet for an invalid ASID. This is not safe since the ASID may have already been reused.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## ILLEGAL\_IOMMU\_PAGE\_FAULT Parameters


| Parameter | Description                           |
|-----------|---------------------------------------|
| 1         | The invalid ASID.                     |
| 2         | The number of ASIDs currently in use. |
| 3         | The process using this ASID.          |
| 4         | The ASID's reference count.           |

 

 

 




