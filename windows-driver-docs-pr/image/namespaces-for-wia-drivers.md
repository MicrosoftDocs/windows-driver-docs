---
title: Namespaces for WIA Drivers
description: Namespaces for WIA Drivers
ms.assetid: 67260a25-6233-4738-a08f-26223cc8e563
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Namespaces for WIA Drivers





All services run in session zero. However, applications might be running in a different session. Each session has its own *namespace*. Therefore, a named object created in one session will not generally be visible to a component in another session.

The solution to this problem is to ensure that both components use the same namespace. The simplest way to do this is to use the *global namespace*. For example, if a bundled component were to access a device outside of WIA, it might use a mutex object named **MyDeviceLock** to synchronize access with its WIA driver. In order to put the mutex name in the global namespace, it should be called **Global\\MyDeviceLock**. The mutex named **Global\\MyDeviceLock** is visible to both the driver and the application, no matter which sessions they are running in, because they both specify that the name belongs to the global namespace.

See "Kernel Object Name Spaces" in the Microsoft Windows SDK documentation for more information.

 

 




