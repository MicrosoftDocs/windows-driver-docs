---
title: WdbgExts Memory Access
description: WdbgExts Memory Access
ms.date: 11/28/2017
---

# WdbgExts Memory Access


This topic provides a brief overview of how memory access can be performed using the WdbgExts API. For an overview of memory access in the [debugger engine](introduction.md#debugger-engine), see [Memory](memory.md) in the [Debugger Engine Overview](debugger-engine-overview.md) section of this documentation.

### <span id="virtual_memory"></span><span id="VIRTUAL_MEMORY"></span>Virtual Memory

The virtual memory of the target can be read by using the [**ReadMemory**](/previous-versions/windows/hardware/previsioning-framework/ff554287(v=vs.85)) function and written using the [**WriteMemory**](/previous-versions/windows/hardware/previsioning-framework/ff561420(v=vs.85)) function. Pointers in the target's memory can be read and written by using the [**ReadPointer**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-readpointer), [**ReadPtr**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-readptr), and [**WritePointer**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-writepointer) functions.

To search the virtual memory for a pattern of bytes, use the [**SearchMemory**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-searchmemory) function.

The [**TranslateVirtualToPhysical**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-translatevirtualtophysical) function can be used to convert a virtual memory address to a physical memory address.

The [**Disasm**](/windows-hardware/drivers/ddi/wdbgexts/nc-wdbgexts-pwindbg_disasm) function can be used to disassemble a single assembly instruction on the target.

To check the low 4 GB of memory for corruption when using physical address extension (PAE), use the [**Ioctl**](/windows-hardware/drivers/ddi/wdbgexts/nc-wdbgexts-pwindbg_ioctl_routine) operation [**IG\_LOWMEM\_CHECK**](/previous-versions/ff550931(v=vs.85)).

### <span id="physical_memory"></span><span id="PHYSICAL_MEMORY"></span>Physical Memory

Physical memory can only be directly accessed in kernel-mode debugging.

The physical memory on the target can be read by using the [**ReadPhysical**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-readphysical) and [**ReadPhysicalWithFlags**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-readphysicalwithflags) functions, and written by using the [**WritePhysical**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-writephysical) and [**WritePhysicalWithFlags**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-writephysicalwithflags) functions.

To search the physical memory for pointers to locations within a specified range, use the [**Ioctl**](/windows-hardware/drivers/ddi/wdbgexts/nc-wdbgexts-pwindbg_ioctl_routine) operation [**IG\_POINTER\_SEARCH\_PHYSICAL**](/windows-hardware/drivers/ddi/wdbgexts/ns-wdbgexts-_pointer_search_physical).

### <span id="other_data_spaces"></span><span id="OTHER_DATA_SPACES"></span>Other Data Spaces

In kernel-mode debugging, it is possible to read and write data to a variety of data spaces in addition to the main memory. The following data spaces can be accessed:

<span id="Control-Space_Memory"></span><span id="control-space_memory"></span><span id="CONTROL-SPACE_MEMORY"></span>Control-Space Memory  
The functions [**ReadControlSpace**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-readcontrolspace), [**ReadControlSpace64**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-readcontrolspace64), [**ReadTypedControlSpace32**](/previous-versions/ff554339(v=vs.85)), and [**ReadTypedControlSpace64**](/previous-versions/ff554341(v=vs.85)) will read data from a control space. The [**WriteControlSpace**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-writecontrolspace) function will write data to a control space.

<span id="I_O_Memory"></span><span id="i_o_memory"></span><span id="I_O_MEMORY"></span>I/O Memory  
The functions [**ReadIoSpace**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-readiospace), [**ReadIoSpace64**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-readiospace64), **ReadIoSpace64**, [**ReadIoSpaceEx64**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-readiospaceex64) will read data from system I/O memory and bus I/O memory. The functions [**WriteIoSpace**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-writeiospace), [**WriteIoSpace64**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-writeiospace64), [**WriteIoSpaceEx**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-writeiospaceex), and [**WriteIoSpaceEx64**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-writeiospaceex64) will write data to system I/O memory and bus I/O memory.

<span id="Model_Specific_Register__MSR_"></span><span id="model_specific_register__msr_"></span><span id="MODEL_SPECIFIC_REGISTER__MSR_"></span>Model Specific Register (MSR)  
The functions [**ReadMsr**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-readmsr) and [**WriteMsr**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-writemsr) read and write MSRs.

<span id="System_Bus"></span><span id="system_bus"></span><span id="SYSTEM_BUS"></span>System Bus  
The [**Ioctl**](/windows-hardware/drivers/ddi/wdbgexts/nc-wdbgexts-pwindbg_ioctl_routine) operations [**IG\_GET\_BUS\_DATA**](/windows-hardware/drivers/ddi/wdbgexts/ns-wdbgexts-_getsetbusdata) and **IG\_SET\_BUS\_DATA** read and write system bus data.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a more powerful memory access API, see [Memory Access](memory-access.md) in the [Using the Debugger Engine API](using-the-debugger-engine-api.md) section of this documentation.

 

