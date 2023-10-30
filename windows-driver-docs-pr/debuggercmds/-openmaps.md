---
title: openmaps (WinDbg)
description: The openmaps extension displays the referenced buffer control blocks (BCBs) and virtual address control blocks (VACBs) for the specified shared cache map.
keywords: ["BCB (buffer control block)", "VACB (virtual address control block)", "shared cache map", "cache manager", "openmaps Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- openmaps
api_type:
- NA
---

# !openmaps


The **!openmaps** extension displays the referenced buffer control blocks (BCBs) and virtual address control blocks (VACBs) for the specified shared cache map.

```dbgcmd
!openmaps Address [Flag]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the shared cache map.

<span id="_______Flag______"></span><span id="_______flag______"></span><span id="_______FLAG______"></span> *Flag*   
Determines which control blocks are displayed. If *Flag* is **1**, the debugger displays all control blocks. If *Flag* is **0**, the debugger displays only referenced control blocks. The default is **0**.

### DLL

Kdexts.dll

 

### Additional Information

For information about cache management, see the Microsoft Windows SDK documentation and *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

For information about other cache management extensions, see the [**!cchelp**](-cchelp.md) extension.

 

 





