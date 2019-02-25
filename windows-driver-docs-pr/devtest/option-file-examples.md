---
title: Option File Examples
description: Option File Examples
ms.assetid: 632c37a8-a1cc-419a-917f-94e9308c4993
keywords:
- options files WDK Static Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Option File Examples


**Example 1: Change the Timeout Value**

In the following example Sdv-default.xml file, the timeout is increased to two hours (that is, 7,200 seconds).

```XML
<?xml version="1.0" encoding="utf-8"?>
<SlamConfig xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
 <SDV_SlamConfig_Timeout xmlns="http://www.microsoft.com/SDV">7200</SDV_SlamConfig_Timeout>
  <SDV_SlamConfig_Spaceout xmlns="http://www.microsoft.com/SDV">2500</SDV_SlamConfig_Spaceout>
  <SDV_SlamConfig_NumberOfThreads xmlns="http://www.microsoft.com/SDV">0</SDV_SlamConfig_NumberOfThreads></SlamConfig>
```

**Example 2: Change the Spaceout Value**

In the following example Sdv-default.xml file, the virtual memory that is available to SDV is increased to 3500 MB (3.5 GB).

```XML
<?xml version="1.0" encoding="utf-8"?>
<SlamConfig xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <SDV_SlamConfig_Timeout xmlns="http://www.microsoft.com/SDV">3000</SDV_SlamConfig_Timeout>
  <SDV_SlamConfig_Spaceout xmlns="http://www.microsoft.com/SDV">3500</SDV_SlamConfig_Spaceout>
  <SDV_SlamConfig_NumberOfThreads xmlns="http://www.microsoft.com/SDV">0</SDV_SlamConfig_NumberOfThreads>
</SlamConfig>
```

**Example 3: Change the NumberOfThreads Value**

In the following example Sdv-default.xml file, the number of threads that are available to SDV is limited to 2.

```XML
<?xml version="1.0" encoding="utf-8" ?> 
- <SlamConfig xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <SDV_SlamConfig_Timeout xmlns="http://www.microsoft.com/SDV">3000</SDV_SlamConfig_Timeout> 
  <SDV_SlamConfig_Spaceout xmlns="http://www.microsoft.com/SDV">2500</SDV_SlamConfig_Spaceout> 
  <SDV_SlamConfig_NumberOfThreads xmlns="http://www.microsoft.com/SDV">2</SDV_SlamConfig_NumberOfThreads> 
  </SlamConfig>
```

 

 





