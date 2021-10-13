---
title: atom (WinDbg)
description: The atom extension displays the formatted atom table for the specified atom or for all atoms of the current process.
keywords: ["atom Windows Debugging"]
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- atom
api_type:
- NA
ms.localizationpriority: medium
---

# !atom


The **!atom** extension displays the formatted atom table for the specified atom or for all atoms of the current process.

```dbgcmd
    !atom [Address] 
```

## <span id="ddk__atom_dbg"></span><span id="DDK__ATOM_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal virtual address of the atom to display. If you omit this parameter or specify zero, the atom table for the current process is displayed. This table lists all atoms for the process.

### <span id="DLL"></span><span id="dll"></span>DLL

<p>Exts.dll</p>
 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about atoms and atom tables, see the Microsoft Windows SDK documentation.

 

 





