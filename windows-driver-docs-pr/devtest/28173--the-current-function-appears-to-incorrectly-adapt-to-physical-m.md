---
title: C28173
description: Warning C28173 The current function appears to incorrectly adapt to physical memory above 4 GB.
ms.assetid: 9332c35e-9d04-4286-9eff-3a639589607e
---

# C28173


warning C28173: The current function appears to incorrectly adapt to physical memory above 4 GB

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>The code does not appear to recover from a call to <strong>IoGetDmaAdapter</strong> that returns a small number of map registers. See the documentation for details.</p></td>
</tr>
</tbody>
</table>

 

On systems that have more than 4 GB of memory, the **IoGetDmaAdapter** function might return fewer map registers than requested; this becomes more likely when the value requested becomes large (approaching 64).This is because of the need to map physical memory above 4 GB into the space below 4 GB.

This warning message appears when code does not adapt to getting fewer registers than it asked for. When a function makes a call to **IoGetDmaAdapter**, the Code Analysis tool simulates that the **IoGetDmaAdapter** function returns a smaller number of registers than requested. The calling function must handle this condition and return successfully.

Note that there are other ways that a driver can fail on systems with more than 4 GB. You should inspect your code for these possible failure modes. For more information about the 4 GB memory issues and the map registers, see [**NdisMAllocateMapRegisters**](https://msdn.microsoft.com/library/windows/hardware/ff552300).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28173%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




