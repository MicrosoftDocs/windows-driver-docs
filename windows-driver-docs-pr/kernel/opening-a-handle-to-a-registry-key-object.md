---
title: Opening a Handle to a Registry-Key Object
author: windows-driver-content
description: Opening a Handle to a Registry-Key Object
ms.assetid: 451e36a1-1cc2-469e-9f54-c02fef7b1666
keywords: ["registry WDK kernel , object routines", "driver registry information WDK kernel , object routines", "object routines WDK kernel", "registry-key objects WDK kernel", "opening handle to registry-key object", "handle to registry-key object WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Opening a Handle to a Registry-Key Object


## <a href="" id="ddk-opening-a-handle-to-a-registry-key-object-kg"></a>


To open a handle to a registry-key object, carry out the following two-step process:

1.  Create an [**OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff557749) structure, and initialize it by calling [**InitializeObjectAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff547804). You specify the name of the key to manipulate as the *ObjectName* parameter to **InitializeObjectAttributes**.

    If you pass **NULL** as the *RootDirectory* parameter to **InitializeObjectAttributes**, *ObjectName* must be the full path of the registry key, beginning with **\\Registry**. Otherwise, *RootDirectory* must be an open handle to a key, and *ObjectName* is the path that is relative to that key.

2.  Open a handle to the key object by calling [**ZwCreateKey**](https://msdn.microsoft.com/library/windows/hardware/ff566425) or [**ZwOpenKey**](https://msdn.microsoft.com/library/windows/hardware/ff567014), and pass the **OBJECT\_ATTRIBUTES** structure to it. If the key does not already exist, **ZwCreateKey** will create the key, whereas **ZwOpenKey** will return STATUS\_OBJECT\_NAME\_NOT\_FOUND.

You pass a *DesiredAccess* parameter to **ZwCreateKey** or **ZwOpenKey** that contains the access rights you are requesting. You must specify the access rights that permit the operations your driver will perform. The following table lists the operations you can perform and the corresponding access rights to request.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Operation</th>
<th>Required access right</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Get a registry-key value.</p></td>
<td><p>KEY_QUERY_VALUE or KEY_READ</p></td>
</tr>
<tr class="even">
<td><p>Set a registry-key value.</p></td>
<td><p>KEY_SET_VALUE or KEY_WRITE</p></td>
</tr>
<tr class="odd">
<td><p>Loop through all of the subkeys of a key.</p></td>
<td><p>KEY_ENUMERATE_SUB_KEYS or KEY_READ</p></td>
</tr>
<tr class="even">
<td><p>Create a subkey.</p></td>
<td><p>KEY_CREATE_SUB_KEY or KEY_WRITE</p></td>
</tr>
<tr class="odd">
<td><p>Delete a key.</p></td>
<td><p>DELETE</p></td>
</tr>
</tbody>
</table>

 

For more information about the available values for the *DesiredAccess* parameter, see [**ZwCreateKey**](https://msdn.microsoft.com/library/windows/hardware/ff566425).

You can also call [**IoOpenDeviceRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff549443) and [**IoOpenDeviceInterfaceRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff549433) to open handles to those registry keys that are device specific and device-interface specific, respectively. For more information, see [Plug and Play Registry Routines](plug-and-play-registry-routines.md).

**Note**  For calls to **ZwCreateKey**, **ZwOpenKey**, **IoOpenDeviceRegistryKey**, and **IoOpenDeviceInterfaceRegistryKey**, the generic access rights, GENERIC\_READ and GENERIC\_WRITE, are equivalent in meaning to the key-specific access rights, KEY\_READ and KEY\_WRITE, respectively, and can be used as substitutes for these key-specific access rights.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Opening%20a%20Handle%20to%20a%20Registry-Key%20Object%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


