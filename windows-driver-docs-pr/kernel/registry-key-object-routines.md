---
title: Registry Key Object Routines
author: windows-driver-content
description: Registry Key Object Routines
MS-HAID:
- 'Other\_716701e4-2217-44e0-978b-4abf3faff31a.xml'
- 'kernel.registry\_key\_object\_routines'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9db6ff0d-8371-41bc-82c4-1bb56f5430f2
keywords: ["registry WDK kernel , object routines", "driver registry information WDK kernel , object routines", "object routines WDK kernel", "registry-key objects WDK kernel"]
---

# Registry Key Object Routines


## <a href="" id="ddk-registry-key-object-routines-kg"></a>


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
<td><p>No simple kernel-mode equivalent, but see [Registry Run-Time Library Routines](registry-run-time-library-routines.md)</p></td>
</tr>
</tbody>
</table>

 

A driver can manipulate a registry-key object by performing the following steps:

1.  Open a handle to the registry-key object. For more information, see [Opening a Handle to a Registry-Key Object](opening-a-handle-to-a-registry-key-object.md).

2.  Perform the intended operations by calling the appropriate **Zw*Xxx*Key** routines. For information about how to do so, see [Using a Handle to a Registry-Key Object](using-a-handle-to-a-registry-key-object.md).

3.  Close the handle by calling [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Registry%20Key%20Object%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


