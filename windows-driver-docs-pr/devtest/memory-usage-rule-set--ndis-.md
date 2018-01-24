---
title: Memory usage rule set (NDIS)
description: Use these rules to verify that your driver correctly calls NDIS functions to allocate and free memory.
ms.assetid: F28314C6-4B4D-479F-BB96-6850C8F98153
---

# Memory usage rule set (NDIS)


Use these rules to verify that your driver correctly calls NDIS functions to allocate and free memory.

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
<td align="left"><p>[<strong>NdisAllocateGenericObject</strong>](ndis-ndisallocategenericobject.md)</p></td>
<td align="left"><p>The [<strong>NdisAllocateGenericObject</strong>](ndis-ndisallocategenericobject.md) rule specifies that [<strong>NdisAllocateGenericObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561603) and [<strong>NdisFreeGenericObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561850) are called in alternate order. The ultimate goal is to make sure all generic objects are freed when [<em>MiniportHaltEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff559388) ends.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NdisAllocateMdl</strong>](ndis-ndisallocatemdl.md)</p></td>
<td align="left"><p>The [<strong>NdisAllocateMdl</strong>](ndis-ndisallocatemdl.md) rule specifies that [<strong>NdisAllocateMdl</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561605) and [<strong>NdisFreeMdl</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562575) are called in alternate order. The ultimate goal is to make sure all MDLs are freed when [<em>MiniportHaltEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff559388) ends.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NdisAllocateMemoryWithTagPriority</strong>](ndis-ndisallocatememorywithtagpriority.md)</p></td>
<td align="left"><p>The [<strong>NdisAllocateMemoryWithTagPriority</strong>](ndis-ndisallocatememorywithtagpriority.md) rule specifies that a driver must not call <strong>NdisAllocateMemoryWithTagPriority</strong> without providing a <em>Tag</em>.</p>
<p>Every memory allocation should use a unique pool tag to ensure that kernel debuggers and Driver Verifier can identify a distinct allocated block of memory.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NdisAllocateNetBuffer</strong>](ndis-ndisallocatenetbuffer.md)</p></td>
<td align="left"><p>The [<strong>NdisAllocateNetBuffer</strong>](ndis-ndisallocatenetbuffer.md) rule specifies that [<strong>NdisAllocateNetBuffer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561607) and [<strong>NdisFreeNetBuffer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562582) are called in alternate order. The ultimate goal is to make sure all instances of [<strong>NET_BUFFER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568376) are freed when [<em>MiniportHaltEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff559388) ends.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NdisMFreeSharedMemory</strong>](ndis-ndismfreesharedmemory.md)</p></td>
<td align="left"><p>[<strong>NdisMFreeSharedMemory</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563589) cannot be called from a [<em>MiniportShutdownEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff559449) function.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NdisMIndicateStatusEx</strong>](ndis-ndismindicatestatusex.md)</p></td>
<td align="left"><p>The driver must not call [<strong>NdisMIndicateStatusEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563600) after it returns from the [<em>MiniportHaltEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff559388) function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NdisMMapIoSpace</strong>](ndis-ndismmapiospace.md)</p></td>
<td align="left"><p>The [<strong>NdisMMapIoSpace</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563613) function should only be called in the context of [<em>MiniportInitializeEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff559389).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NdisMRegisterIoPortRange</strong>](ndis-ndismregisterioportrange.md)</p></td>
<td align="left"><p>A miniport driver calls [<strong>NdisMRegisterIoPortRange</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563651) from its [<em>MiniportInitializeEx</em>](https://msdn.microsoft.com/library/windows/hardware/ff559389) or MINIPORT_ADD_DEVICE functions. <em>MiniportInitializeEx</em> or MINIPORT_ADD_DEVICE must call [<strong>NdisMSetMiniportAttributes</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563672) before calling <strong>NdisMRegisterIoPortRange</strong>.</p></td>
</tr>
</tbody>
</table>

 

**To select the Memory usage rule set**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **MemoryUsage**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **MemoryUsage.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:MemoryUsage.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Memory%20usage%20rule%20set%20%28NDIS%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




