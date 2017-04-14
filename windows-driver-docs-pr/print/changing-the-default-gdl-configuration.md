---
title: Changing the Default GDL Configuration
author: windows-driver-content
description: Changing the Default GDL Configuration
ms.assetid: ecc4a6ab-869a-402e-b90e-5ad94e0347c3
keywords: ["GDL WDK , configurations", "configurations WDK GDL , default configurations", "configurations WDK GDL , changing the default configuration", "default GDL configurations WDK", "DefaultOption directive WDK GDL"]
---

# Changing the Default GDL Configuration


The **\*DefaultOption** directive itself might depend on a configuration. You can define different default configurations by defining the directive multiple times within a **\*Switch** and **\*Case** construct. However, you must ensure that the dependencies do not conflict with the **\*ConflictPriority** that is established for each parameter.

You should start with the default configuration because it is the safest, even if you are planning to explicitly set some of the parameter's values. The complete configuration might contain parameters that you are not aware of and that would not have been specified if you tried to create your own configuration from scratch. Also, the GDL file might not define some parameters that you were planning to set.

For example, assume that a client obtains the default configuration and wants to update two of the parameters to a new value. If the two parameters are Today and Weather, the client queries the date function and finds that Today is Friday. The client checks the current weather from the Internet and finds that Weather is Sunny).

First, the client should verify, by looking at the default snapshot, that the Today and Weather parameter are defined in the GDL file. The client should then verify that the Friday and Sunny values are defined in the GDL file. It can verify these values by using DOM methods to search the default snapshot. After this validation, the client can locate the node that is holding the default value for each of these parameters in the configuration and update them to the new values.

In other cases, the configuration is obtained from user input or it is retrieved from persistent storage. The client could also use these configurations to obtain a snapshot.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Changing%20the%20Default%20GDL%20Configuration%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


