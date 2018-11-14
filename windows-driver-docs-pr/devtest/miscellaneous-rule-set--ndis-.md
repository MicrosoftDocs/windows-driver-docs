---
title: Miscellaneous rule set (NDIS)
description: Use these rules to verify that your driver correctly follows a general set of requirements for the proper handling of timers, pause operations, keys, strings and bindings.
ms.assetid: 2F4A68DB-7619-4F36-8FA1-C9350604FDED
ms.date: 05/21/2018
ms.localizationpriority: medium
---

# Miscellaneous rule set (NDIS)


Use these rules to verify that your driver correctly follows a general set of requirements for the proper handling of timers, pause operations, keys, strings and bindings.

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
<td align="left"><p><a href="ndis-canceltimerobject.md" data-raw-source="[&lt;strong&gt;CancelTimerObject&lt;/strong&gt;](ndis-canceltimerobject.md)"><strong>CancelTimerObject</strong></a></p></td>
<td align="left"><p>The <a href="ndis-canceltimerobject.md" data-raw-source="[&lt;strong&gt;CancelTimerObject&lt;/strong&gt;](ndis-canceltimerobject.md)"><strong>CancelTimerObject</strong></a> rule specifies that <a href="https://msdn.microsoft.com/library/windows/hardware/ff564563" data-raw-source="[&lt;strong&gt;NdisSetTimerObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564563)"><strong>NdisSetTimerObject</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff561624" data-raw-source="[&lt;strong&gt;NdisCancelTimerObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561624)"><strong>NdisCancelTimerObject</strong></a> are called in alternate order. The ultimate goal is to make sure all timers are cancelled when <a href="https://msdn.microsoft.com/library/windows/hardware/ff559388" data-raw-source="[&lt;em&gt;MiniportHaltEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559388)"><em>MiniportHaltEx</em></a> ends.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-miniportpause-return.md" data-raw-source="[&lt;strong&gt;MiniportPause_Return&lt;/strong&gt;](ndis-miniportpause-return.md)"><strong>MiniportPause_Return</strong></a></p></td>
<td align="left"><p>The <a href="ndis-miniportpause-return.md" data-raw-source="[&lt;strong&gt;MiniportPause_Return&lt;/strong&gt;](ndis-miniportpause-return.md)"><strong>MiniportPause_Return</strong></a> rule specifies that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559418" data-raw-source="[&lt;em&gt;MiniportPause&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559418)"><em>MiniportPause</em></a> callback function should return only NDIS_STATUS_SUCCESS if the pause operation is complete, or NDIS_STATUS_PENDING if the miniport driver is in the pausing state. Any other returned status is invalid.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-ndisopenconfigurationex.md" data-raw-source="[&lt;strong&gt;NdisOpenConfigurationEx&lt;/strong&gt;](ndis-ndisopenconfigurationex.md)"><strong>NdisOpenConfigurationEx</strong></a></p></td>
<td align="left"><p>This rule checks that <a href="https://msdn.microsoft.com/library/windows/hardware/ff563717" data-raw-source="[&lt;strong&gt;NdisOpenConfigurationEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563717)"><strong>NdisOpenConfigurationEx</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff561642" data-raw-source="[&lt;strong&gt;NdisCloseConfiguration&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561642)"><strong>NdisCloseConfiguration</strong></a> are called in alternate order. The ultimate goal is to make sure that configuration handles are closed when <a href="https://msdn.microsoft.com/library/windows/hardware/ff559388" data-raw-source="[&lt;em&gt;MiniportHaltEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559388)"><em>MiniportHaltEx</em></a> exits</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-ndisquerybindinstancename.md" data-raw-source="[&lt;strong&gt;NdisQueryBindInstanceName&lt;/strong&gt;](ndis-ndisquerybindinstancename.md)"><strong>NdisQueryBindInstanceName</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563748" data-raw-source="[&lt;strong&gt;NdisQueryBindInstanceName&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563748)"><strong>NdisQueryBindInstanceName</strong></a> allocates memory for the string that specifies the friendly name. After the caller finishes using this memory, the caller must call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562577" data-raw-source="[&lt;strong&gt;NdisFreeMemory&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562577)"><strong>NdisFreeMemory</strong></a> function to release the memory.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-ndisreenumerateprotocolbindings.md" data-raw-source="[&lt;strong&gt;NdisReEnumerateProtocolBindings&lt;/strong&gt;](ndis-ndisreenumerateprotocolbindings.md)"><strong>NdisReEnumerateProtocolBindings</strong></a></p></td>
<td align="left"><p>Protocol drivers cannot call <a href="https://msdn.microsoft.com/library/windows/hardware/ff564516" data-raw-source="[&lt;strong&gt;NdisReEnumerateProtocolBindings&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564516)"><strong>NdisReEnumerateProtocolBindings</strong></a> from within the context of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570220" data-raw-source="[&lt;em&gt;ProtocolBindAdapterEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570220)"><em>ProtocolBindAdapterEx</em></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff570278" data-raw-source="[&lt;em&gt;ProtocolUnbindAdapterEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570278)"><em>ProtocolUnbindAdapterEx</em></a> functions. Also, protocol drivers cannot call <strong>NdisReEnumerateProtocolBindings</strong> from within the context of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570263" data-raw-source="[&lt;em&gt;ProtocolNetPnPEvent&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570263)"><em>ProtocolNetPnPEvent</em></a> function if the <em>ProtocolBindingContext</em> parameter of <em>ProtocolNetPnPEvent</em> is not NULL. However, protocol drivers can call <strong>NdisReEnumerateProtocolBindings</strong> from within the context of <em>ProtocolNetPnPEvent</em> if <em>ProtocolBindingContext</em> is NULL. A NULL <em>ProtocolBindingContext</em> value indicates that the event applies to all bindings.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-periodictimer.md" data-raw-source="[&lt;strong&gt;PeriodicTimer&lt;/strong&gt;](ndis-periodictimer.md)"><strong>PeriodicTimer</strong></a></p></td>
<td align="left"><p>The <a href="ndis-periodictimer.md" data-raw-source="[&lt;strong&gt;PeriodicTimer&lt;/strong&gt;](ndis-periodictimer.md)"><strong>PeriodicTimer</strong></a> rule specifies that the caller of <a href="https://msdn.microsoft.com/library/windows/hardware/ff561624" data-raw-source="[&lt;strong&gt;NdisCancelTimerObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561624)"><strong>NdisCancelTimerObject</strong></a> must be running at <strong>IRQL = PASSIVE_LEVEL</strong> if a nonzero value was specified in the <em>MillisecondsPeriod</em> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564563" data-raw-source="[&lt;strong&gt;NdisSetTimerObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564563)"><strong>NdisSetTimerObject</strong></a> function. If the <em>MillisecondsPeriod</em> parameter of the <strong>NdisSetTimerObject</strong> function was zero, callers of <strong>NdisCancelTimerObject</strong> can be running at <strong>IRQL &lt;= DISPATCH_LEVEL</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-writeerrorlog.md" data-raw-source="[&lt;strong&gt;WriteErrorLog&lt;/strong&gt;](ndis-writeerrorlog.md)"><strong>WriteErrorLog</strong></a></p></td>
<td align="left"><p>The WriteErrorLog rule specifies that if the <strong>NdisMAllocateSharedMemory</strong> function is called in the <em>MiniportInitializeEx</em> function, the driver should also call <strong>NdisWriteErrorLogEntry</strong> if the allocation fails.</p></td>
</tr>
</tbody>
</table>

 

**To select the Miscellaneous rule set**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **Miscellaneous**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **Miscellaneous.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:Miscellaneous.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 





