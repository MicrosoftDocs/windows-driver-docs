---
title: Accessing Global Variables
description: Accessing Global Variables
ms.assetid: 81daf418-d3cf-413a-8ee0-790b0c0f86c0
keywords: ["global variables", "global variables, accessing"]
---

# Accessing Global Variables


## <span id="ddk_debugging_bios_code_dbg"></span><span id="DDK_DEBUGGING_BIOS_CODE_DBG"></span>


The names of global variables are stored in the symbol files that are created when an application is compiled. The debugger interprets the name of a global variable as a virtual address. Any command that accepts an address as a parameter also accepts the name of a variable. Therefore, you can use all of the commands that are described in [Accessing Memory by Virtual Address](accessing-memory-by-virtual-address.md) to read or write global variables.

In addition, you can use the [**? (Evaluate Expression)**](---evaluate-expression-.md) command to display the address that is associated with any symbol.

Visual Studio and WinDbg provide user interface elements that you can use (in addition to commands) to view and edit global variables. See [Viewing and Editing Memory and Registers in Visual Studio](viewing-memory--variables--and-registers-in-visual-studio.md) and [Viewing and Editing Global Variables in WinDbg](viewing-and-editing-global-variables-in-windbg.md).

Consider the following example. Suppose that you want to examine the `MyCounter` global variable, which is a 32-bit integer. Also suppose that the default radix is 10.

You can obtain this variable's address and then display it as follows.

```
0:000> ? MyCounter 
Evaluate expression: 1244892 = 0012fedc
0:000> dd 0x0012fedc L1 
0012fedc  00000052
```

The first command output tells you that the address of `MyCounter` is 0x0012FEDC. You can then use the [**d\* (Display Memory)**](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) command to display one double-word at this address. (You could also use 1244892, which is the decimal version of this address. However, most C programmers prefer to use 0x0012FEDC.) The second command tells you that the value of MyCounter is 0x52 (decimal 82).

You could also perform these steps in the following command.

```
0:000> dd MyCounter L1 
0012fedc  00000052
```

To change the value of `MyCounter` to decimal 83, use the following command.

```
0:000> ed MyCounter 83 
```

This example uses decimal input, because that format seems more natural for an integer. However, the output of the [**d\***](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) command is still in hexadecimal format.

```
0:000> dd MyCounter L1 0012fedc  00000053
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Accessing%20Global%20Variables%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




