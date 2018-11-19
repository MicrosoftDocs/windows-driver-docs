---
title: Registry Key Object Routines
description: Registry Key Object Routines
ms.assetid: 9db6ff0d-8371-41bc-82c4-1bb56f5430f2
keywords: ["registry WDK kernel , object routines", "driver registry information WDK kernel , object routines", "object routines WDK kernel", "registry-key objects WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Registry Key Object Routines





The Windows executive represents registry keys as executive objects that are managed by the object manager. (For more information about the object manager, see [Object Management](managing-kernel-objects.md).) In particular, every key has an object name, and you can open a handle to a key.

User-mode applications access keys relative to global handles, such as HKEY\_LOCAL\_MACHINE or HKEY\_CURRENT\_USER. However, these handles are not available to kernel-mode code. Instead, you refer to a key by its object name. The root for all registry keys is the **\\Registry** object. The global handles correspond to descendants of the **\\Registry** object, as shown in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>User-mode handle</th>
<th>Corresponding object name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>HKEY_LOCAL_MACHINE</p></td>
<td><p><strong>\Registry\Machine</strong></p></td>
</tr>
<tr class="even">
<td><p>HKEY_USERS</p></td>
<td><p><strong>\Registry\User</strong></p></td>
</tr>
<tr class="odd">
<td><p>HKEY_CLASSES_ROOT</p></td>
<td><p>No kernel-mode equivalent</p></td>
</tr>
<tr class="even">
<td><p>HKEY_CURRENT_USER</p></td>
<td><p>No simple kernel-mode equivalent, but see <a href="registry-run-time-library-routines.md" data-raw-source="[Registry Run-Time Library Routines](registry-run-time-library-routines.md)">Registry Run-Time Library Routines</a></p></td>
</tr>
</tbody>
</table>

 

A driver can manipulate a registry-key object by performing the following steps:

1.  Open a handle to the registry-key object. For more information, see [Opening a Handle to a Registry-Key Object](opening-a-handle-to-a-registry-key-object.md).

2.  Perform the intended operations by calling the appropriate **Zw*Xxx*Key** routines. For information about how to do so, see [Using a Handle to a Registry-Key Object](using-a-handle-to-a-registry-key-object.md).

3.  Close the handle by calling [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417).

 

 




