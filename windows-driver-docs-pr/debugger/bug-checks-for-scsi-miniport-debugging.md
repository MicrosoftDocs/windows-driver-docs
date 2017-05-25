---
title: Bug Checks for SCSI Miniport Debugging
description: Bug Checks for SCSI Miniport Debugging
ms.assetid: 9a517096-f708-452b-83f6-e7d4f0d41ac3
keywords: ["SCSI Miniport debugging, bug checks"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Bug Checks for SCSI Miniport Debugging


There are primarily two bug checks that arise in the course of debugging a SCSI miniport driver: bug check 0x77 (KERNEL\_STACK\_INPAGE\_ERROR) and bug check 0x7A (KERNEL\_DATA\_INPAGE\_ERROR). For full details of their parameters, see [**Bug Check 0x77**](bug-check-0x77--kernel-stack-inpage-error.md) and [**Bug Check 0x7A**](bug-check-0x7a--kernel-data-inpage-error.md).

Each of these bug checks indicates that a paging error has occurred. There are three main causes for these bug checks:

-   Full bus reset due to a timeout on a particular device or no activity on an adapter

-   Selection time-out

-   Controller errors

To determine the precise cause of the failure, begin by using the [**!scsikd.classext**](-scsikd-classext.md) extension, which displays information about recently failed requests, including the SRB status, SCSI status, and sense data of the request.

```
kd> !scsikd.classext 816e96b0
Storage class device 816e96b0 with extension at 816e9768

Classpnp Internal Information at 817b4008

    Failed requests:

           Srb    Scsi
    Opcode Status Status Sense Code  Sector   Time  Stamp
    ------ ------ ------ ---------- -------- ------------
      2a     0a     02    03 0c 00  0000abcd 23:01:07.453  Retried
      28     0a     02    03 04 00  0000abcd 23:01:07.984  Retried

dt classpnp!_CLASS_PRIVATE_FDO_DATA 817b4008 -

...
```

In the previous example, opcode 0x2A indicates a write operation, and 0x28 indicates a read operation. The SCSI status in the example is 02, which indicates a check condition. The sense codes provide more error information.

As always, miniport driver developers are responsible for associating error codes from their hardware to the SRB status codes. Typically, timeouts are associated with SRB 0x0A, the code for a selection timeout. SRB 0x0e is typically associated with a full bus reset, but it can also be associated with controller errors.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Bug%20Checks%20for%20SCSI%20Miniport%20Debugging%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




