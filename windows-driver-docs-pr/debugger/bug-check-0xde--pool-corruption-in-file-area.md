---
title: Bug Check 0xDE POOL_CORRUPTION_IN_FILE_AREA
description: The POOL_CORRUPTION_IN_FILE_AREA bug check has a value of 0x000000DE. This indicates that a driver has corrupted pool memory that is used for holding pages destined for disk.
keywords: ["Bug Check 0xDE POOL_CORRUPTION_IN_FILE_AREA", "POOL_CORRUPTION_IN_FILE_AREA"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- POOL_CORRUPTION_IN_FILE_AREA
api_type:
- NA
---

# Bug Check 0xDE: POOL\_CORRUPTION\_IN\_FILE\_AREA


The POOL\_CORRUPTION\_IN\_FILE\_AREA bug check has a value of 0x000000DE. This indicates that a driver has corrupted pool memory that is used for holding pages destined for disk.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## POOL\_CORRUPTION\_IN\_FILE\_AREA Parameters


None

## Cause

When the Memory Manager dereferenced the file, it discovered this corruption in pool memory.

 

 




