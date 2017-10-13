---
title: IRP_MJ_SYSTEM_CONTROL
author: windows-driver-content
description: All drivers must provide a DispatchSystemControl routine that handles IRP\_MJ\_SYSTEM\_CONTROL requests, which are sent by the kernel-mode component of Windows Management Instrumentation (WMI).
ms.author: windowsdriverdev
ms.date: 08/12/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.assetid: 1b4dfc87-3f74-4e33-9dbb-72d4f72480fc
keywords:
 - IRP_MJ_SYSTEM_CONTROL Kernel-Mode Driver Architecture
---

# IRP\_MJ\_SYSTEM\_CONTROL


All drivers must provide a [*DispatchSystemControl*](https://msdn.microsoft.com/library/windows/hardware/ff543412) routine that handles **IRP\_MJ\_SYSTEM\_CONTROL** requests, which are sent by the kernel-mode component of [Windows Management Instrumentation](https://msdn.microsoft.com/library/windows/hardware/ff547139) (WMI).

When Sent
---------

The WMI kernel-mode component can send an **IRP\_MJ\_SYSTEM\_CONTROL** request any time following a driver's successful registration as a supplier of WMI data. WMI IRPs typically are sent when a user-mode data consumer has requested WMI data.

## Input Parameters


Depends on the value at **MinorFunction** in the current I/O stack location of the IRP. Every **IRP\_MJ\_SYSTEM\_CONTROL** request specifies a minor function code that identifies the requested WMI action.

## Output Parameters


Depends on the value at **MinorFunction** in the current I/O stack location of the IRP.

Operation
---------

All drivers must support **IRP\_MJ\_SYSTEM\_CONTROL** requests by supplying a [*DispatchSystemControl*](https://msdn.microsoft.com/library/windows/hardware/ff543412) routine.

Drivers that support [Windows Management Instrumentation](https://msdn.microsoft.com/library/windows/hardware/ff547139) (WMI) must handle **IRP\_MJ\_SYSTEM\_CONTROL** requests by processing the minor function codes associated with this major function code. For information about the WMI minor function codes, see [WMI Minor IRPs](wmi-minor-irps.md).

Drivers that do not support WMI by [registering as a WMI data provider](https://msdn.microsoft.com/library/windows/hardware/ff560870) must pass **IRP\_MJ\_SYSTEM\_CONTROL** requests to the next lower driver.

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


[*DispatchSystemControl*](https://msdn.microsoft.com/library/windows/hardware/ff543412)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20IRP_MJ_SYSTEM_CONTROL%20%20RELEASE:%20%288/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


