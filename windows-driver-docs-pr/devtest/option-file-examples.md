---
title: Option File Examples
description: Option File Examples
ms.assetid: 632c37a8-a1cc-419a-917f-94e9308c4993
keywords: ["options files WDK Static Driver Verifier"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Option%20File%20Examples%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




