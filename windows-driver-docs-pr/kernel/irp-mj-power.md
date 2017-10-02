---
title: IRP_MJ_POWER
author: windows-driver-content
description: All drivers must be prepared to service IRP\_MJ\_POWER requests in a DispatchPower routine.
ms.author: windowsdriverdev
ms.date: 08/12/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.assetid: ca53ceef-2755-49d3-aab9-0d12a0e51e75
keywords:
 - IRP_MJ_POWER Kernel-Mode Driver Architecture
---

# IRP\_MJ\_POWER


All drivers must be prepared to service **IRP\_MJ\_POWER** requests in a [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routine.

When Sent
---------

The power manager or a driver can send **IRP\_MJ\_POWER** requests at any time the operating system is running.

## Input Parameters


Depends on the value at **MinorFunction** in the current I/O stack location of the IRP. Every **IRP\_MJ\_POWER** request specifies a minor function code that identifies the requested power action.

## Output Parameters


Depends on the value at **MinorFunction** in the current I/O stack location of the IRP.

Operation
---------

In addition to the usual rules that govern the processing of IRPs, **IRP\_MJ\_POWER** IRPs have the following special requirement: A driver that receives a power IRP must not change the major and minor function codes in any I/O stack locations in the IRP that have been set by the power manager or by higher-level drivers. The power manager relies on these function codes remaining unchanged until the IRP is completed. Violations of this rule can cause problems that are difficult to debug. For example, the operating system might stop responding, or "hang."

See [Power Management Minor IRPs](power-management-minor-irps.md) for detailed information about **IRP\_MJ\_POWER** requests.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</td>
</tr>
</tbody>
</table>

## See also


[*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20IRP_MJ_POWER%20%20RELEASE:%20%288/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


