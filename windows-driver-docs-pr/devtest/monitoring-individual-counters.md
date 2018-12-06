---
title: Monitoring Individual Counters
description: Monitoring Individual Counters
ms.assetid: 95d4492b-20b9-401a-97aa-eaf700b64420
keywords:
- individual counters WDK Driver Verifier
- Driver Verifier WDK , counters
- statistics WDK Driver Verifier
- counters WDK Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Monitoring Individual Counters


## <span id="ddk_monitoring_individual_counters_tools"></span><span id="DDK_MONITORING_INDIVIDUAL_COUNTERS_TOOLS"></span>


*Individual counters* are statistics which monitor some of the actions that Driver Verifier performs on drivers. These statistics are kept separately for each driver being verified.

Individual counters can be viewed by using the [**Verifier Command Line**](verifier-command-line.md), or by using Driver Verifier Manager. There are two versions of Driver Verifier Manager -- one for [Windows 2000](driver-verifier-manager--windows-2000-.md) and one for [Windows XP and later](driver-verifier-manager--windows-xp-and-later-.md).

### <span id="verifier_command_line"></span><span id="VERIFIER_COMMAND_LINE"></span>Verifier Command Line

To view individual counters, use the **verifier /query** command. This will show both individual counters and [global counters](monitoring-global-counters.md).

Individual counters are also included in Driver Verifier [log files](creating-log-files.md).

### <span id="driver_verifier_manager__windows_2000_"></span><span id="DRIVER_VERIFIER_MANAGER__WINDOWS_2000_"></span>Driver Verifier Manager (Windows 2000)

To view individual counters, select the **Pool Tracking** tab. Then select the desired driver from the drop-down box.

### <span id="driver_verifier_manager__windows_xp_and_later_"></span><span id="DRIVER_VERIFIER_MANAGER__WINDOWS_XP_AND_LATER_"></span>Driver Verifier Manager (Windows XP and later)

To view individual counters, start Driver Verifier Manager and select the **Display information about the currently verified drivers** task. Then press **Next** three times.

Finally, select the desired driver from the drop-down box.

### <span id="explanation_of_individual_counters"></span><span id="EXPLANATION_OF_INDIVIDUAL_COUNTERS"></span>Explanation of Individual Counters

Individual counters monitor statistics related to the [Pool Tracking](pool-tracking.md) option. They will all be zero if this option is not active.

These statistics are divided into two sections: **Paged Pool** and **Nonpaged Pool**. For each type of memory pool, the following four counters are shown:

<span id="Current_Number_of_Allocations"></span><span id="current_number_of_allocations"></span><span id="CURRENT_NUMBER_OF_ALLOCATIONS"></span>**Current Number of Allocations**  
The current number of individual allocations made by the specified driver from this type of memory pool.

<span id="Peak_Number_of_Allocations"></span><span id="peak_number_of_allocations"></span><span id="PEAK_NUMBER_OF_ALLOCATIONS"></span>**Peak Number of Allocations**  
The greatest number of individual allocations made at any single time since the last boot by the specified driver from this type of memory pool.

<span id="Current_Bytes_Allocated"></span><span id="current_bytes_allocated"></span><span id="CURRENT_BYTES_ALLOCATED"></span>**Current Bytes Allocated**  
The current number of bytes allocated to the specified driver from this type of memory pool.

<span id="Peak_Bytes_Allocated"></span><span id="peak_bytes_allocated"></span><span id="PEAK_BYTES_ALLOCATED"></span>**Peak Bytes Allocated**  
The greatest number of bytes allocated at any single time since the last boot to the specified driver from this type of memory pool.

Allocations whose size is one page or larger are not tracked by Pool Tracking and cannot be allocated from the special pool. These individual counters do not reflect these large allocations. A count of all such allocations can be seen in the [global counters](monitoring-global-counters.md).

 

 





