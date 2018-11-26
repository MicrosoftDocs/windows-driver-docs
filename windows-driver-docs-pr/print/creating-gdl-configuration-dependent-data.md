---
title: Creating GDL Configuration-Dependent Data
description: Creating GDL Configuration-Dependent Data
ms.assetid: 5b00903c-a637-4f83-96b8-92fe850d309e
keywords:
- GDL WDK , configurations
- configurations WDK GDL , creating configuration-dependent data
- creating configuration-dependent data WDK GDL
- GDL WDK , organizing data
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




