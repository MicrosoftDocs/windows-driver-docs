---
title: amli bl
description: The amli bl extension displays a list of all AML breakpoints.
ms.assetid: 4ce52006-d44e-40ab-b669-2aa9509b6b21
keywords: ["amli bl Windows Debugging"]
topic_type:
- apiref
api_name:
- amli bl
api_type:
- NA
---

# !amli bl


The **!amli bl** extension displays a list of all AML breakpoints.

Syntax

``` syntax
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

```
kd> !amli bl
 0: <e> ffffffff80e5e2f1:[\_SB.LNKD._SRS]
 1: <e> ffffffff80e5d969:[\_SB.LNKB._STA]
 2: <d> ffffffff80e630c9:[\_WAK]
 3: <e> ffffffff80e612c9:[\_SB.MBRD._CRS]
```

The first column gives the breakpoint number. The **&lt;e&gt;** and **&lt;d&gt;** marks indicate whether the breakpoint is enabled or disabled. The address of the breakpoint is in the next column. Finally, the method containing the breakpoint is listed, with the offset of the breakpoint if it is not set at the start of the method.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!amli%20bl%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




