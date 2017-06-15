---
title: Platform Performance Thresholds
author: windows-driver-content
description: There are two types of performance thresholds: static thresholds which remain fixed for the platform and dynamic thresholds that change at runtime.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4FB3AFEF-1560-4683-9D57-3029DAA50FE8
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Platform%20Performance%20Thresholds%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


