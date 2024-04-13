---
title: DDI Usage Rule Set (NDIS)
description: Use these rules to verify that your driver correctly uses NDIS DDIs correctly.
ms.date: 05/21/2018
---

# DDI usage rule set (NDIS)


Use these rules to verify that your driver correctly uses NDIS DDIs correctly.

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
<td align="left"><p><a href="ndis-init-deregisterinterrupt.md" data-raw-source="[&lt;strong&gt;Init_DeRegisterInterrupt&lt;/strong&gt;](ndis-init-deregisterinterrupt.md)"><strong>Init_DeRegisterInterrupt</strong></a></p></td>
<td align="left"><p>The <a href="ndis-init-deregisterinterrupt.md" data-raw-source="[&lt;strong&gt;Init_DeRegisterInterrupt&lt;/strong&gt;](ndis-init-deregisterinterrupt.md)"><strong>Init_DeRegisterInterrupt</strong></a> rule specifies that if <a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterinterruptex" data-raw-source="[&lt;strong&gt;NdisMRegisterInterruptEx&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterinterruptex)"><strong>NdisMRegisterInterruptEx</strong></a> is called at least once during MPInitilize, <a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismderegisterinterruptex" data-raw-source="[&lt;strong&gt;NdisMDeregisterInterruptEx&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismderegisterinterruptex)"><strong>NdisMDeregisterInterruptEx</strong></a> should be called at least once in MPHaltEx.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-init-ndisallocateioworkitem.md" data-raw-source="[&lt;strong&gt;Init_NdisAllocateIoWorkItem&lt;/strong&gt;](ndis-init-ndisallocateioworkitem.md)"><strong>Init_NdisAllocateIoWorkItem</strong></a></p></td>
<td align="left"><p>The <a href="ndis-init-ndisallocateioworkitem.md" data-raw-source="[&lt;strong&gt;Init_NdisAllocateIoWorkItem&lt;/strong&gt;](ndis-init-ndisallocateioworkitem.md)"><strong>Init_NdisAllocateIoWorkItem</strong></a> rule specifies that if <a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocateioworkitem" data-raw-source="[&lt;strong&gt;NdisAllocateIoWorkItem&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocateioworkitem)"><strong>NdisAllocateIoWorkItem</strong></a> is called at least once during <a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize" data-raw-source="[&lt;em&gt;MiniportInitializeEx&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize)"><em>MiniportInitializeEx</em></a>, the <a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreeioworkitem" data-raw-source="[&lt;strong&gt;NdisFreeIoWorkItem&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfreeioworkitem)"><strong>NdisFreeIoWorkItem</strong></a> function should:</p>
<ul>
<li>- be called at least once in MPHaltEx, if <a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize" data-raw-source="[&lt;em&gt;MiniportInitializeEx&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize)"><em>MiniportInitializeEx</em></a> succeeds.</li>
<li>- be called in <a href="/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize" data-raw-source="[&lt;em&gt;MiniportInitializeEx&lt;/em&gt;](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize)"><em>MiniportInitializeEx</em></a>, if <em>MiniportInitializeEx</em> fails.</li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-init-registerinterrupt.md" data-raw-source="[&lt;strong&gt;Init_RegisterInterrupt&lt;/strong&gt;](ndis-init-registerinterrupt.md)"><strong>Init_RegisterInterrupt</strong></a></p></td>
<td align="left"><p>The Init_RegisterInterrupt rule specifies that the registration of interrupts, which usually happens during initialization, must be undone if something goes wrong in the initialization process or during the halting of the miniport driver.</p>
<p>If <strong>NdisMRegisterInterruptEx</strong> is called at least one time during <strong>MiniportInitializeEx</strong>, the <strong>NdisMDeregisterInterruptEx</strong> function must be called at least one time in <strong>MiniportHaltEx</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-init-registersg.md" data-raw-source="[&lt;strong&gt;Init_RegisterSG&lt;/strong&gt;](ndis-init-registersg.md)"><strong>Init_RegisterSG</strong></a></p></td>
<td align="left"><p>The Init_RegisterSG rule specifies that the registration of the scatter-gather list (SG), which usually happens during initialization, must be undone if something goes wrong in the initialization process or during the halting of the miniport driver.</p>
<p>If <strong>NdisMRegisterScatterGatherDma</strong> is called at least one time during <strong>MiniportInitializeEx</strong>, the <strong>NdisMDeregisterScatterGatherDma</strong> function should be called at least one time in <strong>MiniportHaltEx</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-ndisfderegisterfilterdriver.md" data-raw-source="[&lt;strong&gt;NdisFDeregisterFilterDriver&lt;/strong&gt;](ndis-ndisfderegisterfilterdriver.md)"><strong>NdisFDeregisterFilterDriver</strong></a></p></td>
<td align="left"><p>A filter driver must call <a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfderegisterfilterdriver" data-raw-source="[&lt;strong&gt;NdisFDeregisterFilterDriver&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfderegisterfilterdriver)"><strong>NdisFDeregisterFilterDriver</strong></a> from its <a href="/windows-hardware/drivers/network/unloading-a-filter-driver" data-raw-source="[&lt;strong&gt;FilterDriverUnload&lt;/strong&gt;](../network/unloading-a-filter-driver.md)"><strong>FilterDriverUnload</strong></a> routine.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-ndismderegisterinterruptex.md" data-raw-source="[&lt;strong&gt;NdisMDeregisterInterruptEx&lt;/strong&gt;](ndis-ndismderegisterinterruptex.md)"><strong>NdisMDeregisterInterruptEx</strong></a></p></td>
<td align="left"><p>After <a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismderegisterinterruptex" data-raw-source="[&lt;strong&gt;NdisMDeregisterInterruptEx&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismderegisterinterruptex)"><strong>NdisMDeregisterInterruptEx</strong></a> returns control, the miniport driver cannot call the <a href="/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsynchronizewithinterruptex" data-raw-source="[&lt;strong&gt;NdisMSynchronizeWithInterruptEx&lt;/strong&gt;](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsynchronizewithinterruptex)"><strong>NdisMSynchronizeWithInterruptEx</strong></a> function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="nullcheckn.md" data-raw-source="[&lt;strong&gt;NullCheck&lt;/strong&gt;](nullcheckn.md)"><strong>NullCheck</strong></a></p></td>
<td align="left"><p>The NullCheck rule verifies that a NULL value inside the driver code is not dereferenced later in the driver. This rule reports a defect if either of these conditions is true:</p>
<ul>
<li>There is an assignment of NULL that is dereferenced later.</li>
<li>There is a global/parameter to a procedure in a driver that may be NULL that is dereferenced later, and there is an explicit check in the driver that suggests that the initial value of the pointer may be NULL.</li>
</ul>
<p>With NullCheck rule violations, the most relevant code statements are highlighted in the trace tree pane. For more information about working with report output, see <a href="/windows-hardware/drivers/devtest/static-driver-verifier-report" data-raw-source="[Static Driver Verifier Report](./static-driver-verifier-report.md)">Static Driver Verifier Report</a> and <a href="/windows-hardware/drivers/devtest/understanding-the-defect-viewer" data-raw-source="[Understanding the Trace Viewer](./understanding-the-defect-viewer.md)">Understanding the Trace Viewer</a>.</p>
<p></p></td>
</tr>
</tbody>
</table>

 

**To select the DDI usage rule set**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **DDIUsage**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **DDIUsage.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:DDIUsage.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md) and [Static Driver Verifier commands (MSBuild)](./-static-driver-verifier-commands--msbuild-.md).

