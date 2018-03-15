---
title: Option File Examples
description: Option File Examples
ms.assetid: 632c37a8-a1cc-419a-917f-94e9308c4993
keywords:
- options files WDK Static Driver Verifier
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Option File Examples


**Example 1: Change the Timeout Value**

In the following example Sdv-default.xml file, the timeout is increased to one hour (that is, 3,600 seconds).

```XML
<?xml version="1.0" encoding="utf-8"?>
<SlamConfig xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
 <SDV_SlamConfig_Timeout xmlns="http://www.microsoft.com/SDV">3600</SDV_SlamConfig_Timeout>
  <SDV_SlamConfig_Spaceout xmlns="http://www.microsoft.com/SDV">400</SDV_SlamConfig_Spaceout>
  <SDV_SlamConfig_NumberOfThreads xmlns="http://www.microsoft.com/SDV">0</SDV_SlamConfig_NumberOfThreads></SlamConfig>
```

**Example 2: Change the Spaceout Value**

In the following example Sdv-default.xml file, the virtual memory that is available to SDV is increased to 1200 MB (1.2 GB).

```XML
<?xml version="1.0" encoding="utf-8"?>
<SlamConfig xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <SDV_SlamConfig_Timeout xmlns="http://www.microsoft.com/SDV">2000</SDV_SlamConfig_Timeout>
  <SDV_SlamConfig_Spaceout xmlns="http://www.microsoft.com/SDV">1200</SDV_SlamConfig_Spaceout>
  <SDV_SlamConfig_NumberOfThreads xmlns="http://www.microsoft.com/SDV">0</SDV_SlamConfig_NumberOfThreads>
</SlamConfig>
```

**Example 3: Change the NumberOfThreads Value**

In the following example Sdv-default.xml file, the number of threads that are available to SDV is increased to 2.

```XML
<?xml version="1.0" encoding="utf-8" ?> 
- <SlamConfig xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <SDV_SlamConfig_Timeout xmlns="http://www.microsoft.com/SDV">2000</SDV_SlamConfig_Timeout> 
  <SDV_SlamConfig_Spaceout xmlns="http://www.microsoft.com/SDV">400</SDV_SlamConfig_Spaceout> 
  <SDV_SlamConfig_NumberOfThreads xmlns="http://www.microsoft.com/SDV">2</SDV_SlamConfig_NumberOfThreads> 
  </SlamConfig>
```

 

 





