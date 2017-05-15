---
title: Reading Symbols from Paged-Out Headers
description: Reading Symbols from Paged-Out Headers
ms.assetid: 74ec20d8-e2b5-449d-8b93-7553c57fac07
keywords: ["symbols, paged-out header problems"]
---

# Reading Symbols from Paged-Out Headers


## <span id="ddk_reading_symbols_from_paged_out_headers_dbg"></span><span id="DDK_READING_SYMBOLS_FROM_PAGED_OUT_HEADERS_DBG"></span>


The kernel debugger must read the header for each loaded module's image in order to know which symbols correspond to that module.

If a module's header is paged out to disk, the debugger will not load symbols for this module. If this happens with a module that is essential to the debugging process, it can be a critical problem.

The following procedure can be used to solve this problem.

**To acquire symbols for paged-out headers**

1.  Make a second copy of the kernel itself. It is probably easiest to put this on a network share.

2.  Append the root directory of this share to the symbol path. See [Symbol Path](symbol-path.md) for the ways to change the symbol path.

3.  Use the [**.reload (Reload Module)**](-reload--reload-module-.md) command.

4.  Use the [**!sym noisy**](-sym.md) extension command to see more verbose output. If this is used, you will be able to see which symbols are loaded from the module images on the target computer, and which are loaded from the copy of the kernel modules.

This technique must be used with care, since the debugger has no way of verifying whether the file copies actually match the originals. So it is crucial that the version of Windows used on the network share matches the version used on the target computer.

This technique is only used for kernel-mode debugging. The operating system is capable of paging in any headers required during user-mode debugging (unless the disk holding the paging file is dismounted or otherwise inaccessible).

Here is an example of this technique being used:

``` syntax
kd> .reload
Connected to Windows XP 2268 x86 compatible target, ptr64 FALSE
Loading Kernel Symbols
..........Unable to read image header for dmload.sys at fe0be000 - NTSTATUS 0xC0000001
..........Unable to read image header for dmboot.sys at fda93000 - NTSTATUS 0xC0000001
.....................................Unable to read image header for fdc.sys at fdfc2000 - NTSTATUS 0xC0000001
...Unable to read image header for flpydisk.sys at fde4a000 - NTSTATUS 0xC0000001
.Unable to read image header for Fs_Rec.SYS at fe0c8000 - NTSTATUS 0xC0000001
.Unable to read image header for Null.SYS at fe2c4000 - NTSTATUS 0xC0000001
...................Unable to read image header for win32k.sys at a0000000 - NTSTATUS 0xC0000001
..Unable to read image header for dxg.sys at a0194000 - NTSTATUS 0xC0000001
.......Unable to read image header for ati2draa.dll at a01a4000 - NTSTATUS 0xC0000001
..Unable to read image header for ParVdm.SYS at fe116000 - NTSTATUS 0xC0000001
.......
Loading unloaded module list
..............
Loading User Symbols
Unable to retrieve the PEB address. This is usually caused
by being in the wrong process context or by paging
```

Notice that many images have inaccessible headers. Check the symbols from one of these files (in this example, fs\_rec.sys):

``` syntax
kd> x fs_rec!*
*** ERROR: Module load completed but symbols could not be loaded for fs_rec.sys
```

These headers are apparently paged out. So you need to add the proper images to the symbol path:

``` syntax
kd> .sympath+ \\myserver\myshare\symbols\x86fre\symbols
Symbol search path is: symsrv*symsrv.dll*c:\localcache*https://msdl.microsoft.com/download/symbols;\\myserver\myshare\symbols\x86fre\symbols

kd> .reload
Connected to Windows XP 2268 x86 compatible target, ptr64 FALSE
Loading Kernel Symbols
..........Unable to read image header for dmload.sys at fe0be000 - NTSTATUS 0xC0000001
..........Unable to read image header for dmboot.sys at fda93000 - NTSTATUS 0xC0000001
.....................................Unable to read image header for fdc.sys at fdfc2000 - NTSTATUS 0xC0000001
...Unable to read image header for flpydisk.sys at fde4a000 - NTSTATUS 0xC0000001
.Unable to read image header for Fs_Rec.SYS at fe0c8000 - NTSTATUS 0xC0000001
.Unable to read image header for Null.SYS at fe2c4000 - NTSTATUS 0xC0000001
...................Unable to read image header for win32k.sys at a0000000 - NTSTATUS 0xC0000001
..Unable to read image header for dxg.sys at a0194000 - NTSTATUS 0xC0000001
.......Unable to read image header for ati2draa.dll at a01a4000 - NTSTATUS 0xC0000001
..Unable to read image header for ParVdm.SYS at fe116000 - NTSTATUS 0xC0000001
.......
Loading unloaded module list
..............
Loading User Symbols
Unable to retrieve the PEB address. This is usually caused
by being in the wrong process context or by paging
```

The same warnings have appeared, but the symbols themselves are now accessible:

``` syntax
kd> x fs_Rec!*
fe0c8358  Fs_Rec!_imp___allmul
fe0c8310  Fs_Rec!_imp__IoCreateDevice
fe0c835c  Fs_Rec!_imp___allshr
........
fe0c8360  Fs_Rec!ntoskrnl_NULL_THUNK_DATA
fe0c832c  Fs_Rec!_imp__KeSetEvent
fe0c9570  Fs_Rec!_NULL_IMPORT_DESCRIPTOR
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Reading%20Symbols%20from%20Paged-Out%20Headers%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




