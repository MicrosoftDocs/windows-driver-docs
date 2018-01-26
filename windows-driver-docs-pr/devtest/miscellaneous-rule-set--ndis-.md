---
title: Miscellaneous rule set (NDIS)
description: Use these rules to verify that your driver correctly follows a general set of requirements for the proper handling of timers, pause operations, keys, strings and bindings.
ms.assetid: 2F4A68DB-7619-4F36-8FA1-C9350604FDED
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Miscellaneous%20rule%20set%20%28NDIS%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




