---
title: C30032
description: Warning C30032 Calling a memory allocating function and forcing the request of executable memory through use of the POOL_NX_OPTOUT directive.
ms.assetid: 7C6F9ACE-DD02-45A7-A601-C5C7A5C89256
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C30032


warning C30032: Calling a memory allocating function and forcing the request of executable memory through use of the [POOL\_NX\_OPTOUT](https://msdn.microsoft.com/library/windows/hardware/hh920401) directive

BANNED\_MEM\_ALLOCATION\_FORCE\_UNSAFE

The preprocessor directive [POOL\_NX\_OPTOUT](https://msdn.microsoft.com/library/windows/hardware/hh920401) prevents the auto-promotion of non-safe types (**MM\_PAGE\_PRIORITY** and **POOL\_TYPE**) to safe types (for example, NonPagedPool to NonPagedPoolNx). The use of POOL\_NX\_OPTOUT in your sources is likely by design. If this is by design and executable memory is required, then you can suppress the warning with [Pragma Prefast to Suppress Warning Messages](https://msdn.microsoft.com/library/gg155764.aspx). This type of allocation is not permitted on Windows 10 systems that have opted-in to additional memory protections.

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

 

 





