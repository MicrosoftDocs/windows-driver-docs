---
title: Modifying the Default Behavior of the IEEE 1394 Bus Driver
description: Windows 7 includes 1394ohci.sys, a new IEEE 1394 bus driver that is implemented by using the kernel-mode driver framework (KMDF).
ms.assetid: B636943E-EE52-4D0D-A638-89C05AD41F1A
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Modifying the Default Behavior of the IEEE 1394 Bus Driver


Windows 7 includes 1394ohci.sys, a new IEEE 1394 bus driver that is implemented by using the kernel-mode driver framework (KMDF). The 1394ohci.sys bus driver replaces the legacy IEEE bus driver in port/miniport configuration-- 1394bus.sys and ochi1394.sys.

In some situations you might want to override the default behavior of 1394ohci.sys,. You can do this by setting certain registry values that it supports.

## Registry Value Locations


You can set the 1394-related registry values either globally for all 1394 controllers in the system or individually for each 1394 controller. The 1394ohci.sys, bus driver first queries the global 1394 registry values and then queries the individual 1394 controller registry values.

The following registry location contains the global 1394 registry values:

`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\1394ohci \Parameters`

The following registry location contains the individual 1394 controller registry values:

`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class \{6BDD1FC1-810F-11D0-BEC7-08002BE2092F}\<NNNN>`

`<NNNN>` represents the instance identification number for each 1394 controller.

## Registry Values


The following table describes the registry values that the new 1394 bus driver supports. You can specify all registry values either globally or for a particular 1394 controller. Any registry values that are specified for a particular 1394 controller override any corresponding globally specified registry values.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Type</th>
<th>Value</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DisableGenerationCountCompare</td>
<td>DWORD</td>
<td>0 or 1</td>
<td>0</td>
<td>The 1394ohci.sys bus driver compares the generation count value in the <strong>self_id</strong> register of the 1394 controller with the generation count value that is received in the asynchronous receive DMA request context buffer when it processes received asynchronous requests. Setting this value to 0 enables generation count comparison. Setting this value to 1 disables generation count comparison.</td>
</tr>
<tr class="even">
<td>UseQuadletReadsForEnumeration</td>
<td>DWORD</td>
<td>0 or 1</td>
<td>0</td>
<td>Setting this value to 0 enables the default method for retrieving the contents of the configuration ROM. Setting this value to 1 causes the new 1394 bus driver to use asynchronous quadlet read transactions to retrieve the contents of the configuration ROM.</td>
</tr>
<tr class="odd">
<td>EnumerateIP1394</td>
<td>DWORD</td>
<td>0 or 1</td>
<td>0</td>
<td>Setting this value to 0 disables enumeration of IP1394 devices on the 1394 bus. Setting this value to 1 enables enumeration of IP1394 devices on the 1394 bus.</td>
</tr>
<tr class="even">
<td>EnableGapCountOptimization</td>
<td>DWORD</td>
<td>0 or 1</td>
<td>Optimize for 1394a topology only</td>
<td>Setting this value to 0 disables gap count optimization. Setting this value to 1 enables gap count optimization.
<div class="alert">
<strong>Note</strong>  Enabling gap count optimization improves the gap count for all 1394 bus topologies, including 1394b. The gap count value that is used is based on the table method, as specified in the IEEE-1394a specification. End-users must make sure that the gap count that is used is valid for their 1394 bus topology.
</div>
<div>
 
</div></td>
</tr>
<tr class="odd">
<td>EnablePersistentCycleStarts</td>
<td>DWORD</td>
<td>0 or 1</td>
<td>0</td>
<td>Setting this value to 0 disables cycle start packets if no isochronous-capable nodes are found on the 1394 bus. Setting this value to 1 enables cycle start packets regardless of whether isochronous-capable nodes are found on the 1394 bus.
<div class="alert">
<strong>Note</strong>  The 1394ohci.sys bus driver disables and enables cycle start packets only if the local node is the bus manager.
</div>
<div>
 
</div></td>
</tr>
</tbody>
</table>

 

## Related topics
[The IEEE 1394 Driver Stack](https://msdn.microsoft.com/library/windows/hardware/ff538867)  
[IEEE 1394 Bus Driver in Windows 7](https://msdn.microsoft.com/library/windows/hardware/gg266402)  



