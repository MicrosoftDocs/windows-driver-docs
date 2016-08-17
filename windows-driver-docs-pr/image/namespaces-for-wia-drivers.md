---
title: Namespaces for WIA Drivers
description: Namespaces for WIA Drivers
MS-HAID:
- 'WIA\_best\_practice\_034aa5e9-1222-405f-894d-9d900aa9bb1a.xml'
- 'image.namespaces\_for\_wia\_drivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 67260a25-6233-4738-a08f-26223cc8e563
---

# Namespaces for WIA Drivers


## <a href="" id="ddk-namespaces-for-wia-drivers-si"></a>


All services run in session zero. However, applications might be running in a different session. Each session has its own *namespace*. Therefore, a named object created in one session will not generally be visible to a component in another session.

The solution to this problem is to ensure that both components use the same namespace. The simplest way to do this is to use the *global namespace*. For example, if a bundled component were to access a device outside of WIA, it might use a mutex object named **MyDeviceLock** to synchronize access with its WIA driver. In order to put the mutex name in the global namespace, it should be called **Global\\MyDeviceLock**. The mutex named **Global\\MyDeviceLock** is visible to both the driver and the application, no matter which sessions they are running in, because they both specify that the name belongs to the global namespace.

See "Kernel Object Name Spaces" in the Microsoft Windows SDK documentation or MSDN for more information.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Namespaces%20for%20WIA%20Drivers%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




