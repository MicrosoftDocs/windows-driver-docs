---
title: WdbgExts Functions
description: WdbgExts Functions
ms.assetid: 1b070b0c-575d-4104-af66-e0a2c2f2c1b6
keywords: ["WdbgExts extensions, functions"]
ms.author: domars
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WdbgExts Functions


## <span id="ddk_wdbgexts_functions_dbwx"></span><span id="DDK_WDBGEXTS_FUNCTIONS_DBWX"></span>


The wdbgexts.h header file contains prototypes for the following functions. These functions use the same prototype for both 32-bit and 64-bit extensions:

[**GetContext**](https://msdn.microsoft.com/library/windows/hardware/ff545736)

[**SetContext**](https://msdn.microsoft.com/library/windows/hardware/ff556644)

[**CheckControlC**](https://msdn.microsoft.com/library/windows/hardware/ff539072)

[**GetCurrentProcessAddr**](https://msdn.microsoft.com/library/windows/hardware/ff545779)

[**GetCurrentProcessHandle**](https://msdn.microsoft.com/library/windows/hardware/ff545816)

[**GetCurrentThreadAddr**](https://msdn.microsoft.com/library/windows/hardware/ff545889)

[**GetDebuggerCacheSize**](https://msdn.microsoft.com/library/windows/hardware/ff546568)

[**GetDebuggerData**](https://msdn.microsoft.com/library/windows/hardware/ff546573)

[**Disasm**](https://msdn.microsoft.com/library/windows/hardware/ff541945)

[**dprintf**](https://msdn.microsoft.com/library/windows/hardware/ff542750)

[**GetExpression**](https://msdn.microsoft.com/library/windows/hardware/ff546683)

[**GetExpressionEx**](https://msdn.microsoft.com/library/windows/hardware/ff546691)

[**GetInputLine**](https://msdn.microsoft.com/library/windows/hardware/ff546905)

[**Ioctl**](https://msdn.microsoft.com/library/windows/hardware/ff551084)

[**GetKdContext**](https://msdn.microsoft.com/library/windows/hardware/ff546962)

[**ReadMemory**](https://msdn.microsoft.com/library/windows/hardware/ff554287)

[**SearchMemory**](https://msdn.microsoft.com/library/windows/hardware/ff554742)

[**WriteMemory**](https://msdn.microsoft.com/library/windows/hardware/ff561420)

[**ReadMsr**](https://msdn.microsoft.com/library/windows/hardware/ff554289)

[**WriteMsr**](https://msdn.microsoft.com/library/windows/hardware/ff561424)

[**GetPebAddress**](https://msdn.microsoft.com/library/windows/hardware/ff548122)

[**ReadPhysical**](https://msdn.microsoft.com/library/windows/hardware/ff554310)

[**ReadPhysicalWithFlags**](https://msdn.microsoft.com/library/windows/hardware/ff554315)

[**WritePhysical**](https://msdn.microsoft.com/library/windows/hardware/ff561432)

[**WritePhysicalWithFlags**](https://msdn.microsoft.com/library/windows/hardware/ff561448)

[**GetTebAddress**](https://msdn.microsoft.com/library/windows/hardware/ff549267)

[**StackTrace**](https://msdn.microsoft.com/library/windows/hardware/ff558794)

[**GetSymbol**](https://msdn.microsoft.com/library/windows/hardware/ff548447)

[**ReloadSymbols**](https://msdn.microsoft.com/library/windows/hardware/ff554381)

[**GetSetSympath**](https://msdn.microsoft.com/library/windows/hardware/ff548291)

[**TranslateVirtualToPhysical**](https://msdn.microsoft.com/library/windows/hardware/ff558914)

The wdbgexts.h header file contains prototypes for the following functions. These functions have different prototypes for 32-bit and 64-bit extensions:

[**ReadControlSpace**](https://msdn.microsoft.com/library/windows/hardware/ff553527)

[**ReadControlSpace64**](https://msdn.microsoft.com/library/windows/hardware/ff553532)

[**ReadTypedControlSpace32**](https://msdn.microsoft.com/library/windows/hardware/ff554339)

[**ReadTypedControlSpace64**](https://msdn.microsoft.com/library/windows/hardware/ff554341)

[**WriteControlSpace**](https://msdn.microsoft.com/library/windows/hardware/ff561375)

[**ReadIoSpace**](https://msdn.microsoft.com/library/windows/hardware/ff553574)

[**ReadIoSpace64**](https://msdn.microsoft.com/library/windows/hardware/ff553577)

[**ReadIoSpaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff553580)

[**ReadIoSpaceEx64**](https://msdn.microsoft.com/library/windows/hardware/ff553583)

[**WriteIoSpace**](https://msdn.microsoft.com/library/windows/hardware/ff561406)

[**WriteIoSpace64**](https://msdn.microsoft.com/library/windows/hardware/ff561408)

[**WriteIoSpaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff561413)

[**WriteIoSpaceEx64**](https://msdn.microsoft.com/library/windows/hardware/ff561414)

[**SetThreadForOperation**](https://msdn.microsoft.com/library/windows/hardware/ff556830)

[**SetThreadForOperation64**](https://msdn.microsoft.com/library/windows/hardware/ff556832)

The wdbgexts.h header file contains prototypes for the following functions. These functions can be used only in 64-bit extensions:

[**GetFieldData**](https://msdn.microsoft.com/library/windows/hardware/ff546743)

[**GetFieldOffset**](https://msdn.microsoft.com/library/windows/hardware/ff546758)

[**GetFieldValue**](https://msdn.microsoft.com/library/windows/hardware/ff546781)

[**GetShortField**](https://msdn.microsoft.com/library/windows/hardware/ff548299)

[**ReadField**](https://msdn.microsoft.com/library/windows/hardware/ff553539)

[**ReadListEntry**](https://msdn.microsoft.com/library/windows/hardware/ff553585)

[**ReadPointer**](https://msdn.microsoft.com/library/windows/hardware/ff554318)

[**WritePointer**](https://msdn.microsoft.com/library/windows/hardware/ff561450)

[**IsPtr64**](https://msdn.microsoft.com/library/windows/hardware/ff551094)

[**ReadPtr**](https://msdn.microsoft.com/library/windows/hardware/ff554330)

[**GetTypeSize**](https://msdn.microsoft.com/library/windows/hardware/ff549446)

[**InitTypeRead**](https://msdn.microsoft.com/library/windows/hardware/ff550953)

[**InitTypeReadPhysical**](https://msdn.microsoft.com/library/windows/hardware/ff550957)

[**ListType**](https://msdn.microsoft.com/library/windows/hardware/ff551988)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20WdbgExts%20Functions%20%20RELEASE:%20%2811/27/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




