---
title: WIA-TWAIN Risks
description: WIA-TWAIN Risks
ms.assetid: f202a0f6-ceec-4658-a499-b3024f6ebb71
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA-TWAIN Risks





If you have a TWAIN driver that uses the STI portion of your WIA driver, you need to be aware of the following:

1.  A TWAIN data source calls [**IStiUSD::LockDevice**](https://msdn.microsoft.com/library/windows/hardware/ff543829) before accessing the driver. This prevents WIA applications from connecting to your WIA driver until [**IStiUSD::UnLockDevice**](https://msdn.microsoft.com/library/windows/hardware/ff543843) is called. To minimize this problem, keep access to the device limited so WIA clients can connect and perform operations. This is important because TWAIN maintains a one-to-one relationship between applications and drivers. WIA permits multiple applications to be connected to a single WIA driver. For this reason, a TWAIN application accessing the TWAIN driver can potentially lock out WIA applications. To prevent this, use proper locking methodology.

2.  Any application or utility that uses the STI interface methods can prevent access to the WIA driver. Some examples are utilities that monitor button or device status, and applications that monitor the system tray.

3.  The WIA driver should ensure that calls to [**IStiUSD::RawReadData**](https://msdn.microsoft.com/library/windows/hardware/ff543834), [**IStiUSD::RawWriteData**](https://msdn.microsoft.com/library/windows/hardware/ff543839), [**IStiUSD::RawReadCommand**](https://msdn.microsoft.com/library/windows/hardware/ff543831), [**IStiUSD::RawWriteCommand**](https://msdn.microsoft.com/library/windows/hardware/ff543836) and [**IStiUSD::Escape**](https://msdn.microsoft.com/library/windows/hardware/ff543815) are properly validated and isolated by using proper locking.

When you write your driver, verify incoming values so only valid data is sent to the device.

For the proper validation sequence when using **IStiUSD::Escape**, see [Using the IStiUSD Escape Method](using-the-istiusd-escape-method.md). For additional information about proper locking, see [Locking and Unlocking Best Practices](locking-and-unlocking-best-practices.md).

 

 




