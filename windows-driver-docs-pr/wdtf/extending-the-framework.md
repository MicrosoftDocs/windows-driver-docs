---
title: Extending the Framework
description: Extending the Framework
ms.assetid: 37a0fd70-0c88-414f-b4e3-afd641f1c667
keywords:
- Windows Device Testing Framework WDK , extending WDTF
- WDTF WDK , extending WDTF
- Windows Device Testing Framework WDK , action interfaces
- WDTF WDK , action interfaces
- Windows Device Testing Framework WDK , samples
- WDTF WDK , samples
- SimpleIO wizard WDK WDTF
- action interfaces WDK WDTF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Extending the Framework


WDTF is built to be extendable. Extendibility is possible in three distinct ways, as the following illustration shows.

![diagram illustrating the wdtf scenario model](images/wdtf-scenariomodel.gif)

The following list describes the three extensibility methods, in order of difficulty:

-   **Modify a sample script**. This method is shown with green in the preceding figure. You can take one of the WDTF-provided [sample scripts](sample-wdtf-scenarios.md) and modify it for your scenario. You can also [create WDTF scenarios](creating-wdtf-scenarios.md) from scratch.

-   **Implement an existing** [**action interface**](https://msdn.microsoft.com/library/windows/hardware/ff538355)**, like** SimpleIO. This method is shown with yellow in the preceding figure. You can implement an existing action interface to extend the types of targets that the interface functions on. If you implement a SimpleIO for your device type, all of the existing WDTF-based scenarios will automatically start performing I/O verification of your device.

    WDTF provides a Microsoft Visual Studio template to aid in implementing SimpleIO. For more information, see [Writing a WDTF SimpleIO plug-in for your device](writing-a-wdtf-simpleio-plug-in-for-your-device.md).

-   **Create (and then implement) a new** [**action interface**](https://msdn.microsoft.com/library/windows/hardware/ff538355). This method is shown with red in the preceding figure. If the functionality that WDTF provides is insufficient to construct your component-based scenarios, you can use WDTF to create new components.

    This method is the most difficult of the three methods because it requires [COM interface design skills](com-interface-design-skills.md). You must be able to design and implement simple abstractions of your functionality by using a COM-automation interface.

 

 




