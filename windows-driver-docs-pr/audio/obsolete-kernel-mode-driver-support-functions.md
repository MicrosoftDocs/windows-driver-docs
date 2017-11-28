---
title: Obsolete Kernel-Mode Driver-Support Functions
description: Obsolete Kernel-Mode Driver-Support Functions
ms.assetid: 8bdfbd2e-a0d6-424f-9092-297e533efa33
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
<td align="left"><p>[<strong>READ_PORT_UCHAR</strong>](https://msdn.microsoft.com/library/windows/hardware/ff560797)</p></td>
</tr>
<tr class="even">
<td align="left"><p>WIN95COMPAT_WritePortUChar</p></td>
<td align="left"><p>[<strong>WRITE_PORT_UCHAR</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566386)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>WIN95COMPAT_ReadPortUShort</p></td>
<td align="left"><p>[<strong>READ_PORT_USHORT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff560806)</p></td>
</tr>
<tr class="even">
<td align="left"><p>WIN95COMPAT_WritePortUShort</p></td>
<td align="left"><p>[<strong>WRITE_PORT_USHORT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566388)</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Obsolete%20Kernel-Mode%20Driver-Support%20Functions%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




