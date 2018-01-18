---
title: DDI usage rule set (NDIS)
description: Use these rules to verify that your driver correctly uses NDIS DDIs correctly.
ms.assetid: A109A452-D3A7-4204-B267-1F0F98652597
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
<td align="left"><p>[<strong>Init_DeRegisterInterrupt</strong>](ndis-init-deregisterinterrupt.md)</p></td>
<td align="left"><p>The [<strong>Init_DeRegisterInterrupt</strong>](ndis-init-deregisterinterrupt.md) rule specifies that if [<strong>NdisMRegisterInterruptEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563649) is called at least once during MPInitilize, [<strong>NdisMDeregisterInterruptEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563575) should be called at least once in MPHaltEx.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>Init_NdisAllocateIoWorkItem</strong>](ndis-init-ndisallocateioworkitem.md)</p></td>
<td align="left"><p>The [<strong>Init_NdisAllocateIoWorkItem</strong>](ndis-init-ndisallocateioworkitem.md) rule specifies that if [<strong>NdisAllocateIoWorkItem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561604) is called at least once during [<em>MiniportInitializeEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff559389), the [<strong>NdisFreeIoWorkItem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561855) function should:</p>
<ul>
<li>- be called at least once in MPHaltEx, if [<em>MiniportInitializeEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff559389) succeeds.</li>
<li>- be called in [<em>MiniportInitializeEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff559389), if <em>MiniportInitializeEx</em> fails.</li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>Init_RegisterInterrupt</strong>](ndis-init-registerinterrupt.md)</p></td>
<td align="left"><p>The Init_RegisterInterrupt rule specifies that the registration of interrupts, which usually happens during initialization, must be undone if something goes wrong in the initialization process or during the halting of the miniport driver.</p>
<p>If <strong>NdisMRegisterInterruptEx</strong> is called at least one time during <strong>MiniportInitializeEx</strong>, the <strong>NdisMDeregisterInterruptEx</strong> function must be called at least one time in <strong>MiniportHaltEx</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>Init_RegisterSG</strong>](ndis-init-registersg.md)</p></td>
<td align="left"><p>The Init_RegisterSG rule specifies that the registration of the scatter-gather list (SG), which usually happens during initialization, must be undone if something goes wrong in the initialization process or during the halting of the miniport driver.</p>
<p>If <strong>NdisMRegisterScatterGatherDma</strong> is called at least one time during <strong>MiniportInitializeEx</strong>, the <strong>NdisMDeregisterScatterGatherDma</strong> function should be called at least one time in <strong>MiniportHaltEx</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NdisFDeregisterFilterDriver</strong>](ndis-ndisfderegisterfilterdriver.md)</p></td>
<td align="left"><p>A filter driver must call [<strong>NdisFDeregisterFilterDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561800) from its [<strong>FilterDriverUnload</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549936) routine.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NdisMDeregisterInterruptEx</strong>](ndis-ndismderegisterinterruptex.md)</p></td>
<td align="left"><p>After [<strong>NdisMDeregisterInterruptEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563575) returns control, the miniport driver cannot call the [<strong>NdisMSynchronizeWithInterruptEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563681) function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NullCheck</strong>](nullcheckn.md)</p></td>
<td align="left"><p>The NullCheck rule verifies that a NULL value inside the driver code is not dereferenced later in the driver. This rule reports a defect if either of these conditions is true:</p>
<ul>
<li>There is an assignment of NULL that is dereferenced later.</li>
<li>There is a global/parameter to a procedure in a driver that may be NULL that is dereferenced later, and there is an explicit check in the driver that suggests that the initial value of the pointer may be NULL.</li>
</ul>
<p>With NullCheck rule violations, the most relevant code statements are highlighted in the trace tree pane. For more information about working with report output, see [Static Driver Verifier Report](https://msdn.microsoft.com/library/windows/hardware/ff552834) and [Understanding the Trace Viewer](https://msdn.microsoft.com/library/windows/hardware/ff554020).</p>
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

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20DDI%20usage%20rule%20set%20%28NDIS%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




