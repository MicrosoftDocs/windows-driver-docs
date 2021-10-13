---
title: WDTF Architecture
description: WDTF Architecture
keywords:
- Windows Device Testing Framework WDK , architecture
- WDTF WDK , architecture
- architecture WDK WDTF
- Windows Device Testing Framework WDK , components
- WDTF WDK , components
- device-oriented target objects WDK WDTF
- system-oriented target objects WDK WDTF
- target objects WDK WDTF
- device depot WDK WDTF
- system depot WDK WDTF
- Simple Data Evaluation Language WDK WDTF
- SDEL WDK WDTF
- code modules WDK WDTF
- query languages WDK WDTF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDTF Architecture


To understand the architecture of WDTF, you should first read [Windows Device Testing Framework Design Guide](wdtf-overview.md). The most important concept is that WDTF uses devices and the system by abstracting each of them into a *target* (an [**IWDTFTarget2**](/windows-hardware/drivers/ddi/wdtf/nn-wdtf-iwdtftarget2) interface). The following illustration shows the core object model that WDTF provides.

![diagram illustrating the wdtf core object model.](images/wdtf-objectmodel.gif)

Your scenario can use some or all of the following WDTF objects and interfaces:

<a href="" id="wdtf-aggregation-object"></a>WDTF aggregation object  
The WDTF aggregation object ([**IWDTF2**](/windows-hardware/drivers/ddi/index)) is the initial instantiation point for the entire framework. Everything in the framework must be accessed through this object.

<a href="" id="systemdepot-property"></a>[**SystemDepot**](/windows-hardware/drivers/ddi/wdtf/nf-wdtf-iwdtf2-get_systemdepot) property  
The [**SystemDepot**](/windows-hardware/drivers/ddi/wdtf/nf-wdtf-iwdtf2-get_systemdepot) property ([**IWDTFSystemDepot2**](/windows-hardware/drivers/ddi/wdtf/nn-wdtf-iwdtfsystemdepot2)) contains only the local computer, which you can access through the [**ThisSystem**](/windows-hardware/drivers/ddi/wdtf/nf-wdtf-iwdtfsystemdepot2-get_thissystem) property.

<a href="" id="devicedepot-property"></a>[**DeviceDepot**](/windows-hardware/drivers/ddi/wdtf/nf-wdtf-iwdtf2-get_devicedepot) property  
The [**DeviceDepot**](/windows-hardware/drivers/ddi/wdtf/nf-wdtf-iwdtf2-get_devicedepot) property ([**IWDTFDeviceDepot2**](/windows-hardware/drivers/ddi/wdtf/nn-wdtf-iwdtfdevicedepot2)) represents a collection of all devices that are available on the computer. A scenario script can query (with the [**Query**](/windows-hardware/drivers/ddi/wdtf/nf-wdtf-iwdtftargets2-query) method) the **DeviceDepot** property for devices that meet one or more criteria that you specify in a search string by using the [Simple Data Evaluation Language](simple-data-evaluation-language-overview.md) (SDEL). As shown in the previous figure, **Query** returns a collection of targets ([**IWDTFTargets2**](/windows-hardware/drivers/ddi/wdtf/nn-wdtf-iwdtftargets2)) that meet the criteria. Additionally, the **DeviceDepot** property has a [**RootDevice**](/windows-hardware/drivers/ddi/wdtf/nf-wdtf-iwdtfdevicedepot2-get_rootdevice) property that represents the logical device object that is the parent of all physically present (also known as *non-phantom*) devices in the computer.

<a href="" id="iwdtftarget2"></a>[**IWDTFTarget2**](/windows-hardware/drivers/ddi/wdtf/nn-wdtf-iwdtftarget2)  
The [**IWDTFTarget2**](/windows-hardware/drivers/ddi/wdtf/nn-wdtf-iwdtftarget2) interface represents a *target* of testing activities. All activities that you perform with the framework involve at least one target. Targets can have one of the following forms:

-   A *device-type target* represents a hardware (or software) device that is attached to the computer.

-   A *system-type target* represents a computer as a whole.

A target contains attributes that describe the device or computer they represent.

<a href="" id="iwdtftargets2"></a>[**IWDTFTargets2**](/windows-hardware/drivers/ddi/wdtf/nn-wdtf-iwdtftargets2)  
The [**IWDTFTargets2**](/windows-hardware/drivers/ddi/wdtf/nn-wdtf-iwdtftargets2) collection interface represents a collection of individual targets ([**IWDTFTarget2**](/windows-hardware/drivers/ddi/wdtf/nn-wdtf-iwdtftarget2)). The [**IWDTFTargets2::Query**](/windows-hardware/drivers/ddi/wdtf/nf-wdtf-iwdtftargets2-query) method enables you to retrieve another collection that contains a subset of the contained targets.

### Action Plug-ins

WDTF includes a set of interfaces and implementations ([**action interfaces**](/windows-hardware/drivers/ddi/index)) that you can use in your test scenarios to control targets. Each implementation knows how to perform target-specific actions, such as enabling and disabling, or performing I/O operations. Your scripts can refer to these interfaces by their interface name, without understanding the specific implementation, as the following illustration shows.

![diagram illustrating the target::getinterface method.](images/wdtf-getinterface.gif)

For more information about these interfaces, see [Controlling Targets](controlling-targets.md).

### Simple Data Evaluation Language (SDEL)

WDTF includes a simple query language, Simple Data Evaluation Language (SDEL), that is similar to XPath and that simplifies the task of collecting targets based on attributes or relationships. SDEL enables you to form brief query statements that define selection constraints based on both the attributes of each target and relationships between them. For more information about SDEL, see [Simple Data Evaluation Language Overview](simple-data-evaluation-language-overview.md).

 

