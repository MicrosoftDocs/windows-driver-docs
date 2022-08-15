---
title: Irql rule set (WDM)
description: Learn about using rules (WDM) to verify that your driver makes DDI calls at the required IRQL. In addition, learn how to select the IRQL rule set.
ms.date: 05/21/2018
---

# Irql rule set (WDM)


Use these rules to verify that your driver makes DDI calls at the required IRQL.

A driver that does not follow the IRQL rules can cause serious problems during operation that can lead to deadlock conditions or computer crashes.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="wdm-forwardedatbadirql.md" data-raw-source="[&lt;strong&gt;ForwardedAtBadIrql&lt;/strong&gt;](wdm-forwardedatbadirql.md)"><strong>ForwardedAtBadIrql</strong></a></p></td>
<td align="left"><p>The <a href="wdm-forwardedatbadirql.md" data-raw-source="[&lt;strong&gt;ForwardedAtBadIrql&lt;/strong&gt;](wdm-forwardedatbadirql.md)"><strong>ForwardedAtBadIrql</strong></a> rule specifies that the driver should call <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver" data-raw-source="[&lt;strong&gt;IoCallDriver&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver)"><strong>IoCallDriver</strong></a> and <a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver" data-raw-source="[&lt;strong&gt;PoCallDriver&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver)"><strong>PoCallDriver</strong></a> at IRQL&lt;DISPATCH_LEVEL unless the IRP major function code being forwarded is one of the following:</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-forwardedatbadirqlallocate.md" data-raw-source="[&lt;strong&gt;ForwardedAtBadIrqlAllocate&lt;/strong&gt;](wdm-forwardedatbadirqlallocate.md)"><strong>ForwardedAtBadIrqlAllocate</strong></a></p></td>
<td align="left"><p>The <a href="wdm-forwardedatbadirqlallocate.md" data-raw-source="[&lt;strong&gt;ForwardedAtBadIrqlAllocate&lt;/strong&gt;](wdm-forwardedatbadirqlallocate.md)"><strong>ForwardedAtBadIrqlAllocate</strong></a> rule specifies that the driver should call <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver" data-raw-source="[&lt;strong&gt;IoCallDriver&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver)"><strong>IoCallDriver</strong></a> and <a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver" data-raw-source="[&lt;strong&gt;PoCallDriver&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver)"><strong>PoCallDriver</strong></a> at IRQL&lt;DISPATCH_LEVEL, unless the IRP major function code being forwarded is one of the following:</p>
<ul>
<li><a href="/windows-hardware/drivers/kernel/irp-mj-power" data-raw-source="[&lt;strong&gt;IRP_MJ_POWER&lt;/strong&gt;](../kernel/irp-mj-power.md)"><strong>IRP_MJ_POWER</strong></a></li>
<li><a href="/windows-hardware/drivers/kernel/irp-mj-read" data-raw-source="[&lt;strong&gt;IRP_MJ_READ&lt;/strong&gt;](../kernel/irp-mj-read.md)"><strong>IRP_MJ_READ</strong></a></li>
<li><a href="/windows-hardware/drivers/kernel/irp-mj-write" data-raw-source="[&lt;strong&gt;IRP_MJ_WRITE&lt;/strong&gt;](../kernel/irp-mj-write.md)"><strong>IRP_MJ_WRITE</strong></a></li>
<li><a href="/windows-hardware/drivers/kernel/irp-mj-device-control" data-raw-source="[&lt;strong&gt;IRP_MJ_DEVICE_CONTROL&lt;/strong&gt;](../kernel/irp-mj-device-control.md)"><strong>IRP_MJ_DEVICE_CONTROL</strong></a></li>
<li><a href="/windows-hardware/drivers/kernel/irp-mj-internal-device-control" data-raw-source="[&lt;strong&gt;IRP_MJ_INTERNAL_DEVICE_CONTROL&lt;/strong&gt;](../kernel/irp-mj-internal-device-control.md)"><strong>IRP_MJ_INTERNAL_DEVICE_CONTROL</strong></a></li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-forwardedatbadirqlfsdasync.md" data-raw-source="[&lt;strong&gt;ForwardedAtBadIrqlFsdAsync&lt;/strong&gt;](wdm-forwardedatbadirqlfsdasync.md)"><strong>ForwardedAtBadIrqlFsdAsync</strong></a></p></td>
<td align="left"><p>The <a href="wdm-forwardedatbadirqlfsdasync.md" data-raw-source="[&lt;strong&gt;ForwardedAtBadIrqlFsdAsync&lt;/strong&gt;](wdm-forwardedatbadirqlfsdasync.md)"><strong>ForwardedAtBadIrqlFsdAsync</strong></a> rule specifies that the driver call <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver" data-raw-source="[&lt;strong&gt;IoCallDriver&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver)"><strong>IoCallDriver</strong></a> and <a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver" data-raw-source="[&lt;strong&gt;PoCallDriver&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver)"><strong>PoCallDriver</strong></a> at IRQL&lt;DISPATCH_LEVEL, unless the IRP major function code being forwarded is one of the following:</p>
<ul>
<li><a href="/windows-hardware/drivers/kernel/irp-mj-power" data-raw-source="[&lt;strong&gt;IRP_MJ_POWER&lt;/strong&gt;](../kernel/irp-mj-power.md)"><strong>IRP_MJ_POWER</strong></a></li>
<li><a href="/windows-hardware/drivers/kernel/irp-mj-read" data-raw-source="[&lt;strong&gt;IRP_MJ_READ&lt;/strong&gt;](../kernel/irp-mj-read.md)"><strong>IRP_MJ_READ</strong></a></li>
<li><a href="/windows-hardware/drivers/kernel/irp-mj-write" data-raw-source="[&lt;strong&gt;IRP_MJ_WRITE&lt;/strong&gt;](../kernel/irp-mj-write.md)"><strong>IRP_MJ_WRITE</strong></a></li>
<li><a href="/windows-hardware/drivers/kernel/irp-mj-device-control" data-raw-source="[&lt;strong&gt;IRP_MJ_DEVICE_CONTROL&lt;/strong&gt;](../kernel/irp-mj-device-control.md)"><strong>IRP_MJ_DEVICE_CONTROL</strong></a></li>
<li><a href="/windows-hardware/drivers/kernel/irp-mj-internal-device-control" data-raw-source="[&lt;strong&gt;IRP_MJ_INTERNAL_DEVICE_CONTROL&lt;/strong&gt;](../kernel/irp-mj-internal-device-control.md)"><strong>IRP_MJ_INTERNAL_DEVICE_CONTROL</strong></a></li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-forwardedatbadirqlfsdsync.md" data-raw-source="[&lt;strong&gt;ForwardedAtBadIrqlFsdSync&lt;/strong&gt;](wdm-forwardedatbadirqlfsdsync.md)"><strong>ForwardedAtBadIrqlFsdSync</strong></a></p></td>
<td align="left"><p>The <a href="wdm-forwardedatbadirqlfsdsync.md" data-raw-source="[&lt;strong&gt;ForwardedAtBadIrqlFsdSync&lt;/strong&gt;](wdm-forwardedatbadirqlfsdsync.md)"><strong>ForwardedAtBadIrqlFsdSync</strong></a> rule specifies that the driver call <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver" data-raw-source="[&lt;strong&gt;IoCallDriver&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver)"><strong>IoCallDriver</strong></a> and <a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver" data-raw-source="[&lt;strong&gt;PoCallDriver&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver)"><strong>PoCallDriver</strong></a> at IRQL&lt;DISPATCH_LEVEL, unless the IRP major function code being forwarded is one of the following:</p>
<ul>
<li><a href="/windows-hardware/drivers/kernel/irp-mj-power" data-raw-source="[&lt;strong&gt;IRP_MJ_POWER&lt;/strong&gt;](../kernel/irp-mj-power.md)"><strong>IRP_MJ_POWER</strong></a></li>
<li><a href="/windows-hardware/drivers/kernel/irp-mj-read" data-raw-source="[&lt;strong&gt;IRP_MJ_READ&lt;/strong&gt;](../kernel/irp-mj-read.md)"><strong>IRP_MJ_READ</strong></a></li>
<li><a href="/windows-hardware/drivers/kernel/irp-mj-write" data-raw-source="[&lt;strong&gt;IRP_MJ_WRITE&lt;/strong&gt;](../kernel/irp-mj-write.md)"><strong>IRP_MJ_WRITE</strong></a></li>
<li><a href="/windows-hardware/drivers/kernel/irp-mj-device-control" data-raw-source="[&lt;strong&gt;IRP_MJ_DEVICE_CONTROL&lt;/strong&gt;](../kernel/irp-mj-device-control.md)"><strong>IRP_MJ_DEVICE_CONTROL</strong></a></li>
<li><a href="/windows-hardware/drivers/kernel/irp-mj-internal-device-control" data-raw-source="[&lt;strong&gt;IRP_MJ_INTERNAL_DEVICE_CONTROL&lt;/strong&gt;](../kernel/irp-mj-internal-device-control.md)"><strong>IRP_MJ_INTERNAL_DEVICE_CONTROL</strong></a></li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-irqlapclte.md" data-raw-source="[&lt;strong&gt;IrqlApcLte&lt;/strong&gt;](wdm-irqlapclte.md)"><strong>IrqlApcLte</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlapclte.md" data-raw-source="[&lt;strong&gt;IrqlApcLte&lt;/strong&gt;](wdm-irqlapclte.md)"><strong>IrqlApcLte</strong></a> rule specifies that the driver calls <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-obgetobjectsecurity" data-raw-source="[&lt;strong&gt;ObGetObjectSecurity&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-obgetobjectsecurity)"><strong>ObGetObjectSecurity</strong></a> and <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-obreleaseobjectsecurity" data-raw-source="[&lt;strong&gt;ObReleaseObjectSecurity&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-obreleaseobjectsecurity)"><strong>ObReleaseObjectSecurity</strong></a> only when it is executing at IRQL &lt;= APC_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-irqldispatch.md" data-raw-source="[&lt;strong&gt;IrqlDispatch&lt;/strong&gt;](wdm-irqldispatch.md)"><strong>IrqlDispatch</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqldispatch.md" data-raw-source="[&lt;strong&gt;IrqlDispatch&lt;/strong&gt;](wdm-irqldispatch.md)"><strong>IrqlDispatch</strong></a> rule specifies that the driver calls the following DDIs only when it is executing at IRQL = DISPATCH_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-irqlexallocatepool.md" data-raw-source="[&lt;strong&gt;IrqlExAllocatePool&lt;/strong&gt;](wdm-irqlexallocatepool.md)"><strong>IrqlExAllocatePool</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlexallocatepool.md" data-raw-source="[&lt;strong&gt;IrqlExAllocatePool&lt;/strong&gt;](wdm-irqlexallocatepool.md)"><strong>IrqlExAllocatePool</strong></a> rule specifies that the driver calls <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtag" data-raw-source="[&lt;strong&gt;ExAllocatePoolWithTag&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtag)"><strong>ExAllocatePoolWithTag</strong></a> and <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtagpriority" data-raw-source="[&lt;strong&gt;ExAllocatePoolWithTagPriority&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtagpriority)"><strong>ExAllocatePoolWithTagPriority</strong></a> only when it is executing at IRQL&lt;=DISPATCH_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-irqlexapclte1.md" data-raw-source="[&lt;strong&gt;IrqlExApcLte1&lt;/strong&gt;](wdm-irqlexapclte1.md)"><strong>IrqlExApcLte1</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlexapclte1.md" data-raw-source="[&lt;strong&gt;IrqlExApcLte1&lt;/strong&gt;](wdm-irqlexapclte1.md)"><strong>IrqlExApcLte1</strong></a> rule specifies that the driver calls <a href="/previous-versions/windows/hardware/drivers/ff544337(v=vs.85)" data-raw-source="[&lt;strong&gt;ExAcquireFastMutex&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff544337(v=vs.85))"><strong>ExAcquireFastMutex</strong></a> and <a href="/previous-versions/windows/hardware/drivers/ff545647(v=vs.85)" data-raw-source="[&lt;strong&gt;ExTryToAcquireFastMutex&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff545647(v=vs.85))"><strong>ExTryToAcquireFastMutex</strong></a> only at IRQL &lt;= APC_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-irqlexapclte2.md" data-raw-source="[&lt;strong&gt;IrqlExApcLte2&lt;/strong&gt;](wdm-irqlexapclte2.md)"><strong>IrqlExApcLte2</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlexapclte2.md" data-raw-source="[&lt;strong&gt;IrqlExApcLte2&lt;/strong&gt;](wdm-irqlexapclte2.md)"><strong>IrqlExApcLte2</strong></a> rule specifies that the driver calls the following routines only at IRQL &lt;= APC_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-irqlexapclte3.md" data-raw-source="[&lt;strong&gt;IrqlExApcLte3&lt;/strong&gt;](wdm-irqlexapclte3.md)"><strong>IrqlExApcLte3</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlexapclte3.md" data-raw-source="[&lt;strong&gt;IrqlExApcLte3&lt;/strong&gt;](wdm-irqlexapclte3.md)"><strong>IrqlExApcLte3</strong></a> rule specifies that the driver calls the following executive support routines only at IRQL &lt;= APC_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-irqlexapclteinline.md" data-raw-source="[&lt;strong&gt;IrqlExApcLteInline&lt;/strong&gt;](wdm-irqlexapclteinline.md)"><strong>IrqlExApcLteInline</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlexapclteinline.md" data-raw-source="[&lt;strong&gt;IrqlExApcLteInline&lt;/strong&gt;](wdm-irqlexapclteinline.md)"><strong>IrqlExApcLteInline</strong></a> rule specifies that DDIs are only called at proper IRQL levels</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-irqlexfree1.md" data-raw-source="[&lt;strong&gt;IrqlExFree1&lt;/strong&gt;](wdm-irqlexfree1.md)"><strong>IrqlExFree1</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlexfree1.md" data-raw-source="[&lt;strong&gt;IrqlExFree1&lt;/strong&gt;](wdm-irqlexfree1.md)"><strong>IrqlExFree1</strong></a> rule specifies that <a href="/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exfreepool" data-raw-source="[&lt;strong&gt;ExFreePool&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exfreepool)"><strong>ExFreePool</strong></a> and <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-exfreepoolwithtag" data-raw-source="[&lt;strong&gt;ExFreePoolWithTag&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-exfreepoolwithtag)"><strong>ExFreePoolWithTag</strong></a> are called at proper IRQL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-irqlexfree2.md" data-raw-source="[&lt;strong&gt;IrqlExFree2&lt;/strong&gt;](wdm-irqlexfree2.md)"><strong>IrqlExFree2</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlexfree2.md" data-raw-source="[&lt;strong&gt;IrqlExFree2&lt;/strong&gt;](wdm-irqlexfree2.md)"><strong>IrqlExFree2</strong></a> rule specifies that <a href="/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exfreepool" data-raw-source="[&lt;strong&gt;ExFreePool&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exfreepool)"><strong>ExFreePool</strong></a> and <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-exfreepoolwithtag" data-raw-source="[&lt;strong&gt;ExFreePoolWithTag&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-exfreepoolwithtag)"><strong>ExFreePoolWithTag</strong></a> are called at proper IRQL.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-irqlexfree3.md" data-raw-source="[&lt;strong&gt;IrqlExFree3&lt;/strong&gt;](wdm-irqlexfree3.md)"><strong>IrqlExFree3</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlexfree3.md" data-raw-source="[&lt;strong&gt;IrqlExFree3&lt;/strong&gt;](wdm-irqlexfree3.md)"><strong>IrqlExFree3</strong></a> rule specifies that <a href="/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exfreepool" data-raw-source="[&lt;strong&gt;ExFreePool&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exfreepool)"><strong>ExFreePool</strong></a> and <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-exfreepoolwithtag" data-raw-source="[&lt;strong&gt;ExFreePoolWithTag&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-exfreepoolwithtag)"><strong>ExFreePoolWithTag</strong></a> are called at proper IRQL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-irqlexpassive.md" data-raw-source="[&lt;strong&gt;IrqlExPassive&lt;/strong&gt;](wdm-irqlexpassive.md)"><strong>IrqlExPassive</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlexpassive.md" data-raw-source="[&lt;strong&gt;IrqlExPassive&lt;/strong&gt;](wdm-irqlexpassive.md)"><strong>IrqlExPassive</strong></a> rule specifies that the driver calls the following executive support routines only at IRQL = PASSIVE_LEVEL:</p>
<ul>
<li><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-excreatecallback" data-raw-source="[&lt;strong&gt;ExCreateCallback&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-excreatecallback)"><strong>ExCreateCallback</strong></a></p></li>
<li><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-exisprocessorfeaturepresent" data-raw-source="[&lt;strong&gt;ExIsProcessorFeaturePresent&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-exisprocessorfeaturepresent)"><strong>ExIsProcessorFeaturePresent</strong></a></p></li>
<li><p><a href="/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exraiseaccessviolation" data-raw-source="[&lt;strong&gt;ExRaiseAccessViolation&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exraiseaccessviolation)"><strong>ExRaiseAccessViolation</strong></a></p></li>
<li><p><a href="/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exraisedatatypemisalignment" data-raw-source="[&lt;strong&gt;ExRaiseDatatypeMisalignment&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exraisedatatypemisalignment)"><strong>ExRaiseDatatypeMisalignment</strong></a></p></li>
<li><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-exraisestatus" data-raw-source="[&lt;strong&gt;ExRaiseStatus&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-exraisestatus)"><strong>ExRaiseStatus</strong></a></p></li>
<li><p><a href="/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exuuidcreate" data-raw-source="[&lt;strong&gt;ExUuidCreate&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exuuidcreate)"><strong>ExUuidCreate</strong></a></p></li>
</ul>
<p>The <a href="wdm-irqlexpassive.md" data-raw-source="[&lt;strong&gt;IrqlExPassive&lt;/strong&gt;](wdm-irqlexpassive.md)"><strong>IrqlExPassive</strong></a> rule also specifies that the driver calls <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-exraisestatus" data-raw-source="[&lt;strong&gt;ExRaiseStatus&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-exraisestatus)"><strong>ExRaiseStatus</strong></a> at IRQL &lt;= APC_LEVEL</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-irqlioapclte.md" data-raw-source="[&lt;strong&gt;IrqlIoApcLte&lt;/strong&gt;](wdm-irqlioapclte.md)"><strong>IrqlIoApcLte</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlioapclte.md" data-raw-source="[&lt;strong&gt;IrqlIoApcLte&lt;/strong&gt;](wdm-irqlioapclte.md)"><strong>IrqlIoApcLte</strong></a> rule specifies that the driver calls the following I/O manager routines only when it is executing at IRQL &lt;= APC_LEVEL:</p>
<ul>
<li><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iodeletedevice" data-raw-source="[&lt;strong&gt;IoDeleteDevice&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iodeletedevice)"><strong>IoDeleteDevice</strong></a></p></li>
<li><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetinitialstack" data-raw-source="[&lt;strong&gt;IoGetInitialStack&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetinitialstack)"><strong>IoGetInitialStack</strong></a></p></li>
<li><p><a href="/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioraiseharderror" data-raw-source="[&lt;strong&gt;IoRaiseHardError&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioraiseharderror)"><strong>IoRaiseHardError</strong></a></p></li>
<li><p><a href="/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioraiseinformationalharderror" data-raw-source="[&lt;strong&gt;IoRaiseInformationalHardError&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioraiseinformationalharderror)"><strong>IoRaiseInformationalHardError</strong></a></p></li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-irqliodispatch.md" data-raw-source="[&lt;strong&gt;IrqlIoDispatch&lt;/strong&gt;](wdm-irqliodispatch.md)"><strong>IrqlIoDispatch</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqliodispatch.md" data-raw-source="[&lt;strong&gt;IrqlIoDispatch&lt;/strong&gt;](wdm-irqliodispatch.md)"><strong>IrqlIoDispatch</strong></a> rule specifies that the driver calls the following I/O Manager routines only when it is executing at IRQL &lt;= DISPATCH_LEVEL: <a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iogetdevicetoverify" data-raw-source="[&lt;strong&gt;IoGetDeviceToVerify&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iogetdevicetoverify)"><strong>IoGetDeviceToVerify</strong></a>, <a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iosetdevicetoverify" data-raw-source="[&lt;strong&gt;IoSetDeviceToVerify&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iosetdevicetoverify)"><strong>IoSetDeviceToVerify</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-irqliopassive1.md" data-raw-source="[&lt;strong&gt;IrqlIoPassive1&lt;/strong&gt;](wdm-irqliopassive1.md)"><strong>IrqlIoPassive1</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqliopassive1.md" data-raw-source="[&lt;strong&gt;IrqlIoPassive1&lt;/strong&gt;](wdm-irqliopassive1.md)"><strong>IrqlIoPassive1</strong></a> rule specifies that the driver calls the following routines only when it is executing at IRQL = PASSIVE_LEVEL:</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-irqliopassive2.md" data-raw-source="[&lt;strong&gt;IrqlIoPassive2&lt;/strong&gt;](wdm-irqliopassive2.md)"><strong>IrqlIoPassive2</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqliopassive2.md" data-raw-source="[&lt;strong&gt;IrqlIoPassive2&lt;/strong&gt;](wdm-irqliopassive2.md)"><strong>IrqlIoPassive2</strong></a> rule specifies that the driver calls the following I/O Manager routines only at IRQL = PASSIVE_LEVEL:</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-irqliopassive3.md" data-raw-source="[&lt;strong&gt;IrqlIoPassive3&lt;/strong&gt;](wdm-irqliopassive3.md)"><strong>IrqlIoPassive3</strong></a></p></td>
<td align="left"><p>The IrqlIoPassive3 rule specifies that the driver calls the following routines only when it is executing at IRQL = PASSIVE_LEVEL:</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-irqliopassive4.md" data-raw-source="[&lt;strong&gt;IrqlIoPassive4&lt;/strong&gt;](wdm-irqliopassive4.md)"><strong>IrqlIoPassive4</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqliopassive4.md" data-raw-source="[&lt;strong&gt;IrqlIoPassive4&lt;/strong&gt;](wdm-irqliopassive4.md)"><strong>IrqlIoPassive4</strong></a> rule specifies that the driver calls the following routines only when it is executing at IRQL = PASSIVE_LEVEL:</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-irqliopassive5.md" data-raw-source="[&lt;strong&gt;IrqlIoPassive5&lt;/strong&gt;](wdm-irqliopassive5.md)"><strong>IrqlIoPassive5</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqliopassive5.md" data-raw-source="[&lt;strong&gt;IrqlIoPassive5&lt;/strong&gt;](wdm-irqliopassive5.md)"><strong>IrqlIoPassive5</strong></a> rule specifies that the driver calls specific I/O Manager routines only when it is executing at IRQL = PASSIVE_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-irqliortlzwpassive.md" data-raw-source="[&lt;strong&gt;IrqlIoRtlZwPassive&lt;/strong&gt;](wdm-irqliortlzwpassive.md)"><strong>IrqlIoRtlZwPassive</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqliortlzwpassive.md" data-raw-source="[&lt;strong&gt;IrqlIoRtlZwPassive&lt;/strong&gt;](wdm-irqliortlzwpassive.md)"><strong>IrqlIoRtlZwPassive</strong></a> rule specifies that the driver calls specific I/O Manager routines only when it is executing at IRQL = PASSIVE_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-irqlkeapclte1.md" data-raw-source="[&lt;strong&gt;IrqlKeApcLte1&lt;/strong&gt;](wdm-irqlkeapclte1.md)"><strong>IrqlKeApcLte1</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlkeapclte1.md" data-raw-source="[&lt;strong&gt;IrqlKeApcLte1&lt;/strong&gt;](wdm-irqlkeapclte1.md)"><strong>IrqlKeApcLte1</strong></a> rule specifies that the driver calls the following kernel routines only when it is executing at IRQL &lt;= APC_LEVEL:</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-irqlkeapclte2.md" data-raw-source="[&lt;strong&gt;IrqlKeApcLte2&lt;/strong&gt;](wdm-irqlkeapclte2.md)"><strong>IrqlKeApcLte2</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlkeapclte2.md" data-raw-source="[&lt;strong&gt;IrqlKeApcLte2&lt;/strong&gt;](wdm-irqlkeapclte2.md)"><strong>IrqlKeApcLte2</strong></a> rule specifies that the driver calls the following kernel routines only when it is executing at IRQL &lt;= APC_LEVEL:</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-irqlkedispatchlte.md" data-raw-source="[&lt;strong&gt;IrqlKeDispatchLte&lt;/strong&gt;](wdm-irqlkedispatchlte.md)"><strong>IrqlKeDispatchLte</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlkedispatchlte.md" data-raw-source="[&lt;strong&gt;IrqlKeDispatchLte&lt;/strong&gt;](wdm-irqlkedispatchlte.md)"><strong>IrqlKeDispatchLte</strong></a> rule specifies that the driver calls the following kernel routines only when it is executing at IRQL &lt;= DISPATCH_LEVEL:</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-irqlkeraiselower.md" data-raw-source="[&lt;strong&gt;IrqlKeRaiseLower&lt;/strong&gt;](wdm-irqlkeraiselower.md)"><strong>IrqlKeRaiseLower</strong></a></p></td>
<td align="left"><p>The <a href="/windows-hardware/drivers/devtest/wdm-irqlkeraiselower" data-raw-source="[&lt;strong&gt;IrqlKeRaiseLower&lt;/strong&gt;](./wdm-irqlkeraiselower.md)"><strong>IrqlKeRaiseLower</strong></a> rule specifies that the driver does the following when raising and lowering the IRQL:</p>
When the driver calls <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-keraiseirql" data-raw-source="[&lt;strong&gt;KeRaiseIrql&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-keraiseirql)"><strong>KeRaiseIrql</strong></a>, it is executing at an IRQL that is lower than or equal to the value of the <em>NewIrql</em> parameter.<br />
The driver calls <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-kelowerirql" data-raw-source="[&lt;strong&gt;KeLowerIrql&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-kelowerirql)"><strong>KeLowerIrql</strong></a> only after calling <strong>KeRaiseIrql</strong> or <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-keraiseirqltodpclevel" data-raw-source="[&lt;strong&gt;KeRaiseIrqlToDpcLevel&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-keraiseirqltodpclevel)"><strong>KeRaiseIrqlToDpcLevel</strong></a>.<br />
</td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-irqlkeraiselower2.md" data-raw-source="[&lt;strong&gt;IrqlKeRaiseLower2&lt;/strong&gt;](wdm-irqlkeraiselower2.md)"><strong>IrqlKeRaiseLower2</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlkeraiselower2.md" data-raw-source="[&lt;strong&gt;IrqlKeRaiseLower2&lt;/strong&gt;](wdm-irqlkeraiselower2.md)"><strong>IrqlKeRaiseLower2</strong></a> rule specifies that drivers use <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-kelowerirql" data-raw-source="[&lt;strong&gt;KeLowerIrql&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-kelowerirql)"><strong>KeLowerIrql</strong></a> to restore the original IRQL raised by a preceding call to <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-keraiseirql" data-raw-source="[&lt;strong&gt;KeRaiseIrql&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-keraiseirql)"><strong>KeRaiseIrql</strong></a> or <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-keraiseirqltodpclevel" data-raw-source="[&lt;strong&gt;KeRaiseIrqlToDpcLevel&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-keraiseirqltodpclevel)"><strong>KeRaiseIrqlToDpcLevel</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-irqlkereleasespinlock.md" data-raw-source="[&lt;strong&gt;IrqlKeReleaseSpinLock&lt;/strong&gt;](wdm-irqlkereleasespinlock.md)"><strong>IrqlKeReleaseSpinLock</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlkereleasespinlock.md" data-raw-source="[&lt;strong&gt;IrqlKeReleaseSpinLock&lt;/strong&gt;](wdm-irqlkereleasespinlock.md)"><strong>IrqlKeReleaseSpinLock</strong></a> rule specifies that the driver calls <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleasespinlock" data-raw-source="[&lt;strong&gt;KeReleaseSpinLock&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleasespinlock)"><strong>KeReleaseSpinLock</strong></a> only when it is executing at IRQL = DISPATCH_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-irqlkesetevent.md" data-raw-source="[&lt;strong&gt;IrqlKeSetEvent&lt;/strong&gt;](wdm-irqlkesetevent.md)"><strong>IrqlKeSetEvent</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlkesetevent.md" data-raw-source="[&lt;strong&gt;IrqlKeSetEvent&lt;/strong&gt;](wdm-irqlkesetevent.md)"><strong>IrqlKeSetEvent</strong></a> rule specifies that the <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-kesetevent" data-raw-source="[&lt;strong&gt;KeSetEvent&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesetevent)"><strong>KeSetEvent</strong></a> routine is only called at IRQL &lt;= DISPATCH_LEVEL when <em>Wait</em> is set to <strong>FALSE</strong>, and at IRQL &lt;= APC_LEVEL when <em>Wait</em> is set to <strong>TRUE</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-irqlkewaitformutexobject.md" data-raw-source="[&lt;strong&gt;IrqlKeWaitForMutexObject&lt;/strong&gt;](wdm-irqlkewaitformutexobject.md)"><strong>IrqlKeWaitForMutexObject</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlkewaitformutexobject.md" data-raw-source="[&lt;strong&gt;IrqlKeWaitForMutexObject&lt;/strong&gt;](wdm-irqlkewaitformutexobject.md)"><strong>IrqlKeWaitForMutexObject</strong></a> rule specifies the driver to call the <a href="wdm-irqlkewaitformutexobject.md" data-raw-source="[&lt;strong&gt;KeWaitForMutexObject&lt;/strong&gt;](wdm-irqlkewaitformutexobject.md)"><strong>KeWaitForMutexObject</strong></a> routine at the proper IRQL based on the value of the <em>Timeout</em> parameter:</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-irqlkewaitformultipleobjects.md" data-raw-source="[&lt;strong&gt;IrqlKeWaitForMultipleObjects&lt;/strong&gt;](wdm-irqlkewaitformultipleobjects.md)"><strong>IrqlKeWaitForMultipleObjects</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlkewaitformultipleobjects.md" data-raw-source="[&lt;strong&gt;IrqlKeWaitForMultipleObjects&lt;/strong&gt;](wdm-irqlkewaitformultipleobjects.md)"><strong>IrqlKeWaitForMultipleObjects</strong></a> rule specifies that callers of the <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitformultipleobjects" data-raw-source="[&lt;strong&gt;KeWaitForMultipleObjects&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitformultipleobjects)"><strong>KeWaitForMultipleObjects</strong></a> routine must be running at proper IRQL based upon the <em>Timeout</em> parameter.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-irqlmmapclte.md" data-raw-source="[&lt;strong&gt;IrqlMmApcLte&lt;/strong&gt;](wdm-irqlmmapclte.md)"><strong>IrqlMmApcLte</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlmmapclte.md" data-raw-source="[&lt;strong&gt;IrqlMmApcLte&lt;/strong&gt;](wdm-irqlmmapclte.md)"><strong>IrqlMmApcLte</strong></a> rule specifies that the driver calls the following memory manager routines only when it is executing at IRQL &lt;= APC_LEVEL:</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-irqlmmdispatch.md" data-raw-source="[&lt;strong&gt;IrqlMmDispatch&lt;/strong&gt;](wdm-irqlmmdispatch.md)"><strong>IrqlMmDispatch</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlmmdispatch.md" data-raw-source="[&lt;strong&gt;IrqlMmDispatch&lt;/strong&gt;](wdm-irqlmmdispatch.md)"><strong>IrqlMmDispatch</strong></a> rule specifies that the driver calls <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-mmfreecontiguousmemory" data-raw-source="[&lt;strong&gt;MmFreeContiguousMemory&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmfreecontiguousmemory)"><strong>MmFreeContiguousMemory</strong></a> only when it is executing at <strong>IRQL &lt;= DISPATCH_LEVEL</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-irqlntifsapcpassive.md" data-raw-source="[&lt;strong&gt;IrqlNtifsApcPassive&lt;/strong&gt;](wdm-irqlntifsapcpassive.md)"><strong>IrqlNtifsApcPassive</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlntifsapcpassive.md" data-raw-source="[&lt;strong&gt;IrqlNtifsApcPassive&lt;/strong&gt;](wdm-irqlntifsapcpassive.md)"><strong>IIrqlNtifsApcPassive</strong></a> rule specifies that the driver calls the DDIs listed in the rule only when it is executing either at IRQL = PASSIVE_LEVEL or at IRQL <= APC_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-irqlobpassive.md" data-raw-source="[&lt;strong&gt;IrqlObPassive&lt;/strong&gt;](wdm-irqlobpassive.md)"><strong>IrqlObPassive</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlobpassive.md" data-raw-source="[&lt;strong&gt;IrqlObPassive&lt;/strong&gt;](wdm-irqlobpassive.md)"><strong>IrqlObPassive</strong></a> rule specifies that the driver calls <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-obreferenceobjectbyhandle" data-raw-source="[&lt;strong&gt;ObReferenceObjectByHandle&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-obreferenceobjectbyhandle)"><strong>ObReferenceObjectByHandle</strong></a> only when it is executing at IRQL = PASSIVE_LEVEL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-irqlpspassive.md" data-raw-source="[&lt;strong&gt;IrqlPsPassive&lt;/strong&gt;](wdm-irqlpspassive.md)"><strong>IrqlPsPassive</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlpspassive.md" data-raw-source="[&lt;strong&gt;IrqlPsPassive&lt;/strong&gt;](wdm-irqlpspassive.md)"><strong>IrqlPsPassive</strong></a> rule specifies that the driver calls the following <a href="/windows-hardware/drivers/ddi/index" data-raw-source="[&lt;strong&gt;Process Structure routines&lt;/strong&gt;](/windows-hardware/drivers/ddi/index)"><strong>Process Structure routines</strong></a> only when it is executing at IRQL = PASSIVE_LEVEL:</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-irqlreturn.md" data-raw-source="[&lt;strong&gt;IrqlReturn&lt;/strong&gt;](wdm-irqlreturn.md)"><strong>IrqlReturn</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlreturn.md" data-raw-source="[&lt;strong&gt;IrqlReturn&lt;/strong&gt;](wdm-irqlreturn.md)"><strong>IrqlReturn</strong></a> rule specifies that the driver's dispatch routines return at the same IRQL at which they were called.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-irqlrtlpassive.md" data-raw-source="[&lt;strong&gt;IrqlRtlPassive&lt;/strong&gt;](wdm-irqlrtlpassive.md)"><strong>IrqlRtlPassive</strong></a></p></td>
<td align="left"><p>The IrqlRtlPassive rule specifies that the driver calls <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-rtldeleteregistryvalue" data-raw-source="[&lt;strong&gt;RtlDeleteRegistryValue&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtldeleteregistryvalue)"><strong>RtlDeleteRegistryValue</strong></a> only when it is executing at IRQL = PASSIVE_LEVEL.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-irqlzwpassive.md" data-raw-source="[&lt;strong&gt;IrqlZwPassive&lt;/strong&gt;](wdm-irqlzwpassive.md)"><strong>IrqlZwPassive</strong></a></p></td>
<td align="left"><p>The <a href="wdm-irqlzwpassive.md" data-raw-source="[&lt;strong&gt;IrqlZwPassive&lt;/strong&gt;](wdm-irqlzwpassive.md)"><strong>IrqlZwPassive</strong></a> rule specifies that the driver calls <a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose" data-raw-source="[&lt;strong&gt;ZwClose&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose)"><strong>ZwClose</strong></a> only when it is executing at IRQL = PASSIVE_LEVEL.</p></td>
</tr>
</tbody>
</table>

 

**To select the Irql rule set**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **Irql**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **Irql.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:Irql.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md) and [Static Driver Verifier commands (MSBuild)](./-static-driver-verifier-commands--msbuild-.md).

