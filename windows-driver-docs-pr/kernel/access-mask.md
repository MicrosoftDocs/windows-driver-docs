---
title: Specifying Access Rights
description: Provides information about specifying access rights.
ms.date: 02/20/2025
---

# Specifying access rights

The ACCESS_MASK type is a bitmask that specifies a set of access rights in the [access mask](../ifs/access-mask.md) of an [access control entry](../ifs/access-control-entry.md).

``` syntax
typedef ULONG  ACCESS_MASK;
```

The following standard specific access rights apply to all types of executive objects.

| Flag | Description |
|--|--|
| DELETE | The caller can delete the object. |
| READ_CONTROL | The caller can read the access control list (ACL) and ownership information for the file. |
| SYNCHRONIZE | The caller can perform a wait operation on the object. For example, the object can be passed to [**KeWaitForMultipleObjects**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitformultipleobjects). |
| WRITE_DAC | The caller can change the discretionary access control list (DACL) information for the object. |
| WRITE_OWNER | The caller can change the ownership information for the file. |

Normally only DELETE and SYNCHRONIZE are of interest to driver writers.

You can also specify the following generic access rights. These also apply to all types of executive objects. The meaning of each generic access right is specific to that type of object.

| Flag | Description |
|--|--|
| GENERIC_READ | The caller can perform normal read operations on the object. |
| GENERIC_WRITE | The caller can perform normal write operations on the object. |
| GENERIC_EXECUTE | The caller can execute the object. This generally only makes sense for certain kinds of objects, such as file objects and section objects. |
| GENERIC_ALL | The caller can perform all normal operations on the object. |

The following combinations of standard specific access rights are also defined. These are not normally used directly, but are used as templates to define other bitmasks. (For example, when you specify GENERIC_READ for a file object, the system maps this to the FILE_GENERIC_READ bitmask of specific access rights. FILE_GENERIC_READ is defined in terms of STANDARD_RIGHTS_READ.)

| Bitmask | Description |
|--|--|
| STANDARD_RIGHTS_READ | Standard specific rights that correspond to GENERIC_READ. |
| STANDARD_RIGHTS_WRITE | Standard specific rights that correspond to GENERIC_WRITE. |
| STANDARD_RIGHTS_EXECUTE | Standard specific rights that correspond to GENERIC_EXECUTE. |
| STANDARD_RIGHTS_REQUIRED | Standard specific rights that correspond to GENERIC_ALL. This includes DELETE, but not SYNCHRONIZE. |
| STANDARD_RIGHTS_ALL | All standard access rights. |

Each type of object can have its own additional access rights. For a description of the access rights that are applicable to a file, directory, or device, see [**ZwCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile).

For a description of the access rights that are applicable to an object manager directory, see [**ZwCreateDirectoryObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatedirectoryobject).

For a description of the access rights that are applicable to a registry key, see [**ZwCreateKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatekey). 

For a description of the access rights that are applicable to a section object, see [**ZwOpenSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopensection). 

For a description of the access rights that are applicable to a WMI data block, see [**IoWMIOpenBlock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iowmiopenblock).

For more information about access rights, see [Access Rights and Access Masks](/windows/desktop/SecAuthZ/access-rights-and-access-masks) and [ACCESS_MASK](/windows/desktop/SecAuthZ/access-mask) in the Windows SDK documentation.

## Related topics

[**IoWMIOpenBlock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iowmiopenblock)  

[**ZwCreateDirectoryObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatedirectoryobject)  

[**ZwCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile)  

[**ZwCreateKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatekey)  

[**ZwOpenSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopensection)
