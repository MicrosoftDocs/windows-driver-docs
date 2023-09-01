---
title: chklowmem (WinDbg)
description: The chklowmem extension determines whether physical memory pages below 4 GB are filled with the required fill pattern on a computer that was booted with the /pae and /nolowmem options.
keywords: ["PAE (physical address extension)", "chklowmem Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- chklowmem
api_type:
- NA
---

# !chklowmem


The **!chklowmem** extension determines whether physical memory pages below 4 GB are filled with the required fill pattern on a computer that was booted with the [**/pae**](https://support.microsoft.com/help/833721/available-switch-options-for-the-windows-xp-and-the-windows-server-200) and [**/nolowmem**](https://support.microsoft.com/help/833721/available-switch-options-for-the-windows-xp-and-the-windows-server-200) options.

```dbgsyntax
!chklowmem
```

### DLL

Kdexts.dll

 

## Remarks

This extension is useful when you are verifying that kernel-mode drivers operate properly with physical memory above the 4 GB boundary. Typically, drivers fail by truncating a physical address to 32 bits and then in writing below the 4 GB boundary. The **!chklowmem** extension will detect any writes below the 4 GB boundary.

 

