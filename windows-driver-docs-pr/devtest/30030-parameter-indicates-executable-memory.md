---
title: C30030
description: Warning C30030 Calling a memory allocating function and passing a parameter that indicates executable memory.
ms.assetid: D1C8B316-DC04-4B18-A0EB-40833D50B843
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C30030


warning C30030: Calling a memory allocating function and passing a parameter that indicates executable memory

BANNED\_MEM\_ALLOCATION\_UNSAFE

Some APIs have parameters that configure whether memory is executable or not. This error indicates that parameters are used that result in executable NonPagedPool being allocated. You should use one of the available options to request non-executable memory.

## <span id="For_defects_involving_the_parameter_types_MM_PAGE_PRIORITY_and_POOL_TYPE"></span><span id="for_defects_involving_the_parameter_types_mm_page_priority_and_pool_type"></span><span id="FOR_DEFECTS_INVOLVING_THE_PARAMETER_TYPES_MM_PAGE_PRIORITY_AND_POOL_TYPE"></span>For defects involving the parameter types **MM\_PAGE\_PRIORITY** and **POOL\_TYPE**


Use one of the following options:

-   Specify the preprocessor definition [POOL\_NX\_OPTIN\_AUTO](https://msdn.microsoft.com/library/windows/hardware/hh920390) in the sources/project settings.
-   Specify the pre-processor definition [POOL\_NX\_OPTIN](https://msdn.microsoft.com/library/windows/hardware/hh920402) in the sources/project settings and call **ExInitializeDriverRuntime(*DrvRtPoolNxOptIn*)** from the driver initialization function (**DriverEntry** or **DllInitialize**).

**Note**  The choice of whether to use [POOL\_NX\_OPTIN\_AUTO](https://msdn.microsoft.com/library/windows/hardware/hh920390) or [POOL\_NX\_OPTIN](https://msdn.microsoft.com/library/windows/hardware/hh920402) largely depends on which platform you are targeting and how many binaries you are making. Both of these options result in these two types being changed for you (either by the compiler or at run time) to their NX equivalents. See the topic links for more information.



**Note**  You may see a false positive warning if one of the following conditions is true:
-   The driver initialization function calls another function that calls **ExInitializeDriverRuntime(*DrvRtPoolNxOptIn*)**
-   You are creating a **DRIVER\_LIBRARY** and have specified [POOL\_NX\_OPTIN](https://msdn.microsoft.com/library/windows/hardware/hh920402) but have no initialization function.



-   Change the allocation type to a non-executable type.

**Example (POOL\_NX\_OPTIN\_AUTO):**

The following setting in the sources file would allow the warning should an executable parameter be supplied in an API call:

```
C_DEFINES=$(C_DEFINES)
```

The following setting in the sources file avoids the warning:

```
C_DEFINES=$(C_DEFINES) -DPOOL_NX_OPTIN_AUTO=1
```

**Example (POOL\_NX\_OPTIN):**

The following code in the sources file generates a warning:

```
C_DEFINES=$(C_DEFINES)
```

The following code in the sources file avoids the warning:

```
C_DEFINES=$(C_DEFINES) -DPOOL_NX_OPTIN=1
```

In **DriverEntry()**, before any memory allocation takes place:

```
NTSTATUS
DriverEntry (
    _In_ PDRIVER_OBJECT DriverObject,
    _In_ PUNICODE_STRING RegistryPath
    )
{
    NTSTATUS status;

    ExInitializeDriverRuntime( DrvRtPoolNxOptIn );
…
```

**Example (Change the allocation type):**

For the **MM\_PAGE\_PRIORITY** type you can fix this by adding the **MdlMappingNoExecute** flag to the priority type. This is only supported on Windows 8 and later.

The following code generates a warning:

```
pPtr = MmGetSystemAddressForMdlSafe( pMdl, NormalPagePriority);
```

The following code avoids the warning:

```
pPtr = MmGetSystemAddressForMdlSafe( pMdl, NormalPagePriority | MdlMappingNoExecute);
```

**Example (POOL\_TYPE)**

For the **POOL\_TYPE** type you can fix this by changing the request type to the non-executable version of the type. This is only supported on Windows 8 and later.

The following code generates a warning:

```
ExAllocatePoolWithTag(NonPagedPool, numberOfBytes, &#39;xppn&#39;);
```

The following code avoids the warning:

```
ExAllocatePoolWithTag(NonPagedPoolNx, numberOfBytes, &#39;xppn&#39;);
```

**Other special cases:**

There has been a change in the [**ExInitializeNPagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff545301) routine that now enables you to specify non-executable nonpaged pool memory. For example, the following code generates this warning:

```
ExInitializeNPagedLookasideList(pLookaside,
                NULL,
                NULL,
                0,
                size,
                tag,
                depth);
```

The following code avoids this warning:

```
ExInitializeNPagedLookasideList(pLookaside,
                NULL,
                NULL,
                POOL_NX_ALLOCATION,
                size,
                tag,
                depth);
```

## <span id="For_defects_involving_page_protections_"></span><span id="for_defects_involving_page_protections_"></span><span id="FOR_DEFECTS_INVOLVING_PAGE_PROTECTIONS_"></span>For defects involving page protections:


Some APIs allow you to specify page protections, [**ZwMapViewOfSection**](https://msdn.microsoft.com/library/windows/hardware/ff566481) is one of these. In these cases, use the non-executable version of the protection type.

Change:

-   PAGE\_EXECUTE to any of the below alternatives or PAGE\_NOACCESS
-   PAGE\_EXECUTE\_READ to PAGE\_READONLY
-   PAGE\_EXECUTE\_READWRITE to PAGE\_READWRITE
-   PAGE\_EXECUTE\_WRITECOPY to PAGE\_WRITECOPY

The following code generates a warning:

```
Status = ZwMapViewOfSection(   handle,
                NtCurrentProcess(),
                Address,
                0,
                0,
                &SectionOffset,
                Size,
                ViewUnmap,
                MEM_LARGE_PAGES,
                PAGE_EXECUTE_READWRITE
                ); 
```

The following code avoids this warning:

```
Status = ZwMapViewOfSection(   handle,
                NtCurrentProcess(),
                Address,
                0,
                0,
                &SectionOffset,
                Size,
                ViewUnmap,
                MEM_LARGE_PAGES,
                PAGE_READWRITE
                ); 
```

## <span id="For_defects_involving_cache_types_"></span><span id="for_defects_involving_cache_types_"></span><span id="FOR_DEFECTS_INVOLVING_CACHE_TYPES_"></span>For defects involving cache types:


Some APIs allocate memory with executable permissions dependent on a cache type. Two such APIs are [**MmAllocateContiguousMemorySpecifyCache**](https://msdn.microsoft.com/library/windows/hardware/ff554464) and [**MmAllocateContiguousMemorySpecifyCacheNode**](https://msdn.microsoft.com/library/windows/hardware/ff554469). Should a cache type of **MmCached** be used (see [**MEMORY\_CACHING\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff554430)), then executable memory will be allocated. To fix this, either select another caching type, or if cached memory is required then use the API [**MmAllocateContiguousNodeMemory**](https://msdn.microsoft.com/library/windows/hardware/jj602795).

Change:

-   **MmCached** to **MmNonCached** or **MmWriteCombined** if cached memory is not required
-   The API to [**MmAllocateContiguousNodeMemory**](https://msdn.microsoft.com/library/windows/hardware/jj602795) if cached memory is required

The following code generates a warning:

```
MmAllocateContiguousMemorySpecifyCache(       numberOfBytes,
                                              lowestAddress,
                                              highestAddress,
                                              NULL,
                                              MmCached,
                                              ); 
```

The following code avoids this warning if cached memory is not required:

```
MmAllocateContiguousMemorySpecifyCache(       numberOfBytes,
                                              lowestAddress,
                                              highestAddress,
                                              NULL,
                                              MmNonCached,
                                              ); 
```

The following code generates a warning:

```
MmAllocateContiguousMemorySpecifyCacheNode(   numberOfBytes,
                                              lowestAddress,
                                              highestAddress,
                                              NULL,
                                              MmCached,
                                              MM_ANY_NODE_OK
                                              ); 
```

The following code avoids this warning if cached memory is required:

```
MmAllocateContiguousNodeMemory(       numberOfBytes,
                                      lowestAddress,
                                      highestAddress,
                                      NULL,
                                      PAGE_READWRITE,
                                      MM_ANY_NODE_OK
                                      ); 
```

The following code use the alternative API when cached memory is not required:

```
MmAllocateContiguousNodeMemory(       numberOfBytes,
                                      lowestAddress,
                                      highestAddress,
                                      NULL,
                                      PAGE_READWRITE | PAGE_NOCACHE,
                                      MM_ANY_NODE_OK
                                      ); 
```

## <span id="related_topics"></span>Related topics


[**POOL\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff559707)










