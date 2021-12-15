---
title: WdbgExts Functions
description: WdbgExts Functions
keywords: ["WdbgExts extensions, functions"]
ms.date: 11/28/2017
---

# WdbgExts Functions


## <span id="ddk_wdbgexts_functions_dbwx"></span><span id="DDK_WDBGEXTS_FUNCTIONS_DBWX"></span>


The wdbgexts.h header file contains prototypes for the following functions. These functions use the same prototype for both 32-bit and 64-bit extensions:

[**GetContext**](/previous-versions/windows/hardware/previsioning-framework/ff545736(v=vs.85))

[**SetContext**](/previous-versions/windows/hardware/previsioning-framework/ff556644(v=vs.85))

[**CheckControlC**](/windows-hardware/drivers/ddi/wdbgexts/nc-wdbgexts-pwindbg_check_control_c)

[**GetCurrentProcessAddr**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-getcurrentprocessaddr)

[**GetCurrentProcessHandle**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects-getcurrentprocesshandle)

[**GetCurrentThreadAddr**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-getcurrentthreadaddr)

[**GetDebuggerCacheSize**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-getdebuggercachesize)

[**GetDebuggerData**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-getdebuggerdata)

[**Disasm**](/windows-hardware/drivers/ddi/wdbgexts/nc-wdbgexts-pwindbg_disasm)

[**dprintf**](/windows-hardware/drivers/ddi/wdbgexts/nc-wdbgexts-pwindbg_output_routine)

[**GetExpression**](/windows-hardware/drivers/ddi/wdbgexts/nc-wdbgexts-pwindbg_get_expression)

[**GetExpressionEx**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-getexpressionex)

[**GetInputLine**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-getinputline)

[**Ioctl**](/windows-hardware/drivers/ddi/wdbgexts/nc-wdbgexts-pwindbg_ioctl_routine)

[**GetKdContext**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-getkdcontext)

[**ReadMemory**](/previous-versions/windows/hardware/previsioning-framework/ff554287(v=vs.85))

[**SearchMemory**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-searchmemory)

[**WriteMemory**](/previous-versions/windows/hardware/previsioning-framework/ff561420(v=vs.85))

[**ReadMsr**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-readmsr)

[**WriteMsr**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-writemsr)

[**GetPebAddress**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-getpebaddress)

[**ReadPhysical**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-readphysical)

[**ReadPhysicalWithFlags**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-readphysicalwithflags)

[**WritePhysical**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-writephysical)

[**WritePhysicalWithFlags**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-writephysicalwithflags)

[**GetTebAddress**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-gettebaddress)

[**StackTrace**](/windows-hardware/drivers/ddi/wdbgexts/nc-wdbgexts-pwindbg_stacktrace_routine)

[**GetSymbol**](/windows-hardware/drivers/ddi/wdbgexts/nc-wdbgexts-pwindbg_get_symbol)

[**ReloadSymbols**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-reloadsymbols)

[**GetSetSympath**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-getsetsympath)

[**TranslateVirtualToPhysical**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-translatevirtualtophysical)

The wdbgexts.h header file contains prototypes for the following functions. These functions have different prototypes for 32-bit and 64-bit extensions:

[**ReadControlSpace**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-readcontrolspace)

[**ReadControlSpace64**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-readcontrolspace64)

[**ReadTypedControlSpace32**](/previous-versions/ff554339(v=vs.85))

[**ReadTypedControlSpace64**](/previous-versions/ff554341(v=vs.85))

[**WriteControlSpace**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-writecontrolspace)

[**ReadIoSpace**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-readiospace)

[**ReadIoSpace64**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-readiospace64)

[**ReadIoSpaceEx**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-readiospaceex)

[**ReadIoSpaceEx64**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-readiospaceex64)

[**WriteIoSpace**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-writeiospace)

[**WriteIoSpace64**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-writeiospace64)

[**WriteIoSpaceEx**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-writeiospaceex)

[**WriteIoSpaceEx64**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-writeiospaceex64)

[**SetThreadForOperation**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-setthreadforoperation)

[**SetThreadForOperation64**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-setthreadforoperation64)

The wdbgexts.h header file contains prototypes for the following functions. These functions can be used only in 64-bit extensions:

[**GetFieldData**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-getfielddata)

[**GetFieldOffset**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols-getfieldoffset)

[**GetFieldValue**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-getfieldvalue)

[**GetShortField**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-getshortfield)

[**ReadField**](/previous-versions/ff553539(v=vs.85))

[**ReadListEntry**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-readlistentry)

[**ReadPointer**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-readpointer)

[**WritePointer**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-writepointer)

[**IsPtr64**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-isptr64)

[**ReadPtr**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-readptr)

[**GetTypeSize**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-gettypesize)

[**InitTypeRead**](/previous-versions/ff550953(v=vs.85))

[**InitTypeReadPhysical**](/previous-versions/ff550957(v=vs.85))

[**ListType**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-listtype)

 

