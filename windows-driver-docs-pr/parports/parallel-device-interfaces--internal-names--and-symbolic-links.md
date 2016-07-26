---
title: Parallel Device Interfaces, Internal Names, and Symbolic Links
author: windows-driver-content
description: Parallel Device Interfaces, Internal Names, and Symbolic Links
MS-HAID:
- 'sspd\_a84208f6-d301-4715-8c80-f39842db46cd.xml'
- 'parports.parallel\_device\_interfaces\_\_internal\_names\_\_and\_symbolic\_links'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 859e20bb-e411-4572-a393-a6faf534cf15
keywords: ["system-supplied parallel drivers WDK , device interfaces", "system-supplied parallel drivers WDK , internal names", "system-supplied parallel drivers WDK , symbolic links", "device interfaces WDK parallel drivers", "symbolic links WDK parallel drivers", "internal names WDK parallel drivers", "names WDK parallel drivers", "unprotected symbolic links WDK", "parallel devices WDK , device interfaces", "device objects WDK parallel drivers", "parallel devices WDK , internal names", "parallel devices WDK , symbolic links"]
---

# Parallel Device Interfaces, Internal Names, and Symbolic Links


## <a href="" id="ddk-parallel-device-interfaces-internal-names-and-symbolic-links-kg"></a>


This section describes the device interfaces, internal names, and symbolic links that are created by the system-supplied parallel drivers for parallel ports and devices attached to parallel ports.

For each parallel port enumerated in the system and for each parallel device enumerated on a parallel port, the parallel drivers create device objects, interfaces, internal names, and unprotected symbolic links as follows.

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
<th>Device type</th>
<th>Device object</th>
<th>Device interface</th>
<th>Internal name</th>
<th>Symbolic link</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Parallel port</p></td>
<td><p>FDO</p></td>
<td><p>GUID_PARALLEL_DEVICE</p></td>
<td><p>&quot;\Device\ParallelPort<em>m&quot;,</em></p>
<p><em>m &gt;=</em> 0</p></td>
<td><p>None</p></td>
</tr>
<tr class="even">
<td><p>Raw parallel device</p></td>
<td><p>PDO</p></td>
<td><p>GUID_PARCLASS_DEVICE</p></td>
<td><p>&quot;\Device\Parallel<em>m</em>&quot;,</p>
<p><em>m &gt;=</em> 0</p></td>
<td><p>&quot;LPT<em>n</em>&quot;,</p>
<p><em>n = m +</em> 1</p></td>
</tr>
<tr class="odd">
<td><p>IEEE 1284.3 device</p></td>
<td><p>PDO</p></td>
<td><p>None</p></td>
<td><p>&quot;\Device\Parallel<em>m.x</em>&quot;,</p>
<p><em>m &gt;=</em> 0<em>,</em></p>
<p>Windows 2000: <em>x =</em> 0 <em>to</em> 3</p>
<p>Windows XP and later: <em>x =</em> 0 <em>or</em> 1</p></td>
<td><p>&quot;LPT<em>n.x</em>&quot;,</p>
<p><em>n = m +</em>1</p></td>
</tr>
<tr class="even">
<td><p>IEEE 1284 end-of-chain device</p></td>
<td><p>PDO</p></td>
<td><p>None</p></td>
<td><p>&quot;\Device\Parallel<em>m.</em>4&quot;</p>
<p><em>m</em> &gt;= 0</p></td>
<td><p>&quot;LPT<em>n.</em>4&quot;</p>
<p><em>n = m +</em>1</p></td>
</tr>
</tbody>
</table>

 

For example, the following device names and symbolic links are assigned to "\\Device\\ParallelPort0", which has two IEEE 1284.3 daisy chain devices and an IEEE 1284 end-of-chain device attached to it.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Device type</th>
<th>Device object</th>
<th>Internal name</th>
<th>Symbolic link</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Parallel Port</p></td>
<td><p>FDO</p></td>
<td><p>&quot;\Device\ParallelPort0&quot;</p></td>
<td><p>None</p></td>
</tr>
<tr class="even">
<td><p>IEEE 1284.3 device</p></td>
<td><p>PDO</p></td>
<td><p>&quot;\Device\Parallel0.0&quot;</p></td>
<td><p>&quot;LPT1.0&quot;</p></td>
</tr>
<tr class="odd">
<td><p>IEEE 1284.3 device</p></td>
<td><p>PDO</p></td>
<td><p>&quot;\Device\Parallel0.1&quot;</p></td>
<td><p>&quot;LPT1.1&quot;</p></td>
</tr>
<tr class="even">
<td><p>IEEE 1284 end-of-chain device</p></td>
<td><p>PDO</p></td>
<td><p>&quot;\Device\Parallel0.4&quot;</p></td>
<td><p>&quot;LPT1.4&quot;</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bparports\parports%5D:%20Parallel%20Device%20Interfaces,%20Internal%20Names,%20and%20Symbolic%20Links%20%20RELEASE:%20%287/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


