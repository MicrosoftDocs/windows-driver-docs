---
title: amli bl
description: The amli bl extension displays a list of all AML breakpoints.
ms.assetid: 4ce52006-d44e-40ab-b669-2aa9509b6b21
keywords: ["amli bl Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- amli bl
api_type:
- NA
ms.localizationpriority: medium
---

# !amli bl


The **!amli bl** extension displays a list of all AML breakpoints.

Syntax

```dbgcmd
   !amli bl
```

## <span id="ddk__amli_bl_dbg"></span><span id="DDK__AMLI_BL_DBG"></span>


### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about related commands and their uses, see [The AMLI Debugger](the-amli-debugger.md).

Remarks
-------

The AMLI Debugger supports a maximum of ten breakpoints.

Here is an example of the **!amli bl** extension:

```console
kd> !amli bl
 0: <e> ffffffff80e5e2f1:[\_SB.LNKD._SRS]
 1: <e> ffffffff80e5d969:[\_SB.LNKB._STA]
 2: <d> ffffffff80e630c9:[\_WAK]
 3: <e> ffffffff80e612c9:[\_SB.MBRD._CRS]
```

The first column gives the breakpoint number. The **&lt;e&gt;** and **&lt;d&gt;** marks indicate whether the breakpoint is enabled or disabled. The address of the breakpoint is in the next column. Finally, the method containing the breakpoint is listed, with the offset of the breakpoint if it is not set at the start of the method.

 

 





