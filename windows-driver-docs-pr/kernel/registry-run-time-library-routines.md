---
title: Registry Run-Time Library Routines
author: windows-driver-content
description: Registry Run-Time Library Routines
ms.assetid: 53e55969-3c8e-44ab-8ba7-6abb0ddbfc24
keywords: ["registry WDK kernel , run-time library routines", "driver registry information WDK kernel , run-time library routines", "run-time library routines WDK kernel", "RtlXxxRegistryYyy routines"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Registry Run-Time Library Routines


## <a href="" id="ddk-registry-run-time-library-routines-kg"></a>


To manipulate registry entries, drivers can call the **Rtl*Xxx*Registry*Xxx*** routines, which provide a simpler interface than the **Zw*Xxx*Key** routines. When doing so, the driver is not required to open and close handles; instead, the driver refers to keys by name.

You pass *RelativeTo* and *Path* parameters to each **Rtl*Xxx*Registry*Xxx*** routine. If *RelativeTo* is RTL\_REGISTRY\_ABSOLUTE, *Path* specifies the full path of the key, beginning with the **\\Registry** root. If *RelativeTo* is RTL\_REGISTRY\_HANDLE, *Path* is actually an open handle. Additional RTL\_REGISTRY\_*XXX* values for *RelativeTo* specify the paths of common roots for the key; in these cases, *Path* specifies the path relative to that root. For example, RTL\_REGISTRY\_USER requires that *Path* be relative to the current user's registry settings. (This value is equivalent to specifying HKEY\_CURRENT\_USER in a user-mode application.) For a description of all the RTL\_REGISTRY\_*XXX* values, see [**RtlCheckRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff561754).

The following table list the operations that drivers can perform by calling the **Rtl*Xxx*Registry*Xxx*** routines.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Operation</th>
<th>Rtl<em>Xxx</em>Registry<em>Xxx</em> routine to call</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Create a registry key</p></td>
<td><p>[<strong>RtlCreateRegistryKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561822)</p></td>
</tr>
<tr class="even">
<td><p>Check whether a registry key exists</p></td>
<td><p>[<strong>RtlCheckRegistryKey</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561754)</p></td>
</tr>
<tr class="odd">
<td><p>Examine one or more registry-key values</p></td>
<td><p>[<strong>RtlQueryRegistryValues</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562046)</p></td>
</tr>
<tr class="even">
<td><p>Write a registry-key value</p></td>
<td><p>[<strong>RtlWriteRegistryValue</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563034)</p></td>
</tr>
<tr class="odd">
<td><p>Delete a registry-key value</p></td>
<td><p>[<strong>RtlDeleteRegistryValue</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561829)</p></td>
</tr>
</tbody>
</table>

 

The following code example illustrates how to set *ValueName* for **\\Registry\\Machine\\System\\***KeyName* to a ULONG value of 0xFF. Compare this example with the corresponding one in the [Registry Key Object Routines](registry-key-object-routines.md) section.

```
NTSTATUS status;
ULONG data = 0xFF;

status = RtlWriteRegistryValue(RTL_REGISTRY_ABSOLUTE,
                               (PWCSTR)L"\\Registry\\Machine\\System\\KeyName",
                               (PWCSTR)L"ValueName",
                               REG_DWORD,
                               &data,
                               sizeof(ULONG));
```

Although you write fewer lines of code when using the **Rtl*Xxx*Registry*Xxx*** routines instead of the **Zw*Xxx*Key** routines, the latter ones are necessary for performing certain operations. For example, no **Rtl*Xxx*Registry*Xxx*** routine exists that corresponds to [**ZwEnumerateKey**](https://msdn.microsoft.com/library/windows/hardware/ff566447).

If you perform multiple operations on the same key, the **Zw*Xxx*Key** routines are more efficient—you can use the same open handle for each operation. In contrast, the **Rtl*Xxx*Registry*Xxx*** routines open and close a new handle for each operation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Registry%20Run-Time%20Library%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


