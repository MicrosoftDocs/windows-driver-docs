---
title: wdfkd.wdfumirps
description: The wdfkd.wdfumirps extension displays the list of pending user-mode I/O request packets (UM IRPs) in the implicit process.
ms.assetid: 1BFFDAC0-AA1F-434A-BB05-6864810F9B98
keywords: ["wdfkd.wdfumirps Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wdfkd.wdfumirps
api_type:
- NA
ms.localizationpriority: medium
---

# !wdfkd.wdfumirps


The **!wdfkd.wdfumirps** extension displays the list of pending user-mode I/O request packets (UM IRPs) in the [implicit process](controlling-threads-and-processes.md).

```dbgcmd
!wdfkd.wdfumirps NumberOfIrps Flags
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______NumberOfIrps______"></span><span id="_______numberofirps______"></span><span id="_______NUMBEROFIRPS______"></span> *NumberOfIrps*   
Optional. Specifies the number of pending UM IRPs to display information about. If *NumberOfIrps* is an asterisk (\*) or is omitted, all UM IRPs will be displayed.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Optional. Specifies the type of information to be displayed. *Flags* can be any combination of the following bits. The default value is 0x01.

<span id="Bit_0__0x01_"></span><span id="bit_0__0x01_"></span><span id="BIT_0__0X01_"></span>Bit 0 (0x01)  
Displays details about the pending IRPs.

## <span id="DLL"></span><span id="dll"></span>DLL


Wdfkd.dll

## <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks


UMDF 2

## <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information


For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

Remarks
-------

You can use this command in a kernel-mode debugging session or in a user-mode debugging session that is attached to the UMDF host process (wudfhost.exe).

This command displays the same information as the user-mode command [**!wudfext.umirps**](-wudfext-umirps.md).

You can use [**!process**](-process.md) to get a list of all UMDF host processes, and you can use [**.process**](-process--set-process-context-.md) to set the implicit process to one of the UMDF host processes. For a detailed example, see [**!wdfkd.wdfumdevstacks**](-wdfkd-wdfumdevstacks.md).

Here is an example of the output of **!wdfkd.wdfumirps**.

```dbgcmd
0: kd> !wdfkd.wdfumirps
Number of pending IRPS: 0x4
####  CWudfIrp     Current Type           UniqueId KernelIrp         Device Stack
----  ----------------  --------------------------------------------------  ----
0000  1ab9e90c40   WdfRequestUndefined        0     0                 1ab9eaa6d0
0001  1ab9ebfa90   WdfRequestInternalIoctl    0     0                 1ab9eaa6d0
0002  1ab9ebfd10   WdfRequestInternalIoctl    0     0                 1ab9eaa6d0
0003  1ab9eae370   Power (WAIT_WAKE)          0     ffffe00000c53010  1ab9eaa6d0
```

 

 





