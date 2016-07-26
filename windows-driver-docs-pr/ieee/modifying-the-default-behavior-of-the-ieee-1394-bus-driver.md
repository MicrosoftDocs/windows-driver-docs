---
title: Modifying the Default Behavior of the IEEE 1394 Bus Driver
author: windows-driver-content
description: Windows 7 includes 1394ohci.sys, a new IEEE 1394 bus driver that is implemented by using the kernel-mode driver framework (KMDF).
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: B636943E-EE52-4D0D-A638-89C05AD41F1A
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

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BIEEE\buses%5D:%20Modifying%20the%20Default%20Behavior%20of%20the%20IEEE%201394%20Bus%20Driver%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


