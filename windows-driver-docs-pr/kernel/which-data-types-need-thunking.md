---
title: Which Data Types Need Thunking
author: windows-driver-content
description: Which Data Types Need Thunking
MS-HAID:
- 'Other\_fd841839-0e4d-44d9-aed7-5aff27163f85.xml'
- 'kernel.which\_data\_types\_need\_thunking'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: af1d7986-7bf2-4587-b487-91658e7a3b19
keywords: ["thunking WDK", "WOW64 thunking layer WDK", "32-bit I/O support WDK 64-bit , thunking", "data types WDK 64-bit", "pointer precision WDK 64-bit", "fixed-precision data types WDK 64-bit"]
---

# Which Data Types Need Thunking


## <a href="" id="ddk-which-data-types-need-thunking-kg"></a>


The following table lists common data types that require thunking, along with their thunked equivalents.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Pointer-precision data type (before thunking)</th>
<th>Equivalent 32-bit fixed-precision data type (after thunking)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>HANDLE</p></td>
<td><p>VOID * POINTER_32</p></td>
</tr>
<tr class="even">
<td><p>INT_PTR</p></td>
<td><p>INT32</p></td>
</tr>
<tr class="odd">
<td><p>LONG_PTR</p></td>
<td><p>LONG32</p></td>
</tr>
<tr class="even">
<td><p>LPARAM</p></td>
<td><p>LONG32</p></td>
</tr>
<tr class="odd">
<td><p>PCHAR</p></td>
<td><p>Char * POINTER_32</p></td>
</tr>
<tr class="even">
<td><p>PDWORD</p></td>
<td><p>DWORD * POINTER_32</p></td>
</tr>
<tr class="odd">
<td><p>PHANDLE</p></td>
<td><p>VOID ** POINTER_32</p></td>
</tr>
<tr class="even">
<td><p>PULONG</p></td>
<td><p>ULONG * POINTER_32</p></td>
</tr>
<tr class="odd">
<td><p>PVOID</p></td>
<td><p>VOID * POINTER_32</p></td>
</tr>
<tr class="even">
<td><p>PWORD</p></td>
<td><p>WORD * POINTER_32</p></td>
</tr>
<tr class="odd">
<td><p>SIZE_T</p></td>
<td><p>INT32</p></td>
</tr>
<tr class="even">
<td><p>ULONG_PTR</p></td>
<td><p>ULONG32</p></td>
</tr>
<tr class="odd">
<td><p>UNICODE_STRING</p></td>
<td><p>UNICODE_STRING32</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Which%20Data%20Types%20Need%20Thunking%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


