---
title: Bug Check 0x158 ILLEGAL_IOMMU_PAGE_FAULT
description: The ILLEGAL_IOMMU_PAGE_FAULT bug check has a value of 0x00000158. This indicates that the IOMMU has delivered a page fault packet for an invalid ASID. 
ms.assetid: E26C9B67-A332-4AE9-9325-9A3378EC9B36
keywords: ["Bug Check 0x158 ILLEGAL_IOMMU_PAGE_FAULT", "ILLEGAL_IOMMU_PAGE_FAULT"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ILLEGAL_IOMMU_PAGE_FAULT
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x158: ILLEGAL\_IOMMU\_PAGE\_FAULT


The ILLEGAL\_IOMMU\_PAGE\_FAULT bug check has a value of 0x00000158. This indicates that the IOMMU has delivered a page fault packet for an invalid ASID. This is not safe since the ASID may have already been reused.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## ILLEGAL\_IOMMU\_PAGE\_FAULT Parameters


| Parameter | Description                           |
|-----------|---------------------------------------|
| 1         | The invalid ASID.                     |
| 2         | The number of ASIDs currently in use. |
| 3         | The process using this ASID.          |
| 4         | The ASID's reference count.           |

 

 

 




