---
title: EFI\_RNG\_ALGORITHM\_LIST structure
description: This data structure contains a list of the supported Random Number Generation (RNG) algorithms.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1481330F-78F3-4C18-BD19-3B4984E0138F
keywords: ["EFI_RNG_ALGORITHM_LIST structure", "PEFI_RNG_ALGORITHM_LIST structure pointer"]
topic_type:
- apiref
api_name:
- EFI_RNG_ALGORITHM_LIST
api_type:
- NA
---

# EFI\_RNG\_ALGORITHM\_LIST structure


This data structure contains a list of the supported Random Number Generation (RNG) algorithms.

Syntax
------

```ManagedCPlusPlus
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

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_RNG_ALGORITHM_LIST%20structure%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




