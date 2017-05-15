---
title: amli ds
description: The amli ds extension displays an AML stack.
ms.assetid: 62a1a1dd-c0d8-4509-a29f-16ad2b96b412
keywords: ["amli ds Windows Debugging"]
topic_type:
- apiref
api_name:
- amli ds
api_type:
- NA
---

# !amli ds


The **!amli ds** extension displays an AML stack.

Syntax

``` syntax
    !amli ds [/v] [Address] 
```

## <span id="ddk__amli_ds_dbg"></span><span id="DDK__AMLI_DS_DBG"></span>Parameters


<span id="________v______"></span><span id="________V______"></span> **/v**   
Causes the display to be verbose. In Windows 2000, this option is available only if you are using the checked build of this extension (w2kchk\\Acpikd.dll).

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the context block whose stack is desired. If *Address* is omitted, the current context is used.

### <span id="DLL"></span><span id="dll"></span>DLL

The !stacks extension displays information about the kernel stacks.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about related commands and their uses, see [The AMLI Debugger](the-amli-debugger.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!amli%20ds%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




