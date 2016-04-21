---
title: Determining Why UMDF Indicates Outstanding Files at Device Removal Time
author: windows-driver-content
description: This topic describes how you can use the Wudfext.dll debugger extensions in conjunction with a User-Mode Driver Framework (UMDF) version 1 or 2 driver to determine why UMDF indicates that there are outstanding files when you remove a device.
ms.assetid: 9a8b3b69-1192-40c1-895b-4abfc01c1ca7
keywords: ["debugging scenarios WDK UMDF , UMDF indicates outstanding files at device removal time", "UMDF WDK , debugging scenarios, UMDF indicates outstanding files at device removal time", "UMDF WDK , UMDF indicates outstanding files at device removal time"]
---

# Determining Why UMDF Indicates Outstanding Files at Device Removal Time


This topic describes how you can use the Wudfext.dll debugger extensions in conjunction with a User-Mode Driver Framework (UMDF) version 1 or 2 driver to determine why UMDF indicates that there are outstanding files when you remove a device.

For UMDF version 1, you'll use extension commands implemented in wudfext.dll. Starting in UMDF version 2, you'll use extension commands implemented in wdfkd.dll.

To determine why UMDF indicates outstanding files, use the following steps:

1.  Use [**!wudfext.umdevstack**](https://msdn.microsoft.com/library/windows/hardware/ff566189) (UMDF 1) or [**!wdfkd.wdfumdevstack**](https://msdn.microsoft.com/library/windows/hardware/dn265379) (UMDF 2) to dump the device stack. The dump includes outstanding UMDF intra-stack files (that is, file objects that a driver in the stack created as opposed to file objects that were created by an application or by a driver in another stack).

2.  For each intra-stack file, run [**!wudfext.umfile**](https://msdn.microsoft.com/library/windows/hardware/ff566193) (UMDF 1) or [**!wdfkd.wdfumfile**](https://msdn.microsoft.com/library/windows/hardware/dn265382) (UMDF 2) to obtain information about the file.

    The output includes the list of IRPs that are pending.

3.  Determine why each IRP is outstanding by using [**!wudfext.umirp**](https://msdn.microsoft.com/library/windows/hardware/ff566195) (UMDF 1) or [**!wdfkd.wdfumirp**](https://msdn.microsoft.com/library/windows/hardware/dn265383) (UMDF 2) to obtain information about the IRP.

    From the output of each [**!wudfext.umirp**](https://msdn.microsoft.com/library/windows/hardware/ff566195) or [**!wdfkd.wdfumirp**](https://msdn.microsoft.com/library/windows/hardware/dn265383):

    -   Determine if the IRP completed.
    -   Determine if a driver-created request was not deleted either explicitly by the driver or implicitly by the object tree.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Determining%20Why%20UMDF%20Indicates%20Outstanding%20Files%20at%20Device%20Removal%20Time%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




