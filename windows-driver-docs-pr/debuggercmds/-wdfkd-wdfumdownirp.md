---
title: "!wdfkd.wdfumdownirp"
description: "The !wdfkd.wdfumdownirp extension displays the kernel-mode I/O request packet (IRP) that is associated with a specified user-mode IRP."
keywords: ["!wdfkd.wdfumdownirp Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wdfkd.wdfumdownirp
api_type:
- NA
---

# !wdfkd.wdfumdownirp

The **!wdfkd.wdfumdownirp** extension displays the kernel-mode I/O request packet (IRP) that is associated with a specified user-mode IRP. This command is used in two steps. See Remarks.

```dbgcmd
!wdfkd.wdfumdownirp UmIrp [FileObject] 
```

## Parameters

<span id="_______UmIrp______"></span><span id="_______umirp______"></span><span id="_______UMIRP______"></span> *UmIrp*   
Specifies the address of a user mode IRP. You can use [**!wdfkd.wdfumirps**](-wdfkd-wdfumirps.md) to get the addresses of UM IRPs in the [implicit process](../debugger/controlling-threads-and-processes.md).

<span id="_______FileObject______"></span><span id="_______fileobject______"></span><span id="_______FILEOBJECT______"></span> *FileObject*   
Specifies the address of a **\_FILE\_OBJECT** structure. For information about how to get this address, see Remarks.

## DLL

Wdfkd.dll

## Frameworks

UMDF 2

## Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](../debugger/kernel-mode-driver-framework-debugging.md).

## Remarks

You can use this command in a kernel-mode debugging session or in a user-mode debugging session that is attached to the UMDF host process (wudfhost.exe).

To use this command, follow these steps:

1.  Enter this command, passing only the address a user-mode IRP. The command displays a handle.
2.  Pass the displayed handle to the [**!handle**](-handle.md) command. In the output of **!handle**, find the address of a **\_FILE\_OBJECT** structure.
3.  Enter this command again, passing both the address of the user-mode IRP and the address of the **\_FILE\_OBJECT** structure.

