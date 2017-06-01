---
title: amli r
description: The amli r extension displays information about the current context or the specified context.
ms.assetid: 1a8977ed-a420-4f68-8580-8e7446075283
keywords: ["amli r Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- amli r
api_type:
- NA
---

# !amli r


The **!amli r** extension displays information about the current context or the specified context.

Syntax

```
!amli r [ContextAddress]
```

## <span id="ddk__amli_r_dbg"></span><span id="DDK__AMLI_R_DBG"></span>Parameters


<span id="_______ContextAddress______"></span><span id="_______contextaddress______"></span><span id="_______CONTEXTADDRESS______"></span> *ContextAddress*   
Specifies the address of the context block to be displayed. The address of a context block can be determined from the **Ctxt** field in the [**!amli lc**](-amli-lc.md) display. If *ContextAddress* is prefixed with two percent signs (**%%**), it is interpreted as a physical address. Otherwise, it is interpreted as a virtual address. If this parameter is omitted, the current context is displayed.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about related commands and their uses, see [The AMLI Debugger](the-amli-debugger.md).

Remarks
-------

If the AMLI Debugger prompt appears suddenly, this is a useful command to use.

For example, the following command will display the current context of the interpreter:

```
AMLI(? for help)-> r

Context=c18b4000*, Queue=00000000, ResList=00000000
ThreadID=c15a6618, Flags=00000010
StackTop=c18b5eec, UsedStackSize=276 bytes, FreeStackSize=7636 bytes
LocalHeap=c18b40c0, CurrentHeap=c18b40c0, UsedHeapSize=88 bytes
Object=\_WAK, Scope=\_WAK, ObjectOwner=c18b4108, SyncLevel=0
AsyncCallBack=ff06b5d0, CallBackData=0, CallBackContext=c99efddc

MethodObject=\_WAK
80e0ff5c: Local0=Unknown()
80e0ff70: Local1=Unknown()
80e0ff84: Local2=Unknown()
80e0ff98: Local3=Unknown()
80e0ffac: Local4=Unknown()
80e0ffc0: Local5=Unknown()
80e0ffd4: Local6=Unknown()
80e0ffe8: Local7=Unknown()
80e0e040: RetObj=Unknown()

Next AML Pointer: ffffffff80e630df:[\_WAK+16]

ffffffff80e630df : If(S4BW
ffffffff80e630e5 : {
ffffffff80e630e5 : | Store(Zero, S4BW)
ffffffff80e630eb : }
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!amli%20r%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




