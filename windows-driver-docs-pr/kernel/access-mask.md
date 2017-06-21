---
title: Specifying Access Rights
author: windows-driver-content
description: Specifying Access Rights
ms.assetid: 8ef4b4bb-5f4e-4095-b4ab-1182c0f75619
---

# Specifying Access Rights


The ACCESS\_MASK type is a bitmask that specifies a set of access rights in the [access mask](https://msdn.microsoft.com/library/windows/hardware/ff538834) of an [access control entry](https://msdn.microsoft.com/library/windows/hardware/ff538813).

``` syntax
typedef ULONG  ACCESS_MASK;
```

The following standard specific access rights apply to all types of executive objects.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Flag</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>DELETE</p></td>
<td><p>The caller can delete the object.</p></td>
</tr>
<tr class="even">
<td><p>READ_CONTROL</p></td>
<td><p>The caller can read the access control list (ACL) and ownership information for the file.</p></td>
</tr>
<tr class="odd">
<td><p>SYNCHRONIZE</p></td>
<td><p>The caller can perform a wait operation on the object. (For example, the object can be passed to [<strong>KeWaitForMultipleObjects</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553324).)</p></td>
</tr>
<tr class="even">
<td><p>WRITE_DAC</p></td>
<td><p>The caller can change the discretionary access control list (DACL) information for the object.</p></td>
</tr>
<tr class="odd">
<td><p>WRITE_OWNER</p></td>
<td><p>The caller can change the ownership information for the file.</p></td>
</tr>
</tbody>
</table>

 

Note that normally only DELETE and SYNCHRONIZE are of interest to driver writers.

You can also specify the following generic access rights. These also apply to all types of executive objects. The meaning of each generic access right is specific to that type of object.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Flag</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>GENERIC_READ</p></td>
<td><p>The caller can perform normal read operations on the object.</p></td>
</tr>
<tr class="even">
<td><p>GENERIC_WRITE</p></td>
<td><p>The caller can perform normal write operations on the object.</p></td>
</tr>
<tr class="odd">
<td><p>GENERIC_EXECUTE</p></td>
<td><p>The caller can execute the object. (Note this generally only makes sense for certain kinds of objects, such as file objects and section objects.)</p></td>
</tr>
<tr class="even">
<td><p>GENERIC_ALL</p></td>
<td><p>The caller can perform all normal operations on the object.</p></td>
</tr>
</tbody>
</table>

 

The following combinations of standard specific access rights are also defined. These are not normally used directly, but are used as templates to define other bitmasks. (For example, when you specify GENERIC\_READ for a file object, the system maps this to the FILE\_GENERIC\_READ bitmask of specific access rights. FILE\_GENERIC\_READ is defined in terms of STANDARD\_RIGHTS\_READ.)

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Bitmask</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>STANDARD_RIGHTS_READ</p></td>
<td><p>Standard specific rights that correspond to GENERIC_READ</p></td>
</tr>
<tr class="even">
<td><p>STANDARD_RIGHTS_WRITE</p></td>
<td><p>Standard specific rights that correspond to GENERIC_WRITE</p></td>
</tr>
<tr class="odd">
<td><p>STANDARD_RIGHTS_EXECUTE</p></td>
<td><p>Standard specific rights that correspond to GENERIC_EXECUTE</p></td>
</tr>
<tr class="even">
<td><p>STANDARD_RIGHTS_REQUIRED</p></td>
<td><p>Standard specific rights that correspond to GENERIC_ALL. This includes DELETE, but not SYNCHRONIZE.</p></td>
</tr>
<tr class="odd">
<td><p>STANDARD_RIGHTS_ALL</p></td>
<td><p>All standard access rights.</p></td>
</tr>
</tbody>
</table>

 

Each type of object can have its own additional access rights. For a description of the access rights that are applicable to a file, directory, or device, see [**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424). For a description of the access rights that are applicable to an object manager directory, see [**ZwCreateDirectoryObject**](https://msdn.microsoft.com/library/windows/hardware/ff566421). For a description of the access rights that are applicable to a registry key, see [**ZwCreateKey**](https://msdn.microsoft.com/library/windows/hardware/ff566425). For a description of the access rights that are applicable to a section object, see [**ZwOpenSection**](https://msdn.microsoft.com/library/windows/hardware/ff567029). For a description of the access rights that are applicable to a WMI data block, see [**IoWMIOpenBlock**](https://msdn.microsoft.com/library/windows/hardware/ff550453).

For more information about access rights, see the following topics in the Microsoft Windows SDK documentation:

-   [Access Rights and Access Masks](https://msdn.microsoft.com/library/windows/desktop/aa374902)
-   [ACCESS\_MASK](https://msdn.microsoft.com/library/windows/desktop/aa374892)

Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)

## Related topics
[**IoWMIOpenBlock**](https://msdn.microsoft.com/library/windows/hardware/ff550453)  
[**ZwCreateDirectoryObject**](https://msdn.microsoft.com/library/windows/hardware/ff566421)  
[**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424)  
[**ZwCreateKey**](https://msdn.microsoft.com/library/windows/hardware/ff566425)  
[**ZwOpenSection**](https://msdn.microsoft.com/library/windows/hardware/ff567029)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Specifying%20Access%20Rights%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


