---
title: Software Defined Battery
description: Software Defined Battery
keywords:
- Software Defined Battery
- SDB
ms.author: windowsdriverdev
ms.date: 11/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Software Defined Battery

The goal of this topic is to introduce Software Defined Batteries (SDB), describe Windows SDB architecture and detail the Windows API and DDI contracts for this feature. 

The topic starts by introducing the Simple Age Balancing SDB algorithm for a hypothetical two battery system. This is followed by architecture layout and API contract needed to implement SDB algorithm.

## Nomenclature

- BattC - Battery Class Driver

- CAD - The Charge Arbitration Driver is a Microsoft driver that arbitrates power between USB Legacy, USB Type-C and wireless charging sources

- Cold Swappable Batteries - Batteries that cannot be removed from the system without a risk of brownouts or total power failure

- Cycle Count - The number of full charge-discharge cycles undergone by the battery, as described in the ACPI specification

- Hot Swappable Batteries - Batteries that can be safely removed while the system is in operation, without any risk of brownouts

- HPMI - Hardware Power Manager Interface

- Non-Hot Swappable Batteries - One or more Cold Swappable and Non-Swappable Batteries installed in the system

- Non-Swappable Batteries - Batteries that are not designed and meant to be removed by the end user

## SDB Overview
The MSR research paper on Software Defined Batteries can be found here: [https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/multibattery_sosp2015.pdf](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/multibattery_sosp2015.pdf). 

This section reprises select ideas described in this paper and presents them with a view of productizing software based battery age balancing feature in laptops and other mobile devices. 

 
Imagine a two battery system. Where one battery is a Non Removable Battery, situated next to the SOC – let’s call this Internal Battery. Other battery is Hot Swappable Battery, situated next to a removable keyboard – let’s call this External Battery. 

*A Multi-Battery System*

![A Multi-Battery System showing internal and external batteries](/images/powermeter-multi-battery.png)

As the keyboard is attached-detached over a period of time, it forces the two batteries to age differently. This creates a scope for age balancing the batteries and prolonging system usability period by employing the SDB Simple Age Balancing Algorithm.

## Simple Age Balancing SDB Algorithm

The algorithm is called *simple age balancing* because it attempts to balance the battery age. The simple age balancing algorithm causes the system to prefer discharging the battery that has aged the least. A battery that has accrued lesser cycle counts not only has higher capacity to hold power, but also generally more efficient in delivering the power. Thereby prolonging the time system can sustain on batteries.

*Simple Age Balancing SDB Algorithm*

![Simple Age Balancing SDB Algorithm](/images/powermeter-simple-age-balancing-algorithm.png)
*Simple Age Balancing SDB Algorithm*

The core idea behind this algorithm is to simply use the battery that has accrued least battery cycle counts, as depicted by decision box (2) in the flowchart above. The hypothetical system in this example, allows for exclusive use of either internal or external batteries. However, this may not be true for all the systems. Other systems may not be as flexible or may have electrical constraints on use of batteries. In such cases the algorithm expects a best attempt of age balancing. For example consider the following.  

    A. A system that is unable to sustain power exclusively on the external battery (may be because the external battery is designed to be only a supplementary power source). This system may implement the simple age balancing algorithm by simultaneously discharging both the internal and external batteries in process block (A) in the above flowchart.

    B. A system that requires the external Battery be used whenever it is present (may be because of the additional power draw associated with keeping the removable keyboard powered up): This system may implement the simple age balancing algorithm by simultaneously discharging both the internal and external batteries in process block (B) in the above flowchart.

The Age Balancing Algorithm may be put to use only when there is enough charge present in the internal and external batteries to run the system, decision box (1) depicts this condition check in the above flowchart. For example (again going back to the hypothetical system) if the external battery has no charge in it, there is no scope for age balancing the batteries and the decision box (1) would result in “NO” branch.

The OEM is free to choose the constraints and conditions when the simple age balancing algorithm is not put into effect, besides when either internal or external Batteries are out of power. For example the OEM may choose to not perform any age balancing when:

1.	The SOC/Processor is running in high performance mode
2.	The system is thermally unstable

When the simple age balancing algorithm is not put in use (because of one or more conditions described above), the logic will revert back to OEM’s proprietary battery usage policy as depicted by process box (3) in the above flowchart. Process box (3) is the logic OEM would have put into effect if SDB was not supported.


## Adapting SDB Algorithm for use with Hot Swappable Batteries

The simple age balancing SDB algorithm attempts to use the battery that is healthiest, although this strategy is works well to improve the long term battery life, it may severely impact the short term usability of the system as described in the following scenario.

In the two battery system described above, consider the following situation:

1.	The user is expected to use the system long enough until charge in both internal and external Batteries is exhausted.

2.	The external battery has aged more compared to the internal battery.

When the simple age balancing algorithm is exercised on this system it will attempt to deplete the charge stored in the internal battery first (based on condition #1 and #2 listed above). When user decides to detach the external battery after a while, it would result in a bad user experience because the battery capacity made available for use would dramatically decrease once external battery is detached as the internal battery would be used up.

On a non-SDB system, this problem generally does not occur, because in most cases the external battery is depleted before the internal battery is put to use.

It is therefore desired to selectively disable the simple age balancing algorithm when above scenario is likely to happen. 

To summarize, whenever the user is expected to use the system for long duration with external battery removed, it is optimal to disable the SDB Algorithm and revert to using the OEM battery usage policy (which generally favors using the external battery first).

Windows calculates the battery availability and produces a “Preserve Non-Hot Swappable Batteries” hint. When this hint is consumed by the SDB algorithm, as depicted by the decision box (X) in the following flow chart.

*Simple Age Balancing SDB Algorithm Adapted for Hot Swappable Batteries*

![Simple Age Balancing SDB Algorithm Adapted for Hot Swappable Batteries](/images/powermeter-simple-age-balancing-algorithm-hot-swap.png)

## Implementing SDB Algorithm in Firmware

This chapter depicts the full battery discharge control logic implemented in the system Firmware. This builds on the battery age balancing logic described above to demonstrate how an existing multi-battery discharge logic (marked in (Y) block) would be incorporated with it.

Note that this is not a prescription of how SDB algorithm should be implemented by the OEMs, but a comprehensive example for the simplistic, hypothetical, multi-battery device described in this chapter.


*Simple Age Balancing SDB Algorithm*

![Simple Age Balancing SDB Algorithm](/images/powermeter-firmware-age-balancing-algorithm-hot-swap.png)


## Architecture Schematic
This section describes the component layout for all components participating in the power stack and their relative relationship with each other.

![Simple Age Balancing SDB Algorithm](/images/powermeter-hpmi-stack-architecture.png)


## Battery Miniport

The battery miniport interfaces remain the same.
SDB interfaces do not affect or influence OEM’s desire to rely on ACPI/CmBatt mechanism or to develop their proprietary miniport.

Note: Windows forwards all [IOCTL_BATTERY_SET_INFORMATION]() commands to all battery devices enumerated on the system.

## HPMI

Hardware Power Manager Interface, is a new component introduced in the power stack.

HPMI is a driver developed and owned by the OEM/device manufacturer.

HPMI has intimate knowledge of the underlying hardware configuration and state, and has access to the system Firmware. 

For implementing SDB feature, HPMI driver will:

1.	Register itself with Windows
2.	Advertise SDB Support
3.	Consume SDB control parameters provided by Windows

Multi-battery systems that support SDB are required to implement HPMI interface going forward. HPMI API protocol is the new de facto standard for implementing multiple battery systems.

In the future, HPMI will be updated to support other charging, discharging and charge management functions.

### Driver Characteristics

No more than one instance of HPMI driver should be present on a system.
HPMI may be implemented as either a user mode or a kernel mode driver.

### Installation

HPMI may be manifested as either an ACPI device or be root enumerated by one of the other OEM services/drivers at the discretion of the OEM.


*Simple Age Balancing SDB Algorithm*

![Simple Age Balancing SDB Algorithm](/images/powermeter-simple-age-balancing-algorithm.png)




--------------------


