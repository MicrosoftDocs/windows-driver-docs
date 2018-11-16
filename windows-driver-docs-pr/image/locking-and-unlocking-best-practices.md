---
title: Locking and Unlocking Best Practices
description: Locking and Unlocking Best Practices
ms.assetid: cfa45c0d-4e92-4455-a8f6-17d4806f9c36
ms.date: 07/18/2018
ms.localizationpriority: medium
---

# Locking and Unlocking Best Practices





Locking for the STI portion of a WIA driver needs special attention. Even though an application can access the published STI interfaces directly, such direct access to the device can be misused. Locking techniques that are implemented improperly can leave a device open to a denial of service (DoS) attack.

### For STI Applications

The following list contains precautions and guidelines you should follow when using STI applications:

-   Do not hold locks for extended periods of time.

-   If you do not need direct access to the device, it might be possible to obtain the same information by using WIA interface methods. This is preferable because the WIA service then controls locking for you.

-   TWAIN drivers that use STI use the [**IStiUSD::LockDevice**](https://msdn.microsoft.com/library/windows/hardware/ff543829) method to control access to the device. When a TWAIN driver uses STI, the TWAIN driver is responsible for controlling lock times.

-   You can create it so that it implements only the **IStiUSD** interface methods. The disadvantage of this approach is that an application can call **IStiUSD::LockDevice** directly, thereby locking the device for exclusive use by the application. The Windows Hardware Quality Lab does not certify drivers that use this technique; such drivers can be installed only as unsigned drivers.

### For WIA Drivers

The following list contains precautions and guidelines you should follow when working with WIA drivers:

-   Monitor the activity of the device during long lock periods. If there is no activity, then the driver should unlock the device, and allow other clients to connect. The driver should not unlock the device, for example, if it is scanning a very large image, or if it is taking an unusually long time to acquire an image. This interrupts the current session. Depending on the device and the bus it operates on, a very large image could be anywhere from 10 megabytes to more than a gigabyte, and a long period of time could be anywhere from 500 milliseconds to more than a minute. You should benchmark your device and the bus it operates on so you know what these specific values are for your device.

-   Applications that use WIA do not access the driver's locking methods, [**IWiaMiniDrv::drvLockWiaDevice**](https://msdn.microsoft.com/library/windows/hardware/ff544995) and [**IWiaMiniDrv::drvUnLockWiaDevice**](https://msdn.microsoft.com/library/windows/hardware/ff545012). Only the WIA service calls these locking methods, the WIA service propagates locking calls to **IStiUSD** using the **IStiUSD::LockDevice** method.

-   If an application exclusively locks a WIA device using the **IStiUSD::LockDevice** method, the WIA service cannot access the device until that application calls the [**IStiUSD::UnLockDevice**](https://msdn.microsoft.com/library/windows/hardware/ff543843) method. If the WIA service cannot lock the device, the device will not be available to any applications or drivers that rely on the WIA service.

-   The [**IWiaMiniDrv::drvLockWiaDevice**](https://msdn.microsoft.com/library/windows/hardware/ff544995) method should always call the [**IStiDevice::LockDevice**](https://msdn.microsoft.com/library/windows/hardware/ff543756) method, and the [**IWiaMiniDrv::drvUnLockWiaDevice**](https://msdn.microsoft.com/library/windows/hardware/ff545012) method should always call the [**IStiDevice::UnLockDevice**](https://msdn.microsoft.com/library/windows/hardware/ff543770) method. This ensures that the WIA service performs proper lock management for the device. The **IStiDevice** interface is passed to the driver in calls to the [**IWiaMiniDrv::drvInitializeWia**](https://msdn.microsoft.com/library/windows/hardware/ff544986) method. This interface should be cached and used to call the **IStiDevice::LockDevice** method. This method calls your driver's **IStiUSD::LockDevice** method.

-   If a BOOL value is used to control locking, protect this value from multiple threads. When two drivers attempt to lock a single device at the same time, only one driver can succeed.

 

 




