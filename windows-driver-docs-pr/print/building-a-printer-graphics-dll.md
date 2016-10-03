---
title: Building a Printer Graphics DLL
author: windows-driver-content
description: Building a Printer Graphics DLL
MS-HAID:
- 'drvarch\_8bf51f8f-9896-470a-b18e-825a6fa274ad.xml'
- 'print.building\_a\_printer\_graphics\_dll'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: bec1e9cc-a846-43e5-bc9e-e43a151ef6c4
keywords: ["printer graphics DLL WDK , building", "graphics DLL WDK printer , building"]
---

# Building a Printer Graphics DLL


## <a href="" id="ddk-building-a-printer-graphics-dll-gg"></a>


When building a printer graphics DLL, you must be aware of the following differences between DLLs intended for user-mode execution and those intended for kernel-mode execution.

**Note**   In Windows Vista, printer graphics DLLs can only execute in user mode. For more information, see [Choosing User Mode or Kernel Mode](choosing-user-mode-or-kernel-mode.md).

 

### Rules for Building a Printer Graphics DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>User-mode graphics DLL</th>
<th>Kernel-mode graphics DLL</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Set TARGETTYPE=DYNLINK in source file.</p></td>
<td><p>Set TARGETTYPE=GDI_DRIVER in source file.</p></td>
</tr>
<tr class="even">
<td><p>Preprocessor macro USERMODE_DRIVER must be defined in source files before winddi.h is included.</p></td>
<td><p>Preprocessor macro USERMODE_DRIVER must not be defined.</p></td>
</tr>
<tr class="odd">
<td><p>Object modules must be linked with the umpdddi.lib and gdi32.lib import libraries.</p></td>
<td><p>Object modules must be linked with the win32k.lib import library.</p></td>
</tr>
<tr class="even">
<td><p>The [<strong>DrvQueryDriverInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556261) function must return <strong>TRUE</strong> for DRVQUERY_USERMODE.</p></td>
<td><p>The [<strong>DrvQueryDriverInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556261) function must return <strong>FALSE</strong> for DRVQUERY_USERMODE. (Alternatively, the function can be omitted.)</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Building%20a%20Printer%20Graphics%20DLL%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


