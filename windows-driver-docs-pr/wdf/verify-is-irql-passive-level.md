---
title: VERIFY_IS_IRQL_PASSIVE_LEVEL macro
description: The VERIFY_IS_IRQL_PASSIVE_LEVEL macro breaks into the kernel debugger if the driver is not executing at IRQL PASSIVE_LEVEL.
ms.assetid: 7f1e25af-df66-46a2-8d27-7924677e4d5d
keywords:
 - VERIFY_IS_IRQL_PASSIVE_LEVEL macro
ms.date: 08/23/2017
ms.localizationpriority: medium
---

# VERIFY_IS_IRQL_PASSIVE_LEVEL macro


[Applies to KMDF only]

The **VERIFY_IS_IRQL_PASSIVE_LEVEL** macro breaks into the kernel debugger if the driver is not executing at IRQL = PASSIVE_LEVEL.

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

The code for the **VERIFY_IS_IRQL_PASSIVE_LEVEL** macro is included in your driver's binary when you build your driver in a release configuration or a debug configuration. If your driver's binary includes **VERIFY_IS_IRQL_PASSIVE_LEVEL** code, the code will run when your driver runs with checked builds or free builds of the Microsoft Windows operating system.

The **VERIFY_IS_IRQL_PASSIVE_LEVEL** code breaks into a kernel debugger if one of the following is true:

-   **DbgBreakOnError** is set to a non-zero value in the registry.
-   **VerifierOn** is set to a non-zero value and **DbgBreakOnError** is not set.
-   Driver Verifier is enabled, the driver was built with framework version 1.9 or later, and neither **VerifierOn** nor **DbgBreakOnError** is set.

For more information about registry entries that you can use to debug your driver, see [Registry Entries for Debugging Framework-Based Drivers](https://msdn.microsoft.com/library/windows/hardware/ff544573).

For more information about debugging your driver, see [Debugging a KMDF Driver](https://msdn.microsoft.com/library/windows/hardware/ff540790).

Examples
--------

The following code example breaks into the kernel debugger if the driver is not executing at IRQL = PASSIVE_LEVEL.

```cpp
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
<td><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" data-raw-source="[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)">Universal</a></td>
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
