---
title: Authentication and Identification
author: windows-driver-content
description: Authentication and Identification
ms.assetid: fe118cf3-05ce-43b1-b878-4bb99b97dc2e
keywords:
- security WDK file systems , minimizing threats
- authentication WDK file systems
- identification WDK file systems
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Authentication and Identification


## <span id="ddk_authentication_and_identification_if"></span><span id="DDK_AUTHENTICATION_AND_IDENTIFICATION_IF"></span>


Most drivers are not involved in authentication or identification issues, leaving this task to individual services. One case where a driver might become involved in authentication or identification processing is in access management. In this case, the authentication step is usually handled through calls to the Security Reference Monitor. Authentication and identification information is normally tracked by the operating system by the security token, an internal data structure that encapsulates the security credentials for a given thread or process.

 

 


--------------------


