---
title: Changing the Default GDL Configuration
description: Changing the Default GDL Configuration
ms.assetid: ecc4a6ab-869a-402e-b90e-5ad94e0347c3
keywords:
- GDL WDK , configurations
- configurations WDK GDL , default configurations
- configurations WDK GDL , changing the default configuration
- default GDL configurations WDK
- DefaultOption directive WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Changing the Default GDL Configuration


The **\*DefaultOption** directive itself might depend on a configuration. You can define different default configurations by defining the directive multiple times within a **\*Switch** and **\*Case** construct. However, you must ensure that the dependencies do not conflict with the **\*ConflictPriority** that is established for each parameter.

You should start with the default configuration because it is the safest, even if you are planning to explicitly set some of the parameter's values. The complete configuration might contain parameters that you are not aware of and that would not have been specified if you tried to create your own configuration from scratch. Also, the GDL file might not define some parameters that you were planning to set.

For example, assume that a client obtains the default configuration and wants to update two of the parameters to a new value. If the two parameters are Today and Weather, the client queries the date function and finds that Today is Friday. The client checks the current weather from the Internet and finds that Weather is Sunny).

First, the client should verify, by looking at the default snapshot, that the Today and Weather parameter are defined in the GDL file. The client should then verify that the Friday and Sunny values are defined in the GDL file. It can verify these values by using DOM methods to search the default snapshot. After this validation, the client can locate the node that is holding the default value for each of these parameters in the configuration and update them to the new values.

In other cases, the configuration is obtained from user input or it is retrieved from persistent storage. The client could also use these configurations to obtain a snapshot.

 

 




