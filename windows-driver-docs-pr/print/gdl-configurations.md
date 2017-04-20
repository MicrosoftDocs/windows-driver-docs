---
title: GDL Configurations
author: windows-driver-content
description: GDL Configurations
ms.assetid: ce698737-c9d8-4502-8823-e249820a06fa
keywords:
- GDL WDK , configurations
- configurations WDK GDL
- configurations WDK GDL , examples
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDL Configurations


GDL enables you to define dependencies in the data. The client does not need to be aware of dependencies; instead, the client specifies the configuration of interest when it requests a snapshot and the parser generates a snapshot that corresponds to that configuration.

For example, the prices that are charged for a phone call depend on the origin and destination points, the time of day and day of the week that the call is placed, the calling plan that is used, and so on. The prices for all possible outcomes can be represented by a large multidimensional array. This data can be represented by using GDL directives to define parameters to represent the various variables, like origin and destination points, time of day, calling plan, and so on. Other directives can be used to define the allowed values for these parameters. Still other directives specify how the data depends on the value of the parameters to be defined. After the data that represents the cost of the phone call (CostOfCall in the following example) has been expressed as a GDL source file, it can be parsed and any client can obtain the cost of making a phone call by simply creating a configuration that assigns the desired value to each parameter that is defined in the GDL.

For example, a client might compose a configuration that contains the following data.

```
OriginationPoint: Seattle
DestinationPoint: SanFrancisco
LengthOfCall: 10minutes
TimeOfDay: Night
CallingPlan: OneRate
```

And the snapshot that generated will contain one piece of data (out of all of the possible combinations) that might look like the following example.

```
CostOfCall: $0.49
```

A GDL snapshot can contain a complex data structure with thousands of items or just one. Each item in the snapshot can have its own set of dependencies on the configuration that the client is not aware of. The client must simply supply the configuration of interest, and the GDL parser will return the snapshot that represents the data that corresponds to that configuration.

In addition, GDL enables selected configurations to be excluded as "not allowed". For example, a printing device might not wish to allow duplex printing on transparent media. The GDL parser interface has methods to detect if the supplied configuration is allowed or disallowed; if the configuration is disallowed, the method will minimally alter the configuration so it is allowed. There are directives to define excluded configurations and directives to specify the relative importance of parameters so that a configuration can be corrected to resolve a conflict and the change can be made so it preserves the original intent as much as possible.

For more information about creating data that is configuration-dependent, see [Creating GDL Configuration-Dependent Data](creating-gdl-configuration-dependent-data.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Configurations%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


