---
title: IRP_MN_POWER_SEQUENCE
description: This IRP returns the power sequence values for a device.
ms.date: 08/12/2017
ms.assetid: f00c0021-a909-4d76-9114-6710e1aa4307
keywords:
 - IRP_MN_POWER_SEQUENCE Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_POWER\_SEQUENCE


This IRP returns the power sequence values for a device.

Major Code
----------

[**IRP\_MJ\_POWER**](irp-mj-power.md)
When Sent
---------

A driver sends this IRP as an optimization to determine whether its device actually entered a specific power state. Support for this IRP is optional.

To send this IRP, a driver must call [**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257) to allocate the IRP, specifying the major IRP code [**IRP\_MJ\_POWER**](irp-mj-power.md) and minor IRP code **IRP\_MN\_POWER\_SEQUENCE**. The driver must then call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) (Windows Vista) or [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654) (Windows Server 2003, Windows XP, and Windows 2000) to pass the IRP to the next lower driver. The power manager cannot send this IRP.

Senders of this IRP must be running at IRQL &lt;= DISPATCH\_LEVEL.

## Input Parameters


None.

## Output Parameters


**Parameters.PowerSequence** points to a **POWER\_SEQUENCE** structure with the following members:

<a href="" id="sequenced1"></a>**SequenceD1**  
Number of times the device has been in power state D1 or lower.

<a href="" id="sequenced2"></a>**SequenceD2**  
Number of times the device has been in power state D2 or lower.

<a href="" id="sequenced3"></a>**SequenceD3**  
Number of times the device has been in power state D3.

The sequence values track the minimum number of times a device has been in the corresponding power state or a lower power state.

The bus driver increments the values in **SequenceD1**, **SequenceD2**, and **SequenceD3** at least each time the device enters in the corresponding power state or a lower power state.

## I/O Status Block


A driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS to indicate that it has returned the requested information, or to STATUS\_NOT\_IMPLEMENTED to indicate that it does not support this IRP.

Operation
---------

This IRP returns the power sequence values for a device. Bus drivers can optionally handle it; function and filter drivers can optionally send it.

For a device that takes a long time to change state, this IRP provides a useful optimization. Every time the device changes its power state, its bus driver increments the sequence value for that power state. The bus driver initializes the sequence values at boot time and continually increments them thereafter; they need not be reset to zero.

A device policy owner can send this IRP once to get the sequence values before shutting off the device and once again to get new values when restoring power to the device. By comparing the two sets of values, the driver can determine whether the device actually entered the lower-powered state. If the device did not lose power, the driver can avoid a time-consuming reinitialization when the device returns to the D0 state.

For example, if the device takes a long time to restore power upon reaching the D2 state, the driver can store the **SequenceD2** value before it sets the device state to D2 or lower. Later, when power is being restored to the device, the driver can compare the new **SequenceD2** value with its stored value to determine whether the device state actually dropped below D2. If the values match, the device did not actually enter power state D2 or a lower state, and the driver can avoid reinitializing the device.

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

 

 




