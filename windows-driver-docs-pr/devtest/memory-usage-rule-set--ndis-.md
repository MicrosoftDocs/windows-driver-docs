---
title: Memory usage rule set (NDIS)
description: Use these rules to verify that your driver correctly calls NDIS functions to allocate and free memory.
ms.assetid: F28314C6-4B4D-479F-BB96-6850C8F98153
ms.date: 05/21/2018
ms.localizationpriority: medium
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
<td align="left"><p><a href="ndis-ndisallocategenericobject.md" data-raw-source="[&lt;strong&gt;NdisAllocateGenericObject&lt;/strong&gt;](ndis-ndisallocategenericobject.md)"><strong>NdisAllocateGenericObject</strong></a></p></td>
<td align="left"><p>The <a href="ndis-ndisallocategenericobject.md" data-raw-source="[&lt;strong&gt;NdisAllocateGenericObject&lt;/strong&gt;](ndis-ndisallocategenericobject.md)"><strong>NdisAllocateGenericObject</strong></a> rule specifies that <a href="https://msdn.microsoft.com/library/windows/hardware/ff561603" data-raw-source="[&lt;strong&gt;NdisAllocateGenericObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561603)"><strong>NdisAllocateGenericObject</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff561850" data-raw-source="[&lt;strong&gt;NdisFreeGenericObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561850)"><strong>NdisFreeGenericObject</strong></a> are called in alternate order. The ultimate goal is to make sure all generic objects are freed when <a href="https://msdn.microsoft.com/library/windows/hardware/ff559388" data-raw-source="[&lt;em&gt;MiniportHaltEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559388)"><em>MiniportHaltEx</em></a> ends.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-ndisallocatemdl.md" data-raw-source="[&lt;strong&gt;NdisAllocateMdl&lt;/strong&gt;](ndis-ndisallocatemdl.md)"><strong>NdisAllocateMdl</strong></a></p></td>
<td align="left"><p>The <a href="ndis-ndisallocatemdl.md" data-raw-source="[&lt;strong&gt;NdisAllocateMdl&lt;/strong&gt;](ndis-ndisallocatemdl.md)"><strong>NdisAllocateMdl</strong></a> rule specifies that <a href="https://msdn.microsoft.com/library/windows/hardware/ff561605" data-raw-source="[&lt;strong&gt;NdisAllocateMdl&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561605)"><strong>NdisAllocateMdl</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff562575" data-raw-source="[&lt;strong&gt;NdisFreeMdl&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562575)"><strong>NdisFreeMdl</strong></a> are called in alternate order. The ultimate goal is to make sure all MDLs are freed when <a href="https://msdn.microsoft.com/library/windows/hardware/ff559388" data-raw-source="[&lt;em&gt;MiniportHaltEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559388)"><em>MiniportHaltEx</em></a> ends.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-ndisallocatememorywithtagpriority.md" data-raw-source="[&lt;strong&gt;NdisAllocateMemoryWithTagPriority&lt;/strong&gt;](ndis-ndisallocatememorywithtagpriority.md)"><strong>NdisAllocateMemoryWithTagPriority</strong></a></p></td>
<td align="left"><p>The <a href="ndis-ndisallocatememorywithtagpriority.md" data-raw-source="[&lt;strong&gt;NdisAllocateMemoryWithTagPriority&lt;/strong&gt;](ndis-ndisallocatememorywithtagpriority.md)"><strong>NdisAllocateMemoryWithTagPriority</strong></a> rule specifies that a driver must not call <strong>NdisAllocateMemoryWithTagPriority</strong> without providing a <em>Tag</em>.</p>
<p>Every memory allocation should use a unique pool tag to ensure that kernel debuggers and Driver Verifier can identify a distinct allocated block of memory.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-ndisallocatenetbuffer.md" data-raw-source="[&lt;strong&gt;NdisAllocateNetBuffer&lt;/strong&gt;](ndis-ndisallocatenetbuffer.md)"><strong>NdisAllocateNetBuffer</strong></a></p></td>
<td align="left"><p>The <a href="ndis-ndisallocatenetbuffer.md" data-raw-source="[&lt;strong&gt;NdisAllocateNetBuffer&lt;/strong&gt;](ndis-ndisallocatenetbuffer.md)"><strong>NdisAllocateNetBuffer</strong></a> rule specifies that <a href="https://msdn.microsoft.com/library/windows/hardware/ff561607" data-raw-source="[&lt;strong&gt;NdisAllocateNetBuffer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561607)"><strong>NdisAllocateNetBuffer</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff562582" data-raw-source="[&lt;strong&gt;NdisFreeNetBuffer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562582)"><strong>NdisFreeNetBuffer</strong></a> are called in alternate order. The ultimate goal is to make sure all instances of <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376" data-raw-source="[&lt;strong&gt;NET_BUFFER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568376)"><strong>NET_BUFFER</strong></a> are freed when <a href="https://msdn.microsoft.com/library/windows/hardware/ff559388" data-raw-source="[&lt;em&gt;MiniportHaltEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559388)"><em>MiniportHaltEx</em></a> ends.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-ndismfreesharedmemory.md" data-raw-source="[&lt;strong&gt;NdisMFreeSharedMemory&lt;/strong&gt;](ndis-ndismfreesharedmemory.md)"><strong>NdisMFreeSharedMemory</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563589" data-raw-source="[&lt;strong&gt;NdisMFreeSharedMemory&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563589)"><strong>NdisMFreeSharedMemory</strong></a> cannot be called from a <a href="https://msdn.microsoft.com/library/windows/hardware/ff559449" data-raw-source="[&lt;em&gt;MiniportShutdownEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559449)"><em>MiniportShutdownEx</em></a> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-ndismindicatestatusex.md" data-raw-source="[&lt;strong&gt;NdisMIndicateStatusEx&lt;/strong&gt;](ndis-ndismindicatestatusex.md)"><strong>NdisMIndicateStatusEx</strong></a></p></td>
<td align="left"><p>The driver must not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff563600" data-raw-source="[&lt;strong&gt;NdisMIndicateStatusEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563600)"><strong>NdisMIndicateStatusEx</strong></a> after it returns from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559388" data-raw-source="[&lt;em&gt;MiniportHaltEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559388)"><em>MiniportHaltEx</em></a> function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="ndis-ndismmapiospace.md" data-raw-source="[&lt;strong&gt;NdisMMapIoSpace&lt;/strong&gt;](ndis-ndismmapiospace.md)"><strong>NdisMMapIoSpace</strong></a></p></td>
<td align="left"><p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff563613" data-raw-source="[&lt;strong&gt;NdisMMapIoSpace&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563613)"><strong>NdisMMapIoSpace</strong></a> function should only be called in the context of <a href="https://msdn.microsoft.com/library/windows/hardware/ff559389" data-raw-source="[&lt;em&gt;MiniportInitializeEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559389)"><em>MiniportInitializeEx</em></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="ndis-ndismregisterioportrange.md" data-raw-source="[&lt;strong&gt;NdisMRegisterIoPortRange&lt;/strong&gt;](ndis-ndismregisterioportrange.md)"><strong>NdisMRegisterIoPortRange</strong></a></p></td>
<td align="left"><p>A miniport driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff563651" data-raw-source="[&lt;strong&gt;NdisMRegisterIoPortRange&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563651)"><strong>NdisMRegisterIoPortRange</strong></a> from its <a href="https://msdn.microsoft.com/library/windows/hardware/ff559389" data-raw-source="[&lt;em&gt;MiniportInitializeEx&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559389)"><em>MiniportInitializeEx</em></a> or MINIPORT_ADD_DEVICE functions. <em>MiniportInitializeEx</em> or MINIPORT_ADD_DEVICE must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff563672" data-raw-source="[&lt;strong&gt;NdisMSetMiniportAttributes&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563672)"><strong>NdisMSetMiniportAttributes</strong></a> before calling <strong>NdisMRegisterIoPortRange</strong>.</p></td>
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

 

 





