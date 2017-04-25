---
title: WdbgExts Memory Access
description: WdbgExts Memory Access
ms.assetid: 7b600d18-343e-4c22-b1e9-5dcc83d88695
---

# WdbgExts Memory Access


This topic provides a brief overview of how memory access can be performed using the WdbgExts API. For an overview of memory access in the [debugger engine](introduction.md#debugger-engine), see [Memory](memory.md) in the [Debugger Engine Overview](debugger-engine-overview.md) section of this documentation.

### <span id="virtual_memory"></span><span id="VIRTUAL_MEMORY"></span>Virtual Memory

The virtual memory of the target can be read by using the [**ReadMemory**](https://msdn.microsoft.com/library/windows/hardware/ff554287) function and written using the [**WriteMemory**](https://msdn.microsoft.com/library/windows/hardware/ff561420) function. Pointers in the target's memory can be read and written by using the [**ReadPointer**](https://msdn.microsoft.com/library/windows/hardware/ff554318), [**ReadPtr**](https://msdn.microsoft.com/library/windows/hardware/ff554330), and [**WritePointer**](https://msdn.microsoft.com/library/windows/hardware/ff561450) functions.

To search the virtual memory for a pattern of bytes, use the [**SearchMemory**](https://msdn.microsoft.com/library/windows/hardware/ff554742) function.

The [**TranslateVirtualToPhysical**](https://msdn.microsoft.com/library/windows/hardware/ff558914) function can be used to convert a virtual memory address to a physical memory address.

The [**Disasm**](https://msdn.microsoft.com/library/windows/hardware/ff541945) function can be used to disassemble a single assembly instruction on the target.

To check the low 4 GB of memory for corruption when using physical address extension (PAE), use the [**Ioctl**](https://msdn.microsoft.com/library/windows/hardware/ff551084) operation [**IG\_LOWMEM\_CHECK**](https://msdn.microsoft.com/library/windows/hardware/ff550931).

### <span id="physical_memory"></span><span id="PHYSICAL_MEMORY"></span>Physical Memory

Physical memory can only be directly accessed in kernel-mode debugging.

The physical memory on the target can be read by using the [**ReadPhysical**](https://msdn.microsoft.com/library/windows/hardware/ff554310) and [**ReadPhysicalWithFlags**](https://msdn.microsoft.com/library/windows/hardware/ff554315) functions, and written by using the [**WritePhysical**](https://msdn.microsoft.com/library/windows/hardware/ff561432) and [**WritePhysicalWithFlags**](https://msdn.microsoft.com/library/windows/hardware/ff561448) functions.

To search the physical memory for pointers to locations within a specified range, use the [**Ioctl**](https://msdn.microsoft.com/library/windows/hardware/ff551084) operation [**IG\_POINTER\_SEARCH\_PHYSICAL**](https://msdn.microsoft.com/library/windows/hardware/ff550935).

### <span id="other_data_spaces"></span><span id="OTHER_DATA_SPACES"></span>Other Data Spaces

In kernel-mode debugging, it is possible to read and write data to a variety of data spaces in addition to the main memory. The following data spaces can be accessed:

<span id="Control-Space_Memory"></span><span id="control-space_memory"></span><span id="CONTROL-SPACE_MEMORY"></span>Control-Space Memory  
The functions [**ReadControlSpace**](https://msdn.microsoft.com/library/windows/hardware/ff553527), [**ReadControlSpace64**](https://msdn.microsoft.com/library/windows/hardware/ff553532), [**ReadTypedControlSpace32**](https://msdn.microsoft.com/library/windows/hardware/ff554339), and [**ReadTypedControlSpace64**](https://msdn.microsoft.com/library/windows/hardware/ff554341) will read data from a control space. The [**WriteControlSpace**](https://msdn.microsoft.com/library/windows/hardware/ff561375) function will write data to a control space.

<span id="I_O_Memory"></span><span id="i_o_memory"></span><span id="I_O_MEMORY"></span>I/O Memory  
The functions [**ReadIoSpace**](https://msdn.microsoft.com/library/windows/hardware/ff553574), [**ReadIoSpace64**](https://msdn.microsoft.com/library/windows/hardware/ff553577), **ReadIoSpace64**, [**ReadIoSpaceEx64**](https://msdn.microsoft.com/library/windows/hardware/ff553583) will read data from system I/O memory and bus I/O memory. The functions [**WriteIoSpace**](https://msdn.microsoft.com/library/windows/hardware/ff561406), [**WriteIoSpace64**](https://msdn.microsoft.com/library/windows/hardware/ff561408), [**WriteIoSpaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff561413), and [**WriteIoSpaceEx64**](https://msdn.microsoft.com/library/windows/hardware/ff561414) will write data to system I/O memory and bus I/O memory.

<span id="Model_Specific_Register__MSR_"></span><span id="model_specific_register__msr_"></span><span id="MODEL_SPECIFIC_REGISTER__MSR_"></span>Model Specific Register (MSR)  
The functions [**ReadMsr**](https://msdn.microsoft.com/library/windows/hardware/ff554289) and [**WriteMsr**](https://msdn.microsoft.com/library/windows/hardware/ff561424) read and write MSRs.

<span id="System_Bus"></span><span id="system_bus"></span><span id="SYSTEM_BUS"></span>System Bus  
The [**Ioctl**](https://msdn.microsoft.com/library/windows/hardware/ff551084) operations [**IG\_GET\_BUS\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff550913) and **IG\_SET\_BUS\_DATA** read and write system bus data.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For a more powerful memory access API, see [Memory Access](memory-access.md) in the [Using the Debugger Engine API](using-the-debugger-engine-api.md) section of this documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20WdbgExts%20Memory%20Access%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




