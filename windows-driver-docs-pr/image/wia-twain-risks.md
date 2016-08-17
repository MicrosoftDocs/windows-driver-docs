---
title: WIA-TWAIN Risks
description: WIA-TWAIN Risks
MS-HAID:
- 'WIA\_drv\_scan\_51c1a3de-521f-40ba-83c4-214ad213ec75.xml'
- 'image.wia\_twain\_risks'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f202a0f6-ceec-4658-a499-b3024f6ebb71
---

# WIA-TWAIN Risks


## <a href="" id="ddk-wia-twain-risks-si"></a>


If you have a TWAIN driver that uses the STI portion of your WIA driver, you need to be aware of the following:

1.  A TWAIN data source calls [**IStiUSD::LockDevice**](https://msdn.microsoft.com/library/windows/hardware/ff543829) before accessing the driver. This prevents WIA applications from connecting to your WIA driver until [**IStiUSD::UnLockDevice**](https://msdn.microsoft.com/library/windows/hardware/ff543843) is called. To minimize this problem, keep access to the device limited so WIA clients can connect and perform operations. This is important because TWAIN maintains a one-to-one relationship between applications and drivers. WIA permits multiple applications to be connected to a single WIA driver. For this reason, a TWAIN application accessing the TWAIN driver can potentially lock out WIA applications. To prevent this, use proper locking methodology.

2.  Any application or utility that uses the STI interface methods can prevent access to the WIA driver. Some examples are utilities that monitor button or device status, and applications that monitor the system tray.

3.  The WIA driver should ensure that calls to [**IStiUSD::RawReadData**](https://msdn.microsoft.com/library/windows/hardware/ff543834), [**IStiUSD::RawWriteData**](https://msdn.microsoft.com/library/windows/hardware/ff543839), [**IStiUSD::RawReadCommand**](https://msdn.microsoft.com/library/windows/hardware/ff543831), [**IStiUSD::RawWriteCommand**](https://msdn.microsoft.com/library/windows/hardware/ff543836) and [**IStiUSD::Escape**](https://msdn.microsoft.com/library/windows/hardware/ff543815) are properly validated and isolated by using proper locking.

When you write your driver, verify incoming values so only valid data is sent to the device.

For the proper validation sequence when using **IStiUSD::Escape**, see [Using the IStiUSD Escape Method](using-the-istiusd-escape-method.md). For additional information about proper locking, see [Locking and Unlocking Best Practices](locking-and-unlocking-best-practices.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA-TWAIN%20Risks%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




