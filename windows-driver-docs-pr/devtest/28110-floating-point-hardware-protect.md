---
title: C28110
description: Warning C28110 Drivers must protect floating-point hardware state. See use of float.
ms.assetid: 2f6045e3-92b2-4773-a8de-3d0ec09c5d31
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28110


warning C28110: Drivers must protect floating-point hardware state. See use of float

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>Use <strong>KeSaveFloatingPointState</strong> and <strong>KeRestoreFloatingPointState</strong> around floating-point operations. Display drivers should use the corresponding <strong>Eng...</strong> routines.</p></td>
</tr>
</tbody>
</table>

 

This warning is only applicable in kernel mode. The driver is attempting to use a variable or constant of a float type when the code is not protected by [**KeSaveFloatingPointState**](https://msdn.microsoft.com/library/windows/hardware/ff553243) and [**KeRestoreFloatingPointState**](https://msdn.microsoft.com/library/windows/hardware/ff553185), or [**EngSaveFloatingPointState**](https://msdn.microsoft.com/library/windows/hardware/ff565010) and [**EngRestoreFloatingPointState**](https://msdn.microsoft.com/library/windows/hardware/ff565006).

Typically, drivers run with the floating-point context of the most recent application, and any use of a floating point that is not protected by [**KeSaveFloatingPointState**](https://msdn.microsoft.com/library/windows/hardware/ff553243) and [**KeRestoreFloatingPointState**](https://msdn.microsoft.com/library/windows/hardware/ff553185) can change the results for other processes and can often cause incorrect or unexpected results in the driver.

Display drivers should use [**EngSaveFloatingPointState**](https://msdn.microsoft.com/library/windows/hardware/ff565010) and [**EngRestoreFloatingPointState**](https://msdn.microsoft.com/library/windows/hardware/ff565006).

After an instance of this error is detected along any particular flow path, the Code Analysis tool suppresses subsequent similar errors. The Code Analysis tool does not report this error for function definitions that take floating-type arguments or that return a floating type, because the caller will report the use.

This warning can be triggered in error when a program saves and restores the floating-point state around a function call, and the called function performs floating-point operations.

If a function uses floating-point operations intentionally, and is expecting to be called in a context where floating point is safe, you should annotate the function with **\_Kernel\_float\_used\_**. This annotation will both suppress the warnings in the function body and cause the calling context to check that the call is safely protected for floating-point operations. If floating-point operations appear in the arguments or return value, the effect is the same as using **\_Kernel\_float\_used\_**.

By using **\_Kernel\_float\_used\_** on (or adding the appropriate save and restore calls to) all functions that use floating point until no warnings remain, a driver can be assured to be free of misuse of the floating-point hardware. For more information, see [Floating point annotations for drivers](floating-point-annotations-for-drivers.md).

 

 





