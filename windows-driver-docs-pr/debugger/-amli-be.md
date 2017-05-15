---
title: amli be
description: The amli be extension enables an AML breakpoint.
ms.assetid: 75c0c05f-8c56-4489-a798-2e5ec6ca26d8
keywords: ["amli be Windows Debugging"]
topic_type:
- apiref
api_name:
- amli be
api_type:
- NA
---

# !amli be


The **!amli be** extension enables an AML breakpoint.

Syntax

``` syntax
!amli be Breakpoint!amli be *
```

## <span id="ddk__amli_be_dbg"></span><span id="DDK__AMLI_BE_DBG"></span>Parameters


<span id="_______Breakpoint______"></span><span id="_______breakpoint______"></span><span id="_______BREAKPOINT______"></span> *Breakpoint*   
Specifies the breakpoint number of the breakpoint to be enabled.

<span id="______________"></span> **\***   
Specifies that all breakpoints should be enabled.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about related commands and their uses, see [The AMLI Debugger](the-amli-debugger.md).

Remarks
-------

All breakpoints are enabled when they are created. Breakpoints are only disabled if you have used the [**!amli bd**](-amli-bd.md) extension.

To determine the breakpoint number of a breakpoint, use the [**!amli bl**](-amli-bl.md) extension.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!amli%20be%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




