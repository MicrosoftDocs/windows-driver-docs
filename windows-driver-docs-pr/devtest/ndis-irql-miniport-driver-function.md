---
title: Irql\_Miniport\_Driver\_Function rule (ndis)
description: The Irql\_Miniport\_Driver\_Function rule specifies that the NDIS functions for miniport drivers must be called at correct IRQL levels.
ms.assetid: b82627db-63bd-413f-9d7f-dbb611cf2c50
keywords: ["Irql_Miniport_Driver_Function rule (ndis)"]
topic_type:
- apiref
api_name:
- Irql_Miniport_Driver_Function
api_type:
- NA
---

# Irql\_Miniport\_Driver\_Function rule (ndis)


The Irql\_Miniport\_Driver\_Function rule specifies that the NDIS functions for miniport drivers must be called at correct IRQL levels.

This rule verifies functions for NDIS miniport driver logging, NDIS ports, and NDIS DMA interface.

**NdisMCreateLog**
**NdisMDeregisterDmaChannel**
**NdisMDeregisterIoPortRange**
**NdisMDeregisterMiniportDriver**
**NdisMFlushLog**
**NdisMFreePort**
**NdisMFreeSharedMemory**
**NdisMGetDeviceProperty**
**NdisMGetDmaAlignment**
**NdisMMapIoSpace**
**NdisMPauseComplete**
**NdisMQueryAdapterInstanceName**
**NdisMReadDmaCounter**
**NdisMRegisterDmaChannel**
**NdisMRegisterIoPortRange**
**NdisMRegisterMiniportDriver**
**NdisMRemoveMiniport**
**NdisMResetComplete**
**NdisMRestartComplete**
**NdisMSetMiniportAttributes**
**NdisMSetupDmaTransfer**
**NdisMSleep**
**NdisMUnmapIoSpace**
**NdisMUpdateSharedMemory**
**NdisMWriteLogData**
|              |      |
|--------------|------|
| Driver model | NDIS |

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At compile time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>Irql_Miniport_Driver_Function</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li>[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)</li>
<li>[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)</li>
<li>[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)</li>
</ol>
<p>For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281).</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**NdisMCreateLog**](https://msdn.microsoft.com/library/windows/hardware/ff563572)
[**NdisMDeregisterDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff563574)
[**NdisMDeregisterIoPortRange**](https://msdn.microsoft.com/library/windows/hardware/ff563577)
[**NdisMDeregisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563578)
[**NdisMFlushLog**](https://msdn.microsoft.com/library/windows/hardware/ff563584)
[**NdisMFreePort**](https://msdn.microsoft.com/library/windows/hardware/ff563588)
[**NdisMFreeSharedMemory**](https://msdn.microsoft.com/library/windows/hardware/ff563589)
[**NdisMGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff563592)
[**NdisMGetDmaAlignment**](https://msdn.microsoft.com/library/windows/hardware/ff563593)
[**NdisMMapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/ff563613)
[**NdisMPauseComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563628)
[**NdisMQueryAdapterInstanceName**](https://msdn.microsoft.com/library/windows/hardware/ff563630)
[**NdisMReadDmaCounter**](https://msdn.microsoft.com/library/windows/hardware/ff563641)
[**NdisMRegisterDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff563646)
[**NdisMRegisterIoPortRange**](https://msdn.microsoft.com/library/windows/hardware/ff563651)
[**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654)
[**NdisMRemoveMiniport**](https://msdn.microsoft.com/library/windows/hardware/ff563661)
[**NdisMResetComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563663)
[**NdisMRestartComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563665)
[**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672)
[**NdisMSetupDmaTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff563675)
[**NdisMSleep**](https://msdn.microsoft.com/library/windows/hardware/ff563677)
[**NdisMUnmapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/ff563691)
[**NdisMWriteLogData**](https://msdn.microsoft.com/library/windows/hardware/ff563695)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Irql_Miniport_Driver_Function%20rule%20%28ndis%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




