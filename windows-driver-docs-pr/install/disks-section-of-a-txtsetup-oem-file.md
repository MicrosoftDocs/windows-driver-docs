---
title: Disks Section of a TxtSetup.oem File
description: The Disks section identifies the disks in the device installation kit.
ms.assetid: 0a1c0bf1-b4b9-45bc-af48-26f19bc72061
keywords: ["Disks Section of a TxtSetup.oem File Device and Driver Installation"]
topic_type:
- apiref
api_name:
- Disks Section of a TxtSetup.oem File
api_type:
- NA
---

# Disks Section of a TxtSetup.oem File


The **Disks** section identifies the disks in the device installation kit. This section has the following format:

``` syntax
[Disks]
diskN = "description",tagfile,directory
...
```

<a href="" id="diskn"></a>*diskN*  
Specifies a key that can be used in subsequent sections to identify the disk.

<a href="" id="description"></a>*description*  
Specifies a string containing the name of the disk. Windows uses the description to prompt the user to insert the disk.

<a href="" id="tagfile"></a>*tagfile*  
Specifies the name of a verification file on the disk. The filename must be specified as a full path from the root and must not specify a drive. Windows checks for this file to ensure that the user inserted the correct disk.

<a href="" id="directory"></a>*directory*  
Specifies the directory on the disk where the installation files are located. The directory must be specified as a full path from the root and must not specify a drive.

The following example shows a **Disks** section for an installation kit with two disks:

``` syntax
[Disks]
disk1 = "OEM SCSI driver disk 1",\disk1.tag,\
disk2 = "OEM SCSI driver disk 2",\disk2.tag,\
; ...
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Disks%20Section%20of%20a%20TxtSetup.oem%20File%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




