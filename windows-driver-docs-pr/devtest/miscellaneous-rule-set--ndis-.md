---
title: Miscellaneous rule set (NDIS)
description: Use these rules to verify that your driver correctly follows a general set of requirements for the proper handling of timers, pause operations, keys, strings and bindings.
ms.assetid: 2F4A68DB-7619-4F36-8FA1-C9350604FDED
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>[<strong>CancelTimerObject</strong>](ndis-canceltimerobject.md)</p></td>
<td align="left"><p>The [<strong>CancelTimerObject</strong>](ndis-canceltimerobject.md) rule specifies that [<strong>NdisSetTimerObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564563) and [<strong>NdisCancelTimerObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561624) are called in alternate order. The ultimate goal is to make sure all timers are cancelled when [<em>MiniportHaltEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff559388) ends.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>MiniportPause_Return</strong>](ndis-miniportpause-return.md)</p></td>
<td align="left"><p>The [<strong>MiniportPause_Return</strong>](ndis-miniportpause-return.md) rule specifies that the [<em>MiniportPause</em>](https://msdn.microsoft.com/library/windows/hardware/ff559418) callback function should return only NDIS_STATUS_SUCCESS if the pause operation is complete, or NDIS_STATUS_PENDING if the miniport driver is in the pausing state. Any other returned status is invalid.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NdisOpenConfigurationEx</strong>](ndis-ndisopenconfigurationex.md)</p></td>
<td align="left"><p>This rule checks that [<strong>NdisOpenConfigurationEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563717) and [<strong>NdisCloseConfiguration</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561642) are called in alternate order. The ultimate goal is to make sure that configuration handles are closed when [<em>MiniportHaltEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff559388) exits</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NdisQueryBindInstanceName</strong>](ndis-ndisquerybindinstancename.md)</p></td>
<td align="left"><p>[<strong>NdisQueryBindInstanceName</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563748) allocates memory for the string that specifies the friendly name. After the caller finishes using this memory, the caller must call the [<strong>NdisFreeMemory</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562577) function to release the memory.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NdisReEnumerateProtocolBindings</strong>](ndis-ndisreenumerateprotocolbindings.md)</p></td>
<td align="left"><p>Protocol drivers cannot call [<strong>NdisReEnumerateProtocolBindings</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564516) from within the context of the [<em>ProtocolBindAdapterEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff570220) or [<em>ProtocolUnbindAdapterEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff570278) functions. Also, protocol drivers cannot call <strong>NdisReEnumerateProtocolBindings</strong> from within the context of the [<em>ProtocolNetPnPEvent</em>](https://msdn.microsoft.com/library/windows/hardware/ff570263) function if the <em>ProtocolBindingContext</em> parameter of <em>ProtocolNetPnPEvent</em> is not NULL. However, protocol drivers can call <strong>NdisReEnumerateProtocolBindings</strong> from within the context of <em>ProtocolNetPnPEvent</em> if <em>ProtocolBindingContext</em> is NULL. A NULL <em>ProtocolBindingContext</em> value indicates that the event applies to all bindings.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>PeriodicTimer</strong>](ndis-periodictimer.md)</p></td>
<td align="left"><p>The [<strong>PeriodicTimer</strong>](ndis-periodictimer.md) rule specifies that the caller of [<strong>NdisCancelTimerObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561624) must be running at <strong>IRQL = PASSIVE_LEVEL</strong> if a nonzero value was specified in the <em>MillisecondsPeriod</em> parameter of the [<strong>NdisSetTimerObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564563) function. If the <em>MillisecondsPeriod</em> parameter of the <strong>NdisSetTimerObject</strong> function was zero, callers of <strong>NdisCancelTimerObject</strong> can be running at <strong>IRQL &lt;= DISPATCH_LEVEL</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>WriteErrorLog</strong>](ndis-writeerrorlog.md)</p></td>
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

 

 





