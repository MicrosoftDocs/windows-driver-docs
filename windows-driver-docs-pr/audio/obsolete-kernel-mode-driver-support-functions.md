---
title: Obsolete Kernel-Mode Driver-Support Functions
description: Obsolete Kernel-Mode Driver-Support Functions
ms.assetid: 8bdfbd2e-a0d6-424f-9092-297e533efa33
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Obsolete Kernel-Mode Driver-Support Functions


## <span id="ddk_obsolete_kernel_mode_driver_support_functions_ks"></span><span id="DDK_OBSOLETE_KERNEL_MODE_DRIVER_SUPPORT_FUNCTIONS_KS"></span>


The header file portcls.hdefines four macros that contain the names of obsolete kernel-mode driver-support functions. These macros allow old source code that contains references to the obsolete function names to be recompiled to use the new kernel functions without requiring any edits to the source files.

When compiling source code that uses the obsolete names, define the parameter name PC\_OLD\_NAMES. This parameter can be defined by the compiler command-line argument "-DPC\_OLD\_NAMES" if that is more convenient than introducing the statement `#define PC_OLD_NAMES` into the source files themselves.

The following table lists the obsolete kernel-mode driver-support function names in the left column. For each obsolete name, the right column contains the name of the new kernel function that replaces it. In each case, the macro definition amounts to a simple name change. The argument lists for the obsolete function and the new function are identical.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Obsolete Function Name</th>
<th align="left">New Function Name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>WIN95COMPAT_ReadPortUChar</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560797" data-raw-source="[&lt;strong&gt;READ_PORT_UCHAR&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560797)"><strong>READ_PORT_UCHAR</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>WIN95COMPAT_WritePortUChar</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566386" data-raw-source="[&lt;strong&gt;WRITE_PORT_UCHAR&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566386)"><strong>WRITE_PORT_UCHAR</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>WIN95COMPAT_ReadPortUShort</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560806" data-raw-source="[&lt;strong&gt;READ_PORT_USHORT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560806)"><strong>READ_PORT_USHORT</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>WIN95COMPAT_WritePortUShort</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566388" data-raw-source="[&lt;strong&gt;WRITE_PORT_USHORT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566388)"><strong>WRITE_PORT_USHORT</strong></a></p></td>
</tr>
</tbody>
</table>

 

 

 





