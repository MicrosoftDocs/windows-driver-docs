---
title: Opening a Handle to a Registry-Key Object
description: Opening a Handle to a Registry-Key Object
ms.assetid: 451e36a1-1cc2-469e-9f54-c02fef7b1666
keywords: ["registry WDK kernel , object routines", "driver registry information WDK kernel , object routines", "object routines WDK kernel", "registry-key objects WDK kernel", "opening handle to registry-key object", "handle to registry-key object WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Opening a Handle to a Registry-Key Object





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

 

 

 




