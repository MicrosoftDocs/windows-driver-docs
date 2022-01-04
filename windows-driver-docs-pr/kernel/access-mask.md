---
title: Specifying Access Rights
description: Specifying Access Rights
ms.date: 10/17/2018
---

# Specifying Access Rights


The ACCESS\_MASK type is a bitmask that specifies a set of access rights in the [access mask](../ifs/access-mask.md) of an [access control entry](../ifs/access-control-entry.md).

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
<td><p>The caller can perform a wait operation on the object. (For example, the object can be passed to <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitformultipleobjects" data-raw-source="[&lt;strong&gt;KeWaitForMultipleObjects&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitformultipleobjects)"><strong>KeWaitForMultipleObjects</strong></a>.)</p></td>
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

 

Each type of object can have its own additional access rights. For a description of the access rights that are applicable to a file, directory, or device, see [**ZwCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile). For a description of the access rights that are applicable to an object manager directory, see [**ZwCreateDirectoryObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatedirectoryobject). For a description of the access rights that are applicable to a registry key, see [**ZwCreateKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatekey). For a description of the access rights that are applicable to a section object, see [**ZwOpenSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopensection). For a description of the access rights that are applicable to a WMI data block, see [**IoWMIOpenBlock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iowmiopenblock).

For more information about access rights, see the following topics in the Microsoft Windows SDK documentation:

-   [Access Rights and Access Masks](/windows/desktop/SecAuthZ/access-rights-and-access-masks)
-   [ACCESS\_MASK](/windows/desktop/SecAuthZ/access-mask)

Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)

## Related topics
[**IoWMIOpenBlock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iowmiopenblock)  
[**ZwCreateDirectoryObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatedirectoryobject)  
[**ZwCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile)  
[**ZwCreateKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatekey)  
[**ZwOpenSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopensection)
