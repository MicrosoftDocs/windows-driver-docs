---
title: Platform Performance Thresholds
description: There are two types of performance thresholds - static thresholds which remain fixed for the platform and dynamic thresholds that change at runtime.
ms.assetid: 4FB3AFEF-1560-4683-9D57-3029DAA50FE8
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Platform Performance Thresholds


There are two types of performance thresholds: static thresholds which remain fixed for the platform and dynamic thresholds that change at runtime. This topic describes the static performance thresholds of the platform and the allowed range for the dynamic threshold.

The static performance thresholds have the following definitions:

<a href="" id="highest-performance"></a>*Highest performance*  
The absolute maximum performance an individual processor may reach, assuming ideal conditions. This performance level may not be sustainable for long durations, and may only be achievable if other platform components are in a specific state (for example, it may require other processors be in an idle state).

<a href="" id="nominal-performance"></a>*Nominal performance*  
The maximum sustained performance level of the processor, assuming ideal environmental conditions (i.e. optimal ambient temperature, the processor is not already hot due to prior activity, available current is not restricted due to a low/cold battery). All processors are expected to be able to sustain continuous activity at their nominal performance simultaneously for at least one second.

<a href="" id="lowest-nonlinear-performance"></a>*Lowest Nonlinear Performance*  
The lowest performance level at which nonlinear power saving is achieved as performance is scaled. For example, due to the combined effects of voltage and frequency scaling better than liner power saving can be achieved by running at a lower performance state. Above this threshold, lower performance levels should be more energy efficient than higher performance levels.

<a href="" id="lowest-performance"></a>*Lowest Performance*  
The absolute lowest performance level of the platform. Selecting a performance level lower than the lowest nonlinear performance level may be equivalent from an efficiency perspective or may actually cause an efficiency penalty, but should reduce the instantaneous power consumption of the processor.

**Note**  All static performance levels do not need to be distinct. A platform's nominal performance level may also be its highest performance level, for example.

 

The platform may optionally also express a dynamic performance threshold, the *Guaranteed Performance* threshold. If present, this represents the maximum sustained performance level of a processor, taking into account all known external constraints (power budgeting, thermal constraints, power source, etc.). All processors are expected to be able to sustain their guaranteed performance levels simultaneously for at least one second. The guaranteed performance level is required to fall in the range \[Lowest Performance, Nominal performance\], inclusive.

## Heterogeneous Performance Thresholds


The PEP must use the same performance scale for all processors in the system. On platforms with heterogeneous processors, the performance characteristics of all processors may not be identical. In this case, the PEP must synthesize a performance scale that adjusts for differences in processors, such that any two processors running the same workload at the same performance level will complete in approximately the same time. The PEP should expose different capabilities for different classes of processors, so as to accurately reflect the performance characteristics of each processor.

 

 




