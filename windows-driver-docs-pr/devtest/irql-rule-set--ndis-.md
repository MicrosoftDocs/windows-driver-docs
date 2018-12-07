---
title: IRQL rule set (NDIS)
description: Use these rules to verify that your driver makes DDI calls at the required IRQL.A driver that does not follow the IRQL rules can cause serious problems during operation that can lead to deadlock conditions or computer crashes.
ms.assetid: EEFEF8E3-8AB8-46AD-A3BD-DA676F8FA786
ms.date: 05/21/2018
ms.localizationpriority: medium
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
<td align="left"><p><a href="ndis-flags-irql.md" data-raw-source="[&lt;strong&gt;Flags_Irql&lt;/strong&gt;](ndis-flags-irql.md)"><strong>Flags_Irql</strong></a></p></td>
<td align="left"><p>The <a href="ndis-flags-irql.md" data-raw-source="[&lt;strong&gt;Flags_Irql&lt;/strong&gt;](ndis-flags-irql.md)"><strong>Flags_Irql</strong></a> rule specifies that <strong>KeGetCurrentIrql</strong> must not be called within callback functions that have a dispatch level flag parameter that indicates the current IRQL.</p>
<p>The correct use of the dispatch level flag can help you avoid unnecessary attempts to set the IRQL. For more information about how to use this flag, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546448" data-raw-source="[Dispatch IRQL Tracking](https://msdn.microsoft.com/library/windows/hardware/ff546448)">Dispatch IRQL Tracking</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-irql-callmanager-function.md" data-raw-source="[&lt;strong&gt;Irql_CallManager_Function&lt;/strong&gt;](ndis-irql-callmanager-function.md)"><strong>Irql_CallManager_Function</strong></a></p></td>
<td align="left"><p>The <a href="ndis-irql-callmanager-function.md" data-raw-source="[&lt;strong&gt;Irql_CallManager_Function&lt;/strong&gt;](ndis-irql-callmanager-function.md)"><strong>Irql_CallManager_Function</strong></a> rule specifies that the NDIS functions for the NDIS CallManager must be called at correct IRQL levels.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-irql-connection-function.md" data-raw-source="[&lt;strong&gt;Irql_Connection_Function&lt;/strong&gt;](ndis-irql-connection-function.md)"><strong>Irql_Connection_Function</strong></a></p></td>
<td align="left"><p>The <a href="ndis-irql-connection-function.md" data-raw-source="[&lt;strong&gt;Irql_Connection_Function&lt;/strong&gt;](ndis-irql-connection-function.md)"><strong>Irql_Connection_Function</strong></a> rule specifies that the NDIS connection functions for protocol drivers must be called at correct IRQL levels.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-irql-filter-driver-function.md" data-raw-source="[&lt;strong&gt;Irql_Filter_Driver_Function&lt;/strong&gt;](ndis-irql-filter-driver-function.md)"><strong>Irql_Filter_Driver_Function</strong></a></p></td>
<td align="left"><p>The Irql_Filter_Driver_Function rule specifies that the NDIS functions for filter drivers must be called at correct IRQL levels.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-irql-gather-dma-function.md" data-raw-source="[&lt;strong&gt;Irql_Gather_DMA_Function&lt;/strong&gt;](ndis-irql-gather-dma-function.md)"><strong>Irql_Gather_DMA_Function</strong></a></p></td>
<td align="left"><p>The Irql_Gather_DMA_Function rule specifies that the NDIS scatter/gather DMA functions must be called at correct IRQL levels.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-irql-im-function.md" data-raw-source="[&lt;strong&gt;Irql_IM_Function&lt;/strong&gt;](ndis-irql-im-function.md)"><strong>Irql_IM_Function</strong></a></p></td>
<td align="left"><p>The Irql_IM_Function rule specifies that the NDIS functions for Intermediate (IM) drivers must be called at correct IRQL levels.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-irql-interfaces-function.md" data-raw-source="[&lt;strong&gt;Irql_Interfaces_Function&lt;/strong&gt;](ndis-irql-interfaces-function.md)"><strong>Irql_Interfaces_Function</strong></a></p></td>
<td align="left"><p>The Irql_Interfaces_Function rule specifies that the NDIS network interface functions must be called at correct IRQL levels.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-irql-interrupt-function.md" data-raw-source="[&lt;strong&gt;Irql_Interrupt_Function&lt;/strong&gt;](ndis-irql-interrupt-function.md)"><strong>Irql_Interrupt_Function</strong></a></p></td>
<td align="left"><p>The Irql_Interrupt_Function rule specifies that the NDIS functions for interrupts must be called at correct IRQL levels.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-irql-irqlsetting-function.md" data-raw-source="[&lt;strong&gt;Irql_IrqlSetting_Function&lt;/strong&gt;](ndis-irql-irqlsetting-function.md)"><strong>Irql_IrqlSetting_Function</strong></a></p></td>
<td align="left"><p>The Irql_IrqlSetting_Function rule specifies that the NDIS interrupt macros must be called at correct IRQL levels.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-irql-mcm-function.md" data-raw-source="[&lt;strong&gt;Irql_MCM_Function&lt;/strong&gt;](ndis-irql-mcm-function.md)"><strong>Irql_MCM_Function</strong></a></p></td>
<td align="left"><p>The <a href="ndis-irql-mcm-function.md" data-raw-source="[&lt;strong&gt;Irql_MCM_Function&lt;/strong&gt;](ndis-irql-mcm-function.md)"><strong>Irql_MCM_Function</strong></a> rule specifies that the NDIS MCM functions for drivers must be called at correct IRQL levels.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-irql-mco-function.md" data-raw-source="[&lt;strong&gt;Irql_MCO_Function&lt;/strong&gt;](ndis-irql-mco-function.md)"><strong>Irql_MCO_Function</strong></a></p></td>
<td align="left"><p>The <a href="ndis-irql-mco-function.md" data-raw-source="[&lt;strong&gt;Irql_MCO_Function&lt;/strong&gt;](ndis-irql-mco-function.md)"><strong>Irql_MCO_Function</strong></a> rule specifies that the NDIS MCO DDIs for miniport drivers must be called at correct IRQL levels.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-irql-miniport-driver-function.md" data-raw-source="[&lt;strong&gt;Irql_Miniport_Driver_Function&lt;/strong&gt;](ndis-irql-miniport-driver-function.md)"><strong>Irql_Miniport_Driver_Function</strong></a></p></td>
<td align="left"><p>The Irql_Miniport_Driver_Function rule specifies that the NDIS functions for miniport drivers must be called at correct IRQL levels.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-irql-miscellaneous-function.md" data-raw-source="[&lt;strong&gt;Irql_Miscellaneous_Function&lt;/strong&gt;](ndis-irql-miscellaneous-function.md)"><strong>Irql_Miscellaneous_Function</strong></a></p></td>
<td align="left"><p>The Irql_Miscellaneous_Function rule specifies that the NDIS functions must be called at correct IRQL levels.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-irql-netbuffer-function.md" data-raw-source="[&lt;strong&gt;Irql_NetBuffer_Function&lt;/strong&gt;](ndis-irql-netbuffer-function.md)"><strong>Irql_NetBuffer_Function</strong></a></p></td>
<td align="left"><p>The Irql_NetBuffer_Function rule specifies that the NET_BUFFER-related functions must be called at correct IRQL levels.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-irql-oid-function.md" data-raw-source="[&lt;strong&gt;Irql_OID_Function&lt;/strong&gt;](ndis-irql-oid-function.md)"><strong>Irql_OID_Function</strong></a></p></td>
<td align="left"><p>The <a href="ndis-irql-oid-function.md" data-raw-source="[&lt;strong&gt;Irql_OID_Function&lt;/strong&gt;](ndis-irql-oid-function.md)"><strong>Irql_OID_Function</strong></a> rule specifies that the NDIS OID request DDIs must be called at correct IRQL levels.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-irql-protocol-driver-function.md" data-raw-source="[&lt;strong&gt;Irql_Protocol_Driver_Function&lt;/strong&gt;](ndis-irql-protocol-driver-function.md)"><strong>Irql_Protocol_Driver_Function</strong></a></p></td>
<td align="left"><p>The Irql_Protocol_Driver_Function rule specifies that the NDIS functions for CoNDIS clients must be called at correct IRQL levels.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-irql-sendrcv-function.md" data-raw-source="[&lt;strong&gt;Irql_SendRcv_Function&lt;/strong&gt;](ndis-irql-sendrcv-function.md)"><strong>Irql_SendRcv_Function</strong></a></p></td>
<td align="left"><p>The <a href="ndis-irql-sendrcv-function.md" data-raw-source="[&lt;strong&gt;Irql_SendRcv_Function&lt;/strong&gt;](ndis-irql-sendrcv-function.md)"><strong>Irql_SendRcv_Function</strong></a> rule specifies that the send and receive functions for NDIS drivers must be called at correct IRQL levels.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-irql-statusindication-function.md" data-raw-source="[&lt;strong&gt;Irql_StatusIndication_Function&lt;/strong&gt;](ndis-irql-statusindication-function.md)"><strong>Irql_StatusIndication_Function</strong></a></p></td>
<td align="left"><p>The Irql_StatusIndication_Function rule specifies that the NDIS status indication functions for miniport and filter drivers must be called at correct IRQL levels.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-irql-synch-function.md" data-raw-source="[&lt;strong&gt;Irql_Synch_Function&lt;/strong&gt;](ndis-irql-synch-function.md)"><strong>Irql_Synch_Function</strong></a></p></td>
<td align="left"><p>The <a href="ndis-irql-synch-function.md" data-raw-source="[&lt;strong&gt;Irql_Synch_Function&lt;/strong&gt;](ndis-irql-synch-function.md)"><strong>Irql_Synch_Function</strong></a> rule specifies that the NDIS interrupt and synchronization DDIs must be called at correct IRQL levels.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-irql-timer-function.md" data-raw-source="[&lt;strong&gt;Irql_Timer_Function&lt;/strong&gt;](ndis-irql-timer-function.md)"><strong>Irql_Timer_Function</strong></a></p></td>
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

 

 





