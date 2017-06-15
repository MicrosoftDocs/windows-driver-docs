---
title: Using NTSTATUS Values
author: windows-driver-content
description: Using NTSTATUS Values
MS-HAID:
- 'Other\_d2d035ed-32f7-41f3-b3f3-ed1316482a39.xml'
- 'kernel.using\_ntstatus\_values'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: fe823930-e3ff-4c95-a640-bb6470c95d1d
keywords: ["NTSTATUS values WDK kernel", "driver support routines WDK kernel", "return values WDK kernel", "testing return values WDK NTSTATUS values", "success values WDK NTSTATUS values", "informational values WDK NTSTATUS values", "warnings WDK NTSTATUS values", "error values WDK NTSTATUS values", "status information WDK NTSTATUS values", "checking return values"]
---

# Using NTSTATUS Values


## <a href="" id="ddk-using-ntstatus-values-kg"></a>


Many kernel-mode [standard driver routines](https://msdn.microsoft.com/library/windows/hardware/ff563842) and [driver support routines](https://msdn.microsoft.com/library/windows/hardware/ff563889) use the NTSTATUS type for return values. Additionally, drivers provide an NTSTATUS-typed value in an IRP's [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure when [completing IRPs](completing-irps.md). The NTSTATUS type is defined in Ntdef.h, and system-supplied status codes are defined in Ntstatus.h. (Vendors can also define private status codes, although they rarely need to. For more information, see [Defining New NTSTATUS Values](defining-new-ntstatus-values.md).)

NTSTATUS values are divided into four types: success values, informational values, warnings, and error values.

Numerous values are assigned to each type. A common mistake, when testing for a successful return from a routine, is to compare the routine's return value with STATUS\_SUCCESS. This comparison checks for only one of several success values.

When testing a return value, you should use one of the following system-supplied macros (defined in Ntdef.h):

<a href="" id="nt-success-status-"></a>NT\_SUCCESS(*Status*)  
Evaluates to **TRUE** if the return value specified by *Status* is a success type (0 − 0x3FFFFFFF) or an informational type (0x40000000 − 0x7FFFFFFF).

<a href="" id="nt-information-status-"></a>NT\_INFORMATION(*Status*)  
Evaluates to **TRUE** if the return value specified by *Status* is an informational type (0x40000000 − 0x7FFFFFFF).

<a href="" id="nt-warning-status-"></a>NT\_WARNING(*Status*)  
Evaluates to **TRUE** if the return value specified by *Status* is a warning type (0x80000000 − 0xBFFFFFFF).

<a href="" id="nt-error-status-"></a>NT\_ERROR(*Status*)  
Evaluates to **TRUE** if the return value specified by *Status* is an error type (0xC0000000 - 0xFFFFFFFF).

For example, suppose a driver calls [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506) to register a device interface. If the driver checks the return value using the NT\_SUCCESS macro, the macro will evaluate to **TRUE** if the routine returns STATUS\_SUCCESS, which indicates no errors, or if it returns the informational status STATUS\_OBJECT\_NAME\_EXISTS, which indicates that the device interface is already registered.

As another example, suppose a driver calls [**ZwEnumerateKey**](https://msdn.microsoft.com/library/windows/hardware/ff566447) to enumerate the subkeys of a specified registry key. If the NT\_SUCCESS macro evaluates to **FALSE**, it might be because the routine returned STATUS\_INVALID\_PARAMETER, which is an error code, or because the routine returned STATUS\_NO\_MORE\_ENTRIES, which is a warning code.

As a final example, suppose a driver sends an IRP that causes a lower-level driver to read information from a device. If the requesting driver specifies a buffer that is too small to receive any information, the lower-level driver might respond by returning STATUS\_BUFFER\_TOO\_SMALL, which is an error code. If the first driver specifies a buffer that can receive some, but not all, of the requested information, the lower-level driver might respond by supplying as much data as possible and then returning STATUS\_BUFFER\_OVERFLOW, which is a warning code. Note that if the first driver tests the status value using NT\_SUCCESS or NT\_ERROR incorrectly, it might inadvertently drop some of the information received.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20NTSTATUS%20Values%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


