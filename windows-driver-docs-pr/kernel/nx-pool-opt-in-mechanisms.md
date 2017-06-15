---
title: NX Pool Opt-In Mechanisms
author: windows-driver-content
description: To port kernel-mode driver code to Windows 8 from earlier versions of Windows, you should use the NonPagedPoolNx type of memory pool as a best practice.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9C868569-14EC-4915-8553-FD2D94C5A855
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
<td><p>[Single Binary Opt-In: POOL_NX_OPTIN](single-binary-opt-in-pool-nx-optin.md)</p></td>
<td><p>To build a single driver binary that runs both in Windows 8 and in earlier versions of Windows, use the POOL_NX_OPTIN opt-in mechanism. This is a porting aid for third-party hardware vendors who supply a single driver binary to support multiple Windows versions.</p></td>
</tr>
<tr class="even">
<td><p>[Multiple Binary Opt-In: POOL_NX_OPTIN_AUTO](multiple-binary-opt-in-pool-nx-optin-auto.md)</p></td>
<td><p>If you are a hardware vendor who supplies different driver binaries for different versions of Windows, you can use the POOL_NX_OPTIN_AUTO opt-in mechanism. This porting aid builds a separate driver binary for Windows 8 and for each earlier version of Windows that your driver supports.</p></td>
</tr>
<tr class="odd">
<td><p>[Selective Opt-Out: POOL_NX_OPTOUT](selective-opt-out-pool-nx-optout.md)</p></td>
<td><p>You can globally enable one of the no-execute (NX) pool opt-in mechanisms for a set of driver source files, and then override this opt-in mechanism for one or more selected source files with POOL_NX_OPTOUT. This allows the selected source files to continue to use executable nonpaged memory. You can use the POOL_NX_OPTOUT opt-out mechanism with either the POOL_NX_OPTIN or the POOL_NX_OPTIN_AUTO opt-in mechanism.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20NX%20Pool%20Opt-In%20Mechanisms%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


