---
title: WDFVERIFY macro
author: windows-driver-content
description: The WDFVERIFY macro tests a logical expression and, if the expression evaluates to FALSE, breaks into the kernel debugger.
ms.assetid: 9dc19299-7eda-42fb-811e-ba8dc5c1cdb5
keywords:
 - WDFVERIFY macro
ms.author: windowsdriverdev
ms.date: 08/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WDFVERIFY macro


\[Applies to KMDF only\]

The **WDFVERIFY** macro tests a logical expression and, if the expression evaluates to **FALSE**, breaks into the kernel debugger.

Syntax
------

```ManagedCPlusPlus
VOID WDFVERIFY(
    exp
);
```

Parameters
----------

*exp*   
A logical expression that WDFVERIFY tests.

Return value
------------

None

Remarks
-------

The code for the **WDFVERIFY** macro is included in your driver's binary when you build your driver in a release configuration or a debug configuration. If your driver's binary includes **WDFVERIFY** code, the code will run when your driver runs with checked builds or free builds of the Microsoft Windows operating system.

The **WDFVERIFY** code breaks into a kernel debugger only if the **VerifyOn** value is set in the registry. For more information about registry entries that you can use to debug your driver, see [Registry Entries for Debugging Framework-Based Drivers](https://msdn.microsoft.com/library/windows/hardware/ff544573).

For more information about debugging your driver, see [Debugging a KMDF Driver](https://msdn.microsoft.com/library/windows/hardware/ff540790).

Examples
--------

The following code example breaks into the debugger if an attempt to reuse a request object fails.

```
status = WdfRequestReuse(Request, &amp;params);
WDFVERIFY(NT_SUCCESS(status));
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


[**VERIFY\_IS\_IRQL\_PASSIVE\_LEVEL**](verify-is-irql-passive-level.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20WDFVERIFY%20macro%20%20RELEASE:%20%288/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


