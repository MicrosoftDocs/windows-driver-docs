---
title: amli bp
description: The amli bp extension places a breakpoint in AML code.
ms.assetid: 830df6b8-835c-4485-a28a-e9a028f166f5
keywords: ["amli bp Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- amli bp
api_type:
- NA
---

# !amli bp


The **!amli bp** extension places a breakpoint in AML code.

Syntax

```
!amli bp { MethodName | CodeAddress }
```

## <span id="ddk__amli_bp_dbg"></span><span id="DDK__AMLI_BP_DBG"></span>Parameters


<span id="_______MethodName______"></span><span id="_______methodname______"></span><span id="_______METHODNAME______"></span> *MethodName*   
Specifies the full path of the method name on which the breakpoint will be set.

<span id="_______CodeAddress______"></span><span id="_______codeaddress______"></span><span id="_______CODEADDRESS______"></span> *CodeAddress*   
Specifies the address of the AML code at which the breakpoint will be set. If *CodeAddress* is prefixed with two percent signs (**%%**), it is interpreted as a physical address. Otherwise, it is interpreted as a virtual address.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about related commands and their uses, see [The AMLI Debugger](the-amli-debugger.md).

Remarks
-------

The AMLI Debugger supports a maximum of 10 breakpoints.

Here is an example. The following command will set a breakpoint on the \_DCK method:

```
kd> !amli bp \_sb.pci0.dock._dck
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!amli%20bp%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




