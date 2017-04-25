---
title: Bug Check 0xDE POOL\_CORRUPTION\_IN\_FILE\_AREA
description: The POOL\_CORRUPTION\_IN\_FILE\_AREA bug check has a value of 0x000000DE. This indicates that a driver has corrupted pool memory that is used for holding pages destined for disk.
ms.assetid: 6394e0fa-76ee-4924-8aa3-d10a4d57c6e8
keywords: ["Bug Check 0xDE POOL_CORRUPTION_IN_FILE_AREA", "POOL_CORRUPTION_IN_FILE_AREA"]
topic_type:
- apiref
api_name:
- POOL_CORRUPTION_IN_FILE_AREA
api_type:
- NA
---

# Bug Check 0xDE: POOL\_CORRUPTION\_IN\_FILE\_AREA


The POOL\_CORRUPTION\_IN\_FILE\_AREA bug check has a value of 0x000000DE. This indicates that a driver has corrupted pool memory that is used for holding pages destined for disk.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](http://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## POOL\_CORRUPTION\_IN\_FILE\_AREA Parameters


None

Cause
-----

When the Memory Manager dereferenced the file, it discovered this corruption in pool memory.

 

 




