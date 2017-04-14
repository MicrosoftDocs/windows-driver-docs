---
title: Starting and Stopping the Still Image Service
author: windows-driver-content
description: Starting and Stopping the Still Image Service
ms.assetid: 52770566-1d03-4ae8-9925-240fffcc5f57
---

# Starting and Stopping the Still Image Service


## <a href="" id="ddk-starting-and-stopping-the-still-image-service-si"></a>


Users do not ordinarily need to start or stop the still image service, but developers must start or stop this service when they install or uninstall drivers. You can start and stop the still image service in either of two different ways:

Issue commands in a command window.

To start the still image service, issue this command:

```
net start stisvc
```

To stop the still image service, issue this command:

```
net stop stisvc
```

Use the Microsoft Management Console (MMC).

Under **Services**, select **Still Image Services**. To start the service, right-click, and then click **Start** from the menu that appears.

To stop the service, right-click, and then click **Stop** from the menu that appears.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Starting%20and%20Stopping%20the%20Still%20Image%20Service%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


