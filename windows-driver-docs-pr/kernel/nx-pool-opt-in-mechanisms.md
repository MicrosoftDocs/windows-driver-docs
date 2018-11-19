---
title: NX Pool Opt-In Mechanisms
description: To port kernel-mode driver code to Windows 8 from earlier versions of Windows, you should use the NonPagedPoolNx type of memory pool as a best practice.
ms.assetid: 9C868569-14EC-4915-8553-FD2D94C5A855
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# NX Pool Opt-In Mechanisms


To port kernel-mode driver code to Windows 8 from earlier versions of Windows, you should use the **NonPagedPoolNx** type of memory pool as a best practice. You can use one of several porting aids to easily "opt in" to use the **NonPagedPoolNx** pool type by default.

These porting aids use one or both of the following techniques to enable the driver to use NX nonpaged pool:

-   Use a `#define` preprocessor statement to create a globally defined macro name.

-   Call an inline function from the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine.

For most kernel-mode driver code, these porting aids enable developers to update their drivers with minimal effort.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="single-binary-opt-in-pool-nx-optin.md" data-raw-source="[Single Binary Opt-In: POOL_NX_OPTIN](single-binary-opt-in-pool-nx-optin.md)">Single Binary Opt-In: POOL_NX_OPTIN</a></p></td>
<td><p>To build a single driver binary that runs both in Windows 8 and in earlier versions of Windows, use the POOL_NX_OPTIN opt-in mechanism. This is a porting aid for third-party hardware vendors who supply a single driver binary to support multiple Windows versions.</p></td>
</tr>
<tr class="even">
<td><p><a href="multiple-binary-opt-in-pool-nx-optin-auto.md" data-raw-source="[Multiple Binary Opt-In: POOL_NX_OPTIN_AUTO](multiple-binary-opt-in-pool-nx-optin-auto.md)">Multiple Binary Opt-In: POOL_NX_OPTIN_AUTO</a></p></td>
<td><p>If you are a hardware vendor who supplies different driver binaries for different versions of Windows, you can use the POOL_NX_OPTIN_AUTO opt-in mechanism. This porting aid builds a separate driver binary for Windows 8 and for each earlier version of Windows that your driver supports.</p></td>
</tr>
<tr class="odd">
<td><p><a href="selective-opt-out-pool-nx-optout.md" data-raw-source="[Selective Opt-Out: POOL_NX_OPTOUT](selective-opt-out-pool-nx-optout.md)">Selective Opt-Out: POOL_NX_OPTOUT</a></p></td>
<td><p>You can globally enable one of the no-execute (NX) pool opt-in mechanisms for a set of driver source files, and then override this opt-in mechanism for one or more selected source files with POOL_NX_OPTOUT. This allows the selected source files to continue to use executable nonpaged memory. You can use the POOL_NX_OPTOUT opt-out mechanism with either the POOL_NX_OPTIN or the POOL_NX_OPTIN_AUTO opt-in mechanism.</p></td>
</tr>
</tbody>
</table>

 

 

 




