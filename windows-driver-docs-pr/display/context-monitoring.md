---
title: Context monitoring
description: A monitored fence object is an advanced form of fence synchronization which allows either a CPU core or a graphics processing unit (GPU) engine to signal or wait on a particular fence object, allowing for very flexible synchronization between GPU engines, or across CPU cores and GPU engines.
ms.assetid: B593FC24-3F8B-4C8A-BBF9-8EF88B748536
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Context monitoring


A monitored fence object is an advanced form of fence synchronization which allows either a CPU core or a graphics processing unit (GPU) engine to signal or wait on a particular fence object, allowing for very flexible synchronization between GPU engines, or across CPU cores and GPU engines.

## <span id="_Monitored_fence_creation"></span><span id="_monitored_fence_creation"></span><span id="_MONITORED_FENCE_CREATION"></span> Monitored fence creation


A monitored fence object is created by calling [*CreateSynchronizationObjectCb*](https://msdn.microsoft.com/library/windows/hardware/ff568897) callback with the new synchronization object type **D3DDDI\_MONITORED\_FENCE**.

A monitored fence object is created along with the following attributes:

-   Initial value
-   Flags (specifying its waiting and signaling behavior)

Upon creation, the graphics kernel returns a fence object composed of the following items:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Item</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="hSyncObject"></span><span id="hsyncobject"></span><span id="HSYNCOBJECT"></span>hSyncObject</p></td>
<td align="left"><p>Handle to the synchronization object. Used to refer to it in a call to the graphics kernel.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="FenceValueCPUVirtualAddress"></span><span id="fencevaluecpuvirtualaddress"></span><span id="FENCEVALUECPUVIRTUALADDRESS"></span>FenceValueCPUVirtualAddress</p></td>
<td align="left"><p>Read-only mapping of the fence value (64bits) for the CPU. This address is mapped WB (cacheable) from the point of view of the CPU on platforms supporting I/O coherency, UC (uncached) on other platforms. Allows the CPU to keep track of the fence progress by simply reading this memory location. The CPU is not allowed to write to this memory location. To signal the fence, the CPU is required to call the <a href="https://msdn.microsoft.com/library/windows/hardware/dn906360" data-raw-source="[&lt;em&gt;SignalSynchronizationObjectFromCpuCb&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/dn906360)"><em>SignalSynchronizationObjectFromCpuCb</em></a>.</p>
<p>Adapters which support <em>IoMmu</em> should use this address for GPU access. The address is mapped as read-write in this case.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="FenceValueGPUVirtualAddress"></span><span id="fencevaluegpuvirtualaddress"></span><span id="FENCEVALUEGPUVIRTUALADDRESS"></span>FenceValueGPUVirtualAddress</p></td>
<td align="left"><p>Read/write mapping of the fence value (64bits) for the GPU. This address is mapped as requiring I/O coherency on platforms supporting it. To signal the fence, the GPU is allowed to write directly to this GPU virtual address.</p>
<p>This address should not be used by <em>IoMmu</em>GPUs.</p></td>
</tr>
</tbody>
</table>

 

The fence value is a 64-bit value with their respective virtual addresses aligned on a 64-bit boundary. GPUs should declare whether they are capable of atomically updating 64-bit values as visible by the CPU via a new [**DXGK\_VIDSCHCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff562863)::**No64BitAtomics** flag. If a GPU is capable of only updating 32-bit values atomically, the OS will handle the fence wraparound case automatically. However it will place a restriction that outstanding wait and signal fence values cannot be more than **UINT\_MAX**/2 away from the last signaled fence value.
## <span id="GPU_signal"></span><span id="gpu_signal"></span><span id="GPU_SIGNAL"></span>GPU signal


In case a GPU engine is not capable of writing to a monitored fence using its virtual address, the user mode driver will use a new [*SignalSynchronizationObjectFromGpuCb*](https://msdn.microsoft.com/library/windows/hardware/dn906362) callback that will queue a software signal packet to the GPU context.

To signal the fence from the GPU, the user mode driver inserts a fence write command in a context command stream directly without going through kernel model. The mechanism by which the kernel monitors fence progress varies depending on whether a particular GPU engine support the basic or advanced implementation of the monitored fence.

When a command buffer completes execution on the GPU, the graphics kernel will go through the list of fence objects with pending waits that could be signaled for this process, read their current fence value, and determine if there are any waiters that need to be un-waited.

## <span id="_GPU_wait"></span><span id="_gpu_wait"></span><span id="_GPU_WAIT"></span> GPU wait


To wait on a monitored fence on a GPU engine, the user mode driver will first need to flush its pending command buffer then call [*WaitForSynchronizationObjectFromGpuCb*](https://msdn.microsoft.com/library/windows/hardware/dn906367) specifying the fence object (**hSyncObject**) as well as the fence value being waited on. The graphics kernel will queue the dependency to its internal database, then return immediately to the user mode driver so that it may continue to queue work behind the wait operation. Command buffers submitted after the wait operation will be not scheduled for execution until the wait operation has been satisfied.

## <span id="CPU_signal"></span><span id="cpu_signal"></span><span id="CPU_SIGNAL"></span>CPU signal


A new [*SignalSynchronizationObjectFromCpuCb*](https://msdn.microsoft.com/library/windows/hardware/dn906360) has been added to allow the CPU to signal a monitored fence object. When a monitored fence object is signaled by the CPU, the graphics kernel will update the fence memory location with the signaled value so that it becomes immediately visible to any user mode reader as well as immediately un-wait any satisfied waiters.

## <span id="CPU_wait"></span><span id="cpu_wait"></span><span id="CPU_WAIT"></span>CPU wait


A new [*WaitForSynchronizationObjectFromCpuCb*](https://msdn.microsoft.com/library/windows/hardware/dn906366) has been added to allow the CPU to wait on a monitored fence object. Two forms of wait operations are available. In the first form, the *WaitForSynchronizationObjectFromCpuCb* callback blocks until the wait has been satisfied. In the second form, *WaitForSynchronizationObjectFromCpuCb* takes a handle to a CPU event that will be signaled once the waiting condition has been satisfied.

 

 





