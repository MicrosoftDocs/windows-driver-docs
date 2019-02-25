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
ms.localizationpriority: medium
ms.date: 10/17/2018
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

 

 





