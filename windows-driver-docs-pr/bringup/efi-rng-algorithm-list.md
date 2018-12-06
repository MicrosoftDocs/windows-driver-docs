---
title: EFI_RNG_ALGORITHM_LIST structure
description: This data structure contains a list of the supported Random Number Generation (RNG) algorithms.
ms.assetid: 1481330F-78F3-4C18-BD19-3B4984E0138F
keywords:
- EFI_RNG_ALGORITHM_LIST structure
- PEFI_RNG_ALGORITHM_LIST structure pointer
topic_type:
- apiref
api_name:
- EFI_RNG_ALGORITHM_LIST
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_RNG\_ALGORITHM\_LIST structure


This data structure contains a list of the supported Random Number Generation (RNG) algorithms.

Syntax
------

```cpp
typedef struct _EFI_RNG_ALGORITHM_LIST {
  UINT32     AlgorithmsCount;
  EFI_GUID * Algorithms;
} EFI_RNG_ALGORITHM_LIST, *PEFI_RNG_ALGORITHM_LIST;
```

Members
-------

**AlgorithmsCount**  
The number of algorithms in the list.

**Algorithms**  
Pointer to a list of RNG algorithms. Each algorithm is `sizeof(EFI_GUID)` bytes long. It is the caller's responsibility to free this memory by using EFI\_BOOT\_SERVICES-&gt;FreePool().

Remarks
-------

An implementation may support one or more ways to provide RNG values. The list of supported RNG algorithms is represented in this structure.

The following list provides EFI GUID values for a selection of EFI\_RNG\_PROTOCOL algorithms. The list is not meant to be exhaustive and may be augmented by vendors or other industry standards.

```cpp
#define EFI_RNG_ALGORITHM_SP800_90_HASH_256_GUID   \
  {0xa7af67cb, 0x603b, 0x4d42, 0xba, 0x21, 0x70, 0xbf, 0xb6, 0x29,\
   0x3f, 0x96}
#define EFI_RNG_ALGORITHM_SP800_90_HMAC_256_GUID    \
  {0xc5149b43, 0xae85, 0x4f53, 0x99, 0x82, 0xb9, 0x43, 0x35, 0xd3,\
   0xa9, 0xe7}
#define EFI_RNG_ALGORITHM_SP800_90_CTR_256_GUID \
  {0x44f0de6e, 0x4d8c, 0x4045, 0xa8, 0xc7, 0x4d, 0xd1, 0x68, 0x85,\
   0x6b, 0x9e}
```
