---
title: C30032 warning
description: Warning C30032 Calling a memory allocating function and forcing the request of executable memory through use of the POOL_NX_OPTOUT directive.
ms.date: 04/20/2017
f1_keywords: 
  - "C30032"
---

# C30032


warning C30032: Calling a memory allocating function and forcing the request of executable memory through use of the [POOL\_NX\_OPTOUT](../kernel/selective-opt-out-pool-nx-optout.md) directive

BANNED\_MEM\_ALLOCATION\_FORCE\_UNSAFE

The preprocessor directive [POOL\_NX\_OPTOUT](../kernel/selective-opt-out-pool-nx-optout.md) prevents the auto-promotion of non-safe types (**MM\_PAGE\_PRIORITY** and **POOL\_TYPE**) to safe types (for example, NonPagedPool to NonPagedPoolNx). The use of POOL\_NX\_OPTOUT in your sources is likely by design. If this is by design and executable memory is required, then you can suppress the warning with [Pragma Prefast to Suppress Warning Messages](/previous-versions/windows/embedded/gg155764(v=winembedded.70)). This type of allocation is not permitted on Windows 10 systems that have opted-in to additional memory protections.

## <span id="Example"></span><span id="example"></span><span id="EXAMPLE"></span>Example


The following code generates this warning:

In the sources file:

```
C_DEFINES=$(C_DEFINES) –DUNICODE -DPOOL_NX_OPTOUT=1
```

in the code file:

```
pPtr = MmGetSystemAddressForMdlSafe( pMdl, NormalPagePriority);
```

The following code avoids this warning:

In the sources file, add:

```
C_DEFINES=$(C_DEFINES) -DUNICODE -DPOOL_NX_OPTIN_AUTO=1
```

in the code file:

```
pPtr = MmGetSystemAddressForMdlSafe( pMdl, NormalPagePriority);
```

 

