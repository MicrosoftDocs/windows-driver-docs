---
title: ZwCurrentThread macro
description: ZwCurrentThread macro
ms.date: 10/17/2018
ms.topic: reference
---

# ZwCurrentThread

Defined in: Wdm.h

The **ZwCurrentThread** macro returns a handle to the current thread.

**Return value**

**HANDLE**

**ZwCurrentThread** returns a special handle value that represents the current thread.

The returned value is not a true handle, but it is a special value that always represents the current thread.

**NtCurrentThread** and **ZwCurrentThread** are two versions of the same Windows Native System Services routine. The **NtCurrentThread** routine in the Windows kernel is not directly accessible to kernel-mode drivers. However, kernel-mode drivers can access this routine indirectly by calling the **ZwCurrentThread** routine.

For calls from kernel-mode drivers, the **Nt_Xxx_** and **Zw_Xxx_** versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the **Nt_Xxx_** and **Zw_Xxx_** versions of a routine, see [Using Nt and Zw Versions of the Native System Services Routines](using-nt-and-zw-versions-of-the-native-system-services-routines.md).

All supported operating systems.

IRQL: Any level
