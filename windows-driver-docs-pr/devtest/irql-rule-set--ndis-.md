---
title: IRQL rule set (NDIS)
description: Use these rules to verify that your driver makes DDI calls at the required IRQL.A driver that does not follow the IRQL rules can cause serious problems during operation that can lead to deadlock conditions or computer crashes.
ms.assetid: EEFEF8E3-8AB8-46AD-A3BD-DA676F8FA786
---

# IRQL rule set (NDIS)


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
<td align="left"><p>[<strong>Flags_Irql</strong>](ndis-flags-irql.md)</p></td>
<td align="left"><p>The [<strong>Flags_Irql</strong>](ndis-flags-irql.md) rule specifies that <strong>KeGetCurrentIrql</strong> must not be called within callback functions that have a dispatch level flag parameter that indicates the current IRQL.</p>
<p>The correct use of the dispatch level flag can help you avoid unnecessary attempts to set the IRQL. For more information about how to use this flag, see [Dispatch IRQL Tracking](https://msdn.microsoft.com/library/windows/hardware/ff546448).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>Irql_CallManager_Function</strong>](ndis-irql-callmanager-function.md)</p></td>
<td align="left"><p>The [<strong>Irql_CallManager_Function</strong>](ndis-irql-callmanager-function.md) rule specifies that the NDIS functions for the NDIS CallManager must be called at correct IRQL levels.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>Irql_Connection_Function</strong>](ndis-irql-connection-function.md)</p></td>
<td align="left"><p>The [<strong>Irql_Connection_Function</strong>](ndis-irql-connection-function.md) rule specifies that the NDIS connection functions for protocol drivers must be called at correct IRQL levels.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>Irql_Filter_Driver_Function</strong>](ndis-irql-filter-driver-function.md)</p></td>
<td align="left"><p>The Irql_Filter_Driver_Function rule specifies that the NDIS functions for filter drivers must be called at correct IRQL levels.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>Irql_Gather_DMA_Function</strong>](ndis-irql-gather-dma-function.md)</p></td>
<td align="left"><p>The Irql_Gather_DMA_Function rule specifies that the NDIS scatter/gather DMA functions must be called at correct IRQL levels.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>Irql_IM_Function</strong>](ndis-irql-im-function.md)</p></td>
<td align="left"><p>The Irql_IM_Function rule specifies that the NDIS functions for Intermediate (IM) drivers must be called at correct IRQL levels.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>Irql_Interfaces_Function</strong>](ndis-irql-interfaces-function.md)</p></td>
<td align="left"><p>The Irql_Interfaces_Function rule specifies that the NDIS network interface functions must be called at correct IRQL levels.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>Irql_Interrupt_Function</strong>](ndis-irql-interrupt-function.md)</p></td>
<td align="left"><p>The Irql_Interrupt_Function rule specifies that the NDIS functions for interrupts must be called at correct IRQL levels.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>Irql_IrqlSetting_Function</strong>](ndis-irql-irqlsetting-function.md)</p></td>
<td align="left"><p>The Irql_IrqlSetting_Function rule specifies that the NDIS interrupt macros must be called at correct IRQL levels.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>Irql_MCM_Function</strong>](ndis-irql-mcm-function.md)</p></td>
<td align="left"><p>The [<strong>Irql_MCM_Function</strong>](ndis-irql-mcm-function.md) rule specifies that the NDIS MCM functions for drivers must be called at correct IRQL levels.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>Irql_MCO_Function</strong>](ndis-irql-mco-function.md)</p></td>
<td align="left"><p>The [<strong>Irql_MCO_Function</strong>](ndis-irql-mco-function.md) rule specifies that the NDIS MCO DDIs for miniport drivers must be called at correct IRQL levels.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>Irql_Miniport_Driver_Function</strong>](ndis-irql-miniport-driver-function.md)</p></td>
<td align="left"><p>The Irql_Miniport_Driver_Function rule specifies that the NDIS functions for miniport drivers must be called at correct IRQL levels.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>Irql_Miscellaneous_Function</strong>](ndis-irql-miscellaneous-function.md)</p></td>
<td align="left"><p>The Irql_Miscellaneous_Function rule specifies that the NDIS functions must be called at correct IRQL levels.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>Irql_NetBuffer_Function</strong>](ndis-irql-netbuffer-function.md)</p></td>
<td align="left"><p>The Irql_NetBuffer_Function rule specifies that the NET_BUFFER-related functions must be called at correct IRQL levels.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>Irql_OID_Function</strong>](ndis-irql-oid-function.md)</p></td>
<td align="left"><p>The [<strong>Irql_OID_Function</strong>](ndis-irql-oid-function.md) rule specifies that the NDIS OID request DDIs must be called at correct IRQL levels.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>Irql_Protocol_Driver_Function</strong>](ndis-irql-protocol-driver-function.md)</p></td>
<td align="left"><p>The Irql_Protocol_Driver_Function rule specifies that the NDIS functions for CoNDIS clients must be called at correct IRQL levels.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>Irql_SendRcv_Function</strong>](ndis-irql-sendrcv-function.md)</p></td>
<td align="left"><p>The [<strong>Irql_SendRcv_Function</strong>](ndis-irql-sendrcv-function.md) rule specifies that the send and receive functions for NDIS drivers must be called at correct IRQL levels.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>Irql_StatusIndication_Function</strong>](ndis-irql-statusindication-function.md)</p></td>
<td align="left"><p>The Irql_StatusIndication_Function rule specifies that the NDIS status indication functions for miniport and filter drivers must be called at correct IRQL levels.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>Irql_Synch_Function</strong>](ndis-irql-synch-function.md)</p></td>
<td align="left"><p>The [<strong>Irql_Synch_Function</strong>](ndis-irql-synch-function.md) rule specifies that the NDIS interrupt and synchronization DDIs must be called at correct IRQL levels.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>Irql_Timer_Function</strong>](ndis-irql-timer-function.md)</p></td>
<td align="left"><p>The Irql_Timer_Function rule specifies that the NDIS timer service functions must be called at correct IRQL levels.</p></td>
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

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20IRQL%20rule%20set%20%28NDIS%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




