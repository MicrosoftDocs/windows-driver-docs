---
title: Accessing Memory by Virtual Address
description: Accessing Memory by Virtual Address
ms.assetid: 13e97cba-c4a4-4240-99b3-88a7537b0ca8
keywords: ["virtual address, accessing memory"]
---

# Accessing Memory by Virtual Address


## <span id="ddk_debugging_bios_code_dbg"></span><span id="DDK_DEBUGGING_BIOS_CODE_DBG"></span>


To access memory addresses or address ranges, you can use several commands. Visual Studio and WinDbg provide user interface elements (as well as commands) that you can use to view and edit memory. For more information, see [Viewing and Editing Memory and Registers in Visual Studio](viewing-memory--variables--and-registers-in-visual-studio.md) and [Viewing and Editing Memory in WinDbg](memory-window.md).

The following commands can read or write memory in a variety of formats. These formats include hexadecimal bytes, words (words, double words, and quad-words), integers (short, long, and quad integers and unsigned integers), floating-point numbers (10-byte, 16-byte, 32-byte, and 64-byte real numbers), and ASCII characters.

-   The [**d\* (Display Memory)**](https://msdn.microsoft.com/library/windows/hardware/ff542790) command displays the contents of a specified memory address or range.

-   The [**e\* (Enter Values)**](https://msdn.microsoft.com/library/windows/hardware/ff545308) command writes a value to the specified memory address.

You can use the following commands to handle more specialized data types:

-   The [**dt (Display Type)**](https://msdn.microsoft.com/library/windows/hardware/ff542772) command finds a variety of data types and displays data structures that have been created by the application that is being debugged. This command is highly versatile and has many variations and options.

-   The [**ds, dS (Display String)**](https://msdn.microsoft.com/library/windows/hardware/ff542767) command displays a STRING, ANSI\_STRING, or UNICODE\_STRING data structure.

-   The [**dl (Display Linked List)**](https://msdn.microsoft.com/library/windows/hardware/ff542740) command traces and displays a linked list.

-   The [**d\*s (Display Words and Symbols)**](https://msdn.microsoft.com/library/windows/hardware/ff540455) command finds double-words or quad-words that might contain symbol information and then displays the data and the symbol information.

-   The [**!address**](https://msdn.microsoft.com/library/windows/hardware/ff561519) extension command displays information about the properties of the memory that is located at a specific address.

You can use the following commands to manipulate memory ranges:

-   The [**m (Move Memory)**](https://msdn.microsoft.com/library/windows/hardware/ff552254) command moves the contents of one memory range to another.

-   The [**f (Fill Memory)**](https://msdn.microsoft.com/library/windows/hardware/ff545511) command writes a pattern to a memory range, repeating it until the range is full.

-   The [**c (Compare Memory)**](https://msdn.microsoft.com/library/windows/hardware/ff540362) command compares the contents of two memory ranges.

-   The [**s (Search Memory)**](https://msdn.microsoft.com/library/windows/hardware/ff558855) command searches for a specified pattern within a memory range or searches for any ASCII or Unicode characters that exist in a memory range.

-   The [**.holdmem (Hold and Compare Memory)**](https://msdn.microsoft.com/library/windows/hardware/ff563204) command compares one memory range to another.

In most situations, these commands interpret their parameters in the current radix. Therefore, you should add **0x** before hexadecimal addresses if the current radix is not 16. However, the display output of these commands is typically in hexadecimal format, regardless of the current radix. (For more information about the output, see the individual command topics.) The [Memory window](memory-window.md) displays integers and real numbers in decimal format and displays other formats in hexadecimal format.

To change the default radix, use the [**n (Set Number Base)**](https://msdn.microsoft.com/library/windows/hardware/ff552287) command. To quickly convert numbers from one base to another, use the [**? (Evaluate Expression)**](https://msdn.microsoft.com/library/windows/hardware/ff566240) command or the [**.formats (Show Number Formats)**](https://msdn.microsoft.com/library/windows/hardware/ff563127) command.

When you are performing user-mode debugging, the meaning of virtual addresses is determined by the current process. When you are performing kernel-mode debugging, the meaning of virtual addresses can be controlled by the debugger. For more information, see [Process Context](changing-contexts.md#process-context).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Accessing%20Memory%20by%20Virtual%20Address%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




