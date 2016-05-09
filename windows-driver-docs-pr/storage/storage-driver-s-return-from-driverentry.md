---
title: Storage Driver's Return from DriverEntry
description: Storage Driver's Return from DriverEntry
ms.assetid: a5772e9c-ec7b-4570-aaae-d2879f7e0bc7
keywords: ["return values WDK SCSI", "ScsiPortInitialize"]
---

# Storage Driver's Return from DriverEntry


## <span id="ddk_storage_driver_s_return_from_driverentry_kg"></span><span id="DDK_STORAGE_DRIVER_S_RETURN_FROM_DRIVERENTRY_KG"></span>


When [**ScsiPortInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff564645) returns control, the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff552654) routine propagates the return value of **ScsiPortInitialize** when **DriverEntry** itself returns control.

If a miniport driver calls **ScsiPortInitialize** more than once, its **DriverEntry** routine *must propagate thelowest value* returned by **ScsiPortInitialize**. A miniport driver writer cannot make any assumptions about the values returned by **ScsiPortInitialize**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storage%20Driver's%20Return%20from%20DriverEntry%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




