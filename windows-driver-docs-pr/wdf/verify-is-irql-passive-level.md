---
title: VERIFY\_IS\_IRQL\_PASSIVE\_LEVEL macro
author: windows-driver-content
description: The VERIFY\_IS\_IRQL\_PASSIVE\_LEVEL macro breaks into the kernel debugger if the driver is not executing at IRQL PASSIVE\_LEVEL.
ms.assetid: 7f1e25af-df66-46a2-8d27-7924677e4d5d
keywords:
 - VERIFY_IS_IRQL_PASSIVE_LEVEL macro
ms.author: windowsdriverdev
ms.date: 08/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# VERIFY\_IS\_IRQL\_PASSIVE\_LEVEL macro


\[Applies to KMDF only\]

The **VERIFY\_IS\_IRQL\_PASSIVE\_LEVEL** macro breaks into the kernel debugger if the driver is not executing at IRQL = PASSIVE\_LEVEL.

Syntax
------

```ManagedCPlusPlus
VOID VERIFY_IS_IRQL_PASSIVE_LEVEL(void);
```

Parameters
----------

This macro has no parameters.

Return value
------------

None

Remarks
-------

The code for the **VERIFY\_IS\_IRQL\_PASSIVE\_LEVEL** macro is included in your driver's binary when you build your driver in a release configuration or a debug configuration. If your driver's binary includes **VERIFY\_IS\_IRQL\_PASSIVE\_LEVEL** code, the code will run when your driver runs with checked builds or free builds of the Microsoft Windows operating system.

The **VERIFY\_IS\_IRQL\_PASSIVE\_LEVEL** code breaks into a kernel debugger if one of the following is true:

-   **DbgBreakOnError** is set to a non-zero value in the registry.
-   **VerifierOn** is set to a non-zero value and **DbgBreakOnError** is not set.
-   Driver Verifier is enabled, the driver was built with framework version 1.9 or later, and neither **VerifierOn** nor **DbgBreakOnError** is set.

For more information about registry entries that you can use to debug your driver, see [Registry Entries for Debugging Framework-Based Drivers](https://msdn.microsoft.com/library/windows/hardware/ff544573).

For more information about debugging your driver, see [Debugging a KMDF Driver](https://msdn.microsoft.com/library/windows/hardware/ff540790).

Examples
--------

The following code example breaks into the kernel debugger if the driver is not executing at IRQL = PASSIVE\_LEVEL.

```
VERIFY_IS_IRQL_PASSIVE_LEVEL();
```

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
</tr>
<tr class="even">
<td><p>Minimum KMDF version</p></td>
<td><p>1.0</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Wdfassert.h (include Wdf.h)</td>
</tr>
</tbody>
</table>

## See also


[**WDFVERIFY**](wdfverify.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20VERIFY_IS_IRQL_PASSIVE_LEVEL%20macro%20%20RELEASE:%20%288/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


