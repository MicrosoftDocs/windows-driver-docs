---
title: Creating GDL Configuration-Dependent Data
author: windows-driver-content
description: Creating GDL Configuration-Dependent Data
ms.assetid: 5b00903c-a637-4f83-96b8-92fe850d309e
keywords:
- GDL WDK , configurations
- configurations WDK GDL , creating configuration-dependent data
- creating configuration-dependent data WDK GDL
- GDL WDK , organizing data
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Creating GDL Configuration-Dependent Data


The GDL language enables you to define data whose value depends on one or more parameters. The GDL client does not need to know the dependence of the data on the parameters or even know that the data depends on the parameters. The GDL client needs to know only the value to be assigned to each parameter, and then GDL will construct the snapshot such that all of the data is appropriate for the specified parameter values.

Configuration-dependent data (CDD) is data that depends on one or more parameters. Clients that need to access the same set of data under different conditions or configurations are ideal consumers of configuration-dependent data. For example, an application that displays the weather conditions at a user-specified location and date always displays the same information (for example, daily rainfall, the daily high and low temperature, and average sky condition). The location and date become the parameters that are used to construct the configuration that is used to obtain the snapshot of the data. GDL easily enables you to organize data into a configuration-dependent form.

To use GDL to organize data into configuration-dependent form, follow these two steps:

1.  Define the parameters.

2.  Add dependencies into the data.

After the GDL file that describes the data has been created, the client needs to specify the desired configuration and request a snapshot.

The following topics describe the steps to create and organize configuration-dependent data:

[Defining the Configuration-Dependent Data Parameters](defining-the-configuration-dependent-data-parameters.md)

[Adding Dependencies to the Configuration-Dependent Data](adding-dependencies-to-the-configuration-dependent-data.md)

[Creating GDL Snapshots](creating-gdl-snapshots.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Creating%20GDL%20Configuration-Dependent%20Data%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


