---
title: amli bc
description: The amli bc extension permanently clears an AML breakpoint.
ms.assetid: e975ee10-cd2f-4944-8d00-b2eda2dd099a
keywords: ["amli bc Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- amli bc
api_type:
- NA
---

# !amli bc


The **!amli bc** extension permanently clears an AML breakpoint.

Syntax

```
!amli bc Breakpoint 
!amli bc *
```

## <span id="ddk__amli_bc_dbg"></span><span id="DDK__AMLI_BC_DBG"></span>Parameters


<span id="_______Breakpoint______"></span><span id="_______breakpoint______"></span><span id="_______BREAKPOINT______"></span> *Breakpoint*   
Specifies the number of the breakpoint to be cleared.

<span id="______________"></span> **\***   
Specifies that all breakpoints should be cleared.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about related commands and their uses, see [The AMLI Debugger](the-amli-debugger.md).

Remarks
-------

To determine the breakpoint number of a breakpoint, use the [**!amli bl**](-amli-bl.md) extension.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!amli%20bc%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




