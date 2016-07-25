---
title: CM\_PROB\_NORMAL\_CONFLICT
description: CM\_PROB\_NORMAL\_CONFLICT
ms.assetid: 18c5ca02-0a4c-4a0e-8b33-5c685a73d4c8
keywords: ["CM_PROB_NORMAL_CONFLICT"]
---

# CM\_PROB\_NORMAL\_CONFLICT


## <a href="" id="ddk-cm-prob-normal-conflict-dg"></a>


Two devices have been assigned the same I/O ports, the same interrupt, or the same DMA channel (either by the BIOS, the operating system, or a combination of the two).

### Error Code

12

### Display Message (Windows 2000 and later versions of Windows)

"This device cannot find enough free resources that it can use. (Code 12)

"If you want to use this device, you will need to disable one of the other devices on this system."

### Recommended Resolution - Windows Vista and later versions of Windows

[Use Device Manager](using-device-manager.md) to determine the source of the conflict and to resolve the conflict. For more information about how to resolve device conflicts, see the Help information about how to use Device Manager.

This error message can also appear if the BIOS did not allocate sufficient resources to a device. For example, this message will be displayed if the BIOS does not allocate an interrupt to a USB controller because of an invalid multiprocessor specification (MPS) table.

### Recommended Resolution − Windows Server 2003, Windows XP, and Windows 2000

To troubleshoot a device conflict, follow these steps:

1.  [Open Device Manager](using-device-manager.md).

2.  Double-click the icon that represents the device in the Device Manager window.

3.  On the device property sheet that appears, click **Troubleshoot** to start the hardware troubleshooter for the device.

This error message can also appear if the BIOS did not allocate sufficient resources to a device. For example, this message will be displayed if the BIOS does not allocate an interrupt to a USB controller because of an invalid multiprocessor specification (MPS) table.

For more information about how to resolve device conflicts, see the Help information about how to use Device Manager.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20CM_PROB_NORMAL_CONFLICT%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




