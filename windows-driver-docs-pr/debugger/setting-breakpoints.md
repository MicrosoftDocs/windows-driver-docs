---
title: Setting Breakpoints
description: Setting Breakpoints
ms.assetid: 9715c35a-0c8c-4e89-be28-2899f21ec964
keywords: ["Debugger Engine API, setting breakpoints"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Setting Breakpoints


## <span id="ddk_using_breakpoints_dbx"></span><span id="DDK_USING_BREAKPOINTS_DBX"></span>


Breakpoints are created with the [**AddBreakpoint**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-addbreakpoint) method. This method creates an [IDebugBreakpoint](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugbreakpoint) object that represents the breakpoint. It also set the *breakpoint type* (software breakpoint or processor breakpoint). Once a breakpoint has been created, its type cannot be changed.

Breakpoints are deleted with the [**RemoveBreakpoint**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-removebreakpoint) method. This also deletes the **IDebugBreakpoint** object; this object may not be used again.

**Note**   Although **IDebugBreakpoint** implements the **IUnknown** interface, the methods **IUnknown::AddRef** and **IUnknown::Release** are not used to control the lifetime of the breakpoint. These methods have no effect on the lifetime of the breakpoint. Instead, an **IDebugBreakpoint** object is deleted after the method [**RemoveBreakpoint**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-removebreakpoint) is called.

 

When the breakpoint is created, it is given a unique *breakpoint ID*. This identifier will not change. However, after the breakpoint has been deleted, its ID may be used for another breakpoint. For details on how to receive notification of the removal of a breakpoint, see [Monitoring Events](monitoring-events.md).

When a breakpoint is created, it is initially disabled; this means that it will not cause the target to stop executing. This breakpoint may be enabled by using the method [**AddFlags**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugbreakpoint2-addflags) to add the DEBUG\_BREAKPOINT\_ENABLED flag.

When a breakpoint is first created, it has the memory location 0x00000000 associated with it. The location can be changed by using [**SetOffset**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugbreakpoint2-setoffset) with an address, or by using [**SetOffsetExpression**](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugbreakpoint2-setoffsetexpression) with a symbolic expression. The breakpoint's location should be changed from its initial value before it is used.

 

 





