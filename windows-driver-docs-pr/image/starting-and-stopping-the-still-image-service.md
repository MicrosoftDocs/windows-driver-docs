---
title: Starting and Stopping the Still Image Service
author: windows-driver-content
description: Starting and Stopping the Still Image Service
ms.assetid: 52770566-1d03-4ae8-9925-240fffcc5f57
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Starting and Stopping the Still Image Service





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

 

 




