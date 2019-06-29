---
title: UMDF Indicates Outstanding Files at Device Removal Time
description: Describes how to use Wudfext.dll to determine why UMDF indicates that there are outstanding files when you remove a device.
ms.assetid: 9a8b3b69-1192-40c1-895b-4abfc01c1ca7
keywords:
- debugging scenarios WDK UMDF , UMDF indicates outstanding files at device removal time
- UMDF WDK , debugging scenarios, UMDF indicates outstanding files at device removal time
- UMDF WDK , UMDF indicates outstanding files at device removal time
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determining Why UMDF Indicates Outstanding Files at Device Removal Time


This topic describes how you can use the Wudfext.dll debugger extensions in conjunction with a User-Mode Driver Framework (UMDF) version 1 or 2 driver to determine why UMDF indicates that there are outstanding files when you remove a device.

For UMDF version 1, you'll use extension commands implemented in wudfext.dll. Starting in UMDF version 2, you'll use extension commands implemented in wdfkd.dll.

To determine why UMDF indicates outstanding files, use the following steps:

1.  Use [**!wudfext.umdevstack**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-wudfext-umdevstack) (UMDF 1) or [**!wdfkd.wdfumdevstack**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-wdfkd-wdfumdevstack) (UMDF 2) to dump the device stack. The dump includes outstanding UMDF intra-stack files (that is, file objects that a driver in the stack created as opposed to file objects that were created by an application or by a driver in another stack).

2.  For each intra-stack file, run [**!wudfext.umfile**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-wudfext-umfile) (UMDF 1) or [**!wdfkd.wdfumfile**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-wdfkd-wdfumfile) (UMDF 2) to obtain information about the file.

    The output includes the list of IRPs that are pending.

3.  Determine why each IRP is outstanding by using [**!wudfext.umirp**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-wudfext-umirp) (UMDF 1) or [**!wdfkd.wdfumirp**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-wdfkd-wdfumirp) (UMDF 2) to obtain information about the IRP.

    From the output of each [**!wudfext.umirp**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-wudfext-umirp) or [**!wdfkd.wdfumirp**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-wdfkd-wdfumirp):

    -   Determine if the IRP completed.
    -   Determine if a driver-created request was not deleted either explicitly by the driver or implicitly by the object tree.

 

 





