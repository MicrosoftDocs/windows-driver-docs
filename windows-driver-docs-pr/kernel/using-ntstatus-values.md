---
title: Using NTSTATUS Values
description: Using NTSTATUS Values
ms.assetid: fe823930-e3ff-4c95-a640-bb6470c95d1d
keywords: ["NTSTATUS values WDK kernel", "driver support routines WDK kernel", "return values WDK kernel", "testing return values WDK NTSTATUS values", "success values WDK NTSTATUS values", "informational values WDK NTSTATUS values", "warnings WDK NTSTATUS values", "error values WDK NTSTATUS values", "status information WDK NTSTATUS values", "checking return values"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using NTSTATUS Values





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

 

 




